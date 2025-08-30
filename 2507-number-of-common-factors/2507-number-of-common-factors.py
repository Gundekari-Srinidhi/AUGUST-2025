class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        l=0
        i=1
        max1=min(a,b)
        while(i<=max1):
            if a%i==0 and b%i==0:
                l+=1
            i+=1
        return l
        