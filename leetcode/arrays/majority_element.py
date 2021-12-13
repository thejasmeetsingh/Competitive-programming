class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = dict()
        limit = len(nums) // 2
        
        for num in nums:
          hmap[num] = hmap.get(num, 0) + 1
          if hmap[num] > limit:
            return num
        
        return 0
