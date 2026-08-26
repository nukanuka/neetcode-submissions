class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Store in hashmap for frquencies 

        freqs = {}
        for l in nums: 
            if(l in freqs): 
                return True 
            freqs[l] = l 
        
        return False 
