class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
          return points
      
        sqrt_map = dict()
        
        for point in points:
          sqrt = (point[0] ** 2 + point[1] ** 2) ** 0.5
          
          if sqrt in sqrt_map:
            sqrt_map[sqrt].append(point)
          else:
            sqrt_map[sqrt] = [point]
          
        sorted_keys = sorted(sqrt_map.keys())
        result = []
        
        while len(result) != k:
          result.extend(sqrt_map[sorted_keys.pop(0)])
        
        return result
