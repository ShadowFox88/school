arr = [5, 4, 3, 2, 1]
swaps = True
passes = 0

print(arr)
while swaps:
    swaps = False
    l, r = 0, 1
    print()
    while r <= len(arr) - (1 + passes):
        if arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            swaps = True
            l += 1
            r += 1
        print(arr)
    passes += 1

print(arr)