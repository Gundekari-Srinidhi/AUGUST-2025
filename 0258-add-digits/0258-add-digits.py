class Solution:
    def addDigits(self, num: int) -> int:
        temp=num
        while(temp>9):
            s=0
            n=temp
            while(n!=0):
                r=n%10
                s+=r
                n=n//10
            temp=s
        return temp