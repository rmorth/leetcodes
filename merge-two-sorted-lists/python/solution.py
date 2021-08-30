# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        untouched = sortedList = ListNode()

        while l1 and l2:
            # We want to skip whenever we add the value
            # We add the value when it's the lesser value

            if l1.val <= l2.val:
                sortedList.next = l1
                l1 = l1.next
            else:
                sortedList.next = l2
                l2 = l2.next
            sortedList = sortedList.next

        if l1 == None:
            sortedList.next = l2
        elif l2 == None:
            sortedList.next = l1

        return untouched.next  # starts at 0 (which we created)


""" 

Optional[ListNode] => l1.next might be None (end of singly-linked list)
code's a bit ugly, i'll try to clean it up

oh, what I'm doing inside the l1/l2 == None is useless...


untouched = sortedList = ListNode()

while l1 != None or l2 != None:
    # We want to skip whenever we add the value
    # We add the value when it's the lesser value

    if l1 == None:
        sortedList.next = l2
        sortedList = sortedList.next
        l2 = l2.next
        continue
    elif l2 == None:
        sortedList.next = l1
        sortedList = sortedList.next
        l1 = l1.next
        continue

    if l1.val <= l2.val:
        sortedList.next = l1
        l1 = l1.next
    else:
        sortedList.next = l2
        l2 = l2.next
    sortedList = sortedList.next

return untouched.next  # starts at 0 (which we created) 

"""


""" 
    Quick Note on the final solution

    For some reason I got a lot more runtime from 40ms (solution1.png) to 94ms
    I ran it again afterwards because it was really weird and got 64ms (solution2.png) which is still slower...
    I thought it'd be faster, since I saved on cycles in the while loop, guess not..?
    I tried one more time, same solution, 46ms...

    Ok apparently, leetcode runtimes are atrocious! The more you know...
    https://leetcode.com/discuss/general-discussion/136683/different-run-time-with-same-code
    https://leetcode.com/problems/two-sum/discuss/652/how-accurate-are-the-timings

    Just as side note on this quick note (hehe):
        - I usually don't really care about runtimes, I base my solution's quality on its time complexity
        - This was just a weird experience for me even though I already kind of knew that runtime measurements in leetcode weren't reliable
        - Maybe I should stop posting solution images... since they're useless.
"""
