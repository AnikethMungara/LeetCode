class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
                sortedS = ''.join(sorted(s))
                res[sortedS].append(s)
        return list(res.values())
    
# Time Complexity: O(k n log n) 
# Space Complexity: O(k*n)
# Using a hashmap to group the anagrams together. For each string, we sort it (O(n log n)) and use the sorted string as a key in the hashmap.
