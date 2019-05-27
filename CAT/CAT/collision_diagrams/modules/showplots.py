#Shows plots based on 'arrow_movements.py' files in 'Modules' folder and
#'PlotText.py' file in respective state folder

#Allows for filtering of how many diagrams to show
def plot_loop(crashes_list,diagram_filter,state, ped_bike_filter, file_length, zs):

    from .showplots import show_plots, circles_func
    
    fig_number = 0
    diagram_filter = int(diagram_filter)
    diagram_filter -= 1 #Because of indexing starting at 0
    diagram_total = 0
    crashids = []
    unknown_crashids = []
    
    
    i = 0
    try:
        
        while diagram_total <= diagram_filter:
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
    
    
    #Intersection level diagrams
    from .plottext import plot_text
    from .drawarrows import add_arrows_to_diagram,add_arrows_to_diagram_ped_bike
    import matplotlib.pyplot as plt    
    import matplotlib.patches as patches

    #Intersection level diagram 1
    top_movements = []
    i = 0
    n = 0
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure()
    
    num_ped_bike = -1
    for crash in crashes_list:
        if 'pedestrian' in crash[0] or 'bicyclist' in crash[0]:
            num_ped_bike += 1
    if ped_bike_filter == 'pedestrian and bicyclist crashes only':
        num_images = min(num_ped_bike, 9)
    else:
        num_images = 9
    
    try:
        while n < num_images:
            index = show_plots_intersection(crashes_list[i],zs,top_movements,n,ped_bike_filter)
            if crashes_list[i][0][0:index] in ['pedestrian','bicyclist'] or crashes_list[i][0][index+1:] in ['pedestrian','bicyclist']:
                if n == 0:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,3.25,0.35,0.078)
                    plt.text(-4.5, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 1:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,3.25,0.35,0.078)
                    plt.text(-1.25, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 2:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,3.25,0.35,0.078)
                    plt.text(2.25, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 3:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,0,0.35,0.078)
                    plt.text(-4.5, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 4:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,0,0.35,0.078)
                    plt.text(-1.25, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 5:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,0,0.35,0.078)
                    plt.text(2.25, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 6:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,-3.25,0.35,0.078)
                    plt.text(-4.5, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 7:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,-3.25,0.35,0.078)
                    plt.text(-1.25, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n == 8:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,-3.25,0.35,0.078)   
                    plt.text(2.25, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    
                n += 1
            else:
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    n += 1
            i += 1
    except IndexError:
        pass
    else:
        pass       

    for arrow_plots in top_movements:
        add_arrows_to_diagram(arrow_plots)    
    
    if ped_bike_filter not in ['pedestrian and bicyclist crashes only']:
        try:            
            plt.text(-4.5, 2.125, crashes_list[0][1][0],horizontalalignment='center', fontsize=6)    
            plt.text(-1.25, 2.125, crashes_list[1][1][0],horizontalalignment='center', fontsize=6)
            plt.text(2.25, 2.125, crashes_list[2][1][0],horizontalalignment='center', fontsize=6)
            
            plt.text(-4.5, -1.375, crashes_list[3][1][0],horizontalalignment='center', fontsize=6)
            plt.text(-1.25, -1.375, crashes_list[4][1][0],horizontalalignment='center', fontsize=6)
            plt.text(2.25, -1.375, crashes_list[5][1][0],horizontalalignment='center', fontsize=6)
            
            plt.text(-4.5, -4.625, crashes_list[6][1][0],horizontalalignment='center', fontsize=6)
            plt.text(-1.25, -4.625, crashes_list[7][1][0],horizontalalignment='center', fontsize=6)
            plt.text(2.25, -4.625, crashes_list[8][1][0],horizontalalignment='center', fontsize=6)
        
            if state in ['alaska','florida','washington']:
                plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[0][1][1]+crashes_list[0][1][2]+crashes_list[0][1][3])/crashes_list[0][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[1][1][1]+crashes_list[1][1][2]+crashes_list[1][1][3])/crashes_list[1][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[2][1][1]+crashes_list[2][1][2]+crashes_list[2][1][3])/crashes_list[2][1][0]),horizontalalignment='center', fontsize=6)
                
                plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[3][1][1]+crashes_list[3][1][2]+crashes_list[3][1][3])/crashes_list[3][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[4][1][1]+crashes_list[4][1][2]+crashes_list[4][1][3])/crashes_list[4][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[5][1][1]+crashes_list[5][1][2]+crashes_list[5][1][3])/crashes_list[5][1][0]),horizontalalignment='center', fontsize=6)
                
                plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[6][1][1]+crashes_list[6][1][2]+crashes_list[6][1][3])/crashes_list[6][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[7][1][1]+crashes_list[7][1][2]+crashes_list[7][1][3])/crashes_list[7][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[8][1][1]+crashes_list[8][1][2]+crashes_list[8][1][3])/crashes_list[8][1][0]),horizontalalignment='center', fontsize=6)
                
            elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[0][1][1]+crashes_list[0][1][2])/crashes_list[0][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[1][1][1]+crashes_list[1][1][2])/crashes_list[1][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[2][1][1]+crashes_list[2][1][2])/crashes_list[2][1][0]),horizontalalignment='center', fontsize=6)
                
                plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[3][1][1]+crashes_list[3][1][2])/crashes_list[3][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[4][1][1]+crashes_list[4][1][2])/crashes_list[4][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[5][1][1]+crashes_list[5][1][2])/crashes_list[5][1][0]),horizontalalignment='center', fontsize=6)

                plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[6][1][1]+crashes_list[6][1][2])/crashes_list[6][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[7][1][1]+crashes_list[7][1][2])/crashes_list[7][1][0]),horizontalalignment='center', fontsize=6)
                plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[8][1][1]+crashes_list[8][1][2])/crashes_list[8][1][0]),horizontalalignment='center', fontsize=6)     
    
        except IndexError:
            pass
        else:
            pass

    circles = circles_func()
    for circle in circles:
        plt.gca().add_patch(circle)
        
    plt.axes().set_xlim(-5, 5)
    plt.axes().set_ylim(-5, 5)
    plt.axes().set_aspect(1)

    plt.xticks([-1.75,1.75])
    plt.yticks([-1.75,1.75])
    plt.grid()
    
    fig_name = str('00_entire_intersection') + '.png'
    zfm = zs.open(fig_name, 'w')
    plt.savefig(zfm, format='png')
    zfm.close()
    
    # Intersection level diagram 2
    top_movements = []
    i = 9
    try:
        while i < 18:
            plots_temp = show_plots_intersection(crashes_list[i],zs,top_movements,i,ped_bike_filter)
            i += 1
    except IndexError:
        pass
    else:
        pass        

    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure()
    
    for arrow_plots in top_movements:
        add_arrows_to_diagram(arrow_plots)            
    
    try:            
        plt.text(-4.5, 2.125, crashes_list[9][1][0],horizontalalignment='center', fontsize=6)    
        plt.text(-1.25, 2.125, crashes_list[10][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, 2.125, crashes_list[11][1][0],horizontalalignment='center', fontsize=6)
        
        plt.text(-4.5, -1.375, crashes_list[12][1][0],horizontalalignment='center', fontsize=6)
        plt.text(-1.25, -1.375, crashes_list[13][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, -1.375, crashes_list[14][1][0],horizontalalignment='center', fontsize=6)
        
        plt.text(-4.5, -4.625, crashes_list[15][1][0],horizontalalignment='center', fontsize=6)
        plt.text(-1.25, -4.625, crashes_list[16][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, -4.625, crashes_list[17][1][0],horizontalalignment='center', fontsize=6)
    
        if state in ['alaska','florida','washington']:
            plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[9][1][1]+crashes_list[9][1][2]+crashes_list[9][1][3])/crashes_list[9][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[10][1][1]+crashes_list[10][1][2]+crashes_list[10][1][3])/crashes_list[10][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[11][1][1]+crashes_list[11][1][2]+crashes_list[11][1][3])/crashes_list[11][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[12][1][1]+crashes_list[12][1][2]+crashes_list[12][1][3])/crashes_list[12][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[13][1][1]+crashes_list[13][1][2]+crashes_list[13][1][3])/crashes_list[13][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[14][1][1]+crashes_list[14][1][2]+crashes_list[14][1][3])/crashes_list[14][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[15][1][1]+crashes_list[15][1][2]+crashes_list[15][1][3])/crashes_list[15][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[16][1][1]+crashes_list[16][1][2]+crashes_list[16][1][3])/crashes_list[16][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[17][1][1]+crashes_list[17][1][2]+crashes_list[17][1][3])/crashes_list[17][1][0]),horizontalalignment='center', fontsize=6)
            
        elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
            plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[9][1][1]+crashes_list[9][1][2])/crashes_list[9][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[10][1][1]+crashes_list[10][1][2])/crashes_list[10][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[11][1][1]+crashes_list[11][1][2])/crashes_list[11][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[12][1][1]+crashes_list[12][1][2])/crashes_list[12][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[13][1][1]+crashes_list[13][1][2])/crashes_list[13][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[14][1][1]+crashes_list[14][1][2])/crashes_list[14][1][0]),horizontalalignment='center', fontsize=6)

            plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[15][1][1]+crashes_list[15][1][2])/crashes_list[15][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[16][1][1]+crashes_list[16][1][2])/crashes_list[16][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[17][1][1]+crashes_list[17][1][2])/crashes_list[17][1][0]),horizontalalignment='center', fontsize=6)                                   
    
    except IndexError:
        pass
    else:
        pass

    circles = circles_func()     
    for circle in circles:
        plt.gca().add_patch(circle)
        
    plt.axes().set_xlim(-5, 5)
    plt.axes().set_ylim(-5, 5)
    plt.axes().set_aspect(1)

    plt.xticks([-1.75,1.75])
    plt.yticks([-1.75,1.75])
    plt.grid()
    
    fig_name = str('00_entire_intersection2') + '.png'
    zfm = zs.open(fig_name, 'w')
    plt.savefig(zfm, format='png')
    zfm.close()
       
    return crashids, unknown_crashids
    
