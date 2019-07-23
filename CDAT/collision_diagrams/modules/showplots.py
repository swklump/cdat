#Shows plots based on 'arrow_movements.py' files in 'Modules' folder and
#'PlotText.py' file in respective state folder

#Allows for filtering of how many diagrams to show
def plot_loop(crashes_list,state, ped_bike_filter, file_length, zs):

    from .drawarrows import circles_func
    
    fig_number = 0
    diagram_total = 0
    crashids = []
    unknown_crashids = []
        
    i = 0
    try:
        
        while diagram_total < len(file_length):
            plots_temp = show_plots(crashes_list[i],fig_number,state,diagram_total,crashids,unknown_crashids,zs,i,ped_bike_filter)
            fig_number = plots_temp[0]
            diagram_total = plots_temp[1]
            crashids = plots_temp[2]
            unknown_crashids = plots_temp[3]
                       
            i += 1            
    
    except IndexError:
        pass
    else:
        pass        
       
    return crashids, unknown_crashids
    
def show_plots(crash,fig_number,state,diagram_total,crashids,unknown_crashids,zs,i,ped_bike_filter):
   
    from .drawarrows import draw_arrows, draw_arrows_ped_bike, assign_arrows
    
    temp_assign_arrows = assign_arrows(crash,0,0,0.125) 
    arrow_movements = temp_assign_arrows[0]
    index = temp_assign_arrows[1]
    arrow_plots = []
    temp_crashids = []
    
    if crash[0][0:index] in ['not right intersection','not an intersection'] or crash[0][index+1:] in ['not right intersection','not an intersection']:
        pass
    elif crash[0][0:index] == crash[0][index+1:]:
        for lookup, arrows in arrow_movements.items():                    
            if crash[0][0:index] == lookup:
                for arr in arrows:
                    arrow_plots.append(arr)
                for arr in arrows:
                    arrow_plots.append(arr)
                    
    else:
        for lookup, arrows in arrow_movements.items():
            if crash[0][0:index] == lookup:
                for arr in arrows:
                    arrow_plots.append(arr)
                for lookup1, arrows1 in arrow_movements.items():
                        if crash[0][index+1:] == lookup1:                                               
                            for arr in arrows1:
                                arrow_plots.append(arr)                              
        
    if crash[0][0:index] in ['pedestrian','bicyclist'] or crash[0][index+1:] in ['pedestrian','bicyclist']:
        if crash[0][0:index] in ['not right intersection','not an intersection'] or crash[0][index+1:] in ['not right intersection','not an intersection']:
            pass
        else:
            draw_arrows_ped_bike(fig_number,arrow_plots,crash,state,zs,0,0,0.5,0.156)
            diagram_total += crash[1][0]
        
        fig_number += 1
        if state in ['alaska', 'florida', 'newyork','washington']:   
            if 'unknown' in crash[0]:
                for k_crash in crash[1][11]:
                    unknown_crashids.append(k_crash)
            for k_crash in crash[1][11]:
                temp_crashids.append(k_crash)
                
        elif state in ['nebraska','nevada','oregon']:
            if 'unknown' in crash[0]:
                for k_crash in crash[1][10]:
                    unknown_crashids.append(k_crash)   
            for k_crash in crash[1][10]:
                    temp_crashids.append(k_crash)                
        elif state in ['colorado']:
            pass #Colorado does not have crash IDS!
    
    else:
        if ped_bike_filter == 'pedestrian and bicyclist crashes only':
            pass
        else:   
            if crash[0][0:index] in ['not right intersection','not an intersection'] or crash[0][index+1:] in ['not right intersection','not an intersection']:
                pass
            else:
                draw_arrows(fig_number,arrow_plots,crash,state,zs)
                diagram_total += crash[1][0]
                fig_number += 1
                if state in ['alaska', 'florida', 'newyork','washington']:   
                    if 'unknown' in crash[0]:
                        for k_crash in crash[1][11]:
                            unknown_crashids.append(k_crash)
                    for k_crash in crash[1][11]:
                        temp_crashids.append(k_crash)
                        
                elif state in ['nebraska','nevada','oregon']:
                    if 'unknown' in crash[0]:
                        for k_crash in crash[1][10]:
                            unknown_crashids.append(k_crash)   
                    for k_crash in crash[1][10]:
                            temp_crashids.append(k_crash)                
                elif state in ['colorado']:
                    pass #Colorado does not have crash IDS!
    
    crashids.append(temp_crashids)
    
    return fig_number, diagram_total, crashids, unknown_crashids    