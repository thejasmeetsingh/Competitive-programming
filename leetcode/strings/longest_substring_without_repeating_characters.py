class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
          return 1
          
        if not s:
          return 0
        
        hmap = {}
        _max = 0
        start = 0
        
        for idx in range(len(s)):
          if s[idx] in hmap:
            start = max(start, hmap[s[idx]] + 1)
            
          hmap[s[idx]] = idx
          _max = max(_max, idx - start + 1)
        
        return _max
