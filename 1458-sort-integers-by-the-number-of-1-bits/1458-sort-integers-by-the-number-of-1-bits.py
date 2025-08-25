from collections import Counter
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d={}
        for num in arr:
            r=bin(num)
            ones=r.count('1')
            if ones in d:
                d[ones].append(num)
            else:
                d[ones] = [num]
        d=dict(sorted(d.items(),key=lambda x:x[0]))
        l=[]
        for k,v in d.items():
            l.extend(sorted(v))
        return l

            