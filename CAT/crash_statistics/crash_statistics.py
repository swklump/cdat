####This module runs the main program for the crash statistics module
    
def get_statistics(state, crash_filename, user_intersection, ped_bike_filter):
    from CAT.collision_diagrams.download_diagrams import get_intersections
    intersections = get_intersections(state, crash_filename)
    junction_type = intersections[1]
    street = intersections[2]
    cross_street = intersections[3]
    
    import csv
    from CAT.collision_diagrams.modules.importdata import prepare_lists #See module for comments
        
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
    
    #Load data into lists
    #alaska
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
                prepare_lists(crash_behaviors,'v1HumanCirc',row,22)
                prepare_lists(time_of_day,'AccTime',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Light',row,19)
                prepare_lists(surf_conditions,'SurfaceCond',row,22)
                prepare_lists(ped,'EveType',row)
                prepare_lists(bike,'EveType',row)      
    
    #colorado
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
                prepare_lists(crash_behaviors,'factor_1',row,22)
                prepare_lists(time_of_day,'time',row)
                prepare_lists(weather,'weather',row,22)
                prepare_lists(light_conditions,'lighting',row,19)
                prepare_lists(surf_conditions,'condition',row,22)
                prepare_lists(ped,'acctype',row)
                prepare_lists(bike,'acctype',row)                   

    #florida
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
                prepare_lists(crash_behaviors_temp,'V1_FRST_DR_ACTN_CD',row,22)
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

    #nebraska
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
                prepare_lists(crash_behaviors,'DRIV_1_CONT_CIRC_DESC',row,22)
                prepare_lists(time_of_day,'TOD',row)
                prepare_lists(weather,'WEATHER_COND_DESC',row,22)
                prepare_lists(light_conditions,'LIGHT_COND_DESC',row,19)
                prepare_lists(surf_conditions,'ROAD_COND_DESC',row,22)
                prepare_lists(ped,'PED',row)
                prepare_lists(bike,'BIKE',row) 

    #nevada
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
                prepare_lists(crash_behaviors,'V1 Vehicle Factors',row,22)
                prepare_lists(time_of_day,'Crash Time',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Lighting',row,19)
                prepare_lists(ped,'V1 All Events',row)
                prepare_lists(bike,'V1 All Events',row)
    
    #newyork
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
                prepare_lists(crash_behaviors,'Apparent Factor Veh 1',row,22)
                prepare_lists(time_of_day,'Accd Time',row)
                prepare_lists(weather,'Weather',row,22)
                prepare_lists(light_conditions,'Light Condition',row,19)
                prepare_lists(surf_conditions,'Road Surf Cond',row,19)
                prepare_lists(ped,'Collision Type',row)
                prepare_lists(bike,'Collision Type',row)
    
    #oregon
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
                prepare_lists(crash_behaviors,'CRASH_CAUSE_1_SHORT_DESC',row,22)
                prepare_lists(time_of_day,'CRASH_HR_NO',row)
                prepare_lists(weather,'WTHR_COND_SHORT_DESC',row,22)
                prepare_lists(light_conditions,'LGT_COND_SHORT_DESC',row,19)
                prepare_lists(surf_conditions,'RD_SURF_SHORT_DESC',row,22)
                prepare_lists(ped,'TOT_PED_CNT',row)
                prepare_lists(bike,'TOT_PEDCYCL_CNT',row) 

    #washington
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
                prepare_lists(crash_behaviors,'VEH 1 MV DRIVER CONTRIBUTING CIRCUMSTANCE 1',row,22)
                prepare_lists(time_of_day,'24 HR TIME',row)
                prepare_lists(weather,'WEATHER',row,22)
                prepare_lists(light_conditions,'LIGHTING CONDITIONS',row,19)
                prepare_lists(surf_conditions,'ROAD SURFACE CONDITIONS',row,22)
                prepare_lists(ped,'TZ Pedestrian Involved Indicator',row)
                prepare_lists(bike,'TZ Pedacyclist Involved Indicator',row)
    
    data_dictionary = {}
    data_dictionary['crash_types'] = []
    data_dictionary['crash_severity'] = []
    data_dictionary['crash_behaviors'] = []
    data_dictionary['time_of_day'] = []
    data_dictionary['weather'] = []
    data_dictionary['light_conditions'] = []
    data_dictionary['surf_conditions'] = []
    data_dictionary['ped'] = []
    data_dictionary['bike'] = []
    
    #crash severity
    data_dictionary['fatal_crashes'] = 0
    data_dictionary['si_crashes'] = 0
    data_dictionary['evident_crashes'] = 0
    data_dictionary['poss_crashes'] = 0
    data_dictionary['pdo_crashes'] = 0
    data_dictionary['unknown_crashes'] = 0
    
    i = 0
    if user_intersection == '_All Data':
        while i < len(file_length):
            get_all_data(state,data_dictionary,file_length,crash_types,crash_severity,crash_behaviors,time_of_day,weather,\
                               light_conditions,surf_conditions,ped,bike,i)

            i += 1
    
    #crash severity as percentage of total crashes
    data_dictionary['total_crashes'] = len(file_length)
    data_dictionary['%_fatal_crashes'] = "{:.0%}".format(data_dictionary['fatal_crashes']/data_dictionary['total_crashes'])
    data_dictionary['%_si_crashes'] = "{:.0%}".format(data_dictionary['si_crashes']/data_dictionary['total_crashes'])
    data_dictionary['%_evident_crashes'] = "{:.0%}".format(data_dictionary['evident_crashes']/data_dictionary['total_crashes'])
    data_dictionary['%_poss_crashes'] = "{:.0%}".format(data_dictionary['poss_crashes']/data_dictionary['total_crashes'])
    data_dictionary['%_pdo_crashes'] = "{:.0%}".format(data_dictionary['pdo_crashes']/data_dictionary['total_crashes'])
    data_dictionary['%_unknown_crashes'] = "{:.0%}".format(data_dictionary['unknown_crashes']/data_dictionary['total_crashes'])
    
    return data_dictionary

#If user selects all data    
def get_all_data(state,data_dictionary,file_length,crash_types,crash_severity,crash_behaviors,time_of_day,weather,\
                               light_conditions,surf_conditions,ped,bike,i):
    
    data_dictionary['crash_types'].append(crash_types[i])
    data_dictionary['crash_behaviors'].append(crash_behaviors[i])
    data_dictionary['time_of_day'].append(time_of_day[i])
    data_dictionary['weather'].append(weather[i])
    data_dictionary['light_conditions'].append(light_conditions[i])
    data_dictionary['surf_conditions'].append(surf_conditions[i])
    data_dictionary['ped'].append(ped[i])
    data_dictionary['bike'].append(bike[i])
    
    #States with all five crash severities
    if state == 'florida':
        if crash_severity[i] == '5':
            data_dictionary['fatal_crashes'] += 1
        elif crash_severity[i] == '4':
            data_dictionary['si_crashes'] += 1
        elif crash_severity[i] == '3':
            data_dictionary['evident_crashes'] += 1
        elif crash_severity[i] == '2':
            data_dictionary['poss_crashes'] += 1
        elif crash_severity[i] == '1':
            data_dictionary['pdo_crashes'] += 1
        elif crash_severity[i]:
            data_dictionary['unknown_crashes'] += 1    