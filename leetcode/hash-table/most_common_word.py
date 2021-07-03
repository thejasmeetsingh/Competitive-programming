from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        if not paragraph:
            return ""
        
        paragraph = ''.join([word.lower() if word.isalnum() else ' ' for word in paragraph])
        
        if not banned:
            return paragraph.replace(" ", "")
        
        most_occured = Counter(paragraph.split(" ")).most_common()
        banned_set = set(banned)

        for word, _ in most_occured:
            if word.isalnum() and word not in banned_set:
                return word
        
        return ""
