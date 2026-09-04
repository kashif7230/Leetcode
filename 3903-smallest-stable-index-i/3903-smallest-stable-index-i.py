class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
      n =len(nums)
      pre_sum = [0] * n
      pre_sum[0] = nums[0]
      for i in range(1, n):
        pre_sum[i] = max(pre_sum[i-1], nums[i])
      suf_sum = [0] * n
      suf_sum[-1] = nums[-1]
      for i in range(n-2,-1,-1):
        suf_sum[i] = min(suf_sum[i+1], nums[i])
      
      for i in range(n):
        if pre_sum[i] - suf_sum[i] <=k:
          return i
      return -1