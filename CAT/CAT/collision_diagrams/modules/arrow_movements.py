#This module defines the arrows that go on the plots

#Normal arrow movements
def arrow_movements(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    #N/S/E/W
    ebl = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    ebt = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw)]
    nbl = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    nbt = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw)]
    sbl = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sbr = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    sbt = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw)]
    wbl = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    wbr = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    wbt = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw)]
    
    ebmisc = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Circle( (x-0.725, y), r, color='blue')]
    nbmisc = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Circle( (x, y-0.725), r, color='blue')]
    sbmisc = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Circle( (x, y+0.725), r, color='blue')]
    wbmisc = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Circle( (x+0.725, y), r, color='blue')]   

    ebother = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Rectangle( (x-0.725, y-(r/2)), r, r, fc='r')]
    nbother = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y-0.725), r, r, fc='r')]
    sbother = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y+0.725), r, r, fc='r')]
    wbother = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Rectangle( (x+0.725, y-(r/2)), r, r, fc='r')]
    
    #NE/NW/SE/SW
    nebl = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nebr = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    nebt = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw)]    
    nwbl = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nwbr = [patches.FancyArrowPatch( (x, y-1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    nwbt = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw)]    
    sebl = [patches.FancyArrowPatch( (x-1.2, y), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sebr = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    sebt = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw)]    
    swbl = [patches.FancyArrowPatch( (x, y+1.2), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    swbr = [patches.FancyArrowPatch( (x+1.2, y), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    swbt = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw)]    
    
    nebmisc = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Circle( (x-0.4, y-0.4), r, color='blue')]
    nwbmisc = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Circle( (x+0.4, y-0.4), r, color='blue')]
    sebmisc = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Circle( (x-0.4, y+0.4), r, color='blue')]
    swbmisc = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Circle( (x+0.4, y+0.4), r, color='blue')]   
    
    nebother = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    nwbother = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y-0.5), r*1.25, r*1.25, fc='r')]
    sebother = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x-0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    swbother = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),**kw),plt.Rectangle( (x+0.5, y+0.5), r*1.25, r*1.25, fc='r')]
    
    single_vehicle = []
    unknown = []
    pedestrian = []
    bicyclist = []
    
    veh_dict = {'ebl':ebl,'ebr':ebr,'ebt':ebt,
                'nbl':nbl,'nbr':nbr,'nbt':nbt,
                'sbl':sbl,'sbr':sbr,'sbt':sbt,
                'wbl':wbl,'wbr':wbr,'wbt':wbt,
                'eb misc. action':ebmisc,'nb misc. action':nbmisc,'sb misc. action':sbmisc,'wb misc. action':wbmisc,
                'eb other':ebother,'nb other':nbother,'sb other':sbother,'wb other':wbother,'(single vehicle crash':single_vehicle,'unknown':unknown,
                'pedestrian':pedestrian,'bicyclist':bicyclist,
                'nebl':nebl,'nebr':nebr,'nebt':nebt,
                'nwbl':nwbl,'nwbr':nwbr,'nwbt':nwbt,
                'sebl':sebl,'sebr':sebr,'sebt':sebt,
                'swbl':swbl,'swbr':swbr,'swbt':swbt,
                'neb misc. action':nebmisc,'nwb misc. action':nwbmisc,'seb misc. action':sebmisc,'swb misc. action':swbmisc,
                'neb other':nebother,'nwb other':nwbother,'seb other':sebother,'swb other':swbother}

    return veh_dict

#Miscellaneous action + thru arrows (so arrows don't overlap)
def arrow_movements_misc_thru(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebt = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw)]
    nbt = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw)]
    sbt = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw)]
    wbt = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw)]
    
    ebmisc = [patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw),plt.Circle( (x+0.525, y), r, color='blue')]
    nbmisc = [patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw),plt.Circle( (x, y+0.525), r, color='blue')]
    sbmisc = [patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw),plt.Circle( (x, y-0.525), r, color='blue')]
    wbmisc = [patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw),plt.Circle( (x-0.525, y), r, color='blue')]   

    ebother = [patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw),plt.Rectangle( (x+0.525, y-(r/2)), r, r, fc='r')]
    nbother = [patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw),plt.Rectangle( (x-(r/2), y+0.525), r, r, fc='r')]
    sbother = [patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw),plt.Rectangle( (x-(r/2), y-0.525), r, r, fc='r')]
    wbother = [patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw),plt.Rectangle( (x-0.525, y-(r/2)), r, r, fc='r')]    

    veh_dict = {'ebt':ebt,'nbt':nbt,'sbt':sbt,'wbt':wbt,
                'eb misc. action':ebmisc,'nb misc. action':nbmisc,'sb misc. action':sbmisc,'wb misc. action':wbmisc,
                'eb other':ebother,'nb other':nbother,'sb other':sbother,'wb other':wbother}

    return veh_dict

