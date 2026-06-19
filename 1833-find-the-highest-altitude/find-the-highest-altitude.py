class Solution(object):
    def largestAltitude(self, gain):
        alti = 0
        maxA = 0
        for x in gain:
            alti += x
            maxA = max(maxA, alti)
        return maxA
        