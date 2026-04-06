class Solution(object):
    def maxArea(self, height):
        l,r,=0,len(height)-1
        cap=0
        maxH= max(height)
        while l<r:
            cap = max(min(height[l],height[r])*(r-l), cap)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            # if maxH*(l-r) < cap:
            #     break
        return cap

        
        