#Create text for time of day in plots. The syntax used for recording time of day
#varies by state, so this is stored in the respective state file.

#Assign text for time of day
def time_text(crash, n, state):

    time = [0,0,0,0,0,0]

    if state in ['alaska','colorado','florida','nebraska']:

        for t in crash[1][n+2]:
            if t == 'na':
                time[5] += 1
            elif int(t) in [75,80,99,9999]:
                time[5] += 1
            elif int(t) < 60:
                time[0] += 1
            elif int(t) >= 100 and int(t) < 600:
                time[0] += 1
            elif int(t) >= 600 and int(t) < 900:
                time[1] += 1
            elif int(t) >= 900 and int(t) < 1500:
                time[2] += 1
            elif int(t) >= 1500 and int(t) < 1800:
                time[3] += 1
            elif int(t) >= 1800 and int(t) < 2400:
                time[4] += 1
            else:
                time[5] += 1

    elif state in ['nevada']:

        for t in crash[1][n+2]:
            if t[6] == 'a':
                if t[0:1] == '12':
                    time[0] += 1
                elif t[0] == '0':
                    if int(t[1]) < 6:
                        time[0] += 1
                    elif int(t[1]) >= 6 and int(t[1]) < 9:
                        time[1] += 1
                    elif int(t[1]) == 9:
                        time[2] += 1
                elif t[0] == '1':
                    time[2] += 1
            elif t[6] == 'p':
                if t[0:1] == '12':
                    time[2] += 1
                elif t[0] == '0':
                    if int(t[1]) < 3:
                        time[2] += 1
                    elif int(t[1]) >= 3 and int(t[1]) < 6:
                        time[3] += 1
                    elif int(t[1]) >= 6:
                        time[4] += 1
                elif t[0] == '1':
                    time[4] += 1

            else:
                time[5] += 1
                
    elif state in ['newyork']:

        for t in crash[1][n+2]:
            if t[5] == 'a':
                if t[0:1] == '12':
                    time[0] += 1
                elif t[0] == '0':
                    if int(t[1]) < 6:
                        time[0] += 1
                    elif int(t[1]) >= 6 and int(t[1]) < 9:
                        time[1] += 1
                    elif int(t[1]) == 9:
                        time[2] += 1

                elif t[0] == '1':
                    time[2] += 1
            elif t[5] == 'p':
                if t[0:1] == '12':
                    time[2] += 1
                elif t[0] == '0':
                    if int(t[1]) < 3:
                        time[2] += 1
                    elif int(t[1]) >= 3 and int(t[1]) < 6:
                        time[3] += 1
                    elif int(t[1]) >= 6:
                        time[4] += 1
                elif t[0] == '1':
                    time[4] += 1

            else:
                time[5] += 1
    
    elif state in ['oregon']:

        for t in crash[1][n+2]:
            if int(t) in [99]:
                time[5] += 1
            elif int(t) < 6:
                time[0] += 1
            elif int(t) >= 6 and int(t) < 9:
                time[1] += 1
            elif int(t) >= 9 and int(t) < 15:
                time[2] += 1
            elif int(t) >= 15 and int(t) < 18:
                time[3] += 1
            elif int(t) >= 18 and int(t) < 24:
                time[4] += 1
            else:
                time[5] += 1                  
    
    elif state in ['washington']:

        for t in crash[1][n+2]:
            if ":" in t:
                if len(t) == 5:
                    if int(t[0:2]) < 6:
                        time[0] += 1
                    elif int(t[0:2]) < 9:
                        time[1] += 1
                    elif int(t[0:2]) < 15:
                        time[2] += 1
                    elif int(t[0:2]) < 18:
                        time[3] += 1
                    elif int(t[0:2]) < 24:
                        time[4] += 1
                    
                elif len(t) == 4:
                    if int(t[0]) < 6:
                        time[0] += 1
                    elif int(t[0]) < 9:
                        time[1] += 1
                    elif int(t[0]) == 9:
                        time[2] += 1
                     
            else:
                try:
                    if t < 0.25:
                        pass
                except TypeError:
                    pass
                else:
                    if t < 0.25:
                        time[0] += 1
                    elif t < 0.375:
                        time[1] += 1
                    elif t < 0.625:
                        time[2] += 1
                    elif t < 0.75:
                        time[3] += 1
                    elif t < 1:
                        time[4] += 1
                    else:
                        time[5] += 1 

    return time
            
