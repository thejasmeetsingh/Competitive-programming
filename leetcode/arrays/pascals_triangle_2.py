class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
      triangle = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
      ]
      
      if rowIndex <= 4:
        return triangle[rowIndex]
      
      for i in range(5, rowIndex + 1):
        new_triangle = [1]
        
        for j in range(1, i):
          new_triangle.append(triangle[-1][j - 1] + triangle[-1][j])
        
        new_triangle.append(1)
        triangle.append(new_triangle)
      
      return triangle[rowIndex]
