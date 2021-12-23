class Solution:
    def binary_search(self, arr: list, target: int) -> bool:
      low = 0
      high = len(arr) - 1
      
      while low <= high:
        mid = (low + high) >> 1
        if arr[mid] == target:
          return True
        elif arr[mid] < target:
          low = mid + 1
        else:
          high = mid - 1
      
      return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      if not matrix:
        return False
      
      for arr in matrix:
        if self.binary_search(arr, target):
          return True
      
      return False
