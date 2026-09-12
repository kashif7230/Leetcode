class Solution:
    def minMoves(self, nums: List[int]) -> int:
      mn = min(nums)
      total = sum(nums)
      n = len(nums)
      return total-(mn* n)

      """ n = len(nums)
      check = 0
      r = n-1
      for l in range(0,n-1):
        sum1 =int(nums[r]-nums[l])
        check+=sum1
      return check """ #failed at 11 test case