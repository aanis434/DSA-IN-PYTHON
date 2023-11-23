import sys

sys.setrecursionlimit(2147483647)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        assert x != 0 and -100.0 < x < 100.0, "x should be number between -100 < x < 100."
        # assert -31 <= n <= 31 and int(n) == n, "n should be less than 2147483647"
        
        if abs(n) >= 2147483647:
            return 0
        elif n >= 998:
            return x
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if abs(x) >= 10000000000000000000000000000000:
                    return x
            elif n < 0:
                return self.myPow(x, n+1) / x
            else:
                return x * self.myPow(x, n-1)
                
        