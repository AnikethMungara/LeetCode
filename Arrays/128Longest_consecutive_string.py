# Using a set to find the longest consecutive sequence in an unsorted array of integers.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length ) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
    

#time complexity: O(n) where n is the number of elements in nums
#space complexity: O(n) for storing the elements in the set