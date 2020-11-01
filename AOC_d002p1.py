

####################### Boiler Plate - getData #######################

from aocd import get_data

def getData():
    data = get_data(day = 2, year = 2019, session="53616c7465645f5f29daa63d4ee96e56f1934780c2c5cd4e26c34b91ade2589ba0a8460c31dde69f3e726ef52eb356cf")
    fData = data.split(',')
    int_list= []
    for i in fData:
        int_list.append(int(i))
    return int_list

data = getData()
###################################################################


##### function


test_1 = [2,4,4,5,99,0]

def opCode(data):
    data[1] = 2
    #data[2] = 2   
    for i in range(0,len(data),4): 
        if data[i] == 99:
            #print("opcode was 99")
            break
            
        elif data[i] == 1:
            #print("opcode was 1")
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            #print("value is" , data[i+3])
        
        elif data[i] == 2:
            #print("opcode was 2")
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            #print("value is" , data[i+3])
        
        else:
            print("failed")
            break
    return data
    
#print(data)
print(opCode(data))
    

