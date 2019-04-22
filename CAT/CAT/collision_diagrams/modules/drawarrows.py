#Draws arrows based on 'arrow_movements.py' files in 'Modules' folder and sets up plots
#based on 'PlotText.py' file in respective state folder

def draw_arrows(fig_number,arrows,crash,state,ped_bike_filter):

    from .plottext import plot_text
    import matplotlib.pyplot as plt
    #Need to make images with figure, write name as file-like object (stream)https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure
    import matplotlib.patches as patches
    import os

    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure(fig_number)

    #Depending on how many arrows will be drawn
    if len(arrows) == 4:
        plt.gca().add_patch(arrows[0])
        plt.gca().add_patch(arrows[1])
        plt.gca().add_patch(arrows[2])
        plt.gca().add_patch(arrows[3])
    elif len(arrows) == 3:
        plt.gca().add_patch(arrows[0])
        plt.gca().add_patch(arrows[1])
        plt.gca().add_patch(arrows[2])
    elif len(arrows) == 2:
        plt.gca().add_patch(arrows[0])
        plt.gca().add_patch(arrows[1])
    else:
        plt.gca().add_patch(arrows[0])
        
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plot_text(crash,state)
    
    if ped_bike_filter in ['pedestrian and bicyclist crashes only']:
        pass
    else:
        try:
            cwd = os.getcwd()
            diagram_folder = cwd + '\diagram_prints/'
            fig_name = diagram_folder + str(fig_number) + '.png'
            plt.savefig(fig_name)    
        except RuntimeError:
            pass
        else:
            pass
   
#Draws arrows based on 'arrow_movements.py' files in 'Modules' folder and sets up plots
#based on 'PlotText.py' file in respective state folder, for peds and bikes

def draw_arrows_ped_bike(fig_number,arrows,crash,state):

    from .plottext import plot_text
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
    from matplotlib.cbook import get_sample_data
    from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)

    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure(fig_number)

    #Add image. https://stackoverflow.com/questions/3765056/combine-picture-and-plot-with-python-matplotlib
    if 'bicyclist' in crash[0]:
        fn = get_sample_data("bike.png", asfileobj=False)
    else:
        fn = get_sample_data("pedestrian.png", asfileobj=False)
    arr_img = plt.imread(fn, format='png')
    move_left = ['pedestrian/nbl','pedestrian/wbt','pedestrian/sbr',
                 'bicyclist/nbl','bicyclist/wbt','bicyclist/sbr']
     
    imagebox = OffsetImage(arr_img, zoom=0.156)
    if crash[0] in move_left[:]:
        xy = (-1,0)
    else:
        xy = (0.00001,0.00001)
    ab = AnnotationBbox(imagebox, xy,xybox=(0.00001,0.00001),xycoords='data',boxcoords="offset points",
                        pad=0.0,arrowprops=dict(arrowstyle="->",
                                                connectionstyle="angle,angleA=0,angleB=90,rad=3"))
    #Plot arrows and save fig
    plt.gca().add_artist(ab)
    plt.gca().add_patch(arrows[0])
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plot_text(crash,state)   
    cwd = os.getcwd()
    diagram_folder = cwd + '\diagram_prints/'
    fig_name = diagram_folder + str(fig_number) + '.png'
    plt.savefig(fig_name) 
    
