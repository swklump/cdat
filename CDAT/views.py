from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CDAT.collision_diagrams.download_diagrams import create_diagrams, get_intersections
import csv
from django.http import StreamingHttpResponse, HttpResponse
import zipfile
import io

#View for the home page
def home(request):
    
    return render(request, 'home.html')

@csrf_exempt
#This function is for selecting the state and crash file. The function
#also loads in the intersections from the crash file.
def file_changed(request):
    if request.method == 'POST':
        crash_file = io.TextIOWrapper(request.FILES['choose_your_crash_file'].file,encoding='ascii')
        crash_file.seek(0)
        state = request.POST['select_your_state']     
        
        try:
            intersections = get_intersections(state, crash_file)
            
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
        crash_file = io.TextIOWrapper(request.FILES['choose_your_crash_file'].file,encoding='utf-8')
        crash_file.seek(0)
        
        user_intersection = request.POST['select_your_intersection']
        sort_by = request.POST['sort_by']
        ped_bike_filter = request.POST['ped_bike_filter']
        
        buf = create_diagrams(state, crash_file, user_intersection, sort_by, ped_bike_filter)
        buf.seek(0)
        response = StreamingHttpResponse(buf,content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename="diagrams.zip"'
        return response

    return render(request, 'inputdata.html')
        
