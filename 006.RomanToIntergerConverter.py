# Roman to interger converter

class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numbers
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        # Result and counter initialization
        result = 0
        i = 0
        s = s.upper()

        # Loop to convert roman number from input string.
        while i < len(s):

            # Frst check check for pairs, that detecs roman (subtraction) pairs
            # If that string does not exist in nums we will check single string in "elif"
            # in "if", counter step is 2 in, "elif" 1
            # Last if string does not exist in nums, roman number is invalid, return -1.
            if s[i]+s[i+1] in nums.keys():
                result += nums[s[i]+s[i+1]]
                i += 2
            
            elif s[i] in nums.keys():
                result += nums[s[i]]
                i += 1
            
            else:
                return -1
        
        return result
            

r = Solution()
# "1994: MCMXCIV"
#print(r.romanToInt("MCMXCIV"))
# "2019: MMXIX"
print(r.romanToInt("MMXIX"))
#print(r.romanToInt("mmxixdsafsfdsfadsfdfadfdsaf"))

