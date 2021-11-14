class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
          return -1
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
          mid = (i + j) // 2
          if nums[mid] == target:
            return mid
          elif target > nums[mid]:
            i = mid + 1
          else:
            j = mid - 1
        
        return -1
