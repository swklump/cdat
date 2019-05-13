#Shows plots based on 'arrow_movements.py' files in 'Modules' folder and
#'PlotText.py' file in respective state folder

def show_plots(crash,fig_number,state,ped_bike_filter,diagram_total, diagram_fi, unknown_crashids, unknown_crashnum, zs, known_crashids):

    from .drawarrows import draw_arrows, draw_arrows_ped_bike
    #There are different scenarios in order to position arrows correctly in plot
    if 'unknown' in crash[0]:
        if state in ['alaska', 'florida', 'newyork','washington']:
            for unk_crash in crash[1][11]:
                unknown_crashids.append(unk_crash)
            unknown_crashnum += len(crash[1][11])
        elif state in ['nebraska','oregon']:
            for unk_crash in crash[1][10]:
                unknown_crashids.append(unk_crash)            
            unknown_crashnum += len(crash[1][10])  
        elif state in ['nevada']:
            for unk_crash in crash[1][10]:
                unknown_crashids.append(unk_crash)            
            unknown_crashnum += len(crash[1][10])             
        
        elif state in ['colorado']:#Colorado does not have crash IDS!
            for unk_crash in crash[1][10]:
                unknown_crashids.append(unk_crash)            
            unknown_crashnum += len(crash[1][10])
            
    #In Scenario 1, pedestrian or bike crash
    elif 'pedestrian' in crash[0] or 'bicyclist' in crash[0]:
        from .arrow_movements1 import arrow_movements1
        arrow_movements = arrow_movements1()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                    
            if crash[0] == lookup:
                position = crash[0]
                draw_arrows_ped_bike(fig_number,arrows,crash,state,zs)
                
                diagram_total += crash[1][0]
                if state in ['alaska','washington']:
                    diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                    for k_crash in crash[1][11]:
                        known_crashids.append(k_crash)
                elif state in ['nebraska', 'nevada', 'newyork']:
                    diagram_fi += (crash[1][1] + crash[1][2])
                
                fig_number += 1
                
    #In Scenario 2, at least one miscellaneous action
    elif 'misc. action' in crash[0]:
        from .arrow_movements2 import arrow_movements2
        arrow_movements = arrow_movements2()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                    
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 3, crash is single vehicle, ex:'nbt/single vehicle crash'
    elif 'single vehicle crash' in crash[0]:
        from .arrow_movements3 import arrow_movements3
        arrow_movements = arrow_movements3()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 4, first letter equals 4th letter, ex: nbl/nbt              
    elif crash[0][0] == crash[0][4]:
        from .arrow_movements4 import arrow_movements4
        arrow_movements = arrow_movements4()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      

            if crash[0][0:3] == lookup[:] and crash[0][4:7] == lookup[:]:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

            elif crash[0][0:3] == lookup[0:3] and crash[0][4:7] == lookup[4:7]:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 5, 3rd and 7th letter equal 't', ex:'ebt/sbt'
    elif crash[0][2] == 't' and crash[0][6] == 't':
        from .arrow_movements5 import arrow_movements5
        arrow_movements = arrow_movements5()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 6, 3rd and 7th letter equal 'l', ex:'ebl/nbl'
    elif crash[0][2] == 'l' and crash[0][6] == 'l':
        from .arrow_movements6 import arrow_movements6
        arrow_movements = arrow_movements6()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 7, one left movement and one thru movement, ex:'ebt/nbl'
    elif crash[0][2] == 'l' and crash[0][6] == 't':        
        from .arrow_movements7 import arrow_movements7
        arrow_movements = arrow_movements7()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                     
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #Still Scenario 7
    elif crash[0][2] == 't' and crash[0][6] == 'l':
        from .arrow_movements7 import arrow_movements7
        arrow_movements = arrow_movements7()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                       
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 8, one right movement and one thru movement, ex:'ebr/sbt'
    elif crash[0][2] == 'r' or crash[0][6] == 'r':
        from .arrow_movements8 import arrow_movements8
        arrow_movements = arrow_movements8()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1

    #In Scenario 9, one "other" movement, ex:'nbt/nb other'
    elif 'other' in crash[0]:
        from .arrow_movements9 import arrow_movements9
        arrow_movements = arrow_movements9()
        veh_movements = arrow_movements[0]
        veh_dict = arrow_movements[1]
        for lookup, arrows in veh_dict.items():                                                                                                                                      
            if crash[0] == lookup:
                draw_arrows(fig_number,arrows,crash,state,ped_bike_filter,zs)
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    diagram_total += crash[1][0]
                    if state in ['alaska','washington']:
                        diagram_fi += (crash[1][1] + crash[1][2] + crash[1][3])
                        for k_crash in crash[1][11]:
                            known_crashids.append(k_crash)
                    elif state in ['nebraska', 'nevada', 'newyork']:
                        diagram_fi += (crash[1][1] + crash[1][2])
                    
                    fig_number += 1               
    
    return fig_number, diagram_total, diagram_fi, unknown_crashids, unknown_crashnum,known_crashids

#Allows for filtering of how many diagrams to show
def plot_loop(crashes_list,diagram_filter,state, ped_bike_filter, file_length, zs):

    from .showplots import show_plots

    fig_number = 0
    diagram_filter = int(diagram_filter)
    diagram_filter -= 1
    known_crashids = []
    unknown_crashnum = 0
    unknown_crashids = []
    diagram_total = 0
    diagram_fi = 0

    i = 0
    try:
        while fig_number <= diagram_filter:
            
            plots_temp = show_plots(crashes_list[i],fig_number,state, ped_bike_filter, diagram_total, diagram_fi,unknown_crashids, unknown_crashnum,zs,known_crashids)
            fig_number = plots_temp[0]
            diagram_total = plots_temp[1]
            diagram_fi = plots_temp[2]
            unknown_crashids = plots_temp[3]
            unknown_crashnum = plots_temp[4] 
            known_crashids = plots_temp[5]
            i += 1

    except IndexError:
        pass
    else:
        pass
        
    # total_accounted_for = int(round(diagram_total / len(file_length) * 100))
    fi_accounted_for = int(round(diagram_fi / len(file_length) * 100))

    return diagram_total, fi_accounted_for, unknown_crashids, unknown_crashnum, known_crashids