class Solution:
    def get_new_string(self, string):
      new_string = ""
      
      for char in string:
        if char != '#':
          new_string += char
        else:
          new_string = new_string[:-1]
      
      return new_string
      
    def backspaceCompare(self, s: str, t: str) -> bool:
      return self.get_new_string(s) == self.get_new_string(t)
