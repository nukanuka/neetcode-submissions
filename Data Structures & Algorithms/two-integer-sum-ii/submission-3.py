class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Need to use 2 pointers but slow/fast turtle method
        #2 pointers starting at 1st index 
        #1st moves by one 2nd moves by 2
        left = 0 
        right = len(numbers)-1
        while(left!=right):
            if(numbers[left]+numbers[right]==target):
                return [left+1,right+1]
            elif(numbers[left]+numbers[right]>target):
                right-=1
            else:
                left+=1
