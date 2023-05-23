round ,point = map(int,input().split())

arr = list(map(int,input().split()))
print(arr)

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    group1 = mergeSort(arr[:mid])
    group2 = mergeSort(arr[mid:])
    print(arr,"the array")
    return merge(arr, group1,group2)
ans = []
def merge(arr , left_half,right_half):
    arr = []
    i, j = 0, 0
    left_len = len(left_half)
    right_len = len(right_half)

    while i < left_len and j < right_len:
        print(left_half,right_half,"lef,right")
        if left_half[i] - right_half[j] > point:
            arr.append(left_half[i])
            i= 1
        elif(right_half[j] - left_half[i] > point):
            arr.append(right_half[j])
            j+= 1
        else:
            if left_half[i] < right_half[i]:
                # arr.append(left_half[i])
                arr.append(right_half[j])
            else:
                arr.append(right_half[j])
                # arr.append(left_half[i])
            i += 1
            j += 1

        print(arr)
    
        # arr += left_half[i:]
        # arr += right_half[j:]
        
        return arr
    

print(mergeSort(arr),"the finela")
    # res = [ans[num] for num in nums]
    # return res/

        















            