#Create plot text

def plot_text(crash, state):
    
    import matplotlib.pyplot as plt
    from collections import Counter
    
    #Set up total crashes variable for text box in diagram
    total_crashes = "Total Crashes = " + str(crash[1][0])

    #Set up severity crashes variable for text box in diagram

    from .time_severity_text import severity_var_text
    #Define variable for list indices
    n = severity_var_text(crash, state)

    #Getting the most common crash type for the vehicle movements
    crash_type = Counter(crash[1][n])
    crash_type = crash_type.most_common(1)
    crash_type = crash_type[0][0]

    
    #BEHAVIOR.......
    #Getting the most common crash behavior for the vehicle movements
    behavior = Counter(crash[1][n+1])
    behavior = behavior.most_common(5)
    behavior_list = ['-','-','-','-','-',]

    #Set up variables for behavior text box
    i = 0
    while i < len(behavior):
        if behavior[i][0] == 'na':
            behavior_list[i] = behavior[i][0].upper() + ' = ' + str(behavior[i][1])
        else:
            behavior_list[i] = behavior[i][0].title() + ' = ' + str(behavior[i][1])
        i += 1

    #Time of Day.......
    #Put time into bins for the vehicle movements
    from .time_severity_text import time_text
    time = time_text(crash,n,state)

    #set up time variables for text box in diagram
    mid_6_crashes = "12am - 6am = " + str(time[0])
    six_9_crashes = "6am - 9am = " + str(time[1])
    nine_3_crashes= "9am - 3pm = " + str(time[2])
    three_6_crashes = "3pm - 6pm = " + str(time[3])
    six_12_crashes = "6pm - 12am = " + str(time[4])
    unknown_time = "Unknown = " + str(time[5])
        
    #WEATHER.......
    #Getting the most common crash weather for the vehicle movements
    weather = Counter(crash[1][n+3])
    weather = weather.most_common(5)
    weather_list = ['-','-','-','-','-',]

    #Set up variables for weather text box
    i = 0
    while i < len(weather):
        if weather[i][0] == 'na':
            weather_list[i] = weather[i][0].upper() + ' = ' + str(weather[i][1])
        else:
            weather_list[i] = weather[i][0].title() + ' = ' + str(weather[i][1])
        
        i += 1

        
    #LIGHTING.......
    #Getting the most common lighting ocnditions for the vehicle movements
    light = Counter(crash[1][n+4])
    light = light.most_common(5)
    light_list = ['-','-','-','-','-',]

    #Set up variables for lighting text box
    i = 0
    while i < len(light):
        if light[i][0] == 'na':
            light_list[i] = light[i][0].upper() + ' = ' + str(light[i][1])
        else:
            light_list[i] = light[i][0].title() + ' = ' + str(light[i][1])
        
        i += 1


    #SURFACE CONDITIONS.......
    #Getting the most common crash surface condition for the vehicle movements
    #Only print if in crash data
    if state=='nevada':
        pass
           
    else: 
        surf = Counter(crash[1][n+6])
        surf = surf.most_common(5)
        surf_list = ['-','-','-','-','-',]

        i = 0
        while i < len(surf):
            if surf[i][0] == 'na':
                surf_list[i] = surf[i][0].upper() + ' = ' + str(surf[i][1])
            else:
                surf_list[i] = surf[i][0].title() + ' = ' + str(surf[i][1])                
            i += 1
        
    #Textbox vehicle movements, crash type, and total crashes at top of diagram        
    # plt.title(intersection_name,loc='right')
    plt.text(0,3.40, crash[0].upper(), horizontalalignment='center',weight = 'bold')
    plt.text(0,3.10, crash_type.title(), horizontalalignment='center', fontsize=9)
    plt.text(0,2.80, total_crashes, horizontalalignment='center',fontsize=9)

    #Text box crash severities in lower left corner
    #See 'severity_var_text' function in 'Time_Severity_Text.py' in respecive state folder

    #Text box crash behaviors in lower right corner
    plt.text(4.8, -2.6, 'Driver Behavior',horizontalalignment='right',weight = 'bold', fontsize=8)
    plt.text(4.8, -2.85, behavior_list[0], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -3.10, behavior_list[1], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -3.35, behavior_list[2], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -3.60, behavior_list[3], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -3.85, behavior_list[4], horizontalalignment='right', fontsize=8)

    #Text box time of day in middle left corner
    plt.text(-4.8, -0.1, 'Time of Day',horizontalalignment='left',weight = 'bold', fontsize=8)
    plt.text(-4.8, -0.35, mid_6_crashes, horizontalalignment='left', fontsize=8)
    plt.text(-4.8, -0.6, six_9_crashes, horizontalalignment='left', fontsize=8)
    plt.text(-4.8, -0.85, nine_3_crashes, horizontalalignment='left', fontsize=8)
    plt.text(-4.8, -1.1, three_6_crashes, horizontalalignment='left', fontsize=8)
    plt.text(-4.8, -1.35, six_12_crashes, horizontalalignment='left', fontsize=8)
    plt.text(-4.8, -1.60, unknown_time, horizontalalignment='left', fontsize=8)

    #Text box weather in upper right hand corner
    plt.text(4.8, 2.2, 'Weather',horizontalalignment='right',weight = 'bold', fontsize=8)
    plt.text(4.8, 1.95, weather_list[0], horizontalalignment='right', fontsize=8)
    plt.text(4.8, 1.7, weather_list[1], horizontalalignment='right', fontsize=8)
    plt.text(4.8, 1.45, weather_list[2], horizontalalignment='right', fontsize=8)
    plt.text(4.8, 1.2, weather_list[3], horizontalalignment='right', fontsize=8)
    plt.text(4.8, 0.95, weather_list[4], horizontalalignment='right', fontsize=8)

    #Text box lighting conditions in middle right corner
    plt.text(4.8, -0.1, 'Lighting Conditions',horizontalalignment='right',weight = 'bold', fontsize=8)
    plt.text(4.8, -0.35, light_list[0], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -0.6, light_list[1], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -0.85, light_list[2], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -1.1, light_list[3], horizontalalignment='right', fontsize=8)
    plt.text(4.8, -1.35, light_list[4], horizontalalignment='right', fontsize=8)
    
    #Text box surface conditions in upper left hand corner. Only print if in crash data
    if state not in ['nevada']:
        plt.text(-4.8, 2.2, 'Surface Conditions',horizontalalignment='left',weight = 'bold', fontsize=8)
        plt.text(-4.8, 1.95, surf_list[0], horizontalalignment='left', fontsize=8)
        plt.text(-4.8, 1.7, surf_list[1], horizontalalignment='left', fontsize=8)
        plt.text(-4.8, 1.45, surf_list[2], horizontalalignment='left', fontsize=8)
        plt.text(-4.8, 1.2, surf_list[3], horizontalalignment='left', fontsize=8)
        plt.text(-4.8, 0.95, surf_list[4], horizontalalignment='left', fontsize=8)

    plt.axes().set_xlim(-5, 5)
    plt.axes().set_ylim(-4, 4)
    plt.axes().set_aspect(1)
