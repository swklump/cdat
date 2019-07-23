#Creates 2 collision diagrams for intersection overview (top 18 movements)

def plot_loop_intersection(crashes_list,state, ped_bike_filter, zs):
    #Intersection level diagrams
    from .plottext import plot_text
    from .drawarrows import add_arrows_to_diagram,add_arrows_to_diagram_ped_bike,circles_func
    import matplotlib.pyplot as plt    
    import matplotlib.patches as patches

    #INTERSECTION LEVEL DIAGRAM 1
    top_movements = []
    i = 0
    n = 0
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure()
    
    num_ped_bike = 0
    for crash in crashes_list:
        if 'pedestrian' in crash[0] or 'bicyclist' in crash[0]:
            num_ped_bike += 1
    if ped_bike_filter == 'pedestrian and bicyclist crashes only':
        num_images = min(num_ped_bike, 9)
    else:
        num_images = 9

    #Add images and text to plots
    x = add_images_text_pedbike(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state) 

    for arrow_plots in top_movements:
        add_arrows_to_diagram(arrow_plots)
    
    if ped_bike_filter not in ['pedestrian and bicyclist crashes only']:
        add_images_text(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state)
    
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
    
    # INTERSECTION LEVEL DIAGRAM 2
    if ped_bike_filter == 'pedestrian and bicyclist crashes only':
        num_images = min(num_ped_bike, 18)
    else:
        num_images = 18
    n = 9
    
    top_movements = []
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure()
    
    if ped_bike_filter in ['pedestrian and bicyclist crashes only']:
        i = x
        i += 1
        add_images_text_pedbike(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state)
    
    elif ped_bike_filter not in ['pedestrian and bicyclist crashes only']:
        i = 9
        add_images_text_pedbike(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state)
        add_images_text(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state)
          

    for arrow_plots in top_movements:
        add_arrows_to_diagram(arrow_plots)            

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
    
def show_plots_intersection(crash,zs,top_movements,i,ped_bike_filter):

    from .drawarrows import draw_arrows, draw_arrows_ped_bike, assign_arrows   
    from .arrow_movements import arrow_movements 
    
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

