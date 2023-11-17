class Solution(object):
    def selfdividing(self, num):
        for digit in str(num):
            if int(digit) == 0 or num % int(digit) != 0:
                return False
        return True

    def selfDividingNumbers(self, left, right):
        result=[]
        for num in range(left,right+1):
          if self.selfdividing(num):
             result.append(num)
        return result
