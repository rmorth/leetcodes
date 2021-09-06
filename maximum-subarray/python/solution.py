from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = current_sum

        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i] + current_sum)
            max_sum = max(current_sum, max_sum)

        return max_sum


"""

Whenever my first (/only) approach is to brute-force it,
I put my head down in shame. :D

I didn't even bother to implement the brute-force technique since its time complexity
would be O(n^2). 
Enter Kadane's algorithm!

    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    https://www.youtube.com/watch?v=jnoVtCKECmQ

embarassed to say it's really simple, but hey that's why I'm doing these.
This leads to an O(n) (time complexity) approach

"""

"""
The follow up - Divide and Conquer

    https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/
    https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
    https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/?ref=rp
"""

# Fun fact: This was my 10th leetcode problem solved!
