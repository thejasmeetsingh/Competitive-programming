class MagicDictionary:

    def __init__(self):
        self.dictionary = set()

    def buildDict(self, dictionary: list) -> None:
        self.dictionary = set(dictionary)

    def search(self, search_word: str) -> bool:
        dictionary = list(filter(lambda x: len(x) == len(search_word), self.dictionary))
        for string in dictionary:
            count = len(list(filter(lambda x: x[0] != x[1], zip(string, search_word))))
            if count == 1:
                return True
        return False