def show_plots(crash,fig_number,state,diagram_total,crashids,unknown_crashids,zs,i,ped_bike_filter):
   
    from .drawarrows import draw_arrows, draw_arrows_ped_bike 
    from .showplots import assign_arrows
    
    temp_assign_arrows = assign_arrows(crash,0,0,0.125) 
    arrow_movements = temp_assign_arrows[0]
    index = temp_assign_arrows[1]
    arrow_plots = []
    temp_crashids = []
    
    if crash[0][0:index] == crash[0][index+1:]:
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

def show_plots_intersection(crash,zs,top_movements,i,ped_bike_filter):

    from .drawarrows import draw_arrows, draw_arrows_ped_bike    
    from .arrow_movements import arrow_movements
    from .showplots import assign_arrows
    
    if i in [0,9]:
        temp_assign_arrows = assign_arrows(crash,-3.25,3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [1,10]:
        temp_assign_arrows = assign_arrows(crash,0,3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [2,11]:
        temp_assign_arrows = assign_arrows(crash,3.25,3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [3,12]:
        temp_assign_arrows = assign_arrows(crash,-3.25,0,0.125) 
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [4,13]:
        temp_assign_arrows = assign_arrows(crash,0,0,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [5,14]:
        temp_assign_arrows = assign_arrows(crash,3.25,0,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [6,15]:        
        temp_assign_arrows = assign_arrows(crash,-3.25,-3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [7,16]:
        temp_assign_arrows = assign_arrows(crash,0,-3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]
    elif i in [8,17]:
        temp_assign_arrows = assign_arrows(crash,3.25,-3.25,0.125)
        arrow_movements = temp_assign_arrows[0]
        index = temp_assign_arrows[1]        
        
    arrow_plots = []

    if '/' in crash[0]:
        index = crash[0].find('/')
    elif '(' in crash[0]:
        if '(' == crash[0][0]:
            index = crash[0].find(')')
        else:
            index = crash[0].find('(')

    if crash[0][0:index] == crash[0][index+1:]:
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
        top_movements.append(arrow_plots)
    else:
        if ped_bike_filter == 'pedestrian and bicyclist crashes only':
            pass
        else:
            top_movements.append(arrow_plots)

    return index
    
def circles_func():
    import matplotlib.pyplot as plt
    
    circles = []        
    circles.append(plt.Circle((-2.25,2.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((-4.5,2.25),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((1.25,2.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((-1.25,2.25),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((4.5,2.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((2.25,2.25),0.4,color='black',fill=False))
    
    
    circles.append(plt.Circle((-2.25,-1.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((-4.5,-1.25),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((1.25,-1.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((-1.25,-1.25),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((4.5,-1.25),0.4,color='red',fill=False))
    circles.append(plt.Circle((2.25,-1.25),0.4,color='black',fill=False))       
    
    
    circles.append(plt.Circle((-2.25,-4.5),0.4,color='red',fill=False))
    circles.append(plt.Circle((-4.5,-4.5),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((1.25,-4.5),0.4,color='red',fill=False))
    circles.append(plt.Circle((-1.25,-4.5),0.4,color='black',fill=False))
    
    circles.append(plt.Circle((4.5,-4.5),0.4,color='red',fill=False))
    circles.append(plt.Circle((2.25,-4.5),0.4,color='black',fill=False))
    
    return circles 

def assign_arrows(crash,x,y,r):
    from .drawarrows import draw_arrows, draw_arrows_ped_bike 
    from .arrow_movements import arrow_movements, arrow_movements_misc_thru, arrow_movements_thru_thru,arrow_movements_misc_misc,arrow_movements_misc_other, arrow_movements_turning, arrow_movements_turning_bothturns, arrow_movements_turning_bothturns_opposite
    
    if '/' in crash[0]:
        index = crash[0].find('/')
        if crash[0] in ['eb misc. action/ebt','eb other/ebt','nb misc. action/nbt','nb other/nbt',
                        'sb misc. action/sbt','sb other/sbt','wb misc. action/wbt','wb other/wbt']:
            arrow_movements = arrow_movements_misc_thru(x,y,r)
        
        elif crash[0] in ['eb misc. action/eb misc. action','eb other/eb other',
                          'nb misc. action/nb misc. action','nb other/nb other',
                          'sb misc. action/sb misc. action','sb other/sb other',
                          'wb misc. action/wb misc. action','wb other/wb other']: 
            arrow_movements = arrow_movements_misc_misc(x,y,r)
                
        elif crash[0] in ['eb misc. action/eb other','nb misc. action/nb other',
                          'sb misc. action/sb other','wb misc. action/wb other']:
            arrow_movements = arrow_movements_misc_other(x,y,r)                                
            
        elif crash[0] in ['ebt/ebt','nbt/nbt','sbt/sbt','wbt/wbt']: 
            arrow_movements = arrow_movements_thru_thru(x,y,r)
        
        elif crash[0] in ['ebl/nbt','nbt/wbr','ebt/sbl','ebt/nbr','ebr/sbt','sbt/wbl','sbr/wbt','nbl/wbt',
                          'ebl/nb misc. action','nb misc. action/wbr','eb misc. action/sbl','eb misc. action/nbr',
                          'ebr/sb misc. action','sb misc. action/wbl','sbr/wb misc. action','nbl/wb misc. action',
                          'ebl/nb other','nb other/wbr','eb other/sbl','eb other/nbr',
                          'ebr/sb other','sb other/wbl','sbr/wb other','nbl/wb other']:
            arrow_movements = arrow_movements_turning(x,y,r)
        
        elif crash[0] in ['ebl/ebl','ebr/ebr','nbl/nbl','nbr/nbr',
                          'sbl/sbl','sbr/sbr','wbl/wbl','wbr/wbr']:
            arrow_movements = arrow_movements_turning_bothturns(x,y,r)
        
        elif crash[0] in ['ebr/wbl','nbr/sbl','nbl/sbr','ebl/wbr']:
            arrow_movements = arrow_movements_turning_bothturns_opposite(x,y,r)        
        else:
            arrow_movements = arrow_movements(x,y,r)
        
    elif '(' in crash[0]:
        if '(' == crash[0][0]:
            index = crash[0].find(')')
        else:
            index = crash[0].find('(')
        arrow_movements = arrow_movements(x,y,r)      
    
    return arrow_movements, index