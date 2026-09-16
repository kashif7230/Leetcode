class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
      ans = 0
      for target in range(1,27):     # use to find 26 uniques characters in string
        count= defaultdict(int)
        unique = l = valid = 0
        for r, ch in enumerate(s):
          count[ch] +=1
          if count[ch] == 1:
            unique +=1
          if count[ch] == k:
            valid +=1
          while unique > target:
            left = s[l]
            if count[left] == k:
              valid -=1
            count[left] -=1
            if count[left] == 0:
              unique -=1
            l+=1
          if target == valid and target == unique:
            ans = max(ans,r-l+1)
      return ans



      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      '''if len(s)<k:
        return 0
      result = []
      ans = defaultdict(int)
      for c in s:
        ans[c] += 1
      #print(ans)
      for value in ans.values():
        if value >=k:
          result.append(value)
      return sum(result)        
'''



        