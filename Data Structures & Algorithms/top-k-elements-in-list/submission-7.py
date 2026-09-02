class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        #One pass through the array and identify number into frequency map 
        for i in nums: 
            if i in freqMap: 
                freqMap[i] +=1
            else: 
                freqMap[i] = 1
            
       
        heap = []

        for num in freqMap.keys():
            heapq.heappush(heap, (freqMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res