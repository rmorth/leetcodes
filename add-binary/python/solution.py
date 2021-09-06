class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        rem, res = 0, ""

        while a or b or rem:
            rem += int(a.pop()) if a else 0
            rem += int(b.pop()) if b else 0

            res = str(rem % 2) + res
            rem //= 2
        return res


print(Solution().addBinary("1010", "1011"))


"""
Cheeky but not fun way of solving it:

a = "0b" + a
b = "0b" + b
s = int(a, base=0) + int(b, base=0)
return bin(s).replace("0b", "")

(Leads to stupidly good results of course)

"""
