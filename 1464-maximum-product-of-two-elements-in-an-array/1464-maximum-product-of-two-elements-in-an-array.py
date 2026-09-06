class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      nums.sort()
      max1 = nums[-1]
      max2 = nums[-2]
      ans = (max1-1) * (max2-1)
      return ans        