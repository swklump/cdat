#This function evaluates direction and action of each vehicle for each crash and adds the
#concatenated direction and veh action to the crash dictionary.
#Example print: {{'crash1' : [ebl,wbt]}              
 
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

#User selects All data
def dir_act(veh_num_dir_to,veh_num_action,file_length,crash_set,i):
    
    if veh_num_dir_to[i] in ['north']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('ebl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('wbr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('nbt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('nb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('nb other')  

    elif veh_num_dir_to[i] in ['northeast','north-east']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('sebl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('nwbr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('nebt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('neb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('neb other')  

    elif veh_num_dir_to[i] in ['northwest','north-west']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('nebl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('swbr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('nwbt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('nwb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('nwb other')              
    
    elif veh_num_dir_to[i] in ['south']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('wbl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('ebr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('sbt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('sb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('sb other')       

    elif veh_num_dir_to[i] in ['southeast','south-east']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('swbl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('nebr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('sebt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('seb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('seb other') 

    elif veh_num_dir_to[i] in ['southwest','south-west']:
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('nwbl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('sebr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('swbt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('swb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('swb other')             
    
    elif veh_num_dir_to[i] == 'east':
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('sbl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('nbr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('ebt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('eb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('eb other')                              
    
    elif veh_num_dir_to[i] == 'west':
        if veh_num_action[i] == "making left turn":
            crash_set["Crash"+str(i+1)].append('nbl')                              
        elif veh_num_action[i] == "making right turn":
            crash_set["Crash"+str(i+1)].append('sbr')                              
        elif veh_num_action[i] == "going straight ahead":
            crash_set["Crash"+str(i+1)].append('wbt')                              
        elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
        "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
        "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
        "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
        "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
            crash_set["Crash"+str(i+1)].append('wb misc. action')                              
        else:
            crash_set["Crash"+str(i+1)].append('wb other')                                                  
    
    elif veh_num_dir_to[i] == 'na':
        crash_set["Crash"+str(i+1)].append('single vehicle crash')                      
    
    else:
        crash_set["Crash"+str(i+1)].append('unknown')                  

#User selects all intersections
def dir_act_all_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type):

    if junction_type[i] == '1':
        
        if veh_num_dir_to[i] in ['north']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('ebl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('wbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('nb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('nb other')  

        elif veh_num_dir_to[i] in ['northeast','north-east']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('sebl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nwbr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nebt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('neb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('neb other')  

        elif veh_num_dir_to[i] in ['northwest','north-west']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nebl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('swbr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nwbt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('nwb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('nwb other')                 
        
        elif veh_num_dir_to[i] in ['south']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('wbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('ebr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('sbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('sb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('sb other') 

        elif veh_num_dir_to[i] in ['southeast','south-east']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('swbl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nebr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('sebt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('seb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('seb other') 

        elif veh_num_dir_to[i] in ['southwest','south-west']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nwbl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('sebr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('swbt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('swb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('swb other')                   
        
        elif veh_num_dir_to[i] == 'east':
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('sbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('ebt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('eb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('eb other')                                  
        
        elif veh_num_dir_to[i] == 'west':
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('sbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('wbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('wb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('wb other')                                                           
        
        elif veh_num_dir_to[i] == 'na':
            crash_set["Crash"+str(i+1)].append('single vehicle crash')                          
        
        else:
            crash_set["Crash"+str(i+1)].append('unknown')                   
    
    else:
        crash_set["Crash"+str(i+1)].append('not an intersection')        

#User selects all segments
def dir_act_all_segments(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type):

    if junction_type[i] not in ['1']:
        
        if veh_num_dir_to[i] in ['north']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('ebl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('wbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('nb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('nb other')  

        elif veh_num_dir_to[i] in ['northeast','north-east']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('sebl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nwbr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nebt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('neb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('neb other')  

        elif veh_num_dir_to[i] in ['northwest','north-west']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nebl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('swbr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('nwbt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('nwb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('nwb other')                 
        
        elif veh_num_dir_to[i] in ['south']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('wbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('ebr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('sbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('sb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('sb other') 

        elif veh_num_dir_to[i] in ['southeast','south-east']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('swbl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nebr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('sebt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('seb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('seb other') 

        elif veh_num_dir_to[i] in ['southwest','south-west']:
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nwbl')                              
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('sebr')                              
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('swbt')                              
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('swb misc. action')                              
            else:
                crash_set["Crash"+str(i+1)].append('swb other')                   
        
        elif veh_num_dir_to[i] == 'east':
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('sbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('nbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('ebt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('eb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('eb other')                                  
        
        elif veh_num_dir_to[i] == 'west':
            if veh_num_action[i] == "making left turn":
                crash_set["Crash"+str(i+1)].append('nbl')                                  
            elif veh_num_action[i] == "making right turn":
                crash_set["Crash"+str(i+1)].append('sbr')                                  
            elif veh_num_action[i] == "going straight ahead":
                crash_set["Crash"+str(i+1)].append('wbt')                                  
            elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
            "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
            "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
            "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
            "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                crash_set["Crash"+str(i+1)].append('wb misc. action')                                  
            else:
                crash_set["Crash"+str(i+1)].append('wb other')                                                          
        
        elif veh_num_dir_to[i] == 'na':
            crash_set["Crash"+str(i+1)].append('single vehicle crash')                          
        
        else:
            crash_set["Crash"+str(i+1)].append('unknown')                   
    
    else:
        crash_set["Crash"+str(i+1)].append('is an intersection')        

#User selects specific intersection        
def dir_act_spec_intersections(veh_num_dir_to,veh_num_action,file_length,crash_set,i,junction_type,user_intersection, street, cross_street):

    if junction_type[i] == '1':
        temp = [street[i],cross_street[i]]
        temp = sorted(temp)
        intersection = temp[0] + '/' + temp[1]
        
        if intersection not in [user_intersection]:
            crash_set["Crash"+str(i+1)].append('not right intersection')
        
        else:
            
            if veh_num_dir_to[i] in ['north']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('ebl')                                      
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('wbr')                                      
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('nbt')                                      
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('nb misc. action')                                      
                else:
                    crash_set["Crash"+str(i+1)].append('nb other') 

            elif veh_num_dir_to[i] in ['northeast','north-east']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('sebl')                              
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('nwbr')                              
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('nebt')                              
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('neb misc. action')                              
                else:
                    crash_set["Crash"+str(i+1)].append('neb other')  

            elif veh_num_dir_to[i] in ['northwest','north-west']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('nebl')                              
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('swbr')                              
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('nwbt')                              
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('nwb misc. action')                              
                else:
                    crash_set["Crash"+str(i+1)].append('nwb other')                     
            
            elif veh_num_dir_to[i] in ['south']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('wbl')                                      
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('ebr')                                      
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('sbt')                                      
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('sb misc. action')                                      
                else:
                    crash_set["Crash"+str(i+1)].append('sb other') 

            elif veh_num_dir_to[i] in ['southeast','south-east']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('swbl')                              
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('nebr')                              
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('sebt')                              
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('seb misc. action')                              
                else:
                    crash_set["Crash"+str(i+1)].append('seb other') 

            elif veh_num_dir_to[i] in ['southwest','south-west']:
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('nwbl')                              
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('sebr')                              
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('swbt')                              
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('swb misc. action')                              
                else:
                    crash_set["Crash"+str(i+1)].append('swb other')                       
            
            elif veh_num_dir_to[i] == 'east':
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('sbl')                                      
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('nbr')                                      
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('ebt')                                      
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('eb misc. action')                                      
                else:
                    crash_set["Crash"+str(i+1)].append('eb other')                                      
            
            elif veh_num_dir_to[i] == 'west':
                if veh_num_action[i] == "making left turn":
                    crash_set["Crash"+str(i+1)].append('nbl')                                      
                elif veh_num_action[i] == "making right turn":
                    crash_set["Crash"+str(i+1)].append('sbr')                                      
                elif veh_num_action[i] == "going straight ahead":
                    crash_set["Crash"+str(i+1)].append('wbt')                                      
                elif veh_num_action[i] in ["overtaking and passing","making u-turn","slowing","stopped for traffic",
                "stopped at signal or stop sign","stopped in roadway","starting in traffic lane","starting from parked position",
                "merging(entering traffic)","legally parked,occupied","legally parked,unoccupied","backing",
                "going wrong way on divided hwy","going wrong way on ramp","going wrong way on one-way street or road",
                "changing lanes","illegally parked,occupied","illegally parked,unoccupied"]:
                    crash_set["Crash"+str(i+1)].append('wb misc. action')                                      
                else:
                    crash_set["Crash"+str(i+1)].append('wb other')                                                                              
            
            elif veh_num_dir_to[i] == 'na':
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
        crash_counts[un_move] = [0,0,0,0,0,0]#These are for the 6 different crash sevs
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])
        crash_counts[un_move].append([])

    #Compare the vehicle movements to the unique set of movements, in order to count
    #up all crashes with the same movements. Then I'm adding crash characteristics to
    #dictionary
    #Print example: {'ebl/wbt' : [1671, 0, 15, 444, 1212, 2,
    #['veh - rear end', 'veh - rear end'], ['inattention','intoxicated'],
    #['12:56','01:23'], ['dry','wet'], ['clear','rainy'], ['daylight','daylight']}
    for un_move in unique_movements:
        i = 0
        while i < len(file_length):
            if un_move == veh_movements[i]:
                crash_counts[un_move][0] += 1
                if cr_severities[i] in ['dead at scene','died in hospital','dead on arrival']:
                    crash_counts[un_move][1] += 1
                elif cr_severities[i] in ['serious injury','suspected serious injury']:
                    crash_counts[un_move][2] += 1
                elif cr_severities[i] in ['possible injury','evident injury',
                                          'suspected minor injury']:
                    crash_counts[un_move][3] += 1
                elif cr_severities[i] in ['no injury','no apparent injury']:
                    crash_counts[un_move][4] += 1
                elif cr_severities[i]:
                    crash_counts[un_move][5] += 1
                crash_counts[un_move][6].append(cr_types[i])
                crash_counts[un_move][7].append(cr_behaviors[i])
                crash_counts[un_move][8].append(cr_time[i])
                crash_counts[un_move][9].append(cr_weather[i])
                crash_counts[un_move][10].append(cr_light[i])
                crash_counts[un_move][11].append(cr_ids[i])
                crash_counts[un_move][12].append(cr_surf[i])
            i +=1

    #Turn dictionary into list
    #Print example:
    #['ebl/wbt', [1671, 0, 15, 444, 1212,
    #['veh - rear end', 'veh - rear end'], ['inattention','intoxicated'],
    #['12:56','01:23'], ['dry','wet'], ['clear','rainy'], ['daylight','daylight']]
    crashes_list = []
    for key,value in crash_counts.items():
        crashes_list.append([key,(value)])

    if sort_by == 'total crashes':   
        crashes_list.sort(key = lambda x: x[1])
        crashes_list.reverse()
    elif sort_by == 'fatal crashes':   
        crashes_list.sort(key = lambda x: x[1][1])
        crashes_list.reverse()
    elif sort_by == 'fatal and serious injury crashes':
        for crash in crashes_list:
            f_i = crash[1][1] + crash[1][2]
            crash.insert(0,f_i)
        crashes_list.sort(key = lambda x: x[0])
        crashes_list.reverse()
        i = 0
        while i < len(crashes_list):
            del crashes_list[i][0]
            i += 1
    elif sort_by in 'fatal and all injury crashes':
        for crash in crashes_list:
            f_i = crash[1][1] + crash[1][2] +crash[1][3]
            crash.insert(0,f_i)
        crashes_list.sort(key = lambda x: x[0])
        crashes_list.reverse()
        i = 0
        while i < len(crashes_list):
            del crashes_list[i][0]
            i += 1

    #Reformat single vehicle crash with parentheses
    for i in range(len(crashes_list)):
        if 'single vehicle crash' in crashes_list[i][0]:
            import re
            crashes_list[i][0] = re.sub('single vehicle crash/','(single vehicle crash)',crashes_list[i][0])
            crashes_list[i][0] = re.sub('/single vehicle crash','(single vehicle crash)',crashes_list[i][0])

    return (crashes_list)
