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

Repated code so this can be reduced by introducing two variables 
- One defines x or y change
- Second defines +/- direction
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

'''
Reset pos for second cable
'''
pos = [0,0]

for i in getData(1):
    addMag(1,i[0],int(i[1:len(i)]))

 
'''
Generate list to store all co-ordinates where cables intersect.
'''
crossing = list(set(c0Path).intersection(set(c1Path)))


# '''
# Get absolute distance from origin and return position.
# '''
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


'''
So we have:
    c0path
    c1path
    all intersections
    
    
for i in cable0:
    full_mag = 999999999 
    c0_mag += i_mag 
    if co-ordinate is within crossing list:
        for i in cable1:
            if i is == crossing point:
                get c1_mag
                x = c0_mag + c1_mag
                if x < full_mag:
                    full_mag = x
                    
To get c_mag we need to consider the loop count since each item in the path list increments by one,
the magnitude of the cable is defined by its position in the path. 

But we also need to take into consideration that the first crossing point reached on c0 may not be the shortest over all.
We will need to hold it in a variable and make a comparison: min_len

We will continue to loop through both paths, eachtime updating min_len if the overall length is shorter.

min_len = 999999
c0_mag=0

for i in cable0 path:
    c0_mag += 1
    if i in crossing point list:
        c1_mag = 0
        for j in cable1 path:
            c1 loop count += 1
            if j == crossing point:
                if c0_len + c1_len < min_len:
                    min_len = c0_mag + c1_mag
return min_len, c0_mag, c1_mag

        

'''

def get_shortest(c0Path,c1Path, crossing):
    min_len = 999999
    c0_mag = 0
    for i in c0Path:
        c0_mag +=1
        if i 
        
        

