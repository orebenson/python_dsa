'''
Binary search algorithm implementation
'''



def binary_search(arr, item):
    # arr = arr.sort()
    l = 0 # start
    u = len(arr)-1 # end
    pos = 0
    
    while l <= u:
        mid = (l+u)//2
        if arr[mid] == item:
            pos = mid
            return pos
        else:
            if arr[mid] < item:
                l = mid+1
            else:
                u = mid-1
    return -1

arr = [0,1,2,3,4,5,12,15,26,37,38,57]
item = 37

print(binary_search(arr, item))