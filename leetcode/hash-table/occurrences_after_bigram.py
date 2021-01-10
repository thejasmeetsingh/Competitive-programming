class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        words = text.split(" ")
        third_word = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                third_word.append(words[i+2])

        return third_word