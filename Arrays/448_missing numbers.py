#Using a set to remove duplicates. Then scanning through the range from 1 to n, appending a new array with the missing numbers which is then returned.
#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set= set(nums)
        ret = []
        
        for i in range (1, len(nums)+1):
            if i not in nums_set:
                ret.append(i)
    
        return ret