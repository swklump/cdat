#Scenario 2, one vehicle movement is miscellaneous action

def arrow_movements2():
  
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebl_miscaction = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, 0.6), (0.55, 0.6),**kw),
                      plt.Circle( (-0.7, 0.6), 0.25, color='blue')]
    ebr_miscaction = [patches.FancyArrowPatch( (-0.7, 0.7), (0.6, -0.6),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, -0.6), (0.55, -0.6),**kw),
                      plt.Circle( (-0.7, -0.6), 0.25, color='blue')]
    ebt_miscaction = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
                      patches.FancyArrowPatch( (0.3, 0), (1.5, 0),**kw),
                      plt.Circle( (0.3, 0), 0.25, color='blue')]
    

    miscaction_nbl = [patches.FancyArrowPatch( (0.6, -0.6), (-0.7, 0.7),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, -0.6), (-0.7, 0.65),**kw),
                      plt.Circle( (0.7, -0.6), 0.25, color='blue')]
    miscaction_nbr = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (-0.6, -1.8), (-0.6, -0.55),**kw),
                      plt.Circle( (0.6, -0.7), 0.25, color='blue')]
    miscaction_nbt = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
                      patches.FancyArrowPatch( (0, 0.3), (0, 1.5),**kw),
                      plt.Circle( (0, 0.3), 0.25, color='blue')]
    

    miscaction_sbl = [patches.FancyArrowPatch( (-0.6, 0.7), (0.7, -0.6),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (0.7, 0.7), (0.7, -0.55),**kw),
                      plt.Circle( (0.7, 0.7), 0.25, color='blue')] 
    miscaction_sbr = [patches.FancyArrowPatch( (0.6, 0.6), (-0.7, -0.7),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, 0.6), (-0.7, -0.65),**kw),
                      plt.Circle( (-0.7, 0.6), 0.25, color='blue')]
    miscaction_sbt = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),
                      patches.FancyArrowPatch( (0, -0.3), (0, -1.5),**kw),
                      plt.Circle( (0, -0.3), 0.25, color='blue')]
    

    miscaction_wbl = [patches.FancyArrowPatch( (0.6, 0.6), (-0.7, -0.7),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (0.6, -0.7), (-0.65, -0.7),**kw),
                      plt.Circle( (0.6, -0.7), 0.25, color='blue')]
    miscaction_wbr = [patches.FancyArrowPatch( (0.6, -0.6), (-0.7, 0.7),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (0.6, 0.7), (-0.65, 0.7),**kw),
                      plt.Circle( (0.6, 0.7), 0.25, color='blue')]
    miscaction_wbt = [patches.FancyArrowPatch( (1.25, 0), (-0.25, 0),**kw),
                      patches.FancyArrowPatch( (-0.55, 0), (-1.75, 0),**kw),
                      plt.Circle( (-0.55, 0), 0.25, color='blue')]
    

    ebmisc_ebmisc = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
                     patches.FancyArrowPatch( (0.3, 0), (1.5, 0),**kw),
                     plt.Circle( (-1.5, 0), 0.25, color='blue'),
                     plt.Circle( (0.3, 0), 0.25, color='blue')] 
    nbmisc_nbmisc = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),
                     patches.FancyArrowPatch( (0, 0.3), (0, 1.5),**kw),
                     plt.Circle( (0, -1.5), 0.25, color='blue'),
                     plt.Circle( (0, 0.3), 0.25, color='blue')] 
    sbmisc_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),
                     patches.FancyArrowPatch( (0, -0.3), (0, -1.5),**kw),
                     plt.Circle( (0, 1.5), 0.25, color='blue'),
                     plt.Circle( (0, -0.3), 0.25, color='blue')]
    wbmisc_wbmisc = [patches.FancyArrowPatch( (1.0, 0), (-0.5, 0),**kw),
                     patches.FancyArrowPatch( (-0.8, 0), (-2.0, 0),**kw),
                     plt.Circle( (1.0, 0), 0.25, color='blue'),
                     plt.Circle( (-0.8, 0), 0.25, color='blue')]
    
    ebmisc_single = [patches.FancyArrowPatch( (-0.75, 0), (0.75, 0),**kw),
                     plt.Circle( (-0.75, 0), 0.25, color='blue')]
    nbmisc_single = [patches.FancyArrowPatch( (0, -0.75), (0, 0.75),**kw),
                     plt.Circle( (0, -0.75), 0.25, color='blue')]
    sbmisc_single = [patches.FancyArrowPatch( (0, 0.75), (0, -0.75),**kw),
                     plt.Circle( (0, 0.75), 0.25, color='blue')]
    single_wbmisc = [patches.FancyArrowPatch( (0.75, 0), (-0.75, 0),**kw),
                     plt.Circle( (0.75, 0), 0.25, color='blue')]

    veh_movements = [ebl_miscaction,ebr_miscaction,ebt_miscaction,
                     miscaction_nbl,miscaction_nbr,miscaction_nbt,
                     miscaction_sbl,miscaction_sbr,miscaction_sbt,
                     miscaction_wbl,miscaction_wbr,miscaction_wbt,
                     ebmisc_ebmisc,nbmisc_nbmisc,sbmisc_sbmisc,wbmisc_wbmisc,
                     ebmisc_single,nbmisc_single,sbmisc_single,single_wbmisc]
    
    veh_dict = {'ebl/eb misc. action':ebl_miscaction,'ebr/eb misc. action':ebr_miscaction,
                'ebt/eb misc. action':ebt_miscaction,'nb misc. action/nbl':miscaction_nbl,
                'nb misc. action/nbr':miscaction_nbr,'nb misc. action/nbt':miscaction_nbt,
                'sb misc. action/sbl':miscaction_sbl,'sb misc. action/sbr':miscaction_sbr,
                'sb misc. action/sbt':miscaction_sbt,'wb misc. action/wbl':miscaction_wbl,
                'wb misc. action/wbr':miscaction_wbr,'wb misc. action/wbt':miscaction_wbt,
                'eb misc. action/eb misc. action':ebmisc_ebmisc,
                'nb misc. action/nb misc. action':nbmisc_nbmisc,
                'sb misc. action/sb misc. action':sbmisc_sbmisc,
                'wb misc. action/wb misc. action':wbmisc_wbmisc,
                'eb misc. action(single vehicle crash)':ebmisc_single,
                'nb misc. action(single vehicle crash)':nbmisc_single,
                'sb misc. action(single vehicle crash)':sbmisc_single,
                '(single vehicle crash)wb misc. action':single_wbmisc}

    return (veh_movements, veh_dict)
