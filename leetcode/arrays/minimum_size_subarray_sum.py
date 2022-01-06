class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        start, end = 0, 0
        ans = float('inf')
        sm = nums[start]

        while end < len(nums):
            if sm >= s:
                ans = min(ans, (end-start)+1)
                sm -= nums[start]
                start += 1
            else:
                end += 1
                if end < len(nums):
                    sm += nums[end]
                else:
                    break

        return ans if ans != float('inf') else 0
