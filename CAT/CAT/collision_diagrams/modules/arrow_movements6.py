#In Scenario 6, both movements are lefts
def arrow_movements6():

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    style="Simple,tail_width=0.3,head_width=3,head_length=8"
    kw = dict(arrowstyle=style, color="k")

    ebl_nbl = [patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebl_sbl = [patches.FancyArrowPatch( (-0.7, -1.3), (0.6, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (-0.7, 1.3), (0.6, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    ebl_wbl = [patches.FancyArrowPatch( (-1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]

    nbl_sbl = [patches.FancyArrowPatch( (1.3, -1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (-1.3, 1.3), (0, 0),connectionstyle="arc3,rad = 0.6", **kw)]
    nbl_wbl = [patches.FancyArrowPatch( (0.3, -1.3), (-1, 0),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (0.3, 1.3), (-1, 0),connectionstyle="arc3,rad = 0.6", **kw)]

    sbl_wbl = [patches.FancyArrowPatch( (-1.3, 0.65), (0, -0.65),connectionstyle="arc3,rad = 0.6", **kw),
               patches.FancyArrowPatch( (1.3, 0.65), (0, -0.65),connectionstyle="arc3,rad = 0.6", **kw)]
      
    veh_movements = [ebl_nbl,ebl_sbl,ebl_wbl,nbl_sbl,nbl_wbl,sbl_wbl]
    veh_dict = {'ebl/nbl':ebl_nbl,'ebl/sbl':ebl_sbl,'ebl/wbl':ebl_wbl,'nbl/sbl':nbl_sbl,\
                'nbl/wbl':nbl_wbl,'sbl/wbl':sbl_wbl}

    return (veh_movements, veh_dict)
