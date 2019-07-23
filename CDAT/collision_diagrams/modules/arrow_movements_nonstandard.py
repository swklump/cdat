#This module defines the arrows that go on the plots

#Miscellaneous action + thru arrows (so arrows don't overlap) DONE
def arrow_movements_misc_thru_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    nebt = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw)]    
    nwbt = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw)]
    sebt = [patches.FancyArrowPatch( (x-1.0, y+1.0), (x-0.2, y+0.2),**kw)]
    swbt = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw)]    
    
    nebmisc = [patches.FancyArrowPatch( (x, y), (x+0.8, y+0.8),**kw),plt.Circle( (x+0.4, y+0.4), r, color='blue')]
    nwbmisc = [patches.FancyArrowPatch( (x, y), (x-0.8, y+0.8),**kw),plt.Circle( (x-0.4, y+0.4), r, color='blue')]
    sebmisc = [patches.FancyArrowPatch( (x-0.2, y+0.2), (x+0.6, y-0.6),**kw),plt.Circle( (x+0.2, y-0.2), r, color='blue')]
    swbmisc = [patches.FancyArrowPatch( (x, y), (x-0.8, y-0.8),**kw),plt.Circle( (x-0.4, y-0.4), r, color='blue')]   
    
    nebother = [patches.FancyArrowPatch( (x, y), (x+0.8, y+0.8),**kw),plt.Rectangle( (x+0.3, y+0.3), r*1.25, r*1.25, fc='r')]
    nwbother = [patches.FancyArrowPatch( (x, y), (x-0.8, y+0.8),**kw),plt.Rectangle( (x-0.46, y+0.3), r*1.25, r*1.25, fc='r')]
    sebother = [patches.FancyArrowPatch( (x, y), (x+0.8, y-0.8),**kw),plt.Rectangle( (x+0.22, y-0.38), r*1.25, r*1.25, fc='r')]
    swbother = [patches.FancyArrowPatch( (x, y), (x-0.8, y-0.8),**kw),plt.Rectangle( (x-0.38, y-0.38), r*1.25, r*1.25, fc='r')]     

    veh_dict = {'nebt':nebt,'nwbt':nwbt,'sebt':sebt,'swbt':swbt,
                'neb misc. action':nebmisc,'nwb misc. action':nwbmisc,'seb misc. action':sebmisc,'swb misc. action':swbmisc,
                'neb other':nebother,'nwb other':nwbother,'seb other':sebother,'swb other':swbother}
                
    return veh_dict

#Both thrus from same direction (so arrows don't overlap) DONE
def arrow_movements_thru_thru_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    nebt = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x+0.8, y+0.8),**kw)]    
    nwbt = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x-0.8, y+0.8),**kw)]
    sebt = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x+0.8, y-0.8),**kw)]
    swbt = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x-0.8, y-0.8),**kw)]   
 
    veh_dict = {'nebt':nebt,'nwbt':nwbt,'sebt':sebt,'swbt':swbt}

    return veh_dict

#Both miscellaneous actions from same direction (so arrows don't overlap)   
def arrow_movements_misc_misc_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    nebmisc = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Circle( (x-0.4, y-0.4), r, color='blue')]
    nwbmisc = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Circle( (x+0.4, y-0.4), r, color='blue')]
    sebmisc = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Circle( (x-0.4, y+0.4), r, color='blue')]
    swbmisc = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Circle( (x+0.4, y+0.4), r, color='blue')]   
    
    nebother = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    nwbother = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    sebother = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    swbother = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y+0.5), r*1.25, r*1.25, fc='r')]  

    veh_dict = {'neb misc. action':nebmisc,'nwb misc. action':nwbmisc,'seb misc. action':sebmisc,'swb misc. action':swbmisc,
                'neb other':nebother,'nwb other':nwbother,'seb other':sebother,'swb other':swbother}
                
    return veh_dict    

