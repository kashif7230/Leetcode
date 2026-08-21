class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)   # remove duplicates
        longest = 0   
        for num in s:   #har value per iterate kar rahe hai
          if num-1 not in s:   #num se ek choti value set me present to nahi hai
            next_num = num+1     
            length = 1     
            while next_num in s:  #num+1 agr set me present hai to loop run hoga
              next_num +=1
              length+=1
            longest = max(longest, length)
        return longest
        #print(s)