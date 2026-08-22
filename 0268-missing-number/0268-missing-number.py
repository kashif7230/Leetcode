class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      initial= sum(nums)
      finals = (n*(n+1)/2)
      ans = finals - initial

      return int(ans)


        