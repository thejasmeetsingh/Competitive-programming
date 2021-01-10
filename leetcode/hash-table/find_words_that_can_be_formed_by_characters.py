class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        n = 0
        for w in words:
            y = chars
            flag = 0
            for i in range(len(w)):
                if w[i] in y:
                    y = y.replace(w[i], '', 1)
                else:
                    flag = 1
                    break

            if flag == 0:
                n += len(w)
        return n