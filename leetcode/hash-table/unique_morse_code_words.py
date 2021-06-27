class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        morse_code = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..'
        }

        unqiue_codes = set()

        for word in words:
            code = "".join(map(lambda x: morse_code[x], word))
            unqiue_codes.add(code)
        
        return len(unqiue_codes)
