from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Distinct values, and sorted in ascending order
        # O (log n) time complexity, hints to binary search?
        # recursive or iterative

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return left


"""
Could be fun to make an algorithm visualizer (even though there's probably tons of those out there)
"""
