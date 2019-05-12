
#Example1, MAP (apply map function on every list member)
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
print (list(map (square,my_nums)))
#stdout: [1, 4, 9, 16, 25]

#########################################################################################

#Example2, MAP
def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names=["Andy", "Eve", "Pera"]
print(list(map(splicer,names)))
#stdout: ['EVEN', 'E', 'EVEN']

#########################################################################################

#Example Filter (get result list based on function, if result is TRUE)
def check_even(num):
    return num%2 == 0

mynums2 = [1,2,3,4,5,6,7,8,9]
print(list(filter(check_even,mynums2)))
#stdout: [2, 4, 6, 8]

#########################################################################################

#Example 1 lambda

#Classic function
def square(numl):
    result = numl**2
    return result

#Shorter version
def square(numl):
    return numl**2

# One liner version
def square(numl): return numl**2

#Transform above fun to lambda (anonymous function)
# numl: is parameter, numl ** , numl ** 2 is what is doe and send return
lambda numl: numl ** 2

#Using lambda with map
mynumsl = [1,2,3,4,5]
x= list (map (lambda num:num**2,mynumsl))
print(x)
#stdout: [1, 4, 9, 16, 25]

#Using lambda with filter
y= list (filter (lambda num:num%2 == 0,mynumsl))
print(y)
#stdout: [2, 4]

#########################################################################################

#Example 2 lambda
# Grab first character in list
print(list(map(lambda x:x[0],names)))

# Reverse names
print(list(map(lambda x:x[::-1],names)))

#########################################################################################

# Example 1 Reduce
# Apply calculation at list pairs and get result.
# classic approach

#product = 1
#list5 = [1, 2, 3, 4]
#for num in list5:
#    product = product * num
#print ("Classic: {}".format(product)

# Reduce with classic function
from functools import reduce
list5 = [1, 2, 3, 4]
def r(x,y): return x*y
z = reduce(r,list5)
print (z)
#stdout: 24

# Reduce approach with lambda:
#from functools import reduce
z2 = reduce((lambda x, y: x * y), list5)
print (z2)
#stdout: 24