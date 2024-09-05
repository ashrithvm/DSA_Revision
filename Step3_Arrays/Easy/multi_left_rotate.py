# question: Left rotate an array by D places

def rotate_left(arr, d):
    n = len(arr)
    d = d % n  # In case d > n, to avoid unnecessary rotations
    return arr[d:] + arr[:d]

a=[1,2,3,4,5]
print(rotate_left(a,2))
