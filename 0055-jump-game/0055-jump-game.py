class Solution:
    def canJump(self, nums: List[int]) -> bool:
      mx = 0
      for index,value in enumerate(nums):
        if mx < index:
          return False
        else:
          mx = max(mx, index + value)
      return True


        