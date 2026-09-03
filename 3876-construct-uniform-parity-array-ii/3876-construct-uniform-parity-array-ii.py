class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
      mn = float(inf)
      for x in nums1:
        if x%2==1:  #odd check
          mn =min(mn,x)
      for x in nums1:
        if x%2==0 and mn!= float(inf) and x<mn: # even check 
          return False
      return True

  #if all values in nums1 is even then mn stays inf till end