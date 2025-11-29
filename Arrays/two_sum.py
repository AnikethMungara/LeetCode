# Using premap to store the indices of the numbers we have seen so far. We calculate the difference between the target and the current number. If the difference is already in the premap, we have found the two numbers that add up to the target, and we return their indices. If not, we store the current number and its index in the premap for future reference. 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap = {}

        for i, n in enumerate(nums):
            diff =target -n 
            if diff in premap:
                return [premap[diff], i ]
            premap[n] = i
        return
    
# Time Complexity: O(n)
# Space Complexity: O(n)   