#Create text for crash severity in plots. The syntax used for recording severity
#varies by state, so this is stored in the respective state file.
def severity_var_text(crash, state):

    import matplotlib.pyplot as plt
    n = 0
    if state in ['alaska']:
        #set up severity variables for text box in diagram
        fatal_crashes = "Fatality = " + str(crash[1][1]) + ' (' + "{:.0%}".format(crash[1][1]/crash[1][0]) + ')'
        incapacitating = "Incapacitating Injury = " + str(crash[1][2]) + ' (' + "{:.0%}".format(crash[1][2]/crash[1][0]) + ')'
        possible_injury = "Possible Injury = " + str(crash[1][3]) + ' (' + "{:.0%}".format(crash[1][3]/crash[1][0]) + ')'
        property_damage_only = "Property Damage Only = " + str(crash[1][4]) + ' (' + "{:.0%}".format(crash[1][5]/crash[1][0]) + ')'
        unknown = "Unknown = " + str(crash[1][5]) + ' (' + "{:.0%}".format(crash[1][5]/crash[1][0]) + ')'

        
        #text box crash severities in lower left corner
        plt.text(-4.8, -2.60, 'Crash Severity',weight = 'bold', fontsize=8)
        plt.text(-4.8, -2.85, fatal_crashes, fontsize=8)
        plt.text(-4.8, -3.10, incapacitating, fontsize=8)
        plt.text(-4.8, -3.35, possible_injury, fontsize=8)
        plt.text(-4.8, -3.60, property_damage_only, fontsize=8)
        plt.text(-4.8, -3.85, unknown, fontsize=8)

        #Define list index based on number of severities above
        n = 6

    elif state in ['colorado','nebraska', 'nevada','oregon']:
        
        fatal_crashes = "Fatal = " + str(crash[1][1]) + ' (' + "{:.0%}".format(crash[1][1]/crash[1][0]) + ')'
        injury = "All Injury = " + str(crash[1][2]) + ' (' + "{:.0%}".format(crash[1][2]/crash[1][0]) + ')'
        property_damage_only = "Property Damage Only = " + str(crash[1][3]) + ' (' + "{:.0%}".format(crash[1][3]/crash[1][0]) + ')'
        unknown = "Unknown = " + str(crash[1][4]) + ' (' + "{:.0%}".format(crash[1][4]/crash[1][0]) + ')'
        
        plt.text(-4.8, -2.60, 'Crash Severity',weight = 'bold', fontsize=8)
        plt.text(-4.8, -2.85, fatal_crashes, fontsize=8)
        plt.text(-4.8, -3.10, injury , fontsize=8)
        plt.text(-4.8, -3.35, property_damage_only, fontsize=8)
        plt.text(-4.8, -3.60, unknown, fontsize=8)

        n = 5

    elif state in ['newyork']:

        fatal_crashes = "Fatal = " + str(crash[1][1]) + ' (' + "{:.0%}".format(crash[1][1]/crash[1][0]) + ')'
        incapacitating = "All Injury = " + str(crash[1][2]) + ' (' + "{:.0%}".format(crash[1][2]/crash[1][0]) + ')'
        possible_injury = "Property Damage Only = " + str(crash[1][3]) + ' (' + "{:.0%}".format(crash[1][3]/crash[1][0]) + ')'
        property_damage_only = "Not-reportable = " + str(crash[1][4]) + ' (' + "{:.0%}".format(crash[1][4]/crash[1][0]) + ')'
        unknown = "Unknown = " + str(crash[1][5]) + ' (' + "{:.0%}".format(crash[1][5]/crash[1][0]) + ')'

        plt.text(-4.8, -2.60, 'Crash Severity',weight = 'bold', fontsize=8)
        plt.text(-4.8, -2.85, fatal_crashes, fontsize=8)
        plt.text(-4.8, -3.10, incapacitating, fontsize=8)
        plt.text(-4.8, -3.35, possible_injury, fontsize=8)
        plt.text(-4.8, -3.60, property_damage_only, fontsize=8)
        plt.text(-4.8, -3.85, unknown, fontsize=8)

        n = 6

    elif state in ['florida','washington']:

        fatal_crashes = "Fatal = " + str(crash[1][1]) + ' (' + "{:.0%}".format(crash[1][1]/crash[1][0]) + ')'
        incapacitating = "Serious Injury = " + str(crash[1][2]) + ' (' + "{:.0%}".format(crash[1][2]/crash[1][0]) + ')'
        possible_injury = "Evident/Possible Injury = " + str(crash[1][3]) + ' (' + "{:.0%}".format(crash[1][3]/crash[1][0]) + ')'
        property_damage_only = "Property Damage Only = " + str(crash[1][4]) + ' (' + "{:.0%}".format(crash[1][4]/crash[1][0]) + ')'
        unknown = "Unknown = " + str(crash[1][5]) + ' (' + "{:.0%}".format(crash[1][5]/crash[1][0]) + ')'

        plt.text(-4.8, -2.60, 'Crash Severity',weight = 'bold', fontsize=8)
        plt.text(-4.8, -2.85, fatal_crashes, fontsize=8)
        plt.text(-4.8, -3.10, incapacitating, fontsize=8)
        plt.text(-4.8, -3.35, possible_injury, fontsize=8)
        plt.text(-4.8, -3.60, property_damage_only, fontsize=8)
        plt.text(-4.8, -3.85, unknown, fontsize=8)

        n = 6

    return n
