def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid + 1

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


print(binary_search([1, 3, 4, 5, 6, 8, 9, 10], 6, 0, 7))
