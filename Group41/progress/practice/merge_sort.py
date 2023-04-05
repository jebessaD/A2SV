def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    
    return merge(left_half, right_half)

def merge(arr1,arr2):
    ptr1 = ptr2 = 0
    merged = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            merged.append(arr1[ptr1])
            ptr1 += 1
        else:
            merged.append(arr2[ptr2])
            ptr2 += 1

    merged.extend(arr1[ptr1:])
    merged.extend(arr2[ptr2:])

    return merged

def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
test()
