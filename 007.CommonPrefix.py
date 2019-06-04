
# Determine common prefix in array of strings.
# Problem has been split in two parts, easier to understand. 
# First function compare two strings.

# Function to find common prefix between two strings
# Result is common prefix.

import profile

def commonPrefix(str1, str2): 
  
    result = ""; 
    n1 = len(str1) 
    n2 = len(str2) 
    a = 0
    b = 0

    #Starting lopping from beginning, a,b = 0 and incrementing by 1
    while a <= n1 - 1 and b <= n2 - 1: 
        
        # Compare string (one letter)
        if (str1[a] != str2[b]): 
            break
              
        result += str1[a] 

        #Incrementing loop counter
        a += 1
        b += 1
  
    return (result)


# Iterating trough array of strings.     
# This is horizontal search, first we compare first two elements in list to get common prefix.
# After that in next loop cycle we compare prefix with next element ( 2, 3 ... -> endOfList)
def commonPrefixArr (list, n): 
    prefix = list[0] 
    for i in range (1, n): 
        # In first iteration we compare index 0 and 1, in second prefix and index 2
        prefix = commonPrefix(prefix, list[i]) 
    return (prefix) 



# This is second (more pythonic) version using python functions (zip, sort)
def longestCommonPrefixPython(list):

        # Some tests at beginning (array with zero or one member)
        if not list: return -1
        if len(list) == 1: 
            return list[0]
        
        # First sorting list
        s = sorted(l1)
        #print(list)
        #print(s)
        
        # Result -> common prefix
        prefix = ""

        # Looping , searching for common prefix 
        # List is sorted, because that we need to check  first two elements
        # Zip function will return zip object: print (tuple(zip(s[0],s[1]))) -> (('f', 'f'), ('l', 'l'), ('o', 'o'), ('p', 'r'), ('p', 'e'), ('e', 's'), ('r', 't'))
        for x, y in zip(s[0], s[-1]):
            
            # If key, value is same we build prefix concating string
            if x == y: 
                prefix += x
            else: 
                break
        
        return prefix


# # First solution (not using python builtin functions)
# Test array  
l1 = ["flower","flowpi","florest", "flopper", "flotto"]
n = len(l1)
# Common prefix
#profile.run("commonPrefixArr(l1, n)")
c = commonPrefixArr(l1, n) 


#Display prefix
if (len(c)): 
    print ("Prefix is -",c)
else: 
        print("No common prefix") 



# Second solution using python zip, sort
print("Second solution: " + longestCommonPrefixPython(l1))
#profile.run("longestCommonPrefixPython(l1)")



# Results of profiler, second solutions is faster.

# python.exe 007.CommonPrefix.py"
#          17 function calls in 0.016 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         4    0.000    0.000    0.000    0.000 007.CommonPrefix.py:11(commonPrefix)
#         1    0.000    0.000    0.000    0.000 007.CommonPrefix.py:38(commonPrefixArr)
#         1    0.000    0.000    0.000    0.000 :0(exec)
#         8    0.000    0.000    0.000    0.000 :0(len)
#         1    0.016    0.016    0.016    0.016 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.016    0.016 profile:0(commonPrefixArr(l1, n))
#         0    0.000             0.000          profile:0(profiler)


#          7 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 007.CommonPrefix.py:48(longestCommonPrefixPython)
#         1    0.000    0.000    0.000    0.000 :0(exec)
#         1    0.000    0.000    0.000    0.000 :0(len)
#         1    0.000    0.000    0.000    0.000 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sorted)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 profile:0(longestCommonPrefixPython(l1))
#         0    0.000             0.000          profile:0(profiler)