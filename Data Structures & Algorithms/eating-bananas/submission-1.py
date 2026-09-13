class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Goal is to find min eating rate of bananas. 
        #How can we do this? 
        #Brute force approach is to go 1 --> Infinity and pushing thru arrary
        
        # Upper bound on the output is Max from piles array
        # So 1 <= k <= max(piles)
        #Not searching through piles itself

        l = 1
        r = max(piles)
        localMin = 0
        while(l<=r): 
            k = (l + r)//2
            totalH = 0
            for pile in piles: 
                totalH += math.ceil(pile/k)
            if(totalH<=h): 
                localMin = k
                r = k-1
            else: 
                l = k+1
        return localMin
           
