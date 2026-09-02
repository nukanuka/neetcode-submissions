class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        #does each non anagram have its own hashmap? 
        for s in strs: 
            count = [0]*26

            for c in s: 
                count[ord(c) - ord("a")] +=1
            if tuple(count) not in result: 
                result[tuple(count)] = []
            result[tuple(count)].append(s)
        return list(result.values())
            
