from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(ransomNote)

        for char in magazine:
            if counter.get(char):
                if counter[char] - 1 == 0:
                    del counter[char]
                else:
                    counter[char] -= 1

        return True if not counter else False
