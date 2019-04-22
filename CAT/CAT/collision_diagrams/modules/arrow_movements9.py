#Scenario 9, "other" movements

def arrow_movements9():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebl_other = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                          connectionstyle="arc3,rad = 0.6", **kw),
                 patches.FancyArrowPatch( (-0.7, 0.6), (0.55, 0.6),**kw),
                 plt.Rectangle( (-0.825, 0.475), 0.25, 0.25, fc='r')]
    ebr_other = [patches.FancyArrowPatch( (-0.7, 0.7), (0.6, -0.6),
                                          connectionstyle="arc3,rad = -0.6", **kw),
                 patches.FancyArrowPatch( (-0.7, -0.6), (0.55, -0.6),**kw),
                 plt.Rectangle( (-0.825, -0.725), 0.25, 0.25, fc='r')]
    ebt_other = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
                 patches.FancyArrowPatch( (0.3, 0), (1.5, 0),**kw),
                 plt.Rectangle( (0.175, -0.125), 0.25, 0.25, fc='r')]
    

    nbl_other = [patches.FancyArrowPatch( (0.6, -0.6), (-0.7, 0.7),
                                          connectionstyle="arc3,rad = 0.6", **kw),
                 patches.FancyArrowPatch( (-0.7, -0.6), (-0.7, 0.65),**kw),
                 plt.Rectangle( (-0.825, -0.725), 0.25, 0.25, fc='r')]
    nbr_other = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                          connectionstyle="arc3,rad = -0.6", **kw),
                 patches.FancyArrowPatch( (0.6, -0.7), (-0.6, 0.55),**kw),
                 plt.Rectangle( (-0.725, -0.825), 0.25, 0.25, fc='r')]
    nbt_other = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
                 patches.FancyArrowPatch( (0, 0.3), (0, 1.5),**kw),
                 plt.Rectangle( (-0.125, 0.175), 0.25, 0.25, fc='r')]
    

    other_sbl = [patches.FancyArrowPatch( (-0.6, 0.7), (0.7, -0.6),
                                          connectionstyle="arc3,rad = 0.6", **kw),
                 patches.FancyArrowPatch( (0.7, 0.7), (0.7, -0.55),**kw),
                 plt.Rectangle( (0.575, 0.575), 0.25, 0.25, fc='r')] 
    other_sbr = [patches.FancyArrowPatch( (0.6, 0.6), (-0.7, -0.7),
                                          connectionstyle="arc3,rad = -0.6", **kw),
                 patches.FancyArrowPatch( (-0.7, 0.6), (-0.7, -0.65),**kw),
                 plt.Rectangle( (-0.825, 0.475), 0.25, 0.25, fc='r')] 
    other_sbt = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),
                 patches.FancyArrowPatch( (0, -0.3), (0, -1.5),**kw),
                 plt.Rectangle( (-0.125, -0.425), 0.25, 0.25, fc='r')] 
    

    other_wbl = [patches.FancyArrowPatch( (0.6, 0.6), (-0.7, -0.7),
                                          connectionstyle="arc3,rad = 0.6", **kw),
                 patches.FancyArrowPatch( (0.6, -0.7), (-0.65, -0.7),**kw),
                 plt.Rectangle( (0.475, -0.825), 0.25, 0.25, fc='r')]
    other_wbr = [patches.FancyArrowPatch( (0.6, -0.6), (-0.7, 0.7),
                                          connectionstyle="arc3,rad = -0.6", **kw),
                 patches.FancyArrowPatch( (0.6, 0.7), (-0.65, 0.7),**kw),
                 plt.Rectangle( (0.475, 0.575), 0.25, 0.25, fc='r')]
    other_wbt = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),
                 patches.FancyArrowPatch( (-0.3, 0), (-1.5, 0),**kw),
                 plt.Rectangle( (-0.425, -0.125), 0.25, 0.25, fc='r')]
    

    ebother_ebother = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
                     patches.FancyArrowPatch( (0.3, 0), (1.5, 0),**kw),
                     plt.Rectangle( (-1.625, -0.125), 0.25, 0.25, fc='r'),
                     plt.Rectangle( (0.175, -0.125), 0.25, 0.25, fc='r')] 
    nbother_nbother = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
                     patches.FancyArrowPatch( (0, 0.3), (0, 1.5),**kw),
                     plt.Rectangle( (-0.125, -1.625), 0.25, 0.25, fc='r'),
                     plt.Rectangle( (-0.125, 0.175), 0.25, 0.25, fc='r')] 
    sbother_sbother = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),
                     patches.FancyArrowPatch( (0, -0.3), (0, -1.5),**kw),
                     plt.Rectangle( (-0.125, 1.375), 0.25, 0.25, fc='r'),
                     plt.Rectangle( (-0.125, -0.475), 0.25, 0.25, fc='r')]
    wbother_wbother = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),
                     patches.FancyArrowPatch( (-0.3, 0), (-1.5, 0),**kw),
                     plt.Rectangle( (1.375, -0.125), 0.25, 0.25, fc='r'),
                     plt.Rectangle( (-0.475, -0.125), 0.25, 0.25, fc='r')]
    

    

    veh_movements = [ebl_other,ebr_other,ebt_other,
                     nbl_other,nbr_other,nbt_other,
                     other_sbl,other_sbr,other_sbt,
                     other_wbl,other_wbr,other_wbt,
                     ebother_ebother,nbother_nbother,sbother_sbother,wbother_wbother]
    
    veh_dict = {'eb other/ebl':ebl_other,'eb other/ebr':ebr_other,
                'eb other/ebt':ebt_other,'nb other/nbl':nbl_other,
                'nb other/nbr':nbr_other,'nb other/nbt':nbt_other,
                'sb other/sbl':other_sbl,'sb other/sbr':other_sbr,
                'sb other/sbt':other_sbt,'wb other/wbl':other_wbl,
                'wb other/wbr':other_wbr,'wb other/wbt':other_wbt,
                'eb other/eb other':ebother_ebother,
                'nb other/nb other':nbother_nbother,
                'sb other/sb other':sbother_sbother,
                'wb other/wb other':wbother_wbother}

    return (veh_movements, veh_dict)
