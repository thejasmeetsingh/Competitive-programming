class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        
        for char in s:
          for idx in range(len(result)):
            if char.isalpha():
              result.append(result[idx] + char.lower())
              result[idx] = result[idx] + char.upper()
            else:
              result[idx] = result[idx] + char
        
        return result
