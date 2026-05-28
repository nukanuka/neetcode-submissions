class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2 pointers at start and end 
        #at each iteration calc max(l,r) x (r-l)
        #if this sum>curMax, then curMax = sum 
        #continue until met in the middle
        l = 0 
        r = len(heights)-1
        curMax=0
        allMax = 0

        while(l<r): 
            curMax = min(heights[l],heights[r]) * (r-l)
            if(curMax>allMax): 
                allMax = curMax
            if(heights[l]<heights[r]): 
                l+=1
            else: 
                r-=1

        return allMax