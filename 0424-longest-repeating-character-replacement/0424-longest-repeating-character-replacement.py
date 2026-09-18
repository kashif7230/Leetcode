from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      check = Counter()
      l = 0
      ans = 0
      for r in range(len(s)):
        check[s[r]] +=1
        while (r-l+1) - max(check.values()) > k:
          check[s[l]] -=1
          l +=1
        ans = max(ans,r-l+1)
      return ans

''' class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      check = Counter()
      l = 0
      max_size = 0
      for r, val in enumerate(s):
        check[val] +=1
        max_size = max(max_size, check[val])

        if r-l+1-max_size > k:
          check[s[l]] -=1
          l +=1
      return len(s) - l  '''