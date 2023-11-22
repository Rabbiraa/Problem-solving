class Solution(object):
    def isPalindrome(self, x):
      xs=str(x)
      n=len(xs)
      i=0
      while i<n:
          if xs[i]==xs[n-1]:
             i+=1
             n-=1
            
          else :
               return False
      return True


