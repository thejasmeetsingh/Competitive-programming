class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        num = 1
        nums = [1]

        for i in range(n - 1):
            choices = [nums[p2] * 2, nums[p3] * 3, nums[p5] * 5]
            num = min(choices)
            nums.append(num)

            if choices[0] == num:
                p2 += 1
            if choices[1] == num:
                p3 += 1
            if choices[2] == num:
                p5 += 1

        return num
