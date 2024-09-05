# question: left rotate array by one place

def left_rotate(nums):
    buffer = nums[0]
    nums = nums[1:]
    nums.append(buffer)
    return nums

a=[1,2,3,4,5]
print(left_rotate(a))
