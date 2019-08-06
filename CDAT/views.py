from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CDAT.collision_diagrams.download_diagrams import create_diagrams, get_intersections
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
        fs = FileSystemStorage()#change to stream storage
        fs.save(crash_file.name, crash_file)

        try:
            intersections = get_intersections(state, crash_file.name)
            
        except Exception as ex:
            return JsonResponse({'success': False, 'message': '\n An error occurred parsing the data file. '+ 
            'Make sure that the file is in .csv data type and is in the standard state DOT format. If neither ' +  
            'of these conditions apply and an error persists, please send an email to Sam Klump at samuel.klump@hdrinc.com.'})

        intersections = intersections[0]
        intersections.insert(0, "_Segments Only")
        intersections.insert(0, "_Intersections Only")
        intersections.insert(0, "_All Data")

        return JsonResponse({'success': True, 'intersections': list(intersections)})

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
        fs = FileSystemStorage()
        fs.save(crash_file.name, crash_file)

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


    del_files()

    return render(request, 'inputdata.html')
        
#Function to delete all files uploaded by user
def del_files():
    import os
    import glob
    delete_files = glob.glob("*.*")
    delete_files.remove('db.sqlite3')
    delete_files.remove('manage.py')
    delete_files.remove('setup.py')
    delete_files.remove('README.txt')
    delete_files.remove('MANIFEST.in')
    delete_files.remove('.gitignore')
    for file in delete_files[:]:
        os.remove(file)