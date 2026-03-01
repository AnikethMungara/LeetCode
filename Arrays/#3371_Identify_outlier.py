# 3371. Identify the largest outlier in an array
# Array contains n elements, where n-2 are special, 1 is an outlier and 1 is the sum of all the special. find the outlier ... 
# Total values of everything in the array is O+Special characters + Sum of special characters
# o+2*sum of special characters = total

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt = Counter(nums)

        best = float("-inf")

        for s in nums:         
            o = total - 2 * s        

            if o != s:
                if cnt.get(o, 0) >= 1:
                    best = max(best, o)
            else:
             
                if cnt[s] >= 2:
                    best = max(best, o)

        return best