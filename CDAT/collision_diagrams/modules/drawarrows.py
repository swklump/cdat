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
    mpl.rcParams['examples.directory'] = os.getcwd() + "\CDAT"
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
    from .arrow_movements import arrow_movements, arrow_movements_misc_thru, arrow_movements_thru_thru,\
    arrow_movements_misc_misc,arrow_movements_misc_other, arrow_movements_turning, \
    arrow_movements_turning_bothturns, arrow_movements_turning_bothturns_opposite

    from .arrow_movements_nonstandard import arrow_movements_misc_thru_x, arrow_movements_thru_thru_x,\
    arrow_movements_misc_misc_x, arrow_movements_misc_other_x, arrow_movements_turning_x, \
    arrow_movements_turning_bothturns_x, arrow_movements_turning_bothturns_opposite_x
    
    if '/' in crash[0]:
        index = crash[0].find('/')
        if crash[0] in ['eb misc. action/ebt','eb other/ebt','nb misc. action/nbt','nb other/nbt',
                        'sb misc. action/sbt','sb other/sbt','wb misc. action/wbt','wb other/wbt']:
            arrow_movements = arrow_movements_misc_thru(x,y,r)
        elif crash[0] in ['neb misc. action/nebt','neb other/nebt','nwb misc. action/nwbt','nwb other/nwbt',
                        'seb misc. action/sebt','seb other/sebt','swb misc. action/swbt','swb other/swbt']:
            arrow_movements = arrow_movements_misc_thru_x(x,y,r)        
        
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
        elif crash[0] in ['nebt/nebt','nwbt/nwbt','sebt/sebt','nwbt/nwbt']: 
            arrow_movements = arrow_movements_thru_thru_x(x,y,r)            
        
        elif crash[0] in ['ebl/nbt','nbt/wbr','ebt/sbl','ebt/nbr','ebr/sbt','sbt/wbl','sbr/wbt','nbl/wbt',
                          'ebl/nb misc. action','nb misc. action/wbr','eb misc. action/sbl','eb misc. action/nbr',
                          'ebr/sb misc. action','sb misc. action/wbl','sbr/wb misc. action','nbl/wb misc. action',
                          'ebl/nb other','nb other/wbr','eb other/sbl','eb other/nbr',
                          'ebr/sb other','sb other/wbl','sbr/wb other','nbl/wb other']:
            arrow_movements = arrow_movements_turning(x,y,r)
        elif crash[0] in ['nwbt/swbr','nebr/sebt','sebt/swbl','nebl/nwbt','nebr/seb misc. action','nwbl/swbt']:#continue
            arrow_movements = arrow_movements_turning_x(x,y,r)    
        
        elif crash[0] in ['ebl/ebl','ebr/ebr','nbl/nbl','nbr/nbr',
                          'sbl/sbl','sbr/sbr','wbl/wbl','wbr/wbr']:
            arrow_movements = arrow_movements_turning_bothturns(x,y,r)
        
        elif crash[0] in ['ebr/wbl','nbr/sbl','nbl/sbr','ebl/wbr']:
            arrow_movements = arrow_movements_turning_bothturns_opposite(x,y,r)          
        
        elif crash[0] in ['not right intersection','not an intersection']:
            pass
    
        else:
            arrow_movements = arrow_movements(x,y,r)
        
    elif '(' in crash[0]:
        if '(' == crash[0][0]:
            index = crash[0].find(')')
        else:
            index = crash[0].find('(')
            
        arrow_movements = arrow_movements(x,y,r)      
    
    return arrow_movements, index    