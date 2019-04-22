#In scenario 5, both movements are thru's
def arrow_movements5():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebt_nbt = [patches.FancyArrowPatch( (-1.25, 0.75), (0.25, 0.75),**kw),
               patches.FancyArrowPatch( (0.25, -0.75), (0.25, 0.75),**kw)]
    ebt_sbt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
               patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    ebt_wbt = [patches.FancyArrowPatch( (-1.75, 0), (-0.25, 0),**kw),
               patches.FancyArrowPatch( (1.25, 0), (-0.25, 0),**kw)]

    nbt_sbt = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
               patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    nbt_wbt = [patches.FancyArrowPatch( (-0.5, -0.75), (-0.5, 0.75),**kw),
               patches.FancyArrowPatch( (1, 0.75), (-0.5, 0.75),**kw)]

    sbt_wbt = [patches.FancyArrowPatch( (-1.0, 0.75), (-1.0, -0.75),**kw),
               patches.FancyArrowPatch( (0.5, -0.75), (-1.0, -0.75),**kw)]
      
    veh_movements = [ebt_nbt,ebt_nbt,ebt_wbt,nbt_sbt,nbt_wbt,sbt_wbt]
    veh_dict = {'ebt/nbt':ebt_nbt,'ebt/nbt':ebt_nbt,'ebt/wbt':ebt_wbt,'nbt/sbt':nbt_sbt,\
                'nbt/wbt':nbt_wbt,'sbt/wbt':sbt_wbt}

    return (veh_movements, veh_dict)
