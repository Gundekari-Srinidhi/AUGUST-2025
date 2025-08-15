class Solution:
    def merge(self,l,r):
        arr=[]
        i=j=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr.append(l[i])
                i+=1
            else:
                arr.append(r[j])
                j+=1
        while i<len(l):
            arr.append(l[i])
            i+=1
        while j<len(r):
            arr.append(r[j])
            j+=1
        return arr

    def mergesort(self,nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.mergesort(nums[:mid])
        right=self.mergesort(nums[mid:])
        return self.merge(left,right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
        

        