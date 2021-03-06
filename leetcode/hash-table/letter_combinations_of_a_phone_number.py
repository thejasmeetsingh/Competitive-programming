class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stack = [("", 0)]
        l = len(digits)
        res = []
        if not l:
            return res

        while stack:
            s, p = stack.pop()

            if p == l:
                res.append(s)
                continue

            if digits[p] == '7' or digits[p] == '9':
                n = 4
            else:
                n = 3

            carry = (digits[p] == '8' or digits[p] == '9')
            start = (ord(digits[p]) - 48 - 2) * 3 + carry

            for i in range(0, n):
                stack.append((s + chr(97 + start), p + 1))
                start += 1
        return res
