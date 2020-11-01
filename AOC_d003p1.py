#################    Specification    ###################################
'''
so we want to create a list of all cooirdinates that exist for each cable.(c0,c1)

after we have created this co-ordinate list, we can run a checker function to confirm if one element exists within both co-ordinate lists. 

After we return this list we can then find the mahattan length from each and determine the co-ordinate that returns the shortest length. 

'''
####################### Boiler Plate - getData #######################

from aocd import get_data


def getData(set):
    '''
        Package I found on GitHub that lets you easily grab the data set.
        
        Formats data into two lists representing each cable.
    '''
    data = get_data(day = 3, year = 2019, session="53616c7465645f5f29daa63d4ee96e56f1934780c2c5cd4e26c34b91ade2589ba0a8460c31dde69f3e726ef52eb356cf")
    mData = data.split('\n')
    c0= mData[0].split(',')
    c1= mData[1].split(',')
    
    if set == 0: 
        return c0
    elif set == 1:
        return c1
    else: 
        print("error")
        return
'''
Initialise empty lists to contain every co-ordiate covered by cables
Initialise list to act as position counter
'''
c0Path = []
c1Path = []
pos = [0,0]

'''
function to append each co-ordinate covered by cable to path list
One function for each direction
'''
def addPath_U(c,dir, mag):
    for i in range (0, mag):
        pos[1] = pos[1] + 1
        x = (tuple(pos))
        c0Path.append(x)  if c == 0 else c1Path.append(x)
        
def addPath_D(c,dir, mag):
    for i in range (0, mag):
        pos[1] = pos[1] - 1
        x = (tuple(pos))
        c0Path.append(x)  if c == 0 else c1Path.append(x)
        
def addPath_R(c,dir, mag):
    for i in range (0, mag):
        pos[0] = pos[0] + 1
        x = (tuple(pos))
        c0Path.append(x)  if c == 0 else c1Path.append(x)

def addPath_L(c,dir, mag):
    for i in range (0, mag):
        pos[0] = pos[0] - 1
        x = (tuple(pos))
        c0Path.append(x)  if c == 0 else c1Path.append(x)
            

'''
Confirm direction of cable length
'''

def addMag(c,dir, mag):
    if dir == 'U':
        addPath_U(c,dir, mag)
    elif dir == 'D':
        addPath_D(c,dir, mag)
    elif dir == 'R':
        addPath_R(c,dir, mag)
    elif dir == 'L':
        addPath_L(c,dir, mag)
    else: 
        print('err - no direction')
        return
    

for i in getData(0):
    addMag(0,i[0],int(i[1:len(i)]))
    
pos = [0,0]

for i in getData(1):
    addMag(1,i[0],int(i[1:len(i)]))

 
'''
Generate list to store all co-ordinates where cables intersect.
'''
crossing = list(set(c0Path).intersection(set(c1Path)))


'''
Get absolute distance from origin and return position.
'''
def get_min (results):
    minDist = 10000
    matDist = 0
    for i in results:
        y = (i[0]**2 + i[1]**2 )**(1/2)
        if y < minDist :
            minDist = y
            pos = i
            matDist = abs(i[0]) + abs(i[1])
            
    print(minDist, "Manhattan Dist: " , matDist, pos)
    
get_min(crossing)




#######################  Solution process:  #############################




# ####################### Boiler Plate - getData #######################

# from aocd import get_data

# def getData(set):
#     data = get_data(day = 3, year = 2019, session="53616c7465645f5f29daa63d4ee96e56f1934780c2c5cd4e26c34b91ade2589ba0a8460c31dde69f3e726ef52eb356cf")
#     mData = data.split('\n')
#     c0= mData[0].split(',')
#     c1= mData[1].split(',')
    
#     if set == 0: 
#         return c0
#     elif set == 1:
#         return c1
#     else: 
#         print("error")
#         return


# #################    Specification    ###################################


# '''

# so we want to create a list of all cooirdinates that exist for each cable.(c0,c1)

# after we have created this co-ordinate list, we can run a checker function to confirm if one element exists within both co-ordinate lists. 

