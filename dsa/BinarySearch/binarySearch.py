
# Basic binary search

def binarySearch(arr,ele):
    low = 0
    high = len(arr)-1
    while(low<= high):
        m = (low+high)//2
        if arr[m] == ele:
            return m
        elif arr[m] >ele :
            high = m-1
        else:
            low = m+1
    return -1


#If a key isn't present in the array
# than it's right place will be low index when it breaks while loop
def rightPlace(arr,ele):
    l = 0
    h = len(arr)-1
    while (l<= h):
        m = (l+h)//2
        if arr[m] > ele:
            h = m-1
        else:
            l = m+1
    return l


## First and last occurance of an element
def firstAndLast(arr, ele):
    l = 0
    h = len(arr)-1
    res = []
    #first occurance
    while(l<=h):
        m = (l+h)//2
        if arr[m] == ele:
            if m == 0 or arr[m-1] != ele:
                res.append(m)
                break
            else:
                h = m-1
        elif arr[m] > ele:
            h = m-1
        else:
            l = m+1
    
    l = 0
    h = len(arr)-1
    # last occurance
    while(l<=h):
        m = (l+h)//2
        if arr[m] == ele:
            if m == (len(arr)-1) or arr[m+1] != ele:
                res.append(m)
                break
            else:
                l = m+1
        elif arr[m] > ele:
            h = m-1
        else:
            l = m+1
    
    return res
        


if __name__ == "__main__":
    arr = [23,57,79,79,79,85,99]
    key = 79
    #print(binarySearch(arr, key))
    #print(rightPlace(arr, key))
    print(firstAndLast(arr, key))