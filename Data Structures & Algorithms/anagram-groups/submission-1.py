class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Storage for all anagrams = hashtable 

            #Check match using an array of chars a-z
            #add same key values to array
            # What defines a key? Same frequency of chars

            #if not matched, add as new key 
        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())