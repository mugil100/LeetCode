class Solution(object):
    def removeDuplicates(self, nums):

        i=0 #last unique ele
        j=1 #find new unique ele
        k=1 #write index
        n=len(nums)
        while j<n:
            if nums[i]!=nums[j]:
                nums[k]=nums[j]
                i=j
                k+=1
            j+=1
        return k