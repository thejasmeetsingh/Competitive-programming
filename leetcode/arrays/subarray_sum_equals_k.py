class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
          return 0
        
        count = 0
        _sum = 0
        hmap = {0: 1}
        
        for idx in range(len(nums)):
          _sum += nums[idx]
          if _sum - k in hmap:
            count += hmap[_sum - k]
          
          hmap.update({_sum: hmap.get(_sum, 0) + 1})
        
        return count
