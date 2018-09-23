#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print(s[0])
# 's'
print(s[3])
# 'ask'
print(s[2:])
# 'las'
print(s[1:4])
# 'k'
print(s[4])
# Bonus: Use indexing to reverse the string
print(s[::-1])
print('DONE WITH 1')
###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
for value in mylist:
    if isinstance(value, list):
        for values in value:
            if values =='hello':
                print('hello')
    else:
        if value =='hello':
            print('hello')
print('DONE WITH 2')
###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
for v in d1.values():
    if v =='hello':
        print (v)

for k,v in d2.items():
    for key,value in v.items():
        if value == 'hello':
            print(key,value)
print('DONE WITH 3')
###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print (set(mylist))
print('DONE WITH 4')
###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
h = "Hello my dog's name is Sammy and he is 4 years old"
test = "Hello my dog's name is {dog} and he is {age} years old".format(dog=name, age=age)

print (test)
print('DONE WITH 5')
