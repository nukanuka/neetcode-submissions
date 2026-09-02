class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        arr = []
        #One pass through the array and identify number into frequency map 
        for i in nums: 
            if i in freqMap: 
                freqMap[i] +=1
            else: 
                freqMap[i] = 1
            
       
        for num, cnt in freqMap.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res