# After we return this list we can then find the mahattan length from each and determine the co-ordinate that returns the shortest length. 

# '''

# ############# accessing the direction and magnitude of a single element: ######################

# # def fData (data):
# #     for i in data[0,11]:
# #         print("Dir: ", i[0], "  Mag: " ,int(i[1:len(i)])) #<-- accessing the direction and magnitude of a single element
# #     return data
    
# # fData(getData(0))

# # print (getData(0)[0], getData(0)[-1] )
# # print (getData(1)[0], getData(1)[-1] )

# #############  setting co-ordinate system:  ####################

# '''
# so we dont need to define an overall co-ordinate system, we only need to track the co-ordinate positions passed by the cable. 

# i.e we need to keep track of the origin of the cable and depending on the direction of the coordinate we can append a co-oridinate position to a list that will 


 
# create empty list to store cable co-oridnates.
# for i in data set: 
#         check direction
#         switch case to define value to be changed:
#             u = +y
#             d = -y
#             l = -x
#             r = +x 
#             append co-ordinate to co-ordinate list
#             repeate in while loop is below value of i.magnitude
#             (will require us to set a count )
#             must return current position + updated co-ordinate list

# '''



# ################# Dirty method ###################

# '''
# Lets have a think about what we need to do here.
# lets accept for now that we need to repeat the code for each direction. We can fix this later

# What do we need to do for each co-ordinat value?

# - increment the position by 1 of the magnitude, append that position to a list.

# In our current solution, we are able to update the positions at each change in direction, but if we run a for loop within the range of the magnitude, 
# on the position value, we can achieve the same end goal. 


# '''
# # c0Path = []
# # c1Path = []
# # pos = [0,0]

# # #for i in getData(1)[0:5]:
# # #    print ("poop")

# # def addMag(dir, mag):
# #     if dir == 'u':
# #         pos[1] = pos[1] + mag
# #         return pos
# #     elif dir == 'd':
# #         pos[1] = pos[1] - mag
# #         return pos
# #     elif dir == 'r':
# #         pos[0] = pos[0] + mag
# #         return pos
# #     elif dir == 'l':
# #         pos[0] = pos[0] - mag
# #         return pos
# #     else: 
# #         print('err - no direction')
# #         return
    
# # def addPath(dir, mag):
# #     for i in range (0, mag):
# #         c0Path.append()                         ''' Hard coded to cable 0!!!!'''


# # addMag('u',234)
# # addPath('u',234)
# # print (pos)
# # print (c0Path)



# ############################################################################

# '''
# In the below solution, ive realised that we can skip using pos as the path nodes, and just use it as the position keeper 
# (as i should have done from the start)

# Moving forward our current issue is that our c0path list keeps reupdating pos for each element within the list within each loop.

# I can use a dirty fix here where i deep copy the value of pos to another variable

# '''

# # c0Path = []
# # c1Path = []
# # pos = [0,0]


# # def addPath_U(dir, mag):
# #     for i in range (0, mag+1):
# #         pos[1] = pos[1] + 1
# #         print(pos)
# #         c0Path.append(pos)
        
# # def addPath_D(dir, mag):
# #     for i in range (0, mag+1):
# #         pos[1] = pos[1] - 1
# #         print(pos)
# #         c0Path.append(pos)
        
# # def addPath_R(dir, mag):
# #     for i in range (0, mag+1):
# #         pos[0] = pos[0] + 1
# #         print(pos)
# #         c0Path.append(pos)

# # def addPath_L(dir, mag):
# #     for i in range (0, mag+1):
# #         pos[0] = pos[0] - 1
# #         print(pos)
# #         c0Path.append(pos)

# # def addMag(dir, mag):
# #     if dir == 'U':
# #         addPath_U(dir, mag)
# #     elif dir == 'D':
# #         addPath_D(dir, mag)
# #     elif dir == 'R':
# #         addPath_R(dir, mag)
# #     elif dir == 'L':
# #         addPath_L(dir, mag)
# #     else: 
# #         print('err - no direction')
# #         return
    
