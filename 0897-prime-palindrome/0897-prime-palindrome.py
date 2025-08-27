class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
        
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            for j in range(3, int(x**0.5) + 1, 2):
                if x % j == 0:
                    return False
            return True
        
        
        length = len(str(n))
        
        while True:
            for half in range(10**((length-1)//2), 10**((length+1)//2)):
                s = str(half)
                pal = int(s + s[-2::-1]) 
                if pal >= n and is_prime(pal):
                    return pal
            length += 1
