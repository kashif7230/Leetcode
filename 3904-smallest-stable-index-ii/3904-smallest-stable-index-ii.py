class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
      n = len(nums)
      pre_sum = [0] * n
      pre_sum[0] = nums[0]
      for i in range(1, n):
        pre_sum[i] = max(nums[i], pre_sum[i-1] )
        #print(pre_sum)
      suff_sum = [0] * n
      suff_sum[-1] = nums[-1]
      for j in range(n-2, -1, -1):
        suff_sum[j] = min(nums[j],suff_sum[j+1] )
       # print(suff_sum)

      for i in range(n):
        if pre_sum[i] - suff_sum[i] <= k:
          return i
      return -1      

        