class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtableS = {}
        hashtableT = {}

        for char in s: 
            hashtableS[char] = hashtableS.get(char, 0) + 1

        for char in t: 
            hashtableT[char] = hashtableT.get(char, 0) + 1
            
        return hashtableS == hashtableT 
        

        