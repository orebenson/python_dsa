'''
Binary search algorithm implementation
'''



def binary_search(arr, item):
    # arr = arr.sort()
    l = 0
    u = len(arr)-1
    pos = 0
    
    while l <= u:
        mid = (l+u)//2
        if arr[mid] == item:
            pos = mid
            return True
        else:
            if arr[mid] < item:
                l = mid+1
            else:
                u = mid-1
    return False

arr = [0,1,2,3,4,5,12,15,26,37,38,57]
item = 37

print(binary_search(arr, item))