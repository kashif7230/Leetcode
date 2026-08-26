class Solution:
    def simplifyPath(self, path: str) -> str:
      ans  = []
      broke_p = path.split('/')
      for c in broke_p:
        if not c or c == '.':
          continue
        if c == '..':
          if ans: #true if contains character and values
            ans.pop()
        else:
          ans.append(c)
      result = '/' + '/'.join(ans)
      return result
      #print (broke_p)

      # . = remove dot
      # .. = remove dot + previous word
      #... = do nothing, consider as a word
      # if contain / at last then remove it