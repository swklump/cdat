####This module runs the main program

def get_intersections(state, crash_filename):
    
    import csv
    from CAT.collision_diagrams.modules.importdata import prepare_lists, prepare_lists_case #See module for comments
    
    file_length = []
    junction_type = []
    street = []
    cross_street = []
    
    if state == 'alaska':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'AccNum',row) 
                prepare_lists(junction_type,'RdJunct',row)
                prepare_lists_case(street,'Street',row)
                prepare_lists_case(cross_street,'CrossStreet',row)

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] in ['4-way intersection', 't - tntersection', 'y - intersection','roundabout']:
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())
        
    elif state == 'colorado':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'rte',row) 
                prepare_lists(junction_type,'road_desc',row)
                prepare_lists_case(street,'loc_01',row)
                prepare_lists_case(cross_street,'loc_02',row)

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] in ['at intersection','intersection related','roundabout']:
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())        
    
    elif state == 'florida':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CRSH_NUM',row) 
                prepare_lists(junction_type,'INTCT_TYP_CD',row)
                prepare_lists_case(street,'EVNT_ON_RD_NM',row)
                prepare_lists_case(cross_street,'EVNT_INTCT_RD_NM',row)    

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] in ['2', '3', '4','5','6','7']:
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())

    elif state == 'nebraska':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CASE_NUMBER',row) 
                prepare_lists(junction_type,'"BETWEEN"_STREET_(BLANK_IF_INT)',row)
                prepare_lists_case(street,'"ON"_STREET',row)
                prepare_lists_case(cross_street,'"AT/BETWEEN"_STREET',row)    

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] == 'na':
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())

    elif state == 'nevada':
        junction_type_temp = []
        
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'Accident Rec Num',row) 
                prepare_lists(junction_type_temp,'Distance',row)
                prepare_lists_case(street,'Primary Street',row)
                prepare_lists_case(cross_street,'Secondary Street',row)        

        junction_type = []
        for j in junction_type_temp:
            try:
                junction_type.append(int(j))
            except ValueError:
                junction_type.append(500)
            else:
                pass

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] <= 250:
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())

    elif state == 'newyork':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'Case Num',row) 
                prepare_lists(junction_type,'At Intersection',row)
                prepare_lists_case(street,'On Street',row)
                prepare_lists_case(cross_street,'Closest Cross Street',row)       

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] == 'y':
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())
        
    elif state == 'oregon':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CRASH_ID',row) 
                prepare_lists(junction_type,'RD_CHAR_SHORT_DESC',row)
                prepare_lists_case(street,'ST_FULL_NM',row)
                prepare_lists_case(cross_street,'ISECT_ST_FULL_NM',row)       

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] == 'inter':
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())

    elif state == 'washington':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'REPORT NUMBER',row) 
                prepare_lists(junction_type,'TZ Intersection Related Collision Indicator',row)
                prepare_lists_case(street,'PRIMARY TRAFFICWAY',row)
                prepare_lists_case(cross_street,'INTERSECTING TRAFFICWAY',row)        

        intersections = []
        i = 0
        while i < len(file_length):
            temp = [street[i],cross_street[i]]
            temp = sorted(temp)
            intersection = temp[0] + '/' + temp[1]
            if junction_type[i] == '1':
                intersections.append(intersection)
            i += 1
        intersections = set(intersections)
        intersections = sorted(intersections,key=lambda s: s.lower())

    return intersections, junction_type, street, cross_street


def create_diagrams(state, crash_filename, diagram_filter, user_intersection, sort_by, ped_bike_filter):
    intersections = get_intersections(state, crash_filename)
    junction_type = intersections[1]
    street = intersections[2]
    cross_street = intersections[3]
    
    import csv
    from CAT.collision_diagrams.modules.importdata import prepare_lists #See module for comments
    import os
    import shutil

    cwd = os.getcwd()
    diagram_folder = cwd + '\diagram_prints'
    if os.path.exists(diagram_folder):
        shutil.rmtree(diagram_folder)
    os.makedirs(diagram_folder)
    
    
