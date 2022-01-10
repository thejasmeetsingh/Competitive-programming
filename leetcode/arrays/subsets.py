class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
          return nums
        
        result = [[]]
        
        for num in nums:
          result += [sub_arr + [num] for sub_arr in result]
      
        return result
        
