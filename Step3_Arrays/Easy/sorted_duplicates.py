# question: Remove duplicates from Sorted array

def remove_duplicates(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            nums.pop(i)
    return nums