def largestElement(arr):
    max_val=arr[0]
    for i in range(len(arr)):
        max_val=max(max_val,arr[i])
    return max_val
