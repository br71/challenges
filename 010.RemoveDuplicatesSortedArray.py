class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        i = 1
        

        for a in range(0,n-1):
            if nums[a] != nums[a+1]:
                i = i + 1
        
        return i



num = [0,0,1,1,1,2,2,3,3,4,4,4,4,4,7,7,7,10,10,10]
s = Solution()

print(s.removeDuplicates(num))

