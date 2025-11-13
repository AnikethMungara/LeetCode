# Time Complexity: O(n)
# Space Complexity: O(n)
#Using a Hashmap called hashset to store the elements as we iterate and compare through the list.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
