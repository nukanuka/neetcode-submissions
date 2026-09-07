class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointer approach: left on first char, right on last char 
        l = 0 
        r = len(s)-1
        while l < r: 
            while l<r and not s[l].isalnum():
                l+=1 
            while l<r and not s[r].isalnum():
                r-=1
            
            lChar = s[l].lower()
            rChar = s[r].lower()
            if(lChar!=rChar):
                return False
            l+=1
            r-=1

        return True
