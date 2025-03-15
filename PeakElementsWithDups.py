def findPeakWithDups(arr):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        left = mid-1 if mid > 0 else -1
        right = mid+1 if mid < len(arr)-1 else -1
        while left!=-1  and left >= 0 and arr[left] == arr[mid]:
            left-=1
        while right != -1 and right<len(arr) and arr[right] == arr[mid]:
            right+=1
        if arr[mid] > arr[left] and arr[mid] > arr[right]:
            return mid
        if arr[mid] > arr[left]:
            l = mid+1
        else:
            r = mid - 1
    return -1

arr = [4,5,6,7,8,8,8,8,8,8,8,9,9,10,11,1,2,3]
print(findPeakWithDups(arr), arr[findPeakWithDups(arr)])