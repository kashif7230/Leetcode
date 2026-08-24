class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      seen = {} 
      for i in range(len(nums)):
        if nums[i] in seen:     # or if nums[i] in seen and abs(i - seen[nums[i]]) <= k:
          if abs(i - seen[nums[i]]) <= k:
            return True
        seen[nums[i]] = i     # dictionary me key nums[i] hai and value is i
      return False
        