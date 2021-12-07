class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
          return False
        
        brackets = {')': '(', '}': '{', ']': '['}
        opening_brackets = set(brackets.values())
        stack = []
        
        for char in s:
          if char in brackets:
            value = stack.pop() if stack else None
            if brackets[char] != value:
              return False
          else:
            stack.append(char)
          
        return not stack
