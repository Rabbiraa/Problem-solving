
class Solution(object):
    def mergeAlternately(self, word1, word2):
     result = ""

     for char1, char2 in zip(word1, word2):
        result += char1 + char2

    
     result += word1[len(word2):] + word2[len(word1):]

     return result
