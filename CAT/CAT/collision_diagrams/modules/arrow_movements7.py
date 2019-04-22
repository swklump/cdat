#In Scenario 7, one left and one thru
def arrow_movements7():

    import matplotlib.patches as patches
    
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebl_nbt = [patches.FancyArrowPatch( (-1.05, -0.65), (0.25, 0.65),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0.38, -0.85), (0.38, 0.65),**kw)]
    ebl_sbt = [patches.FancyArrowPatch( (-0.8, -1.3), (0.5, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0.5, 1.5), (0.5, 0),**kw)]
    ebl_wbt = [patches.FancyArrowPatch( (-1.3, -0.65), (0, 0.65),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.5, 0.65), (0, 0.65),**kw)]

    ebt_nbl = [patches.FancyArrowPatch( (-1.75, 0), (-0.25, 0),**kw),
               patches.FancyArrowPatch( (1.05, -1.3), (-0.25, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbl_sbt = [patches.FancyArrowPatch( (0.5, -1.3), (-0.8, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (-0.8, 1.5), (-0.8, 0),**kw)]
    nbl_wbt = [patches.FancyArrowPatch( (0.3, -1.3), (-1, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0.5, 0.13), (-1, 0.13),**kw)]

    ebt_sbl = [patches.FancyArrowPatch( (-1, -0.13), (0.5, -0.13),**kw),
               patches.FancyArrowPatch( (-0.8, 1.3), (0.5, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbt_sbl = [patches.FancyArrowPatch( (0.5, -1.5), (0.5, 0),**kw),
               patches.FancyArrowPatch( (-0.8, 1.3), (0.5, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    sbl_wbt = [patches.FancyArrowPatch( (-1.8, 0.65), (-0.5, -0.65),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.0, -0.65), (-0.5, -0.65),**kw)]

    ebt_wbl = [patches.FancyArrowPatch( (-1.5, -0.65), (0, -0.65),**kw),
               patches.FancyArrowPatch( (1.3, 0.65), (0, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    nbt_wbl = [patches.FancyArrowPatch( (-0.65, -1.5), (-0.65, 0),**kw),
               patches.FancyArrowPatch( (0.65, 1.3), (-0.65, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    sbt_wbl = [patches.FancyArrowPatch( (-0.63, 0.75), (-0.63, -0.75),**kw),
               patches.FancyArrowPatch( (0.8, 0.55), (-0.5, -0.75),connectionstyle="arc3,rad = 0.6", **kw)]
      
    veh_movements = [ebl_nbt,ebl_sbt,ebl_wbt,\
                     ebt_nbl,nbl_sbt,nbl_wbt,\
                     ebt_sbl,nbt_sbl,sbl_wbt,\
                     ebt_wbl,nbt_wbl,sbt_wbl]

    veh_dict = {'ebl/nbt':ebl_nbt,'ebl/sbt':ebl_sbt,'ebl/wbt':ebl_wbt,\
                'ebt/nbl':ebt_nbl,'nbl/sbt':nbl_sbt,'nbl/wbt':nbl_wbt,\
                'ebt/sbl':ebt_sbl,'nbt/sbl':nbt_sbl,'sbl/wbt':sbl_wbt,\
                'ebt/wbl':ebt_wbl,'nbt/wbl':nbt_wbl,'sbt/wbl':sbt_wbl}

    return (veh_movements, veh_dict)
