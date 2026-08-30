class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
      n = len(nums)
      mn= nums.index(min(nums))
      mx = nums.index(max(nums))
      l = min(mn,mx)
      r = max(mn,mx)
      front = r+1
      back = n-l
      mid = n+l+1-r
      return min(front,back,mid)



     # print(mn , mx)
    #  print(l,r)
      