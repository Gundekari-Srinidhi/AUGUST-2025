class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        n=len(s)
        for i in range(n):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        print(d)
        for k,v in d.items():
            if v==1:
                r=k
                break   
            else:
                r=-1
        if r==-1:
            return -1
        else:
            for i in range(n):
                if s[i]==r:
                    return i

            