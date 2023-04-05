arr = [4,5,6,8,7,2,3,4,2,8]
print(arr)
# print(sorted(arr))

def quickSort(arr,start,end,length):

    if length == 1:
        return arr[start]

    pivot_num = arr[start]
    pivot = start

    print(start,end,length)
    while end < length:
        if arr[end] <= pivot_num:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
        end += 1

    arr[pivot],arr[start] =arr[start], arr[pivot]

    # quickSort(arr,0,0,start)
    quickSort(arr,start,start,end-start)
    print(arr,start,end)

quickSort(arr,0,0,len(arr))