def moveZero(arr):
    i = 0
    j = 0 
    while i < len(arr):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1
            j = j+1
        else:
            i = i+1
    return arr
  
arr1=[0,1,0,3,12]
print(moveZero(arr1))

arr2=[0]
print(moveZero(arr2))