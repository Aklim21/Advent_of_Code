

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

###################### OpCode ####################################

def opCode(data):
    #data[1] = 5
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
            print("failed", data[0:3])
            break
    return data
    
##print(data)
##print(opCode(data)[0:4])


############################ Working example for data[1] iteration####################################
   
#import copy
    
#def grav(data):
#    base = data
#    x = copy.deepcopy(data)
#    
#    for i in range (0,100):
#        x[1] = i
#        y = opCode(x)
#        print(y[0:3])
#        if y[0] == 19690720:
#            break
#        else: 
#            print('----------------------------------------------\n')
#            x = copy.deepcopy(base) #reset data set
#         
##grav(data)

#############################################################################
            
            
            
# need data[0] = 19690720
#find requirements for data[1] & data[2] to get this result

############################################################################


# import copy
    
# def grav(data):
#     base = copy.deepcopy(data)
#     x = copy.deepcopy(data)
    
#     for i in range (0,99):
#         print('---------------------------------------------- new i loop \n')
#         x[1] = i
#         print(x[0:20],"current i loop data set")
#         y = opCode(x)
#         print(y[0:20],"post opcode i loop data set")
#         if y[0] == 19690720:
#             print("fuck yeah!", y[0:3])
#             return
            
#         else:
#             print("no-match")
#             z = copy.deepcopy(base)
#             print(z[0:20], "post i loop data reset")
#             for j in range(0,99):
#                 print('---------------------------------------------- new j loop \n')
#                 z[1]=i
#                 z[2]=j
#                 print(z[0:20], "current j data set")
#                 a = opCode(z)
#                 print(a[0:20] ,"post j loop op code data set")
#                 if a[0]== 19690720:
#                     print("fuck yeah!", a[0:3])
#                     return
#                 else:
#                     print("no-match")
#                     z = copy.deepcopy(base)
#                     print (a[0:20] , "j loop data reset")
#                 print(a[0:3])

# # it fails because i havent reset the dataset after having applied the first function during the parent for loop.
                
#             x = copy.deepcopy(base) #reset data set for data
         
# grav(data)


'''
So after realising i wasnt passing through the correct data set i just printed the fuck out of these lines to confirm what was being passed through and reset at each stage.

Now we can work on cleaning up the code.


'''


###########################################################################################################################

import copy
    
def grav(data):

    
    for i in range (0,99):
        x = copy.deepcopy(data)
        x[1] = i
        y = opCode(x)
        if y[0] == 19690720:
            print("match!", y[0:3])
            return
            
        else:
            print("no-match")
            for j in range(0,99):
                z = copy.deepcopy(data)
                z[1]=i
                z[2]=j
                a = opCode(z)
                if a[0]== 19690720:
                    print("match!", a[0:3])
                    print (100* a[1] + a[2])
                    return
                else:
                    print("no-match")
     
grav(data)

# from my horrific trialling above, i can see that now all we need to do is reset the dataset prior to any loop and then set the variables. 
# Initially I didn't think this would work since I didn't think the j loop would recognise i as a variable.
# but since the function still exists within the i for loop its still within scope.



