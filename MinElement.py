def minElement(arr):
    l = 0
    r = len(arr)-1
    while l<r:
        mid = (l+r)//2
        if arr[mid] > arr[r]:
            l = mid+1
        else:
            r = mid
    return arr[l]

arr = [4,5,6,7,0,1,2]
print("at index ",arr.index(minElement(arr)),minElement(arr))