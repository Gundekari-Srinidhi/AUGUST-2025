class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=[]
        for k,v in d.items():
            if v==1:
                r.append(k)
        return r
        