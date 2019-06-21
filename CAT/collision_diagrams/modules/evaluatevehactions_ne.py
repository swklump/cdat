#This function evaluates direction and action of each vehicle for each crash and adds the
#concatenated direction and veh action to the crash dictionary.
#Example print: {{'crash1' : [ebl,wbl]}              

#Main function         
def veh_dir_act(veh_num_dir_to,veh_num_action,file_length,crash_set,user_intersection,junction_type,street,cross_street):                                              
    i = 0
    if user_intersection == '_All Data':
        while i < len(file_length):
            dir_act(veh_num_dir_to,veh_num_action,file_length,crash_set,i)
            i += 1
    elif user_intersection == '_All Intersections':
        while i < len(file_length):
            dir_act_all_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type)
            i += 1
    elif user_intersection == '_Segments Only':
        while i < len(file_length):
            dir_act_all_segments(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type)
            i += 1             
    else:
        while i < len(file_length):
            dir_act_spec_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type,user_intersection,street,cross_street)
            i += 1
    i = 0

#User selects all data
def dir_act(veh_num_dir_to,veh_num_action,file_length,crash_set,i):
    
    if veh_num_dir_to[i] in ['n','nw','ne']:
        if veh_num_action[i] == "turning left":
            crash_set["Crash"+str(i+1)].append('ebl')            
        elif veh_num_action[i] == "turning right":
            crash_set["Crash"+str(i+1)].append('wbr')            
        elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
            crash_set["Crash"+str(i+1)].append('nbt')            
        elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
        "leaving traffic lane","parked","slowing or stopped in traffic"]:
            crash_set["Crash"+str(i+1)].append('nb misc. action')            
        else:
            crash_set["Crash"+str(i+1)].append('nb other')            
    
    elif veh_num_dir_to[i] in ['s','sw','se']:
        if veh_num_action[i] == "turning left":
            crash_set["Crash"+str(i+1)].append('wbl')            
        elif veh_num_action[i] == "turning right":
            crash_set["Crash"+str(i+1)].append('ebr')            
        elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
            crash_set["Crash"+str(i+1)].append('sbt')            
        elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
        "leaving traffic lane","parked","slowing or stopped in traffic"]:
            crash_set["Crash"+str(i+1)].append('sb misc. action')            
        else:
            crash_set["Crash"+str(i+1)].append('sb other')            
    
    elif veh_num_dir_to[i] == 'e':
        if veh_num_action[i] == "turning left":
            crash_set["Crash"+str(i+1)].append('sbl')            
        elif veh_num_action[i] == "turning right":
            crash_set["Crash"+str(i+1)].append('nbr')            
        elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
            crash_set["Crash"+str(i+1)].append('ebt')            
        elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
        "leaving traffic lane","parked","slowing or stopped in traffic"]:
            crash_set["Crash"+str(i+1)].append('eb misc. action')            
        else:
            crash_set["Crash"+str(i+1)].append('eb other')            
    
    elif veh_num_dir_to[i] == 'w':
        if veh_num_action[i] == "turning left":
            crash_set["Crash"+str(i+1)].append('nbl')            
        elif veh_num_action[i] == "turning right":
            crash_set["Crash"+str(i+1)].append('sbr')            
        elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
            crash_set["Crash"+str(i+1)].append('wbt')            
        elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
        "leaving traffic lane","parked","slowing or stopped in traffic"]:
            crash_set["Crash"+str(i+1)].append('wb misc. action')            
        else:
            crash_set["Crash"+str(i+1)].append('wb other')            
    
    elif veh_num_dir_to[i] == '':
        crash_set["Crash"+str(i+1)].append('single vehicle crash')        
    
    else:
        crash_set["Crash"+str(i+1)].append('unknown')        

