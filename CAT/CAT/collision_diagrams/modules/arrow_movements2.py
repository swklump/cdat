#Scenario 2, one vehicle movement is miscellaneous action

def arrow_movements2():
  
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    #NORMAL SITUATIONS (PHASE 1)
    miscaction_ebl = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, 0.6), (0.55, 0.6),**kw),
                      plt.Circle( (-0.7, 0.6), 0.25, color='blue')]
    miscaction_ebr = [patches.FancyArrowPatch( (-0.7, 0.7), (0.6, -0.6),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, -0.6), (0.55, -0.6),**kw),
                      plt.Circle( (-0.7, -0.6), 0.25, color='blue')]
    miscaction_ebt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),
                      patches.FancyArrowPatch( (0.3, 0), (1.5, 0),**kw),
                      plt.Circle( (0.3, 0), 0.25, color='blue')]
    

    miscaction_nbl = [patches.FancyArrowPatch( (0.6, -0.6), (-0.7, 0.7),
                                               connectionstyle="arc3,rad = 0.6", **kw),
                      patches.FancyArrowPatch( (-0.7, -0.6), (-0.7, 0.65),**kw),
                      plt.Circle( (-0.7, -0.6), 0.25, color='blue')]
    miscaction_nbr = [patches.FancyArrowPatch( (-0.7, -0.7), (0.6, 0.6),
                                               connectionstyle="arc3,rad = -0.6", **kw),
                      patches.FancyArrowPatch( (0.6, -0.7), (0.6, 0.6),**kw),
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


    #NOT NORMAL SITUATIONS (PHASE 2)
    
    #good
    ebmisc_nbl = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebmisc_nbt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw)]
    ebmisc_nbr = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, -1.425), (0, -0.125),connectionstyle="arc3,rad = -0.6", **kw)] 
    ebmisc_sbl = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.425), (0, 0.125),connectionstyle="arc3,rad = 0.6", **kw)]
    ebmisc_sbt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    ebmisc_sbr = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, 1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    ebmisc_wbl = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebmisc_wbt = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw)]
    ebmisc_wbr = [patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw),plt.Circle( (-1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, -1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]  
    
    ebl_nbmisc = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.425, -1.3), (-0.125, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebt_nbmisc = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw)]
    ebr_nbmisc = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]   
    nbmisc_sbl = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbmisc_sbt = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    nbmisc_sbr = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, 1.425), (0, 0.125),connectionstyle="arc3,rad = -0.6", **kw)]    
    nbmisc_wbl = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbmisc_wbt = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw)]
    nbmisc_wbr = [patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw),plt.Circle( (0, -1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.425, -1.3), (0.125, 0),connectionstyle="arc3,rad = -0.6", **kw)]                     
    
    ebl_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebt_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw)]
    ebr_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    nbl_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, -1.425), (0, -0.125),connectionstyle="arc3,rad = 0.6", **kw)]
    nbt_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw)]
    nbr_sbmisc = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]      
    sbmisc_wbl = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.425, 1.3), (0.125, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    sbmisc_wbt = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw)]
    sbmisc_wbr = [patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw),plt.Circle( (0, 1.25), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, -1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]                     
    
    #good
    ebl_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebt_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.5, 0), (0, 0),**kw)]
    ebr_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]   
    nbl_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, -1.425), (0, -0.125),connectionstyle="arc3,rad = 0.6", **kw)]
    nbt_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (0, -1.5), (0, 0),**kw)]
    nbr_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = -0.6", **kw)]     
    sbl_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    sbt_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (0, 1.5), (0, 0),**kw)]
    sbr_wbmisc = [patches.FancyArrowPatch( (1.5, 0), (0, 0),**kw),plt.Circle( (1.25, 0), 0.25, color='blue'),patches.FancyArrowPatch( (1.3, 1.425), (0, 0.125),connectionstyle="arc3,rad = -0.6", **kw)]    
 
    
    veh_movements = [ebmisc_ebmisc,nbmisc_nbmisc,sbmisc_sbmisc,wbmisc_wbmisc,
    
                     ebmisc_single,nbmisc_single,sbmisc_single,single_wbmisc,
                     
                     miscaction_ebl,miscaction_ebr,miscaction_ebt,
                     ebmisc_nbl,ebmisc_nbt,ebmisc_nbr,
                     ebmisc_sbl,ebmisc_sbt,ebmisc_sbr,
                     ebmisc_wbl,ebmisc_wbt,ebmisc_wbr,
                     
                     ebl_nbmisc,ebt_nbmisc,ebr_nbmisc,
                     miscaction_nbl,miscaction_nbr,miscaction_nbt,
                     nbmisc_sbl,nbmisc_sbt,nbmisc_sbr,
                     nbmisc_wbl,nbmisc_wbt,nbmisc_wbr,
                     
                     ebl_sbmisc,ebt_sbmisc,ebr_sbmisc,
                     nbl_sbmisc,nbt_sbmisc,nbr_sbmisc,                      
                     miscaction_sbl,miscaction_sbr,miscaction_sbt,
                     sbmisc_wbl,sbmisc_wbt,sbmisc_wbr,
                     
                     ebl_wbmisc,ebt_wbmisc,ebr_wbmisc,
                     nbl_wbmisc,nbt_wbmisc,nbr_wbmisc,
                     sbl_wbmisc,sbt_wbmisc,sbr_wbmisc,
                     miscaction_wbl,miscaction_wbr,miscaction_wbt]
    
    veh_dict = {'eb misc. action/eb misc. action':ebmisc_ebmisc,
                'nb misc. action/nb misc. action':nbmisc_nbmisc,
                'sb misc. action/sb misc. action':sbmisc_sbmisc,
                'wb misc. action/wb misc. action':wbmisc_wbmisc,
                
                'eb misc. action(single vehicle crash)':ebmisc_single,
                'nb misc. action(single vehicle crash)':nbmisc_single,
                'sb misc. action(single vehicle crash)':sbmisc_single,
                '(single vehicle crash)wb misc. action':single_wbmisc,
                
                'eb misc. action/ebl':miscaction_ebl,'eb misc. action/ebt':miscaction_ebt,'eb misc. action/ebr':miscaction_ebr,                
                'eb misc. action/nbl':ebmisc_nbl,'eb misc. action/nbt':ebmisc_nbt,'eb misc. action/nbr':ebmisc_nbr,
                'eb misc. action/sbl':ebmisc_sbl,'eb misc. action/sbt':ebmisc_sbt,'eb misc. action/sbr':ebmisc_sbr,
                'eb misc. action/wbl':ebmisc_wbl,'eb misc. action/wbt':ebmisc_wbt,'eb misc. action/wbr':ebmisc_wbr,
                
                'ebl/nb misc. action':ebl_nbmisc,'ebt/nb misc. action':ebt_nbmisc,'ebr/nb misc. action':ebr_nbmisc,
                'nb misc. action/nbl':miscaction_nbl,'nb misc. action/nbt':miscaction_nbt,'nb misc. action/nbr':miscaction_nbr,                
                'nb misc. action/sbl':nbmisc_sbl,'nb misc. action/sbt':nbmisc_sbt,'nb misc. action/sbr':nbmisc_sbr,
                'nb misc. action/wbl':nbmisc_wbl,'nb misc. action/wbt':nbmisc_wbt,'nb misc. action/wbr':nbmisc_wbr,
                
                'ebl/sb misc. action':ebl_sbmisc,'ebt/sb misc. action':ebt_sbmisc,'ebr/sb misc. action':ebr_sbmisc,
                'nbl/sb misc. action':nbl_sbmisc,'nbt/sb misc. action':nbt_sbmisc,'nbr/sb misc. action':nbr_sbmisc,
                'sb misc. action/sbl':miscaction_sbl,'sb misc. action/sbt':miscaction_sbt,'sb misc. action/sbr':miscaction_sbr,
                'sb misc. action/wbl':sbmisc_wbl,'sb misc. action/wbt':sbmisc_wbt,'sb misc. action/wbr':sbmisc_wbr,
                
                'ebl/wb misc. action':ebl_wbmisc,'ebt/wb misc. action':ebt_wbmisc,'ebr/wb misc. action':ebr_wbmisc,
                'nbl/wb misc. action':nbl_wbmisc,'nbt/wb misc. action':nbt_wbmisc,'nbr/wb misc. action':nbr_wbmisc,
                'sbl/wb misc. action':sbl_wbmisc,'sbt/wb misc. action':sbt_wbmisc,'sbr/wb misc. action':sbr_wbmisc,
                'wb misc. action/wbl':miscaction_wbl,'wb misc. action/wbt':miscaction_wbt,'wb misc. action/wbr':miscaction_wbr}                                
                                               

    return (veh_movements, veh_dict)
