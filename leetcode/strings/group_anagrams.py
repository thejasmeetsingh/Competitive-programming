from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      if not strs:
        return strs
      
      result = defaultdict(list)
      
      for string in strs:
        result["".join(sorted(string))].append(string)
      
      return list(result.values())
