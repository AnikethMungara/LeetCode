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
#The algorithm sorts both the greed factors of the children and the sizes of the cookies. 
#It then uses two pointers to iterate through both arrays, assigning cookies to children whenever a cookie is large enough to satisfy a child's greed factor.
# The process continues until we have either assigned cookies to all children or run out of cookies.
# The final count of satisfied children is returned.

