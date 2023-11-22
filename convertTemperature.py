class Solution(object):
    def convertTemperature(self, celsius):
        if 0 <= celsius <= 1000:
           list=[]
           Kelvin = celsius + 273.15
           Fahrenheit = celsius * 1.80 + 32.00
           list.append(Kelvin)
           list.append(Fahrenheit )
           return list
