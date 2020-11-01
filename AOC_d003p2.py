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


'''
So we have:
    c0path
    c1path
    all intersections
    
    
for each co-ordinate :

    return index of object that matches co-ordinate for c0,c1
    NOTE: ensure exception check for duplicates
    sum indexes to get max circuit length
    
    
    
'''



