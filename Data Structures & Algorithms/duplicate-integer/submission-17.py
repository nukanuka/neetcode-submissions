class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #While passing through the array, 
         #Check whether already exists in Set
        #If so, return true (duplicate found)
        #Else, add that Value to Set and continue 
        #Time complexity = O(n)

        dupTrackSet = set()

        for i, num in enumerate(nums): 
            if num in dupTrackSet: 
                return True
            dupTrackSet.add(num)
        
        return False