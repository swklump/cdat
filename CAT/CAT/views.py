from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CAT.collision_diagrams.collision_program import create_diagrams, get_intersections
import csv
from django.http import StreamingHttpResponse, HttpResponse
import zipfile


def home(request):
    return render(request, 'home.html')
 
@csrf_exempt
def file_changed(request):
    
    if request.method == 'POST':
        import os
        import glob        
        delete_files = glob.glob("*.csv")
        for file in delete_files[:]:
            os.remove(file)
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

def analysis(request):
    
    if request.method == "POST":

        state = request.POST['select_your_state'] 
        crash_file = request.FILES['choose_your_crash_file']
        diagram_filter = request.POST['select_how_many_crashes_to_show']
        user_intersection = request.POST['select_your_intersection']
        sort_by = request.POST['sort_by']
        ped_bike_filter = request.POST['ped_bike_filter']
        fs = FileSystemStorage()
        fs.save(crash_file.name, crash_file)

        total_crashes = []
        crash_severity = []
        fatal_crashes = 0
        si_crashes = 0
        ev_crashes = 0
        poss_crashes = 0
        pdo_crashes = 0
        unknown_crashes = 0

        allinj_crashes = 0
        noreport_crashes = 0

        from CAT.collision_diagrams.collision_program import create_diagrams
        from CAT.collision_diagrams.modules.importdata import prepare_lists

        if state == 'alaska':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'AccNum',row)
                        prepare_lists(crash_severity,'AccSeverity',row)                     

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] == 'fatality':
                        fatal_crashes += 1
                    elif crash_severity[i] == 'incapacitating injury':
                        si_crashes += 1
                    elif crash_severity[i] == 'non-incapacitating/possible injury':
                        poss_crashes += 1
                    elif crash_severity[i] == 'property damage only':
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'starting in traffic', 'stopped', 'slowing', 'parked'," \
                "'skidding', 'out of control', or 'backing'."

        elif state == 'colorado':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'rte',row)
                        prepare_lists(crash_severity,'severity',row)                     

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] in ['fat']:
                        fatal_crashes += 1
                    elif crash_severity[i] in ['inj']:
                        allinj_crashes += 1
                    elif crash_severity[i] in ['pdo']:
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'avoiding object/vehicle in road','backing',"\
        "'changing lanes','entering/leaving parked position','making u-turn','parked',"\
        "'passing','slowing','stopped in traffic','weaving','parked','skidding',"\
        "'out of control','backing', or 'avoiding objects in road'."
                
        elif state == 'florida':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'CRSH_NUM',row)
                        prepare_lists(crash_severity,'ACCISEV',row)              

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:                
                    if crash_severity[i] in ['5']:
                        fatal_crashes += 1
                    elif crash_severity[i] in ['4']:
                        si_crashes += 1
                    elif crash_severity[i] in ['3','2']:
                        poss_crashes += 1
                    elif crash_severity[i] in ['1']:
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                    
                misc_action = "Miscellaneous action = 'backing', 'changing lanes', 'parked', 'making u-turn', 'overtaking/passing'," \
                                "'stopped in traffic', 'slowing', 'negotiating a curve', 'leaving traffic lane', or 'entering traffic lane'."
        
        elif state == 'nebraska':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'CASE_NUMBER',row)
                        prepare_lists(crash_severity,'POL_INC_CODE_DESC',row)              

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                #Ask Jon Markt for data dictionary on crash severities
                while i < total_crashes:
                    if crash_severity[i] in ['acc fat hr','acc fat']:
                        fatal_crashes += 1
                    elif crash_severity[i] in ['acc inj hr','acc inj']:
                        allinj_crashes += 1
                    elif crash_severity[i] in ['acc pd h&r','acc pd']:
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'backing', 'entering traffic lane', 'leaving traffic lane', \
                'slowing or stopped in traffic', or 'parked'."

        elif state == 'nevada':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'Accident Rec Num',row)
                        prepare_lists(crash_severity,'Crash Severity',row)                 

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] == 'fatal crash':
                        fatal_crashes += 1
                    elif crash_severity[i] == 'injury crash':
                        allinj_crashes += 1
                    elif crash_severity[i] == 'property damage only':
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'backing up' or 'stopped'."

        elif state == 'newyork':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'Case Num',row)
                        prepare_lists(crash_severity,'Severity',row)               

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] == 'fatal':
                        fatal_crashes += 1
                    elif crash_severity[i] in ['injury','property damage and injury']:
                        allinj_crashes += 1
                    elif crash_severity[i] == 'property damage':
                        pdo_crashes += 1
                    elif crash_severity[i] == 'non-reportable':
                        noreport_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'backing', 'entering parked position', 'not entered', \
                'parked', 'slowing or stopping', 'starting in traffic', or 'stopped in traffic'."

        elif state == 'oregon':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'CRASH_ID',row)
                        prepare_lists(crash_severity,'CRASH_SVRTY_SHORT_DESC',row)               

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] == 'fat':
                        fatal_crashes += 1
                    elif crash_severity[i] in ['inj']:
                        allinj_crashes += 1
                    elif crash_severity[i] == 'pdo':
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'making a u-turn', 'backing', 'stopped in traffic', "\
        "'parked - properly', 'parked - improperly' ,or 'parking maneuver'."

        elif state == 'washington':
            
            try:
                with open(crash_file.name, 'r', encoding="utf-8") as f:                           
                    reader = csv.DictReader(f)
                    for row in reader:
                        prepare_lists(total_crashes,'REPORT NUMBER',row)
                        prepare_lists(crash_severity,'MOST SEVERE INJURY TYPE',row)                

            except ValueError:
                messages.error(request, f'The wrong file may have been selected or the csv file is \
                not in the correct format. If you have selected the correct file, please \
                send an email to Sam Klump at samuel.klump@hdrinc.com.')
                return redirect('http://127.0.0.1:8000/analysis/')
            
            else:
                total_crashes = len(total_crashes)
                i = 0
                while i < total_crashes:
                    if crash_severity[i] in ['dead at scene','died in hospital','dead on arrival']:
                        fatal_crashes += 1
                    elif crash_severity[i] in ['serious injury','suspected serious injury']:
                        si_crashes += 1
                    elif crash_severity[i] in ['possible injury','evident injury','suspected minor injury']:
                        poss_crashes += 1
                    elif crash_severity[i] in ['no injury','no apparent injury']:
                        pdo_crashes += 1
                    else:
                        unknown_crashes += 1
                    i += 1
                misc_action = "Miscellaneous action = 'backing', 'slowing', 'starting from parked position', \
                'starting in traffic lane', 'stopped at signal or stop sign','stopped in traffic', or 'stopped in roadway'."

        buf = create_diagrams(state, crash_file.name, diagram_filter, user_intersection, sort_by, ped_bike_filter)
        buf.seek(0)

        # success = True
        # messages.success(request, f'Collision diagrams have been created!')
        import os
        import glob        
        delete_files = glob.glob("*.csv")
        for file in delete_files[:]:
            os.remove(file)    
        response = StreamingHttpResponse(buf,content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename="diagrams.zip"'
        return response
        return redirect('http://127.0.0.1:8000/analysis/')

    else:
        total_crashes = ''
        fatal_crashes = ''
        si_crashes = ''
        ev_crashes = ''
        poss_crashes = ''
        pdo_crashes = ''
        unknown_crashes = ''
        allinj_crashes = ''
        noreport_crashes = ''
        misc_action = ''
        state = ''
    

        
    return render(request, 'analysis_form.html', {'state': state, 'misc_action':misc_action, 'total_crashes':total_crashes,
    'fatal_crashes':fatal_crashes, 'si_crashes':si_crashes, 'ev_crashes':ev_crashes, 'poss_crashes': poss_crashes,
    'pdo_crashes':pdo_crashes, 'unknown_crashes':unknown_crashes, 'allinj_crashes':allinj_crashes,'noreport_crashes':noreport_crashes})

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value
