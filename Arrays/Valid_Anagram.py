class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)== sorted(t)
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Strings can only be anagrams if they are of the same length, when we sort by alphabetical order, they should be identical.
# Time complexity is based on the sorting algorithm used which is typically O(n log n).Can be O(n^2) for simpler algorithms like bubble sort.