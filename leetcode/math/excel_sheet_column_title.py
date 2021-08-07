class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""

        while columnNumber:
          columnNumber -= 1
          column_title = chr(65 + columnNumber % 26) + columnNumber
          columnNumber //= 26
        
        return column_title
