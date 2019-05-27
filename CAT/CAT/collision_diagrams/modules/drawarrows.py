#Draws arrows based on 'arrow_movements.py' files in 'Modules' folder and sets up plots
#based on 'PlotText.py' file in respective state folder

def draw_arrows(fig_number,arrow_plots,crash,state,zs):

    from .plottext import plot_text
    import matplotlib.pyplot as plt    
    import matplotlib.patches as patches
    from .drawarrows import add_arrows_to_diagram

    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure(fig_number)

    add_arrows_to_diagram(arrow_plots)
    
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plot_text(crash,state)
    
    try:
        fig_name = str(fig_number) + '.png'
        zfm = zs.open(fig_name, 'w')
        plt.savefig(zfm, format='png')
        zfm.close()   
    except RuntimeError:
        pass
    else:
        pass   
            
def draw_arrows_ped_bike(fig_number,arrow_plots,crash,state,zs,x,y,move,zoom_factor):

    from .plottext import plot_text
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.cbook import get_sample_data
    from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)
    import matplotlib as mpl
    import os
    from .drawarrows import add_arrows_to_diagram, add_arrows_to_diagram_ped_bike

    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.clf()
    plt.figure(fig_number)
    
    add_arrows_to_diagram_ped_bike(crash,x,y,move,zoom_factor)
    add_arrows_to_diagram(arrow_plots)
        
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plot_text(crash,state) 
    
    fig_name = str(fig_number) + '.png'
    zfm = zs.open(fig_name, 'w')
    plt.savefig(zfm, format='png')   
    zfm.close()
  
def add_arrows_to_diagram(arrow_plots):

    import matplotlib.pyplot as plt    
    import matplotlib.patches as patches

    #Depending on how many arrows will be drawn
    if len(arrow_plots) in [4,8]:
        plt.gca().add_patch(arrow_plots[0])
        plt.gca().add_patch(arrow_plots[1])
        plt.gca().add_patch(arrow_plots[2])
        plt.gca().add_patch(arrow_plots[3])
    elif len(arrow_plots) == 3:
        plt.gca().add_patch(arrow_plots[0])
        plt.gca().add_patch(arrow_plots[1])
        plt.gca().add_patch(arrow_plots[2])
    elif len(arrow_plots) == 2:
        plt.gca().add_patch(arrow_plots[0])
        plt.gca().add_patch(arrow_plots[1])
    elif len(arrow_plots) == 1:
        plt.gca().add_patch(arrow_plots[0])
    else:
        pass  
           
def add_arrows_to_diagram_ped_bike(crash,x,y,move,zoom_factor):

    import matplotlib.pyplot as plt
    from matplotlib.cbook import get_sample_data
    from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)
    import matplotlib as mpl
    import os
    
    #Depending on how many arrows will be drawn
    mpl.rcParams['examples.directory'] = os.getcwd() + "\CAT"
    if 'bicyclist' in crash[0]:
        fn = get_sample_data('bike.png', asfileobj=False)
    else:
        fn = get_sample_data('pedestrian.png', asfileobj=False)
    arr_img = plt.imread(fn, format='png')
    move_left = ['pedestrian/nbl','pedestrian/wbt','pedestrian/sbr',
                 'bicyclist/nbl','bicyclist/wbt','bicyclist/sbr',
                 'pedestrian/wb misc. action','pedestrian/wb other',
                 'bicyclist/wb misc. action','bicyclist/wb other']
    move_right = ['pedestrian/nbr','pedestrian/ebt','pedestrian/sbl',
                  'bicyclist/nbr','bicyclist/ebt','bicyclist/sbl',
                  'pedestrian/eb misc. action','pedestrian/eb other',
                  'bicyclist/eb misc. action','bicyclist/eb other']
    move_up = ['pedestrian/ebl','pedestrian/nbt','pedestrian/wbr',
               'bicyclist/ebl','bicyclist/nbt','bicyclist/wbr',
               'pedestrian/nb misc. action','pedestrian/nb other',
               'bicyclist/nb misc. action','bicyclist/nb other']
    move_down = ['pedestrian/wbl','pedestrian/sbt','pedestrian/ebr',
                 'bicyclist/wbl','bicyclist/sbt','bicyclist/ebr',
                 'pedestrian/sb misc. action','pedestrian/sb other',
                 'bicyclist/sb misc. action','bicyclist/sb other']             
    
    imagebox = OffsetImage(arr_img, zoom=zoom_factor)
    
    if crash[0] in move_left[:]:
        xy = (x-move,y)
    elif crash[0] in move_right[:]:
        xy = (x+move,y)
    elif crash[0] in move_up[:]:
        xy = (x,y+move)
    elif crash[0] in move_down[:]:
        xy = (x,y-move)
    else:
        xy = (x,y)
    
    ab = AnnotationBbox(imagebox, xy,xybox=(0.00001,0.00001),xycoords='data',boxcoords="offset points",
                        pad=0.0,arrowprops=dict(arrowstyle="->",
                                                connectionstyle="angle,angleA=0,angleB=90,rad=3"))
    #Plot arrows and save fig
    plt.gca().add_artist(ab) 