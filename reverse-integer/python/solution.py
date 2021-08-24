class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        res = sign * int(str(abs(x))[::-1])
        if -(2**31)-1 < res < (2**31):
            return res
        else:
            return 0
