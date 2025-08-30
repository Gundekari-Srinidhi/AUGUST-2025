import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            count = (mid // a) + (mid // b) + (mid // c) \
                    - (mid // ab) - (mid // bc) - (mid // ac) + (mid // abc)
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left
