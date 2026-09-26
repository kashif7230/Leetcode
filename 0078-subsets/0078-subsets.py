class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
      ans = []
      path= []
      def backtracking(i):   # base case
        ans.append(path.copy())
        
        for j in range(i,len(nums)):
          path.append(nums[j])
          backtracking(j+1)
          path.pop()
      backtracking(0)
      return ans
        
        