def add_images_text_pedbike(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state):

    from .drawarrows import add_arrows_to_diagram, add_arrows_to_diagram_ped_bike, circles_func
    import matplotlib.pyplot as plt
    x = 0
    try:
        while n < num_images:
            index = show_plots_intersection(crashes_list[i],zs,top_movements,n,ped_bike_filter)
            if crashes_list[i][0][0:index] in ['pedestrian','bicyclist'] or crashes_list[i][0][index+1:] in ['pedestrian','bicyclist']:
                if n in [0,9]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,3.25,0.35,0.078)
                    plt.text(-4.5, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [1,10]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,3.25,0.35,0.078)
                    plt.text(-1.25, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [2,11]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,3.25,0.35,0.078)
                    plt.text(2.25, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [3,12]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,0,0.35,0.078)
                    plt.text(-4.5, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [4,13]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,0,0.35,0.078)
                    plt.text(-1.25, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [5,14]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,0,0.35,0.078)
                    plt.text(2.25, -1.375, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [6,15]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],-3.25,-3.25,0.35,0.078)
                    plt.text(-4.5, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [7,16]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],0,-3.25,0.35,0.078)
                    plt.text(-1.25, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                elif n in [8,17]:
                    add_arrows_to_diagram_ped_bike(crashes_list[i],3.25,-3.25,0.35,0.078)   
                    plt.text(2.25, -4.625, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)
                    if state in ['alaska','florida','washington']:
                        plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
                        plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
                    x = i
                if crashes_list[i][0][0:index] in ['not right intersection','not an intersection'] or crashes_list[i][0][index+1:] in ['not right intersection','not an intersection']:
                    pass
                else:
                    n += 1
            else:
                if ped_bike_filter == 'pedestrian and bicyclist crashes only':
                    pass
                else:
                    if crashes_list[i][0][0:index] in ['not right intersection','not an intersection'] or crashes_list[i][0][index+1:] in ['not right intersection','not an intersection']:
                        pass
                    else:
                        n += 1
            i += 1
    except IndexError:
        pass
    else:
        pass
    
    return x
        
def add_images_text(crashes_list,zs,top_movements,n,ped_bike_filter,i,num_images,state):

    import matplotlib.pyplot as plt
    
    try:            
        plt.text(-4.5, 2.125, crashes_list[i][1][0],horizontalalignment='center', fontsize=6)    
        plt.text(-1.25, 2.125, crashes_list[i+1][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, 2.125, crashes_list[i+2][1][0],horizontalalignment='center', fontsize=6)
        
        plt.text(-4.5, -1.375, crashes_list[i+3][1][0],horizontalalignment='center', fontsize=6)
        plt.text(-1.25, -1.375, crashes_list[i+4][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, -1.375, crashes_list[i+5][1][0],horizontalalignment='center', fontsize=6)
        
        plt.text(-4.5, -4.625, crashes_list[i+6][1][0],horizontalalignment='center', fontsize=6)
        plt.text(-1.25, -4.625, crashes_list[i+7][1][0],horizontalalignment='center', fontsize=6)
        plt.text(2.25, -4.625, crashes_list[i+8][1][0],horizontalalignment='center', fontsize=6)
    
        if state in ['alaska','florida','washington']:
            plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2]+crashes_list[i][1][3])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i+1][1][1]+crashes_list[i+1][1][2]+crashes_list[i+1][1][3])/crashes_list[i+1][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i+2][1][1]+crashes_list[i+2][1][2]+crashes_list[i+2][1][3])/crashes_list[i+2][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i+3][1][1]+crashes_list[i+3][1][2]+crashes_list[i+3][1][3])/crashes_list[i+3][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i+4][1][1]+crashes_list[i+4][1][2]+crashes_list[i+4][1][3])/crashes_list[i+4][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i+5][1][1]+crashes_list[i+5][1][2]+crashes_list[i+5][1][3])/crashes_list[i+5][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i+6][1][1]+crashes_list[i+6][1][2]+crashes_list[i+6][1][3])/crashes_list[i+6][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i+7][1][1]+crashes_list[i+7][1][2]+crashes_list[i+7][1][3])/crashes_list[i+7][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i+8][1][1]+crashes_list[i+8][1][2]+crashes_list[i+8][1][3])/crashes_list[i+8][1][0]),horizontalalignment='center', fontsize=6)
            
        elif state in ['colorado','nebraska', 'nevada','newyork','oregon']:
            plt.text(-2.25, 2.125, "{:.0%}".format((crashes_list[i][1][1]+crashes_list[i][1][2])/crashes_list[i][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, 2.125, "{:.0%}".format((crashes_list[i+1][1][1]+crashes_list[i+1][1][2])/crashes_list[i+1][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, 2.125, "{:.0%}".format((crashes_list[i+2][1][1]+crashes_list[i+2][1][2])/crashes_list[i+2][1][0]),horizontalalignment='center', fontsize=6)
            
            plt.text(-2.25, -1.375, "{:.0%}".format((crashes_list[i+3][1][1]+crashes_list[i+3][1][2])/crashes_list[i+3][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -1.375, "{:.0%}".format((crashes_list[i+4][1][1]+crashes_list[i+4][1][2])/crashes_list[i+4][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -1.375, "{:.0%}".format((crashes_list[i+5][1][1]+crashes_list[i+5][1][2])/crashes_list[i+5][1][0]),horizontalalignment='center', fontsize=6)

            plt.text(-2.25, -4.625, "{:.0%}".format((crashes_list[i+6][1][1]+crashes_list[i+6][1][2])/crashes_list[i+6][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(1.25, -4.625, "{:.0%}".format((crashes_list[i+7][1][1]+crashes_list[i+7][1][2])/crashes_list[i+7][1][0]),horizontalalignment='center', fontsize=6)
            plt.text(4.5, -4.625, "{:.0%}".format((crashes_list[i+8][1][1]+crashes_list[i+8][1][2])/crashes_list[i+8][1][0]),horizontalalignment='center', fontsize=6)                                   
    
    except IndexError:
        pass
    else:
        pass                   