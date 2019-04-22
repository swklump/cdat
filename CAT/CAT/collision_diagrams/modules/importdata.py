#This function puts the columns in the crash csv file into columns for data manipulation

def prepare_lists(data_list,col,row,length = ''):
    
    if length:
        if len(row[col]) > length:
            data_list.append(row[col][0:length].lower())  
        elif row[col] == '':
            data_list.append('na')
        else:
            data_list.append(row[col].lower())     
    else:
        if row[col] == '':
            data_list.append('na')
        else:
            data_list.append(row[col].lower())


def prepare_lists_case(data_list,col,row):
    if row[col] == '':
        data_list.append('na')
    else:
        data_list.append(row[col])

