from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        idx = 0

        while idx <= len(s2) - len(s1):
          if s1_counter == Counter(s2[idx:idx + len(s1)]):
            return True
          idx += 1
        
        return False
