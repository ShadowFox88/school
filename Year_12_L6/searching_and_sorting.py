import random

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    mid = len(arr) // 2

    passes = 0

    while left <= right:
        passes += 1
        if target == arr[mid]:
            print(f"took {passes} passes")
            return mid
        if target > arr[mid]:
            left = mid + 1
            mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
            mid = (left + right) // 2
    
    return -1

def create_unordered_test(max, size):

    uo_list = random.sample(range(0, max), size)
    random_index = random.randint(0, size - 1)

    return (uo_list, uo_list[random_index], random_index)

def create_ordered_test(max, size):

    o_list = sorted(random.sample(range(0, max), size))
    random_index = random.randint(0, size - 1)

    return (o_list, o_list[random_index], random_index)

def bubble_sort(arr):
    passes = 0
    l, r = 0, 1

    sorted = False

    while not sorted:
        sorted = True
        l, r = 0, 1
        passes += 1

        while r <= len(arr) - 1:
            if arr[l] > arr[r]:
                sorted = False
                arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r + 1
    
    print(f"took {passes} passes")
    return arr

def test():
    ordered_list, ordered_check, ordered_index = create_ordered_test(10  ** 15, 10 ** 3)
    unordered_list, unordered_check, unordered_index = create_ordered_test(10  ** 15, 10 ** 3)

    binary_search_test = binary_search(ordered_list, ordered_check)

    if binary_search_test == ordered_index:
        print("Binary Search Test Passed.")
    else:
        print("Binary Search Test Failed")
        print(f"Output: {binary_search_test} Expected: {ordered_index}")

    ordered_linear_search_test = linear_search(ordered_list, ordered_check)
    unordered_linear_search_test = linear_search(unordered_list, unordered_check)

    if ordered_linear_search_test == ordered_index and unordered_linear_search_test == unordered_index:
        print("Linear Search Test Passed.")
    else:
        print("Linear Search Test Failed")
        print(f"Ordered Output: {ordered_linear_search_test} Expected: {ordered_index}")
        print(f"Unordered Output: {unordered_linear_search_test} Expected: {unordered_index}")

    bubble_sort_test = bubble_sort(random.sample(ordered_list, len(ordered_list)))

    if bubble_sort_test == ordered_list:
        print("Bubble Sort Test Passed")
    else:
        print("Bubble Sort Test Failed")

test()