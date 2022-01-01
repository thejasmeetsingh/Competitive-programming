from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
          return nums
        
        result = Counter(nums).most_common(k)
        return list(map(lambda x: x[0], result))
