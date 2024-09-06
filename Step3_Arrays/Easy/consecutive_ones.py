# GFG: 485. Max Consecutive Ones

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros = [-1] + [i for i, x in enumerate(nums) if x == 0] + [len(nums)]
        if len(zeros) == 2:  # No zeros in the list
            return len(nums)
        
        big = 0
        for i in range(1, len(zeros)):
            big = max(big, zeros[i] - zeros[i-1] - 1)
        return big