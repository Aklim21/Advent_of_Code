# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, the following are now true:

# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?

# Your puzzle input is 152085-670283.


'''
Password requirements: 
    
    - Must be 6 digits long <- already a given due to range check
    - Following digits cannot decrease in value
    - within the range: 152085 - 670283
    - there is a double digit pair in the password
    - The double digit pair must not exceed 2****



Solution: 
  - Same solution as before still holds
  - Require a counter check to confirm that the double digit pair still stands
  
    
Note: 
    - Need to be careful of soultions like: 111122. 
    - This solution is still correct since it contains a double digit pair.
    
'''

####### Check pair component #########

from itertools import tee, islice, chain

#Used itertools package here to run simultaneous iterations so we can compare iterated values more efficiently.
#input password, output the current and next values in the string.

def gen_pair(password):
    i, n = tee(password, 2)
    n = chain(islice(n, 1, None), [None]) 
    return zip(i, n)  

#Changes to part 1 required here.  
#Just needed to add a count to ensure the string does not contain more than two of the particular digit.

def check_valid (password):
    for i, n in gen_pair(password):
        if (i == n and password.count(i)<3):
            return True
    return False


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


