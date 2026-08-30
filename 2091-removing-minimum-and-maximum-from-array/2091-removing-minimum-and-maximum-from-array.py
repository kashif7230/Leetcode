class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
      n = len(nums)
      mn= nums.index(min(nums))
      mx = nums.index(max(nums))
      l = min(mn,mx)
      r = max(mn,mx)
      return min(r+1, n-l, n+l+1-r)



     # print(mn , mx)
    #  print(l,r)
      