#One miscellaneous action + one other movement from same direction (so arrows don't overlap)    
def arrow_movements_misc_other_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    nebmisc = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Circle( (x-0.4, y-0.4), r, color='blue')]
    nwbmisc = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Circle( (x+0.4, y-0.4), r, color='blue')]
    sebmisc = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Circle( (x-0.4, y+0.4), r, color='blue')]
    swbmisc = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Circle( (x+0.4, y+0.4), r, color='blue')]   
    
    nebother = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    nwbother = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    sebother = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    swbother = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    
    veh_dict = {'neb misc. action':nebmisc,'nwb misc. action':nwbmisc,'seb misc. action':sebmisc,'swb misc. action':swbmisc,
                'neb other':nebother,'nwb other':nwbother,'seb other':sebother,'swb other':swbother}
                

    return veh_dict

#One turning movement (so arrows don't overlap)    
def arrow_movements_turning_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    nebl = [patches.FancyArrowPatch( (x-0.12, y-1.32), (x-0.12, y-0.12),connectionstyle="arc3,rad = 0.6", **kw)]
    nebr = [patches.FancyArrowPatch( (x-1.32, y-0.12), (x-0.12, y-0.12),connectionstyle="arc3,rad = -0.6", **kw)]
    nebt = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw)]    
    nwbl = [patches.FancyArrowPatch( (x+1.32, y-0.12), (x+0.12, y-0.12),connectionstyle="arc3,rad = 0.6", **kw)]
    nwbr = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    nwbt = [patches.FancyArrowPatch( (x+0.6, y-0.6), (x-0.2, y+0.2),**kw)]    
    sebl = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sebr = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    sebt = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw)]    
    swbl = [patches.FancyArrowPatch( (x+0.12, y+1.32), (x+0.12, y+0.12),connectionstyle="arc3,rad = 0.6", **kw)]
    swbr = [patches.FancyArrowPatch( (x+1.12, y+0.32), (x-0.08, y+0.32),connectionstyle="arc3,rad = -0.6", **kw)]
    swbt = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw)]    
    
    nebmisc = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Circle( (x-0.4, y-0.4), r, color='blue')]
    nwbmisc = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Circle( (x+0.4, y-0.4), r, color='blue')]
    sebmisc = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Circle( (x-0.4, y+0.4), r, color='blue')]
    swbmisc = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Circle( (x+0.4, y+0.4), r, color='blue')]   
    
    nebother = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    nwbother = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    sebother = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    swbother = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    
    veh_dict = {'nebl':nebl,'nebr':nebr,'nebt':nebt,
                'nwbl':nwbl,'nwbr':nwbr,'nwbt':nwbt,
                'sebl':sebl,'sebr':sebr,'sebt':sebt,
                'swbl':swbl,'swbr':swbr,'swbt':swbt,
                'neb misc. action':nebmisc,'nwb misc. action':nwbmisc,'seb misc. action':sebmisc,'swb misc. action':swbmisc,
                'neb other':nebother,'nwb other':nwbother,'seb other':sebother,'swb other':swbother,}

    return veh_dict

#Both turning movements (so arrows don't overlap)    
def arrow_movements_turning_bothturns_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    nebl = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nebr = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    
    nwbl = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nwbr = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
 
    sebl = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sebr = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    
    swbl = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    swbr = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)] 
    
    veh_dict = {'nebl':nebl,'nebr':nebr,'nwbl':nwbl,'nwbr':nwbr,                
                'sebl':sebl,'sebr':sebr,'swbl':swbl,'swbr':swbr}                

    return veh_dict

#Both turns from opposite directions    
def arrow_movements_turning_bothturns_opposite_x(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    nebl = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nebr = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    
    nwbl = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nwbr = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
 
    sebl = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sebr = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    
    swbl = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    swbr = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)] 

    veh_dict = {'nebl':nebl,'nebr':nebr,'nwbl':nwbl,'nwbr':nwbr,                
                'sebl':sebl,'sebr':sebr,'swbl':swbl,'swbr':swbr}                 

    return veh_dict    