class Solution(object):
    def maxArea(self, height):
        l,r,=0,len(height)-1
        cap=0
        while l<r:
            cap = max(min(height[l],height[r])*(abs(l-r)), cap)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return cap

        
        