# Leetcode: 268. Missing Number

def missingNumber(self, nums) -> int:
    n = len(nums)
    total = (n*(n+1))//2
    for i in nums:
        total-=i
    return total