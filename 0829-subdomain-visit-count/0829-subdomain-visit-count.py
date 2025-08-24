class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for i in cpdomains:
            s=i.split()
            count=int(s[0])
            word=s[1]
            if word in d:
                d[word]+=count
            else:
                d[word]=count
            t=word.split(".")
            for j in range(1,len(t)):
                h=".".join(t[j:])
                if h in d:
                    d[h]+=count
                else:
                    d[h]=count
        l=[]
        for k,v in d.items():
            l.append(f"{v} {k}")
        return l
                