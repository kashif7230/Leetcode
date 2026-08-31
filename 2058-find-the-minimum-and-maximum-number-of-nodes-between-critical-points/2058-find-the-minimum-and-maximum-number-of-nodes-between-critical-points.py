class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
      nums = []
      while head:
        nums.append(head.val)
        head = head.next
      #print(nums) convert linked list into an array
      ans = []
      n= len(nums)
      for i in range(1,n-1):
        if nums[i-1] < nums[i] > nums[i+1] or nums[i-1]> nums[i] < nums[i+1]:
          ans.append(i)
      if len(ans) < 2: return [-1,-1]

      #print(ans)  
      mx = ans[-1]-ans[0]
      mn = float(inf)
      for i in range(1,len(ans)):
        mn = min(mn, ans[i]-ans[i-1])
      return [mn,mx]


        