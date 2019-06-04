
# Determine common prefix in array of strings.
# Problem has been split in two parts, easier to understand. 
# first function to compare two strings.

# Function to find commot prefix between two strings
# Result is common prefix.

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
# Tho sis horizontal search, first we compare first two elements in list to get common prefix.
# After that in next loop cycle we compare prefix with next element ( 2, 3 ... -> endOfList)
def commonPrefixArr (list, n): 
    prefix = list[0] 
    for i in range (1, n): 
        # In first iteration we compare index 0 and 1, in second prefix and index 2
        prefix = commonPrefix(prefix, list[i]) 
    return (prefix) 


# Test array  
l1 = ["flower","flowpi","florest", "flopper", "flotto"]
n = len(l1)

# Common prefix
c = commonPrefixArr(l1, n) 
  
# Display prefix
if (len(c)): 
    print ("Prefix is -",c)
else: 
        print("No common prefix") 



