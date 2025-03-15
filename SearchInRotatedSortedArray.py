def func(arr, target):
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = (l+r)//2
        # print(l,r,mid)
        if arr[mid] == target:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:  
                r = mid - 1
            else:
                l = mid + 1
        else:  
            if arr[mid] < target <= arr[r]:  
                l = mid + 1
            else:
                r = mid - 1

arr = [5,7,9,11,1,2,4]
for i in arr:
    print(func(arr,i))