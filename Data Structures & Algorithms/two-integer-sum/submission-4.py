class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Loop through array and check whether (target - existing value in array)
        # = an element in hashtable, if so: targets found
        #if not, add the existing value to hashtable 

        targetsHash = {}
        for i, num in enumerate(nums): 
            diff = target - num

            if diff in targetsHash: 
                return [targetsHash[diff], i]
            
            targetsHash[num] = i
