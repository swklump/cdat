#In Scenario 3, single vehicle crash
def arrow_movements3():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
  
    ebl_single = [patches.FancyArrowPatch( (-0.65, -0.65), (0.65, 0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr_single = [patches.FancyArrowPatch( (-0.65, 0.65), (0.65, -0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    ebt_single = [patches.FancyArrowPatch( (-0.75, 0), (0.75, 0),**kw)]
    
    nbl_single = [patches.FancyArrowPatch( (0.65, -0.65), (-0.65, 0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr_single = [patches.FancyArrowPatch( (-0.65, -0.65), (0.65, 0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    nbt_single = [patches.FancyArrowPatch( (0, -0.75), (0, 0.75),**kw)]

    sbl_single = [patches.FancyArrowPatch( (-0.65, 0.65), (0.65, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    sbr_single = [patches.FancyArrowPatch( (0.65, 0.65), (-0.65, -0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    sbt_single = [patches.FancyArrowPatch( (0, 0.75), (0, -0.75),**kw)]

    single_wbl = [patches.FancyArrowPatch( (0.65, 0.65), (-0.65, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    single_wbr = [patches.FancyArrowPatch( (0.65, -0.65), (-0.65, 0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    single_wbt = [patches.FancyArrowPatch( (0.75, 0), (-0.75, 0),**kw)]
    
    ebother_single = [patches.FancyArrowPatch( (-0.75, 0), (0.75, 0),**kw),
                     plt.Rectangle( (-0.875, -0.125), 0.25, 0.25, fc='r')]
    nbother_single = [patches.FancyArrowPatch( (0, -0.75), (0, 0.75),**kw),
                     plt.Rectangle( (-0.125, -0.875), 0.25, 0.25, fc='r')]
    sbother_single = [patches.FancyArrowPatch( (0, 0.75), (0, -0.75),**kw),
                     plt.Rectangle( (-0.125, 0.625), 0.25, 0.25, fc='r')]
    single_wbother = [patches.FancyArrowPatch( (0.75, 0), (-0.75, 0),**kw),
                     plt.Rectangle( (0.625, -0.125), 0.25, 0.25, fc='r')]    


    veh_movements = [ebl_single,ebr_single,ebt_single,
                     nbl_single,nbr_single,nbt_single,
                     sbl_single,sbr_single,sbt_single,
                     single_wbl,single_wbr,single_wbt,
                     ebother_single,nbother_single,sbother_single,single_wbother]

    veh_dict = {'ebl(single vehicle crash)':ebl_single,'ebr(single vehicle crash)':ebr_single,
                'ebt(single vehicle crash)':ebt_single,'nbl(single vehicle crash)':nbl_single,
                'nbr(single vehicle crash)':nbr_single,'nbt(single vehicle crash)':nbt_single,
                'sbl(single vehicle crash)':sbl_single,'sbr(single vehicle crash)':sbr_single,
                'sbt(single vehicle crash)':sbt_single,'(single vehicle crash)wbl':single_wbl,
                '(single vehicle crash)wbr':single_wbr,'(single vehicle crash)wbt':single_wbt,
                'eb other(single vehicle crash)':ebother_single,
                'nb other(single vehicle crash)':nbother_single,
                'sb other(single vehicle crash)':sbother_single,
                '(single vehicle crash)wb other':single_wbother}

    return (veh_movements, veh_dict) 
