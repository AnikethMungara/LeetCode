#The algorithm sorts both the greed factors of the children and the sizes of the cookies. 
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child

#time complexity: O(n log n) due to sorting
#space complexity: O(1) since we are using only a constant amount of extra space
#We can not reduce the time complexity further because we need to sort the arrays to efficiently match cookies to children.

