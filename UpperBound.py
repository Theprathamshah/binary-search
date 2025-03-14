def upperBound(arr,target):
    l = 0
    r = len(arr) - 1
    res = len(arr)
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] > target:
            res = mid
            r = mid-1
        else: 
            l = mid+1
    return res
arr = [1,2,3,4,5,6,7,8,9,10]
print(upperBound(arr, 6))
print(upperBound(arr, 1))
print(upperBound(arr, 8))
print(upperBound(arr, -43))
print(upperBound(arr, 4))
print(upperBound(arr, 43))