class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        s=sorted(nums)
        max1=s[-1]
        min1=s[0]
        r=self.gcd(max1,min1)
        return r
        