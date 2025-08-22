class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word=s1.split()+s2.split()
        d={}
        l=[]
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v==1:
                l.append(k)
        return l