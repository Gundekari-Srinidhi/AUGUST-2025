class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=list(d.values())
        s=min(l)
        if s<2:
            return False
        for i in range(2,s+1):
            flag=True
            for count in l:
                if count%i!=0:
                    flag=False
                    break
            if flag:
                return True
        return False