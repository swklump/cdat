#In Scenario 8, one right turn
def arrow_movements8():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebr_sbt = [patches.FancyArrowPatch( (-1.3, 0.65), (0, -0.65),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (0.13, 0.85), (0.13, -0.65),**kw)]
    ebr_wbl = [patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (1.43, 1.3), (0.13, 0),connectionstyle="arc3,rad = 0.6", **kw)]

    ebt_nbr = [patches.FancyArrowPatch( (-1, 0.715), (0.5, 0.715),**kw),
               patches.FancyArrowPatch( (-0.8, -0.715), (0.5, 0.585),connectionstyle="arc3,rad = -0.6", **kw)]
    nbr_sbl = [patches.FancyArrowPatch( (-0.8, -1.3), (0.5, 0),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (-0.8, 1.43), (0.5, 0.13),connectionstyle="arc3,rad = 0.6", **kw)]

    sbr_wbt = [patches.FancyArrowPatch( (0.3, 0.65), (-1, -0.65),connectionstyle="arc3,rad = -0.6", **kw),
               patches.FancyArrowPatch( (0.5, -0.78), (-1, -0.78),**kw)]
    nbl_sbr = [patches.FancyArrowPatch( (0.3, -1.43), (-1, -0.13),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0.3, 1.3), (-1, 0),connectionstyle="arc3,rad = -0.6", **kw)]

    nbt_wbr = [patches.FancyArrowPatch( (-0.63, -1), (-0.63, 0.5),**kw),
               patches.FancyArrowPatch( (0.8, -0.8), (-0.5, 0.5),connectionstyle="arc3,rad = -0.6", **kw)]
    ebl_wbr = [patches.FancyArrowPatch( (-1.3, -0.3), (0, 1),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.3, -0.3), (0, 1),connectionstyle="arc3,rad = -0.6", **kw)]
      
    veh_movements = [ebr_sbt,ebr_wbl,\
                     ebt_nbr,nbr_sbl,\
                     sbr_wbt,nbl_sbr,\
                     nbt_wbr,ebl_wbr]

    veh_dict = {'ebr/sbt':ebr_sbt,'ebr/wbl':ebr_wbl,\
                'ebt/nbr':ebt_nbr,'nbr/sbl':nbr_sbl,\
                'sbr/wbt':sbr_wbt,'nbl/sbr':nbl_sbr,\
                'nbt/wbr':nbt_wbr,'ebl/wbr':ebl_wbr}

    return (veh_movements, veh_dict)
