from functools import reduce

# Merge two list node by node, ascent order of nodes.
def mergeTwoLists(l1, l2):

    t = []

    #The method extend() appends the contents of argument to list
    # Zip function will pair nodes of list
    for i in list(zip(l1,l2)):
        t.extend(list(i))

    print(sorted(t))

l1 = [1,2,4]
l2 = [5,3,1]
mergeTwoLists(l1,l2)