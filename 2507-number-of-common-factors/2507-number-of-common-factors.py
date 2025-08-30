class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        l=[]
        i=1
        max1=min(a,b)
        while(i<=max1):
            if a%i==0 and b%i==0:
                l.append(i)
            i+=1
        return len(l)
        