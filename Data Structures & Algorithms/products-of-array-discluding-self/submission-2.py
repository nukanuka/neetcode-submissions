class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Output products of all elements in array except itself
        #We need pre and postfix array
        pre = [1]*len(nums)
        post = [1]*len(nums)
        out = []
        flippedNums = nums[::-1]


        for i in range(len(nums)): 
            pre[i] = (pre[i-1] * nums[i])
        for j in range(len(nums)): 
            post[j] = (post[j-1] * flippedNums[j])
        post = post[::-1]

      # output = prefix(currentIndex-1) * postfix(currentIndex+1)

        for n in range (len(nums)): 
            leftProd = pre[n-1] if n > 0 else 1 
            rightProd = post[n+1] if n<len(nums)-1 else 1
            out.append(leftProd * rightProd) 
        
        return out
    


