
def arrow_movements(x, y, r):

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
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
                'pedestrian':pedestrian,'bicyclist':bicyclist}

    return veh_dict

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