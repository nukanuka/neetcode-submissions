class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Go through the array as if it is in sequence 
    #Add every element to hashmap
        curMax = 0 
        totMax = 0 
        seqSet = set(nums)
        for n in nums: 
            #Start of a new sequence
            if n-1 not in seqSet: 
                curMax = 1
                while(n+curMax) in seqSet: 
                    curMax+=1
                totMax = max(totMax,curMax)
        return totMax