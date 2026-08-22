class Solution:
    def checkDivisibility(self, n: int) -> bool:
      sum1 =0
      multi = 1
      temp = n
      while temp>0:
        digit = temp%10
        
        sum1 += digit
        multi *= digit
        temp //= 10
      
      check = sum1 + multi
      if n%check== 0:
        return True

      return False

        