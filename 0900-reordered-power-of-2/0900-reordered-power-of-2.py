class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=sorted(str(n))
        for i in range(30):
            power=1<<i
            s1=sorted(str(power))
            if s==s1:
                return True
        return False
        