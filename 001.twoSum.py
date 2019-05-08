# Function  finds numbers which sum is equal as predefined sum. Source of intergers is from list.
# Result is dict with pairs (index values) from list
def twoSum(nums,target):

    #Initial check for nums
    if not nums or len(nums) < 2:
        return[-1,-1]

    hashmap = dict()
    n = len(nums)
    result = dict()

    # Fill hashmap with data. Value of list is key of hashmap. Hashmap value is index of list(nums).
    # We need as result key of initial of complement value (7=9-num[i]).
    # At this way we can make instant search of s and get list(nums) index number
    for i in range(0,n):
        hashmap[nums[i]]=i

    #Second loop  trough list (nums) to determine complement number
    for j in range(0,n):
        s = target - nums[j]

        # Search for complement value in hasmap and ad to result hashmap  
        if s in hashmap.keys():
            # Removing (not adding) duplicated results: {0: 3, 3: 0, ...})
            if j not in result.values():
                result[j] = hashmap.get(s)
        
    #Check if resupt is not empty. If it is empty there is no matches.
    if bool(result):
        return result   
    else:      
        return[-1,-1]



##############################################

nums_ = [3, 15, 11, 7, 2, 8]
target_ = 10
print(twoSum(nums_,target_))

#######################################
#STDOUT: {0: 3, 4: 5}

