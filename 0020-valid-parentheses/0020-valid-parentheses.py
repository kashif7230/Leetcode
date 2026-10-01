class Solution:
    def isValid(self, s: str) -> bool:
      ans = []
      valid = { '()', '[]', '{}'}
      for c in s:
        if c in '( [ {':
          ans.append(c)
        else:
          if not ans or ans[-1] + c not in valid:
            return False
          ans.pop()
      return True if len(ans) == 0 else False 