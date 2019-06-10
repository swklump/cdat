from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CAT.collision_diagrams.download_diagrams import create_diagrams, get_intersections
from CAT.crash_statistics.crash_statistics import get_statistics
import csv
from django.http import StreamingHttpResponse, HttpResponse
import zipfile 

#View for the home page
def home(request):
    del_files()
    return render(request, 'home.html')
 
@csrf_exempt
#This function is for selecting the state and crash file. The function
#also loads in the intersections from the crash file.
def file_changed(request):
    if request.method == 'POST':
        del_files()           
        
        crash_file = request.FILES['choose_your_crash_file']
        state = request.POST['select_your_state']    
        fs = FileSystemStorage()
        fs.save(crash_file.name, crash_file)
        
        #Need to add make this exception work

        intersections = get_intersections(state, crash_file.name)
        intersections = intersections[0]
        intersections.insert(0, "_Segments Only")        
        intersections.insert(0, "_Intersections Only")        
        intersections.insert(0, "_All Data")

        return JsonResponse({'intersections': list(intersections)})
    
    else:
        state = ''

#View for the input data page. Redirects user to the analysis they 
#select (download diagrams, crash statistics, or cmf optimizer).
def inputdata(request):
    
    if request.method == "POST":

        state = request.POST['select_your_state'] 
        crash_file = request.FILES['choose_your_crash_file']
        user_intersection = request.POST['select_your_intersection']
        sort_by = request.POST['sort_by']
        ped_bike_filter = request.POST['ped_bike_filter']
        choose_analysis = request.POST['choose_analysis']
        fs = FileSystemStorage()
        fs.save(crash_file.name, crash_file)

        if choose_analysis == 'download_crash_diagrams':
            import os
            import glob 
            buf = create_diagrams(state, crash_file.name, user_intersection, sort_by, ped_bike_filter)
            buf.seek(0)            
            delete_files = glob.glob("*.csv")
            for file in delete_files[:]:
                os.remove(file)    
            response = StreamingHttpResponse(buf,content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename="diagrams.zip"'
            return response
        
        elif choose_analysis == 'go_to_crash_statistics':

            statistics = get_statistics(state, crash_file.name, user_intersection, ped_bike_filter)
            total_crashes = statistics['total_crashes']
            fatal_crashes = statistics['fatal_crashes']
            si_crashes = statistics['si_crashes']
            evident_crashes = statistics['evident_crashes']
            poss_crashes = statistics['poss_crashes']
            pdo_crashes = statistics['pdo_crashes']
            unknown_crashes = statistics['unknown_crashes']
            percent_fatal_crashes = statistics['%_fatal_crashes']
            percent_si_crashes = statistics['%_si_crashes']
            percent_evident_crashes = statistics['%_evident_crashes']
            percent_poss_crashes = statistics['%_poss_crashes']
            percent_pdo_crashes = statistics['%_pdo_crashes']
            percent_unknown_crashes = statistics['%_unknown_crashes']
            
            request.session['state'] = state
            request.session['total_crashes'] = total_crashes
            request.session['fatal_crashes'] = fatal_crashes
            request.session['si_crashes'] = si_crashes
            request.session['evident_crashes'] = evident_crashes
            request.session['poss_crashes'] = poss_crashes
            request.session['pdo_crashes'] = pdo_crashes
            request.session['unknown_crashes'] = unknown_crashes
            request.session['percent_fatal_crashes'] = percent_fatal_crashes
            request.session['percent_si_crashes'] = percent_si_crashes
            request.session['percent_evident_crashes'] = percent_evident_crashes
            request.session['percent_poss_crashes'] = percent_poss_crashes
            request.session['percent_pdo_crashes'] = percent_pdo_crashes
            request.session['percent_unknown_crashes'] = percent_unknown_crashes
            
            return redirect('http://127.0.0.1:8000/crashstatistics')
        
        elif choose_analysis == 'go_to_countermeasures_optimizer':
            return redirect('http://127.0.0.1:8000/cmfoptimizer')    
    
    del_files()
    
    return render(request, 'inputdata.html')

#View for the crash statistics page
def crashstatistics(request):
    del_files()
        
    state = request.session['state'] 
    total_crashes = request.session['total_crashes']
    fatal_crashes = request.session['fatal_crashes']
    si_crashes = request.session['si_crashes']
    evident_crashes = request.session['evident_crashes']
    poss_crashes = request.session['poss_crashes']
    pdo_crashes = request.session['pdo_crashes']
    unknown_crashes = request.session['unknown_crashes']
    percent_fatal_crashes = request.session['percent_fatal_crashes']
    percent_si_crashes = request.session['percent_si_crashes']
    percent_evident_crashes = request.session['percent_evident_crashes']
    percent_poss_crashes = request.session['percent_poss_crashes']
    percent_pdo_crashes = request.session['percent_pdo_crashes']
    percent_unknown_crashes = request.session['percent_unknown_crashes']

    return render(request, 'crashstatistics.html', {'state': state,'total_crashes':total_crashes,'fatal_crashes':fatal_crashes,
    'si_crashes':si_crashes,'evident_crashes':evident_crashes,'poss_crashes':poss_crashes,
    'pdo_crashes':pdo_crashes,'unknown_crashes':unknown_crashes,
    'percent_fatal_crashes':percent_fatal_crashes,'percent_si_crashes':percent_si_crashes,
    'percent_evident_crashes':percent_evident_crashes,'percent_poss_crashes':percent_poss_crashes,
    'percent_pdo_crashes':percent_pdo_crashes,'percent_unknown_crashes':percent_unknown_crashes})

#View for the cmf optimizer page    
def cmfoptimizer(request): 
    return render(request, 'cmfoptimizer.html')    

#Function to delete all files uploaded by user
def del_files():
    import os
    import glob        
    delete_files = glob.glob("*.*")
    delete_files.remove('db.sqlite3')
    delete_files.remove('manage.py')
    # delete_files.remove('setup.py')
    # delete_files.remove('README.txt')
    for file in delete_files[:]:
        os.remove(file)