def peakElement(arr):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        left = arr[mid-1] if mid>0 else -999999
        right = arr[mid+1] if mid<len(arr)-1 else -999999
        print(mid, arr[mid], left,right)
        if arr[mid] > left and arr[mid] > right:
            return mid
        if arr[mid] > left:
            l = mid+1
        else:
            r = mid-1
    return -1

arr = [4,5,6,7,8,9,10,11,1,2,3]
arr2 = [4,5,6,7,8,8,8,8,8,8,8,9,9,10,11,1,2,3]
print(peakElement(arr))
print(peakElement(arr2))