####SECTION 1....Put csv columns into lists (See 'ImportData.py' in 'Modules' folder
    #for additional comments)

    #Vehicle movements and directions to create arrows
    file_length = []
    veh1_dir_to = []
    veh1_act = []
    veh2_dir_to = []
    veh2_act = []
    crash_types = []
    crash_severity = []
    crash_behaviors = []
    time_of_day = []
    weather = []
    light_conditions = []
    surf_conditions = []
    ped = []
    bike = []
    
    if state == 'alaska':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'AccNum',row)
                prepare_lists(veh1_dir_to,'v1TrvDirect',row)                
                prepare_lists(veh1_act,'v1ActionPreaction',row)        
                prepare_lists(veh2_dir_to,'v2TrvDirect',row) 
                prepare_lists(veh2_act,'v2ActionPreaction',row)
                prepare_lists(crash_types,'EveType',row)
                prepare_lists(crash_severity,'AccSeverity',row)
                prepare_lists(crash_behaviors,'v1HumanCirc',row,40)
                prepare_lists(time_of_day,'AccTime',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Light',row,19)
                prepare_lists(surf_conditions,'SurfaceCond',row,22)
                prepare_lists(ped,'EveType',row)
                prepare_lists(bike,'EveType',row)      
                
    elif state == 'colorado':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'rte',row)
                prepare_lists(veh1_dir_to,'dir_1',row)                
                prepare_lists(veh1_act,'veh_move_1',row)        
                prepare_lists(veh2_dir_to,'dir_2',row) 
                prepare_lists(veh2_act,'veh_move_2',row)
                prepare_lists(crash_types,'acctype',row)
                prepare_lists(crash_severity,'severity',row)
                prepare_lists(crash_behaviors,'factor_1',row,40)
                prepare_lists(time_of_day,'time',row)
                prepare_lists(weather,'weather',row,22)
                prepare_lists(light_conditions,'lighting',row,19)
                prepare_lists(surf_conditions,'condition',row,22)
                prepare_lists(ped,'acctype',row)
                prepare_lists(bike,'acctype',row)                   

    elif state == 'florida':
    
        crash_types_temp = []
        crash_behaviors_temp = []
        weather_temp = []
        light_conditions_temp = []
        surf_conditions_temp = []
        
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CRSH_NUM',row)
                prepare_lists(veh1_dir_to,'V1_TRAVDIR',row)  
                prepare_lists(veh1_act,'V1_VHCL_MOVE_CD',row)  
                prepare_lists(veh2_dir_to,'V2_TRAVDIR',row) 
                prepare_lists(veh2_act,'V2_VHCL_MOVE_CD',row)
                prepare_lists(crash_types_temp,'IMPCT_TYP_CD',row)
                prepare_lists(crash_severity,'ACCISEV',row)
                prepare_lists(crash_behaviors_temp,'V1_FRST_DR_ACTN_CD',row,25)
                prepare_lists(time_of_day,'EVNT_CRSH_TM',row)
                prepare_lists(weather_temp,'EVNT_WTHR_COND_CD',row,22)
                prepare_lists(light_conditions_temp,'LGHT_COND_CD',row,19)
                prepare_lists(surf_conditions_temp,'RD_SRFC_COND_CD',row,22)
                prepare_lists(ped,'TOT_OF_PEDST_NUM',row)
                prepare_lists(bike,'TOTOF_PEDLCYCL_NUM',row) 
        
        for n in crash_types_temp[:]:
            if n == '1':
                crash_types.append('Front to Rear')
            elif n == '2':
                crash_types.append('Front to Front')
            elif n == '3':
                crash_types.append('Angle')
            elif n == '4':
                crash_types.append('Sideswipe, Same Direction')
            elif n == '5':
                crash_types.append('Sideswipe, Opposite Direction')
            elif n == '6':
                crash_types.append('Rear to Side')
            elif n == '7':
                crash_types.append('Rear to Rear')
            elif n == '77':
                crash_types.append('Other, Explain in Narrative')
            elif n == '88':
                crash_types.append('Unknown')
            else:
                crash_types.append('Unknown')
            
        for n in crash_behaviors_temp[:]:
            if n == '1':
                crash_behaviors.append('No Contributing Action')
            elif n == '2':
                crash_behaviors.append('Operating MV in Careless')
            elif n == '3':
                crash_behaviors.append('Failed to Yield ROW')
            elif n == '4':
                crash_behaviors.append('Improper Backing')
            elif n == '6':
                crash_behaviors.append('Improper Turn')
            elif n == '10':
                crash_behaviors.append('Followed too Closely')
            elif n == '11':
                crash_behaviors.append('Ran Red Light')
            elif n == '12':
                crash_behaviors.append('Drove too Fast for Condit')
            elif n == '13':
                crash_behaviors.append('Ran Stop Sign')
            elif n == '15':
                crash_behaviors.append('Improper Passing')
            elif n == '17':
                crash_behaviors.append('Exceeded Posted Speed')
            elif n == '21':
                crash_behaviors.append('Wrong Side of Wrong Way')
            elif n == '25':
                crash_behaviors.append('Failed to Keep in Proper Ln')
            elif n == '26':
                crash_behaviors.append('Ran off Roadway')
            elif n == '27':
                crash_behaviors.append('Disregarded Other Sign')
            elif n == '28':
                crash_behaviors.append('Disregarded Other Markings')
            elif n == '29':
                crash_behaviors.append('Over-Correcting')
            elif n == '30':
                crash_behaviors.append('Swerved/Avoided:Object,etc')
            elif n == '31':
                crash_behaviors.append('Reckless/Aggressive Driving')
            elif n == '77':
                crash_behaviors.append('Other Contributing Action')
            else:
                crash_behaviors.append('Other Contributing Action')

        for n in weather_temp[:]:
            if n == '1':
                weather.append('Clear')
            elif n == '2':
                weather.append('Cloudy')
            elif n == '3':
                weather.append('Rain')
            elif n == '4':
                weather.append('Fog, Smog, Smoke')
            elif n == '5':
                weather.append('Sleet/Hail/Freezing Rain')
            elif n == '6':
                weather.append('Blowing Sand, Soil, Dirt')
            elif n == '7':
                weather.append('Severe Crosswinds')
            elif n == '77':
                weather.append('Other')
            else:
                weather.append('Unknown')

        for n in light_conditions_temp[:]:
            if n == '1':
                light_conditions.append('Daylight')
            elif n == '2':
                light_conditions.append('Dusk')
            elif n == '3':
                light_conditions.append('Dawn')
            elif n == '4':
                light_conditions.append('Dark-Lighted')
            elif n == '5':
                light_conditions.append('Dark-Not Lighted')
            elif n == '6':
                light_conditions.append('Dark-Unknown Lighting')
            elif n == '77':
                light_conditions.append('Other')
            elif n == '88':
                light_conditions.append('Unknown')
            else:
                light_conditions.append('Unknown')

        for n in surf_conditions_temp[:]:
            if n == '1':
                surf_conditions.append('Dry')
            elif n == '2':
                surf_conditions.append('Wet')
            elif n == '4':
                surf_conditions.append('Ice/Frost')
            elif n == '5':
                surf_conditions.append('Oil')
            elif n == '6':
                surf_conditions.append('Mud, Dirt, Gravel')
            elif n == '7':
                surf_conditions.append('Sand')
            elif n == '8':
                surf_conditions.append('Water (standing/moving)')
            elif n == '77':
                surf_conditions.append('Other')
            elif n == '88':
                surf_conditions.append('Unknown')
            else:
                surf_conditions.append('Unknown')                
                
    elif state == 'nebraska':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CASE_NUMBER',row)
                prepare_lists(veh1_dir_to,'VEH_1_DIR',row)  
                prepare_lists(veh1_act,'VEH_1_MVMT_DESC',row)  
                prepare_lists(veh2_dir_to,'VEH_2_DIR',row) 
                prepare_lists(veh2_act,'VEH_2_MVMT_DESC',row)
                prepare_lists(crash_types,'ACC_TYPE_DESC',row)
                prepare_lists(crash_severity,'POL_INC_CODE_DESC',row)
                prepare_lists(crash_behaviors,'DRIV_1_CONT_CIRC_DESC',row,40)
                prepare_lists(time_of_day,'TOD',row)
                prepare_lists(weather,'WEATHER_COND_DESC',row,22)
                prepare_lists(light_conditions,'LIGHT_COND_DESC',row,19)
                prepare_lists(surf_conditions,'ROAD_COND_DESC',row,22)
                prepare_lists(ped,'PED',row)
                prepare_lists(bike,'BIKE',row) 

    elif state == 'nevada':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'Accident Rec Num',row)
                prepare_lists(veh1_dir_to,'V1 Dir',row)                
                prepare_lists(veh1_act,'V1 Action',row)
                prepare_lists(veh2_dir_to,'V2 Dir',row)
                prepare_lists(veh2_act,'V2 Action',row)
                prepare_lists(crash_types,'Crash Type',row)
                prepare_lists(crash_severity,'Crash Severity',row)
                prepare_lists(crash_behaviors,'V1 Vehicle Factors',row,40)
                prepare_lists(time_of_day,'Crash Time',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Lighting',row,19)
                prepare_lists(ped,'V1 All Events',row)
                prepare_lists(bike,'V1 All Events',row)
      
    elif state == 'newyork':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'Case Num',row)
                prepare_lists(veh1_dir_to,'Dir Of Travel Veh 1',row)
                prepare_lists(veh1_act,'PRE_ACCD_ACTN_VEH1',row)
                prepare_lists(veh2_dir_to,'Dir Of Travel Veh 2',row)
                prepare_lists(veh2_act,'PRE_ACCD_ACTN_VEH2',row)
                prepare_lists(crash_types,'Collision Type',row)
                prepare_lists(crash_severity,'Severity',row)
                prepare_lists(crash_behaviors,'Apparent Factor Veh 1',row,40)
                prepare_lists(time_of_day,'Accd Time',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Light Condition',row,19)
                prepare_lists(surf_conditions,'Road Surf Cond',row,19)
                prepare_lists(ped,'Collision Type',row)
                prepare_lists(bike,'Collision Type',row)
    
    elif state == 'oregon':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'CRASH_ID',row)
                prepare_lists(veh1_dir_to,'VHCL_CMPSS_DIR_TO_SHORT_DESC1',row)
                prepare_lists(veh1_act,'MVMNT_SHORT_DESC1',row)
                prepare_lists(veh2_dir_to,'VHCL_CMPSS_DIR_TO_SHORT_DESC2',row)
                prepare_lists(veh2_act,'MVMNT_SHORT_DESC2',row)
                prepare_lists(crash_types,'COLLIS_TYP_SHORT_DESC',row)
                prepare_lists(crash_severity,'CRASH_SVRTY_SHORT_DESC',row)
                prepare_lists(crash_behaviors,'CRASH_CAUSE_1_SHORT_DESC',row,40)
                prepare_lists(time_of_day,'CRASH_HR_NO',row)
                prepare_lists(weather,'WTHR_COND_SHORT_DESC',row,22)
                prepare_lists(light_conditions,'LGT_COND_SHORT_DESC',row,19)
                prepare_lists(surf_conditions,'RD_SURF_SHORT_DESC',row,19)
                prepare_lists(ped,'TOT_PED_CNT',row)
                prepare_lists(bike,'TOT_PEDCYCL_CNT',row) 
            print(crash_types)

    elif state == 'washington':
        with open(crash_filename, 'r', encoding="utf-8") as f:                           
            reader = csv.DictReader(f)
            for row in reader:
                prepare_lists(file_length,'REPORT NUMBER',row)
                prepare_lists(veh1_dir_to,'VEH 1 COMPASS DIRECTION TO',row)
                prepare_lists(veh1_act,'VEH 1 ACTION',row)
                prepare_lists(veh2_dir_to,'VEH 2 COMPASS DIRECTION TO',row)
                prepare_lists(veh2_act,'VEH 2 ACTION',row)
                prepare_lists(crash_types,'FIRST COLLISION TYPE / OBJECT STRUCK',row)
                prepare_lists(crash_severity,'MOST SEVERE INJURY TYPE',row)
                prepare_lists(crash_behaviors,'VEH 1 MV DRIVER CONTRIBUTING CIRCUMSTANCE 1',row,40)
                prepare_lists(time_of_day,'24 HR TIME',row)
                prepare_lists(weather,'WEATHER',row,22)
                prepare_lists(light_conditions,'LIGHTING CONDITIONS',row,19)
                prepare_lists(surf_conditions,'ROAD SURFACE CONDITIONS',row,19)
                prepare_lists(ped,'TZ Pedestrian Involved Indicator',row)
                prepare_lists(bike,'TZ Pedacyclist Involved Indicator',row)


