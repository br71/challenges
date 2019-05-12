# Reversing Interger with some shecks

import sys

class Solution:
    def reverse(self, x: int) -> int:

        if x > 2147483647 or x < -2147483648:
            print("Number must be signed interger")
            

        if x < 0:
            # Removing, slicing - sign before reversing number (str(x)[1:])
            t = int(str(str(x)[1:])[::-1])
        else:
            #Reverse slicing !!!
            t = int(str(x)[::-1])

        #Check for owerflow, t must be signed 32 bit interger
        if t > 2147483647 or t < -2147483648:
            return 0
        else:
            return t

y= -12345678
r = Solution()
print(r.reverse(y))