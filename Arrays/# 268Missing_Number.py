# 268. Missing Number
# Method 1: Using Sum Formula; Since these are arrays from 0 to n, we can subtract the sum of the array from the expected sum of numbers from 0 to n.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n*(n+1)//2
        actual = sum(nums)
        m_n= expected-actual
        return m_n
    
#Method 2: Using XOR; XOR all the numbers from 0 to n and XOR all the numbers in the array. The missing number will be the result of XORing these two results.
def missingNumber(nums):
    xor_all = 0
    n = len(nums)
    
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
        
    return xor_all


#both have a time complexity of O(n) and space complexity of O(1).
