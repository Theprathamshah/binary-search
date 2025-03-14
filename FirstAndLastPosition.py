def firstPos(arr, target):
    l = 0
    r = len(arr) - 1
    res = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            res = mid
            r = mid-1
        elif arr[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return res

def lastPos(arr, target):
    l = 0
    r = len(arr) - 1
    res = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            res = mid
            l = mid+1
        elif arr[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return res

arr = [1,2,3,6,6,6,7,8,9,9]

print(firstPos(arr,1), lastPos(arr,1))
print(firstPos(arr,6), lastPos(arr,6))
print(firstPos(arr,7), lastPos(arr,7))
print(firstPos(arr,9), lastPos(arr,9))