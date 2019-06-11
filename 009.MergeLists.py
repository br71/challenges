from functools import reduce

# Merge two list node by node, ascent order of nodes.
def mergeTwoLists(l1, l2):

    a = list(zip(l1,l2))

    print(sorted(reduce(lambda x, y: x + list(y),a,[])))

l1 = [1,2,4]
l2 = [5,3,1]
mergeTwoLists(l1,l2)