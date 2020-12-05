class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        elements = set()
        for num in nums:
            if num in elements:
                return True
            elements.add(num)
        return False