class Solution(object):
    def smallestEvenMultiple(self, n):
      result=[]
      counter = 2
      while  counter <= n:
           if n % counter == 0:
               result.append(counter)
               n = n // counter
               counter = 2
           else:
                counter += 1

      if 2 not in result:
           result.append(2)
      total=1
      for num in result:
           total *= num
      return total

