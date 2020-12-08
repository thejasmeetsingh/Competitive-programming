class Solution(object):
    def findShortestSubArray(self, nums) -> int:
        left, right, count = {}, {}, {}
        degree = 0

        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            degree = count[x] if degree < count[x] else degree

        return min([right[x] - left[x] + 1 for x in count if count[x] == degree])