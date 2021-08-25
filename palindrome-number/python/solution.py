class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is negative
        # if x's last digit is 0 and it x != 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + (x % 10)
            x = x // 10

        return x == reverse or (x == reverse // 10)


# Basic Approach
# if x < 0:
#     return False
# return str(x) == str(x)[::-1]
#
# str(x)[::-1] time complexity is O(n)
# https://stackoverflow.com/questions/52294373/how-to-find-the-implementation-of-1-reversing-list-in-python-in-cpython

"""Logic for solution without casting
if it's negative, it's not a palindrome
if the last digit is 0 it'd only be a palindrome if x = 0; (it would have to start with 0 somehow)

for us to check if it's a palindrome, we can build the number in reverse
take for example: x = 4114; we only need half: 41
x % 10 = 4 (gets us the last digit);
if we multiply it by 10: (x % 10) * 10 = 40

now, we're missing the second to last digit which is 1
x / 10 = 411 (mod 4 as we saw previously)
(x / 10) % 10 = 1 (second to last digit, see the pattern?)

so we start with reverse = 0
the stop condition is if reverse is greater than or equal to x:
x = 4114; reverse = 41; remember that we alter x throughout the cycles,
so it will be more like: x = 4114 -> 411 -> 41;
since x = reverse it stops;
if x = 4321 -> 432 -> 43 (while reverse is: 12) -> 4 with reverse = 123
it stops and will return false

What about numbers with odd length? (12321, 44544, ...)
x = 12321
at the end it will be: x = 12, reverse = 123; reverse // 10 = 12
that's the x == reverse // 10 comparison, the middle number doesn't matter
"""
