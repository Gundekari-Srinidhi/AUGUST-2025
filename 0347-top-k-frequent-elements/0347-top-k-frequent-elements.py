class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=dict(sorted(d.items(),key=lambda x:-x[1]))
        l=list(r)
        return l[:k]