class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #I would create a hashmap with key as every unique element, 
        #value as its frequency. But I dont know how to sort it in decreasing order 
        #so that I can pick the first k keys.

        freqMap = {}
        freq = []

        # Count frequencies
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        # Sort by frequency descending
        sortedFreq = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)

        # Take first k elements
        for i in range(k):
            freq.append(sortedFreq[i][0])

        return freq
        