# # for i in getData(0)[0:2]:
# #     addMag(i[0],int(i[1:len(i)]))
# #     print(c0Path)
    
    

# ############################################################################

# '''
# I can use a dirty fix here where i deep copy the value of pos to another variable

# '''

# c0Path = []
# c1Path = []
# pos = [0,0]


# def addPath_U(c,dir, mag):
#     for i in range (0, mag):
#         pos[1] = pos[1] + 1
#         x = (tuple(pos))
#         c0Path.append(x)  if c == 0 else c1Path.append(x)
        
# def addPath_D(c,dir, mag):
#     for i in range (0, mag):
#         pos[1] = pos[1] - 1
#         x = (tuple(pos))
#         c0Path.append(x)  if c == 0 else c1Path.append(x)
        
# def addPath_R(c,dir, mag):
#     for i in range (0, mag):
#         pos[0] = pos[0] + 1
#         x = (tuple(pos))
#         c0Path.append(x)  if c == 0 else c1Path.append(x)

# def addPath_L(c,dir, mag):
#     for i in range (0, mag):
#         pos[0] = pos[0] - 1
#         x = (tuple(pos))
#         c0Path.append(x)  if c == 0 else c1Path.append(x)
            

# def addMag(c,dir, mag):
#     if dir == 'U':
#         addPath_U(c,dir, mag)
#     elif dir == 'D':
#         addPath_D(c,dir, mag)
#     elif dir == 'R':
#         addPath_R(c,dir, mag)
#     elif dir == 'L':
#         addPath_L(c,dir, mag)
#     else: 
#         print('err - no direction')
#         return
    
# for i in getData(0):
#     addMag(0,i[0],int(i[1:len(i)]))
    
# pos = [0,0]

# for i in getData(1):
#     addMag(1,i[0],int(i[1:len(i)]))

# # print(c0Path)
# # print("--------------------------------------")
# # print(c1Path)
 

# crossing = list(set(c0Path).intersection(set(c1Path)))



# def get_min (results):
#     minDist = 10000
#     matDist = 0
#     for i in results:
#         y = (i[0]**2 + i[1]**2 )**(1/2)
#         if y < minDist :
#             minDist = y
#             pos = i
#             matDist = abs(i[0]) + abs(i[1])
            
#     print(minDist, "Manhattan Dist: " , matDist, pos)
    
# get_min(crossing)


# '''
# At this point I basically have the solution.
# I have returned two lists that contains all co-ordinates traversed along each cable. We now need to compare the lists and return any elements 
# that appear in both since these indicate crossing points. 

# The current issue im facing is the simplest way to do this is to use sets, however you cannot set a list, since lists are un-hashable objects within 
# Python.

# -------------

# The standing issue is that although i converted the cable list into a tuple, the elements within the tuple were still lists. 
# This was addressed within the addMag function

# -------------

# submitted 1849 but this was too high, however i wasnt expecting this to return a mistake 



# --------------


# Would help if knew what the pythagoras theorm was....


# ---------------------


# submitted 873 but this is still too high...

# -----------------------



# issues we've addressed: 
    
# - so within the add path function we were iterating over a magnitude of one too many.
# ---> this  hase been adddresssed by changing the range in our for loops. 

# we can consider  the issue of negative values but there are addressed withing the pythagoran calculation.

# we also need to return  the manhattan lenghh, but  we can still calculate the closest value using the pythagoran theorem.

# So still use pythagoras theorem to get dist, but then need to return manhattan distance.

# Also needed to return the absolute magnitude of each value in the case these may have been negative in the manhattan distance calculation

# '''

# #########################################################################

# '''
# Here im thinking about how to simplify down the code to reduce repetition.
# '''

# # def addMag(dir, mag):
    
# #     x= 0
# #     y=1
    
# #     if dir == ('u'|'r'):
# #         pos[1] = pos[1] + mag
# #         return pos
    
    
    
# #     elif dir == 'd':
# #         pos[1] = pos[1] - mag
# #         return pos



# ######################################################################








