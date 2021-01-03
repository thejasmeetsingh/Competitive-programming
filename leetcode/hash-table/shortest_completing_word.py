class Solution:
    def shortestCompletingWord(self, license_plate: str, words: list) -> str:
        strings = []
        for char in license_plate.lower():
            if char.isalpha():
                strings.append(char)
        words.sort(key=len)

        def words_in(_strings, _words):
            for _char in _strings:
                if _strings.count(_char) > _words.count(_char):
                    return False
            return True

        for word in words:
            if words_in(strings, word):
                return word