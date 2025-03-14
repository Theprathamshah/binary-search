def searchInsertPosition(arr,target):
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

arr = [1,3,5,6,7,8,9,14,23,56]

print(searchInsertPosition(arr,1))
print(searchInsertPosition(arr,4))
print(searchInsertPosition(arr,10))
print(searchInsertPosition(arr,21))
print(searchInsertPosition(arr,111))