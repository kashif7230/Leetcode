class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
      if len(s) != len(goal):
        return False
      string = s+s
      print(string)
      if goal in string:
        return True
      return False
     
      

        