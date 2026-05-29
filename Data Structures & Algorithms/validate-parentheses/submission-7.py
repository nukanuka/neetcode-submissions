class Solution:
    def isValid(self, s: str) -> bool:
    # Optimization: Odd length strings can never be valid pairs
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Hash map to keep track of our matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top of the stack if it exists, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped bracket doesn't match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty at the end, all brackets were matched perfectly
        return not stack


