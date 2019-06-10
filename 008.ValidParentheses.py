
# Valid parentheses challenge
def validBrackets(s):
    stack = []
    # Hash map to define brackets. 
    map = {")": "(", "}": "{", "]": "["}

    # Loop trough expression.
    for char in s:

        # If the character is closed bracket
        if char in map:
            # char == ) or ] or }

            # Pop the topmost element (open bracket) from the stack if stack have some elements
            if stack:
                top_element = stack.pop()
            else:
                # Assign dummy value if stack is empty
                top_element = "#"

            # Check type of elements, if does not exist in map it will return false
            if map[char] != top_element:
                return False
        else:
            # Push open bracket in stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression (when stack is empty it returns False). 
    # Int that case we have to return True (not (stack)) 
    # t is helper variable, for debugger
    t = not stack
    return not stack

#s1 = "({(((())))))"
s1 = "))(("
#s2 = "(((((((()"
#s3 = "()()()()"
#s4 = "()[](){{}"
#s5 = "()()()()"

print(validBrackets(s1))
#print(validBrackets(s2))
#print(validBrackets(s3))
#print(validBrackets(s4))
#print(validBrackets(s5))




