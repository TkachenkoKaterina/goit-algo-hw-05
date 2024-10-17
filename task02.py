def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


arr = [1.2, 2.5, 3.7, 5.1, 6.8, 8.3, 9.9]
target = 6.5
result = binary_search(arr, target)
print(result)  # Виведе: (3, 6.8)
