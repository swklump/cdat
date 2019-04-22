#In Scenario 1, pedestrian or bicyclist involved
def arrow_movements1():

    import matplotlib.patches as patches

    style = "Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    
    ebl_pedestrian = [patches.FancyArrowPatch( (-0.975, -1.625), (0, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    ebr_pedestrian = [patches.FancyArrowPatch( (-0.975, 1.625), (0, 0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    ebt_pedestrian = [patches.FancyArrowPatch( (-1.6, 0), (-0.65, 0),**kw)]
    
    nbl_pedestrian = [patches.FancyArrowPatch( (0.625, -0.975), (-0.35, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbr_pedestrian = [patches.FancyArrowPatch( (-1.625, -0.975), (-0.65, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    nbt_pedestrian = [patches.FancyArrowPatch( (0, -1.6), (0, -0.65),**kw)]

    pedestrian_sbl = [patches.FancyArrowPatch( (-1.625, 0.975), (-0.65, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    pedestrian_sbr = [patches.FancyArrowPatch( (0.625, 0.975), (-0.35, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    pedestrian_sbt = [patches.FancyArrowPatch( (0, 1.6), (0, 0.65),**kw)]

    pedestrian_wbl = [patches.FancyArrowPatch( (0.975, 1.625), (0, 0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    pedestrian_wbr = [patches.FancyArrowPatch( (0.975, -1.625), (0, -0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    pedestrian_wbt = [patches.FancyArrowPatch( (0.6, 0), (-0.35, 0),**kw)]

    bicyclist_ebl = [patches.FancyArrowPatch( (-0.975, -1.625), (0, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    bicyclist_ebr = [patches.FancyArrowPatch( (-0.975, 1.625), (0, 0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    bicyclist_ebt = [patches.FancyArrowPatch( (-1.6, 0), (-0.65, 0),**kw)]
    
    bicyclist_nbl = [patches.FancyArrowPatch( (0.625, -0.975), (-0.35, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    bicyclist_nbr = [patches.FancyArrowPatch( (-1.625, -0.975), (-0.65, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    bicyclist_nbt = [patches.FancyArrowPatch( (0, -1.6), (0, -0.65),**kw)]

    bicyclist_sbl = [patches.FancyArrowPatch( (-1.625, 0.975), (-0.65, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    bicyclist_sbr = [patches.FancyArrowPatch( (0.625, 0.975), (-0.35, 0),connectionstyle="arc3,rad = -0.6", **kw)]
    bicyclist_sbt = [patches.FancyArrowPatch( (0, 1.6), (0, 0.65),**kw)]

    bicyclist_wbl = [patches.FancyArrowPatch( (0.975, 1.625), (0, 0.65),connectionstyle="arc3,rad = 0.6", **kw)]
    bicyclist_wbr = [patches.FancyArrowPatch( (0.975, -1.625), (0, -0.65),connectionstyle="arc3,rad = -0.6", **kw)]
    bicyclist_wbt = [patches.FancyArrowPatch( (0.6, 0), (-0.35, 0),**kw)]


    veh_movements = [ebl_pedestrian,ebr_pedestrian,ebt_pedestrian,
                     nbl_pedestrian,nbr_pedestrian,nbt_pedestrian,
                     pedestrian_sbl,pedestrian_sbr,pedestrian_sbt,
                     pedestrian_wbl,pedestrian_wbr,pedestrian_wbt,
                     bicyclist_ebl,bicyclist_ebr,bicyclist_ebt,
                     bicyclist_nbl,bicyclist_nbr,bicyclist_nbt,
                     bicyclist_sbl,bicyclist_sbr,bicyclist_sbt,
                     bicyclist_wbl,bicyclist_wbr,bicyclist_wbt]

    veh_dict = {'pedestrian/ebl':ebl_pedestrian,'pedestrian/ebr':ebr_pedestrian,
                'pedestrian/ebt':ebt_pedestrian,'pedestrian/nbl':nbl_pedestrian,
                'pedestrian/nbr':nbr_pedestrian,'pedestrian/nbt':nbt_pedestrian,
                'pedestrian/sbl':pedestrian_sbl,'pedestrian/sbr':pedestrian_sbr,
                'pedestrian/sbt':pedestrian_sbt,'pedestrian/wbl':pedestrian_wbl,
                'pedestrian/wbr':pedestrian_wbr,'pedestrian/wbt':pedestrian_wbt,
                'bicyclist/ebl':bicyclist_ebl,'bicyclist/ebr':bicyclist_ebr,
                'bicyclist/ebt':bicyclist_ebt,'bicyclist/nbl':bicyclist_nbl,
                'bicyclist/nbr':bicyclist_nbr,'bicyclist/nbt':bicyclist_nbt,
                'bicyclist/sbl':bicyclist_sbl,'bicyclist/sbr':bicyclist_sbr,
                'bicyclist/sbt':bicyclist_sbt,'bicyclist/wbl':bicyclist_wbl,
                'bicyclist/wbr':bicyclist_wbr,'bicyclist/wbt':bicyclist_wbt}

    return (veh_movements, veh_dict) 
