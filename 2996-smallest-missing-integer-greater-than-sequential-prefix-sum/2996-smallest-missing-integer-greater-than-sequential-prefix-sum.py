class Solution:
    def missingInteger(self, nums: List[int]) -> int:
      num = set(nums)
      ans = nums[0]

      for i in range(1,len(num)):
        if nums[i] == nums[i-1]+1:
          ans += nums[i]
        else:
          break
      while ans in nums:
        ans +=1
      return ans
