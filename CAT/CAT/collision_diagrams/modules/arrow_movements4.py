#Scenario 4 = both vehicles same direction (ex: 'nbt/nbl')

def arrow_movements4():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
           patches.FancyArrowPatch( (0, 0), (1.5, 0),**kw)]
    nbt = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
           patches.FancyArrowPatch( (0, 0), (0, 1.5),**kw)]
    sbt = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),
           patches.FancyArrowPatch( (0, 0), (0, -1.5),**kw)]
    wbt = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),
           patches.FancyArrowPatch( (0, 0), (-1.5, 0),**kw)]

    ebl = [patches.FancyArrowPatch( (-1.5, -1), (-0.2, 0.3),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (-1, 0.2), (0.3, 1.5),connectionstyle="arc3,rad = 0.6", **kw)]  
    nbl = [patches.FancyArrowPatch( (0.7, -1.5), (-0.6, -0.2),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (-0.5, -1), (-1.8, 0.3),connectionstyle="arc3,rad = 0.6", **kw)]
    sbl = [patches.FancyArrowPatch( (-1.7, 1.3), (-0.4, 0),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (-0.5, 0.8), (0.8, -0.5),connectionstyle="arc3,rad = 0.6", **kw)]
    wbl = [patches.FancyArrowPatch( (0.2, -0.2), (-1.1, -1.5),connectionstyle="arc3,rad = 0.6", **kw),
           patches.FancyArrowPatch( (0.7, 1), (-0.6, -0.3),connectionstyle="arc3,rad = 0.6", **kw)]

    ebr = [patches.FancyArrowPatch( (-0.9, 1), (0.4, -0.3),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (-0.4, -0.2), (0.9, -1.5),connectionstyle="arc3,rad = -0.6", **kw)]   
    nbr = [patches.FancyArrowPatch( (-1.2, -1.5), (0.1, -0.2),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (0, -1), (1.3, 0.3),connectionstyle="arc3,rad = -0.6", **kw)]
    sbr = [patches.FancyArrowPatch( (0.7, 0.9), (-0.6, -0.65),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (-0.5, 0.15), (-1.8, -0.9),connectionstyle="arc3,rad = -0.6", **kw)]
    wbr = [patches.FancyArrowPatch( (0.2, 0.2), (-1.1, 1.5),connectionstyle="arc3,rad = -0.6", **kw),
           patches.FancyArrowPatch( (0.7, -1), (-0.6, 0.3),connectionstyle="arc3,rad = -0.6", **kw)]

    ebl_ebt = [patches.FancyArrowPatch( (-0.5, 0), (0.8, 1.3),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (-2, 0), (-0.45, 0),**kw)]
    ebr_ebt = [patches.FancyArrowPatch( (-0.5, 0), (0.8, -1.3),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (-2, 0), (-0.45, 0),**kw)]
    nbl_nbt = [patches.FancyArrowPatch( (0, 0), (-1.3, 1.3),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw)]
    nbr_nbt = [patches.FancyArrowPatch( (-0.75, 0), (0.55, 1.3),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (-0.75, -1.5), (-0.75, 0),**kw)]
    sbl_sbt = [patches.FancyArrowPatch( (-0.75, 0), (0.55, -1.3),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (-0.75, 1.5), (-0.75, 0),**kw)]
    sbr_sbt = [patches.FancyArrowPatch( (0, 0), (-1.3, -1.3),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    wbl_wbt = [patches.FancyArrowPatch( (-0.55, 0.65), (-1.85, -0.65),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1, 0.65), (-0.55, 0.65),**kw)]
    wbr_wbt = [patches.FancyArrowPatch( (-0.65, -0.65), (-1.95, 0.65),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (0.9, -0.65), (-0.65, -0.65),**kw)]

    veh_movements = [ebt,nbt,sbt,wbt,ebl,nbl,sbl,wbl,ebr,nbr,sbr,wbr,
                     ebl_ebt,ebr_ebt,nbl_nbt,nbr_nbt,sbl_sbt,sbr_sbt,
                     wbl_wbt,wbr_wbt]
    
    veh_dict = {'ebt':ebt,'nbt':nbt,'sbt':sbt,'wbt':wbt,'ebl':ebl,               
                'nbl':nbl,'sbl':sbl,'wbl':wbl,'ebr':ebr,'nbr':nbr,
                'sbr':sbr,'wbr':wbr,'ebl/ebt':ebl_ebt,'ebr/ebt':ebr_ebt,
                'nbl/nbt':nbl_nbt,'nbr/nbt':nbr_nbt,'sbl/sbt':sbl_sbt,
                'sbr/sbt':sbr_sbt,'wbl/wbt':wbl_wbt,'wbr/wbt':wbr_wbt}

    return (veh_movements, veh_dict)
