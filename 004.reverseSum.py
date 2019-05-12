# Reversing Interger with some shecks

import sys

class Solution:
    def reverse(self, x: int) -> int:

        if x > 2147483647 or x < -2147483648:
            print("Number must be signed interger")
            sys.exit(1)
            

        if x < 0:
            # Removing, slicing - sign before reversing number [1:] , reversing -> [::-1]
            t = int("-" + str(x)[1:][::-1])
        else:
            #Reverse slicing !!!
            t = int(str(x)[::-1])

        #Check for owerflow, t must be signed 32 bit interger
        if t > 2147483647 or t < -2147483648:
            return 0
        else:
            return t

z1= -1234567890
z2= 1234567890
r = Solution()
print(r.reverse(z1))
print(r.reverse(z2))