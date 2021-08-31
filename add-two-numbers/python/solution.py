# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = constructor = ListNode(0)
        prev_remainder = 0

        while l1 or l2 or prev_remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            prev_remainder, mod = divmod(val1 + val2 + prev_remainder, 10)
            constructor.next = ListNode(mod)
            constructor = constructor.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


"""
it's easier to come up with the solution if you handle these types of inputs:

9 9 9 9 9 9 9
+ + + + + + +
9 9 9 9
--------------
8 9 9 9 0 0 0 1
1 1 1 1 1 1 1

You do the sum, i.e 9 + 9 = 18
divide by 10 to get the last digit and the remainder
divmod(18,10) -- to get a nice tuple -- (result: 1, mod: 8)
the result == (prev_)remainder, because it's needed for the next addition in line

so, you use the prev_remainder in the addition before the dividing, that's it!

"""
