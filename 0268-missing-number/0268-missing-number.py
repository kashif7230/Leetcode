class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      #solution 1
     # n = len(nums)
     # initial= sum(nums)
     # finals = (n*(n+1)/2)
     # ans = finals - initial
     # return int(ans)


      #solution  2
      result = len(nums)
      for idx, value in enumerate(nums):
        result ^= idx ^ value
      return result
        