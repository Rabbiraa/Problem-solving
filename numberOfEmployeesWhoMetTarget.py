class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        n= len(hours)
        count=0
        for i in range(n):
            if hours[i]>=target:
                count+=1
        return count
