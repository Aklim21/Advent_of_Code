# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, 
# but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 152085-670283.


'''
Password requirements: 
    
    - Must be 6 digits long <- already a given due to range check
    - Following digits cannot decrease in value
    - within the range: 152085 - 670283
    - there is a double digit pair in the password


Solution: 
    
    generate for loop within range
    create if statement for each criteria
    If a value passes all checks, store value in list
    solution will be list.length
'''

####### Check pair component #########

#tee splits a single iterator into two. Since we are looking to return two values (current and next) we set this to: 2
#chain merges two lists of objects into a single list, islice cuts off the starting values determined by the value used. i.e , we cut off the none value.
#^ don't think this is necessary
#zip grabs iterables from two variables and bunches them together. The total length of iterable values is determined by the shorter list.

from itertools import tee, islice, chain

def gen_pair(password):
    p, i, n = tee(password, 2)
    p = chain([None], p)
    n = chain(islice(n, 1, None), [None]) 
    return zip(p, i, n)  

def check_valid (password):
    for p, i, n in gen_pair(password):
        if (p == i and p != n):
            return True
        


############## Check No Decrease ###############

def check_decrease(password):
    a = 0
    for i in str(password):
        if int(i) < a :
            return False
        a = int(i)
    return True

    
########### Functional loop #################

valid =[]

for i in range (152085,670283):   
    if check_valid(str(i)) == True:
        if check_decrease(i) ==True: 
            valid.append(i)

print (len(valid))

