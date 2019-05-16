# Check does is number "palindrom" , without converting it to string
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Reversed number initial value
        rn = 0

        # Basic check, palindrom is not number which ends with 0  and it is not 0 at same time)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Chopping end of input number and addind to reversed number "rn". 
        # Every next digit is added to right side by multipling "rn" with 10 and ading x%10 to "rn".
        # Loop  until x is greater than nr -> at that moment half of processed digits of number is processed. 
        while x > rn:
            rn = rn*10 + x%10
            # rn = 4, 41, 412, 4123 during loop
            x = x / 10

            # Casting of result in int: 4123321.4, -> 4123321
            x = int(x)
            # x = 4123321, 412332, 41233, 4123 during loop

        # Check if it is palindrome: "nr" is reversed "right" half on input number (x) 
        if x == rn:
            return True
        else:
            return False

        
d = Solution()
print(d.isPalindrome(41233214))
        
