class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        l=[]
        d={}
        r={}
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s2:
            if i in r:
                r[i]+=1
            else:
                r[i]=1
        for k,v in d.items():
            if v==1 and k not in s2:
                l.append(k)
        for k,v in r.items():
            if v==1 and k not in s1:
                l.append(k)
        return l
