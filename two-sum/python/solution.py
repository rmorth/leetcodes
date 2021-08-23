from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([4, 60, 25, 38, 11, 34, 14, 13], 36))


# Basic approach (O(n^2))
# for i in range(nums.__len__()):
#     for j in range(nums.__len__()):
#         if i == j:
#             continue
#         if nums[i] + nums[j] == target:
#             return [i, j]