#############SECTION 3....Data Manipulation (See 'EvaluateVehActions.py' in current folder and
    #'EvaluateVehActions_fuctions.py' in 'Modules' folder for additional comments)
    from CAT.collision_diagrams.modules.evaluatevehactions_functions import crash_dict, crash_characteristics,\
         unique_movements

    #Create crash dictionary
    #Comments in 'EvaluateVehActions_functions.py' in 'Modules' folder
    crash_dict = crash_dict(file_length)

    #Assign vehicle direction and action for Vehicle 1 and Vehicle 2. Comments in
    #'EvaluateVehActions_wash.py' in current folder
    if state == 'alaska':
        from CAT.collision_diagrams.modules.evaluatevehactions_ak import veh_dir_act, crashes_list
    elif state == 'colorado':
        from CAT.collision_diagrams.modules.evaluatevehactions_co import veh_dir_act, crashes_list        
    elif state == 'florida':
        from CAT.collision_diagrams.modules.evaluatevehactions_fl import veh_dir_act, crashes_list
    elif state == 'nebraska':
        from CAT.collision_diagrams.modules.evaluatevehactions_ne import veh_dir_act, crashes_list
    elif state == 'nevada':
        from CAT.collision_diagrams.modules.evaluatevehactions_nv import veh_dir_act, crashes_list
    elif state == 'newyork':
        from CAT.collision_diagrams.modules.evaluatevehactions_ny import veh_dir_act, crashes_list
    elif state == 'oregon':
        from CAT.collision_diagrams.modules.evaluatevehactions_or import veh_dir_act, crashes_list        
    elif state == 'washington':
        from CAT.collision_diagrams.modules.evaluatevehactions_wa import veh_dir_act, crashes_list


    ucrashes1 = veh_dir_act(veh1_dir_to,veh1_act,file_length,crash_dict,user_intersection,junction_type,street,cross_street) #Vehicle 1
    unknown_crashes1 = ucrashes1[0]
    known_crashes1 = ucrashes1[1]

    ucrashes2 = veh_dir_act(veh2_dir_to,veh2_act,file_length,crash_dict,user_intersection,junction_type,street,cross_street) #Vehicle 2
    unknown_crashes2 = ucrashes2[0]
    known_crashes2 = ucrashes2[1]

    for crash in unknown_crashes2[:]:
        unknown_crashes1.append(crash)
    unknown_crashes = list(dict.fromkeys(unknown_crashes1))

    for crash in known_crashes2[:]:
        known_crashes1.append(crash)
    known_crashes = list(dict.fromkeys(known_crashes1))

    k = ', '
    unknown_crashes = k.join(unknown_crashes)
    known_crashes = k.join(known_crashes)


    #Add crash characteristics to crash dictionary.
    #Comments in 'EvaluateVehActions_functions.py' in 'Modules' folder
    #Create lists for each crash characteristic
    #See 'EvaluateVehActions_functions.py' in 'Modules' folder for comments
    #Create final list of crash characteristics
    if state in ['alaska','colorado','florida','nebraska', 'newyork','oregon','washington']:
        crash_characteristics(crash_severity, file_length, crash_dict, crash_types, crash_behaviors,
            time_of_day, weather, light_conditions, surf_conditions)
        veh_movements_unique_movements = unique_movements(crash_dict, file_length, ped, bike, surf_conditions)
        veh_movements = veh_movements_unique_movements[0]
        unique_movements = veh_movements_unique_movements[1]
        cr_severities = veh_movements_unique_movements[2]
        cr_types = veh_movements_unique_movements[3]
        cr_behaviors = veh_movements_unique_movements[4]
        cr_time = veh_movements_unique_movements[5]
        cr_weather = veh_movements_unique_movements[6]
        cr_light = veh_movements_unique_movements[7]
        cr_surf = veh_movements_unique_movements[8]
        crashes_list = crashes_list(unique_movements, veh_movements, cr_severities, file_length,
            cr_types, cr_behaviors, cr_time, cr_weather, cr_light, cr_surf, sort_by)

    #Nevada doesn't record road surface condition
    elif state in ['nevada']:
        crash_characteristics(crash_severity, file_length, crash_dict, crash_types,
            crash_behaviors, time_of_day, weather, light_conditions)
        veh_movements_unique_movements = unique_movements(crash_dict, file_length, ped, bike)
        veh_movements = veh_movements_unique_movements[0]
        unique_movements = veh_movements_unique_movements[1]
        cr_severities = veh_movements_unique_movements[2]
        cr_types = veh_movements_unique_movements[3]
        cr_behaviors = veh_movements_unique_movements[4]
        cr_time = veh_movements_unique_movements[5]
        cr_weather = veh_movements_unique_movements[6]
        cr_light = veh_movements_unique_movements[7]
        crashes_list = crashes_list(unique_movements, veh_movements, cr_severities,
            file_length, cr_types, cr_behaviors, cr_time, cr_weather, cr_light, sort_by)

##############SECTION 4....Create and show plots
    #Everything runs from 'plot_loop' function in 'ShowPlots.py' file ('Modules' folder)
    #The 'plot_loop' function brings in the 'show_plots' function in the same file
    #The 'show_plots' function brings in the 'DrawArrows' file ('Modules' folder)
    #The 'DrawArrows' file brings in 'PlotText' (state folder)

    #In summation: 'PlotText.py'>>'DrawArrows.py'>>'ShowPlots.py'

    #Run plot loop
    from CAT.collision_diagrams.modules.showplots import plot_loop

    #See comments in the these files sequentially in the order stated at beginning of
    #Section 4
    results = plot_loop(crashes_list,diagram_filter,state,ped_bike_filter, file_length)
    total_accounted_for = results[0]
    fi_accounted_for = results[1]

    f = open("unknown_crashIDs.txt", "w")
    f.write(unknown_crashes)

    g = open("known_crashIDs.txt", "w")
    g.write(known_crashes)


    return total_accounted_for, fi_accounted_for, diagram_folder