#User selects all intersections
def dir_act_all_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type):
    
    if junction_type[i] == 'na':
        
        if veh_num_dir_to[i] in ['n','nw','ne']:
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('ebl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('wbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('nbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('nb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('nb other')                
        
        elif veh_num_dir_to[i] in ['s','sw','se']:
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('wbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('ebr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('sbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('sb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('sb other')                
        
        elif veh_num_dir_to[i] == 'e':
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('sbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('nbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('ebt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('eb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('eb other')                
        
        elif veh_num_dir_to[i] == 'w':
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('nbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('sbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('wbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('wb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('wb other')                
        
        elif veh_num_dir_to[i] == '':
            crash_set["Crash"+str(i+1)].append('single vehicle crash')            
        
        else:
            crash_set["Crash"+str(i+1)].append('unknown')            

    else:
        crash_set["Crash"+str(i+1)].append('not an intersection')            

#User selects all segments
def dir_act_all_segments(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type):
    
    if junction_type[i] not in ['na']:
        
        if veh_num_dir_to[i] in ['n','nw','ne']:
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('ebl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('wbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('nbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('nb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('nb other')                
        
        elif veh_num_dir_to[i] in ['s','sw','se']:
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('wbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('ebr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('sbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('sb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('sb other')                
        
        elif veh_num_dir_to[i] == 'e':
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('sbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('nbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('ebt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('eb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('eb other')                
        
        elif veh_num_dir_to[i] == 'w':
            if veh_num_action[i] == "turning left":
                crash_set["Crash"+str(i+1)].append('nbl')                
            elif veh_num_action[i] == "turning right":
                crash_set["Crash"+str(i+1)].append('sbr')                
            elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                crash_set["Crash"+str(i+1)].append('wbt')                
            elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
            "leaving traffic lane","parked","slowing or stopped in traffic"]:
                crash_set["Crash"+str(i+1)].append('wb misc. action')                
            else:
                crash_set["Crash"+str(i+1)].append('wb other')                
        
        elif veh_num_dir_to[i] == '':
            crash_set["Crash"+str(i+1)].append('single vehicle crash')            
        
        else:
            crash_set["Crash"+str(i+1)].append('unknown')            

    else:
        crash_set["Crash"+str(i+1)].append('is an intersection')         

#User selects specific intersection         
def dir_act_spec_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type,user_intersection, street, cross_street):

    if junction_type[i] == 'na':
        temp = [street[i],cross_street[i]]
        temp = sorted(temp)
        intersection = temp[0] + '/' + temp[1]
        
        if intersection not in [user_intersection]:
            crash_set["Crash"+str(i+1)].append('not right intersection')
        
        else:
            
            if veh_num_dir_to[i] in ['n','nw','ne']:
                if veh_num_action[i] == "turning left":
                    crash_set["Crash"+str(i+1)].append('ebl')                    
                elif veh_num_action[i] == "turning right":
                    crash_set["Crash"+str(i+1)].append('wbr')                    
                elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                    crash_set["Crash"+str(i+1)].append('nbt')                    
                elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
                "leaving traffic lane","parked","slowing or stopped in traffic"]:
                    crash_set["Crash"+str(i+1)].append('nb misc. action')                    
                else:
                    crash_set["Crash"+str(i+1)].append('nb other')                    
            
            elif veh_num_dir_to[i] in ['s','sw','se']:
                if veh_num_action[i] == "turning left":
                    crash_set["Crash"+str(i+1)].append('wbl')                    
                elif veh_num_action[i] == "turning right":
                    crash_set["Crash"+str(i+1)].append('ebr')                    
                elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                    crash_set["Crash"+str(i+1)].append('sbt')                    
                elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
                "leaving traffic lane","parked","slowing or stopped in traffic"]:
                    crash_set["Crash"+str(i+1)].append('sb misc. action')                    
                else:
                    crash_set["Crash"+str(i+1)].append('sb other')                    
            
            elif veh_num_dir_to[i] == 'e':
                if veh_num_action[i] == "turning left":
                    crash_set["Crash"+str(i+1)].append('sbl')                    
                elif veh_num_action[i] == "turning right":
                    crash_set["Crash"+str(i+1)].append('nbr')                    
                elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                    crash_set["Crash"+str(i+1)].append('ebt')                    
                elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
                "leaving traffic lane","parked","slowing or stopped in traffic"]:
                    crash_set["Crash"+str(i+1)].append('eb misc. action')                    
                else:
                    crash_set["Crash"+str(i+1)].append('eb other')                    
            
            elif veh_num_dir_to[i] == 'w':
                if veh_num_action[i] == "turning left":
                    crash_set["Crash"+str(i+1)].append('nbl')                    
                elif veh_num_action[i] == "turning right":
                    crash_set["Crash"+str(i+1)].append('sbr')                    
                elif veh_num_action[i] in ["going ahead","essentially straight ahead"]:
                    crash_set["Crash"+str(i+1)].append('wbt')                    
                elif veh_num_action[i] in ["backing","changing lanes","overtaking/passing","making u-turn","entering traffic lane",
                "leaving traffic lane","parked","slowing or stopped in traffic"]:
                    crash_set["Crash"+str(i+1)].append('wb misc. action')                    
                else:
                    crash_set["Crash"+str(i+1)].append('wb other')                    
            
            elif veh_num_dir_to[i] == '':
                crash_set["Crash"+str(i+1)].append('single vehicle crash')                
            
            else:
                crash_set["Crash"+str(i+1)].append('unknown')                

    else:
        crash_set["Crash"+str(i+1)].append('not an intersection')  

#Put crash movements as keys in dictionary and crash characteristics as values.
def crashes_list(unique_movements, veh_movements, cr_severities, file_length, \
                 cr_types, cr_behaviors, cr_time, cr_weather, cr_light, cr_ids, cr_surf, sort_by):


    #Setting up the dictionary
    crash_counts = {}
    for un_move in unique_movements:
        crash_counts[un_move] = [0,0,0,0,0]#These are for the 5 different crash sevs
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])

    #I'm comparing the vehicle movments to the unique set of movements, so I can count
    #up all crashes with the same movements. Then I'm adding the severity to the
    #dictionary
    #Print example: {'ebl/wbt' : [1671, 0, 15, 444, 1212, ['veh - rear end', 'veh - rear end'], ['inattention','intoxicated']}
    for un_move in unique_movements:
        i = 0
        while i < len(file_length):
            if un_move == veh_movements[i]:
                crash_counts[un_move][0] += 1
                if cr_severities[i] in ['acc fat hr','acc fat']:
                    crash_counts[un_move][1] += 1
                elif cr_severities[i] in ['acc inj hr','acc inj']:
                    crash_counts[un_move][2] += 1
                elif cr_severities[i] in ['acc pd h&r','acc pd']:
                    crash_counts[un_move][3] += 1
                elif cr_severities[i] in ['acc h&r','acc']:
                    crash_counts[un_move][4] += 1
                elif cr_severities[i]:
                    crash_counts[un_move][4] += 1
                crash_counts[un_move][5].append(cr_types[i])
                crash_counts[un_move][6].append(cr_behaviors[i])
                crash_counts[un_move][7].append(cr_time[i])
                crash_counts[un_move][8].append(cr_weather[i])
                crash_counts[un_move][9].append(cr_light[i])
                crash_counts[un_move][10].append(cr_ids[i])
                crash_counts[un_move][11].append(cr_surf[i])
            i +=1

    #Print example:
    #['wb misc. action/wb misc. action', [1671, 0, 15, 444, 1212, ['veh - rear end', 'veh - rear end'], ['inattention','intoxicated']]
    crashes_list = []
    for key,value in crash_counts.items():
        crashes_list.append([key,(value)])

    if sort_by == 'total crashes':   
        crashes_list.sort(key = lambda x: x[1])
        crashes_list.reverse()
    elif sort_by == 'fatal crashes':   
        crashes_list.sort(key = lambda x: x[1][1])
        crashes_list.reverse()
    elif sort_by in ['fatal and serious injury crashes','fatal and all injury crashes']:
        for crash in crashes_list:
            f_i = crash[1][1] + crash[1][2]
            crash.insert(0,f_i)
        crashes_list.sort(key = lambda x: x[0])
        crashes_list.reverse()
        i = 0
        while i < len(crashes_list):
            del crashes_list[i][0]
            i += 1

    for i in range(len(crashes_list)):
        if 'single vehicle crash' in crashes_list[i][0]:
            import re
            crashes_list[i][0] = re.sub('single vehicle crash/','(single vehicle crash)', crashes_list[i][0])
            crashes_list[i][0] = re.sub('/single vehicle crash','(single vehicle crash)', crashes_list[i][0])

    return (crashes_list)
