class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        bulls=0
        cows=0
        l=list(secret)
        for i in range(n):
            if secret[i]==guess[i]:
                bulls+=1
                l[i]="*"
        for i in range(n):
            if secret[i]!=guess[i] and guess[i] in l:
                cows+=1
                l[l.index(guess[i])]="#"
        return str(bulls)+"A"+str(cows)+"B"
        
        