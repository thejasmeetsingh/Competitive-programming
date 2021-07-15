class Solution:
    roman_number = ''

    def intToRoman(self, num: int) -> str:
        symbols = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        for key in symbols:
            num = self.convertNumToLetter(num, symbols[key], key)
        return self.roman_number

    def convertNumToLetter(self, num: int, value: int, symbol: str) -> int:
        out = num // value
        self.roman_number += symbol * out
        return num - (out * value)