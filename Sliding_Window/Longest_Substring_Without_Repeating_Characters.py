class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l=0
        res=0


        for i in range(len(s)):
            if s[i] in mp:
                l=max(mp[s[i]]+1, l)
            mp[s[i]]=i
            res = max(res,i-l+1)
        return res



# Time Complexity: O(n)
# Space Complexity: O(min(m,n)) where m is the size of the character set and n is the length of the string.

# The algorithm uses a sliding window approach to find the longest substring without repeating characters.