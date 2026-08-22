class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      result = len(nums)
      for idx, value in enumerate(nums):
        result ^= idx ^ value
      return result
        