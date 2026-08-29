#from typing import List 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      check = defaultdict(int)
      for c in nums:
        check[c] +=1
      for c,check in check.items():
        if check ==1:
          return c
    #  print(check)