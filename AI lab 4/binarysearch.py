def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid   # mid + 1 if want to start array from index 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Example
arr = [12,25,32,44,67,74,99]
target = 32

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")