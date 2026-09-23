def bubbleSort(l):
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp
                swaps = True
            print(l)
        print()
    
    return l

def merge(l_arr, r_arr):
    l_idx = 0 
    r_idx = 0
    
    out = []
    while len(out) != (len(r_arr) + len(l_arr)):
        if l_idx == len(l_arr) and r_idx != len(r_arr):
            out.append(r_arr[r_idx])
            r_idx += 1
        elif r_idx == len(r_arr) and l_idx != len(l_arr):
            out.append(l_arr[l_idx])
            l_idx += 1
        elif l_arr[l_idx] <= r_arr[r_idx]:
            out.append(l_arr[l_idx])
            l_idx += 1
        elif l_arr[l_idx] >= r_arr[r_idx]:
            out.append(r_arr[r_idx])
            r_idx += 1
    
    return out

def split(arr):
    midpoint = len(arr) // 2
    out_l = arr[:midpoint]
    out_r = arr[midpoint:]
    
    return out_l, out_r
        
def is_arr_all_of_len_1(arr):
    out = True
    for i in arr:
        if len(i) != 1:
            out = False
    return out

def mergeSort(arr):
    arrays = [arr]
    out = []
    while not is_arr_all_of_len_1(arrays):
        l, r = split(arrays.pop(0))
        if l:
            arrays.append(l)
        if r:
            arrays.append(r)
    
    while len(arrays) != 0:
        out = merge(out, arrays.pop(0))
       
    return out

def insertionSort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            correct = False
            temp = i
            while not correct:
                if temp == 0 or arr[temp] >= arr[temp-1]:
                    correct = True
                else:
                    arr[temp], arr[temp-1] = arr[temp-1], arr[temp]
                    temp -= 1

        print(arr)

def binarySearch(arr, target):
    l = 0
    r = len(arr)

    found_index = None
    while found_index is None:
        midpoint = (l + r) // 2
        if arr[midpoint] == target:
            found_index = midpoint
        elif arr[midpoint] > target:
            r = midpoint
        elif arr[midpoint] < target:
            l = midpoint
    
    return found_index
    
print(binarySearch(list(range(1, 100000)), 7))