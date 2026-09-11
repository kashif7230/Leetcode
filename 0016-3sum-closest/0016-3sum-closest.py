class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums.sort()
      n = len(nums)
      close = nums[0]+nums[1]+nums[2]
      for i in range(n-2):
        l=i+1
        r= n-1
        while l<r:
          check = nums[i]+nums[l]+nums[r]
          if check == target:
            return check
          if abs(check-target) < abs(close-target):
            close = check
          if check <target:
            l+=1
          else: 
            r-=1
      return close

        
        