#Both thrus from same direction (so arrows don't overlap)
def arrow_movements_thru_thru(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebt = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw)]
    nbt = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw)]
    sbt = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw)]
    wbt = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw)]    

    veh_dict = {'ebt':ebt,'nbt':nbt,'sbt':sbt,'wbt':wbt}

    return veh_dict

#Both miscellaneous actions from same direction (so arrows don't overlap)   
def arrow_movements_misc_misc(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebmisc = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Circle( (x-0.725, y), r, color='blue'),
              patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw),plt.Circle( (x+0.525, y), r, color='blue')]
    nbmisc = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Circle( (x, y-0.725), r, color='blue'),
              patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw),plt.Circle( (x, y+0.525), r, color='blue')]
    sbmisc = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Circle( (x, y+0.725), r, color='blue'),
              patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw),plt.Circle( (x, y-0.525), r, color='blue')]
    wbmisc = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Circle( (x+0.725, y), r, color='blue'),
              patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw),plt.Circle( (x-0.525, y), r, color='blue')]   

    ebother = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Rectangle( (x-0.725, y-(r/2)), r, r, fc='r'),
               patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw),plt.Rectangle( (x+0.525, y-(r/2)), r, r, fc='r')]
    nbother = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y-0.725), r, r, fc='r'),
               patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw),plt.Rectangle( (x-(r/2), y+0.525), r, r, fc='r')]
    sbother = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y+0.725), r, r, fc='r'),
               patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw),plt.Rectangle( (x-(r/2), y-0.525), r, r, fc='r')]
    wbother = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Rectangle( (x+0.725, y-(r/2)), r, r, fc='r'),
               patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw),plt.Rectangle( (x-0.525, y-(r/2)), r, r, fc='r')]

    veh_dict = {'eb misc. action':ebmisc,'nb misc. action':nbmisc,'sb misc. action':sbmisc,'wb misc. action':wbmisc,
                'eb other':ebother,'nb other':nbother,'sb other':sbother,'wb other':wbother}
                

    return veh_dict    

#One miscellaneous action + one other movement from same direction (so arrows don't overlap)    
def arrow_movements_misc_other(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebmisc = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Circle( (x-0.725, y), r, color='blue')]
    nbmisc = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Circle( (x, y-0.725), r, color='blue')]
    sbmisc = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Circle( (x, y+0.725), r, color='blue')]
    wbmisc = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Circle( (x+0.725, y), r, color='blue')]   

    ebother = [patches.FancyArrowPatch( (x, y), (x+1.25, y),**kw),plt.Rectangle( (x+0.525, y-(r/2)), r, r, fc='r')]
    nbother = [patches.FancyArrowPatch( (x, y), (x, y+1.25),**kw),plt.Rectangle( (x-(r/2), y+0.525), r, r, fc='r')]
    sbother = [patches.FancyArrowPatch( (x, y), (x, y-1.25),**kw),plt.Rectangle( (x-(r/2), y-0.525), r, r, fc='r')]
    wbother = [patches.FancyArrowPatch( (x, y), (x-1.25, y),**kw),plt.Rectangle( (x-0.525, y-(r/2)), r, r, fc='r')]
    
    veh_dict = {'eb misc. action':ebmisc,'nb misc. action':nbmisc,'sb misc. action':sbmisc,'wb misc. action':wbmisc,
                'eb other':ebother,'nb other':nbother,'sb other':sbother,'wb other':wbother}
                

    return veh_dict

