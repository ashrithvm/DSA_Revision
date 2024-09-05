def check_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return 0
    return 1