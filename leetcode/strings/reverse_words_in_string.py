class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
          return ""
        
        result = ""
        idx = 0
        curr_chars = ""
        
        while idx < len(s):
          if s[idx] == " ":
            result += curr_chars[::-1] + s[idx]
            curr_chars = ""
          else:
            curr_chars += s[idx]
          idx += 1
        
        if curr_chars:
          result += curr_chars[::-1]
          
        return result
