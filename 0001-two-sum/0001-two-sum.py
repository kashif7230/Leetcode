class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      dict1 = {}
      for i in range(len(nums)):
        check = target - nums[i]
        if check in dict1:
          return [i,dict1[check]]
        dict1[nums[i]] = i
        