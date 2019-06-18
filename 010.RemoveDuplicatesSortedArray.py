import profile

class Solution:
    def removeDuplicates(self, nums) -> int:

        i = 0
        j = len(nums)

        while True:
            
            if nums[i] == nums[i+1]:
               del nums[i+1]
               j = j - 1
            else:
                i += 1

            if i + 1 == j:
                break

        return i+1


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()

print(s.removeDuplicates(nums))

#print(profile.run("s.removeDuplicates(nums)"))