class Solution:
    def findDuplicates(self, nums: list) -> list:
        if not nums:
            return False

        appeared = set()
        result = set()

        for num in nums:
            if num in appeared:
                result.add(num)
            else:
                appeared.add(num)

        return sorted(result)