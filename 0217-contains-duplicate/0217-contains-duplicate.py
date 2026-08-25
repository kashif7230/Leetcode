class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      seen ={}
      for i in range(len(nums)):
        if nums[i] in seen:
          return True
          break
        seen[nums[i]] = True
        # seen[i] = nums[i]
      return False

        