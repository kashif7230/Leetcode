class Solution:
    def maxArea(self, height: List[int]) -> int:
      l = 0
      r = len(height)-1
      max_ans = 0
      while l<=r:
        ans = min(height[l],height[r]) * (r-l)
        print(ans)
        max_ans = max(ans, max_ans)
        print(max_ans)
        if height[l]<height[r]:
          l+=1
        else: r-=1
      return max_ans        