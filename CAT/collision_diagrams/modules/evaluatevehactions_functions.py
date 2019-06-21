#Create crash dictionary with unique crash ID's (crash ID)
#Example print: {['crash1':,'crash2':]}
def crash_dict(file_length):
    crash_dict = {} 
    i = 0
    while i < len(file_length):
        crash_dict["Crash"+str(i+1)] = []
        i += 1
    return(crash_dict)

#Adding in the crash seveity, type, behavior, time of day, surface conditions, weather,
#and lighting conditions to each crash ID
#Example print: {'Crash630': ['sbl', 'wbt', 'fatality', 'veh - head on', 'improper turn',
#'12:56','dry','rainy','daylight']}
#Surface conditions is optional
def crash_characteristics(crash_severity, file_length, crash_dict, crash_types, \
                          crash_behaviors,time_of_day, weather, light_conditions,\
                          crash_ids, surf_conditions=''):

    i = 0
    while i < len(file_length):
        crash_dict["Crash"+str(i+1)].append(crash_severity[i])
        crash_dict["Crash"+str(i+1)].append(crash_types[i])
        crash_dict["Crash"+str(i+1)].append(crash_behaviors[i])
        crash_dict["Crash"+str(i+1)].append(time_of_day[i])
        crash_dict["Crash"+str(i+1)].append(weather[i])
        crash_dict["Crash"+str(i+1)].append(light_conditions[i])
        crash_dict["Crash"+str(i+1)].append(crash_ids[i])
        
        i += 1

    if surf_conditions:
        i = 0
        while i < len(file_length):
            crash_dict["Crash"+str(i+1)].append(surf_conditions[i])

            i += 1
        
#Add list values from crash_dict to list. Will be list within a list of all vehicle crash
#movements, change lists in list to strings
def unique_movements(crash_dict, file_length, ped, bike, surf_conditions='',):
    
    #Sorts two vehicle movements for each crash. Then combines the first two values in the
    #lists (vehicle movements) into one.
    #Print example: {'Crash631': ['ebr/wbt', 'fatality', 'veh - head on', 'improper turn',
    #'12:56','dry','rainy','daylight']}

    #Alaska: ped = 'pedestrian', bike = 'bicyclist'
    #Colorado: ped = 'pedestrian', bike = 'bicycle'
    #Florida: ped = >=1, bike = >=1
    #Nebraska: ped = 'yes', bike = 'yes'
    #Nevada: ped = 'pedestrian', bike = 'bicyclist'
    #New York: ped = 'collision with pedestrian', bike = 'collision with bicyclist'
    #Oregon: ped >= 1, bike = >= 1
    #Washington: ped = '1', bike = '1'
    
    ped_values = ['pedestrian','yes','collision with pedestrian','1']
    ped_numbers = []
    ped_numbers_temp = list(range(1,100))
    for n in ped_numbers_temp:
        ped_numbers.append(str(n))
        
    bike_values = ['bicyclist','yes','collision with bicyclist','1','bicycle']
    bike_numbers = []
    bike_numbers_temp = list(range(1,100))
    for n in bike_numbers_temp:
        bike_numbers.append(str(n))    
    
    i = 0
    while i < len(file_length):
        veh1 = crash_dict["Crash"+str(i+1)][0]
        veh2 = crash_dict["Crash"+str(i+1)][1]
        temp_list = [veh1,veh2]
        temp_list = sorted(temp_list)
        if ped[i] in ped_values[:] or ped[i] in ped_numbers[:]:
            if 'wb' in temp_list[1]:
                crash_dict["Crash"+str(i+1)][0] = 'pedestrian/' + temp_list[1]
            else:
                crash_dict["Crash"+str(i+1)][0] = 'pedestrian/' + temp_list[0]
        elif bike[i] in bike_values[:] or bike[i] in bike_numbers[:]:
            if 'wb' in temp_list[1]:
                crash_dict["Crash"+str(i+1)][0] = 'bicyclist/' + temp_list[1]
            else:
                crash_dict["Crash"+str(i+1)][0] = 'bicyclist/' + temp_list[0]
        else:
            crash_dict["Crash"+str(i+1)][0] = temp_list[0] + '/' + temp_list[1]
        del crash_dict["Crash"+str(i+1)][1]
        i += 1


    #Create a unique set of crash movements. 
    veh_movements = []
    for movements in crash_dict.values():
        veh_movements.append(movements[0])
    unique_movements = set(veh_movements)

    #Create a list of crash characteristics. 
    cr_severities = []
    cr_types = []
    cr_behaviors = []
    cr_time = []
    cr_weather = []
    cr_light = []
    cr_ids = []
    if surf_conditions: #Only if in crash data set
        cr_surf = []
    for sev in crash_dict.values():
        cr_severities.append(sev[1])
        cr_types.append(sev[2])
        cr_behaviors.append(sev[3])
        cr_time.append(sev[4])
        cr_weather.append(sev[5])
        cr_light.append(sev[6])
        cr_ids.append(sev[7])
        if surf_conditions: #Only if in crash data set
            cr_surf.append(sev[8])

    if surf_conditions: #Only if in crash data set
        return(veh_movements, unique_movements, cr_severities, cr_types, cr_behaviors,
               cr_time, cr_weather, cr_light, cr_ids, surf_conditions)
    else:
        return(veh_movements, unique_movements, cr_severities, cr_types, cr_behaviors,
               cr_time, cr_weather, cr_light, cr_ids)
    
