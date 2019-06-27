class Solution:
    def removeElement(self,nums,val) -> int:

        i = 0
        j = len(nums)

        while True:

            if nums[i] == val:
                del nums[i]
                j = j - 1
            else:
                i = i +1

            if i == j:
                break
        
        print (nums)

        return i

nums = [2,1,0,1,2,2,3,0,4,2]
val = 2

s = Solution()

print(s.removeElement(nums,val))