#One turning movement (so arrows don't overlap)    
def arrow_movements_turning(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebl = [patches.FancyArrowPatch( (x-0.95, y-0.8), (x-0.15, y),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr = [patches.FancyArrowPatch( (x-0.95, y+0.8), (x-0.15, y),connectionstyle="arc3,rad = -0.6", **kw)]
    ebt = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw)]
    nbl = [patches.FancyArrowPatch( (x+0.8, y-0.95), (x, y-0.15),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr = [patches.FancyArrowPatch( (x-0.8, y-0.95), (x, y-0.15),connectionstyle="arc3,rad = -0.6", **kw)]
    nbt = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw)]
    sbl = [patches.FancyArrowPatch( (x-0.8, y+0.95), (x, y+0.15),connectionstyle="arc3,rad = 0.6", **kw)]
    sbr = [patches.FancyArrowPatch( (x+0.8, y+0.95), (x, y+0.15),connectionstyle="arc3,rad = -0.6", **kw)]
    sbt = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw)]
    wbl = [patches.FancyArrowPatch( (x+0.95, y+0.8), (x+0.15, y),connectionstyle="arc3,rad = 0.6", **kw)]
    wbr = [patches.FancyArrowPatch( (x+0.95, y-0.8), (x+0.15, y),connectionstyle="arc3,rad = -0.6", **kw)]
    wbt = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw)]
    
    ebmisc = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Circle( (x-0.725, y), r, color='blue')]
    nbmisc = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Circle( (x, y-0.725), r, color='blue')]
    sbmisc = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Circle( (x, y+0.725), r, color='blue')]
    wbmisc = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Circle( (x+0.725, y), r, color='blue')]   

    ebother = [patches.FancyArrowPatch( (x-1.25, y), (x, y),**kw),plt.Rectangle( (x-0.725, y-(r/2)), r, r, fc='r')]
    nbother = [patches.FancyArrowPatch( (x, y-1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y-0.725), r, r, fc='r')]
    sbother = [patches.FancyArrowPatch( (x, y+1.25), (x, y),**kw),plt.Rectangle( (x-(r/2), y+0.725), r, r, fc='r')]
    wbother = [patches.FancyArrowPatch( (x+1.25, y), (x, y),**kw),plt.Rectangle( (x+0.725, y-(r/2)), r, r, fc='r')]
    
    veh_dict = {'ebl':ebl,'ebr':ebr,'ebt':ebt,
                'nbl':nbl,'nbr':nbr,'nbt':nbt,
                'sbl':sbl,'sbr':sbr,'sbt':sbt,
                'wbl':wbl,'wbr':wbr,'wbt':wbt,
                'eb misc. action':ebmisc,'nb misc. action':nbmisc,'sb misc. action':sbmisc,'wb misc. action':wbmisc,
                'eb other':ebother,'nb other':nbother,'sb other':sbother,'wb other':wbother,}

    return veh_dict

#Both turning movements (so arrows don't overlap)    
def arrow_movements_turning_bothturns(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebl = [patches.FancyArrowPatch( (x-0.4, y-0.05), (x+0.4, y+0.75),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr = [patches.FancyArrowPatch( (x-0.4, y+0.05), (x+0.4, y-0.75),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    nbl = [patches.FancyArrowPatch( (x+0.05, y-0.4), (x-0.75, y+0.4),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr = [patches.FancyArrowPatch( (x-0.05, y-0.4), (x+0.75, y+0.4),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    sbl = [patches.FancyArrowPatch( (x-0.05, y+0.4), (x+0.75, y-0.4),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    sbr = [patches.FancyArrowPatch( (x+0.05, y+0.4), (x-0.75, y-0.4),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    wbl = [patches.FancyArrowPatch( (x+0.4, y+0.05), (x-0.4, y-0.75),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),connectionstyle="arc3,rad = 0.6", **kw)]
    wbr = [patches.FancyArrowPatch( (x+0.4, y-0.05), (x-0.4, y+0.75),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]
    
    veh_dict = {'ebl':ebl,'ebr':ebr,'nbl':nbl,'nbr':nbr,                
                'sbl':sbl,'sbr':sbr,'wbl':wbl,'wbr':wbr}                

    return veh_dict

#Both turns from opposite directions    
def arrow_movements_turning_bothturns_opposite(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebl = [patches.FancyArrowPatch( (x-0.95, y-0.8), (x-0.15, y),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr = [patches.FancyArrowPatch( (x-0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    nbl = [patches.FancyArrowPatch( (x+0.8, y-0.95), (x, y-0.15),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr = [patches.FancyArrowPatch( (x-0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    sbl = [patches.FancyArrowPatch( (x-0.8, y+0.95), (x, y+0.15),connectionstyle="arc3,rad = 0.6", **kw)]
    sbr = [patches.FancyArrowPatch( (x+0.8, y+0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    wbl = [patches.FancyArrowPatch( (x+0.95, y+0.8), (x+0.15, y),connectionstyle="arc3,rad = 0.6", **kw)]
    wbr = [patches.FancyArrowPatch( (x+0.8, y-0.8), (x, y),connectionstyle="arc3,rad = -0.6", **kw)]

    
    veh_dict = {'ebl':ebl,'ebr':ebr,'nbl':nbl,'nbr':nbr,                
                'sbl':sbl,'sbr':sbr,'wbl':wbl,'wbr':wbr}                

    return veh_dict    