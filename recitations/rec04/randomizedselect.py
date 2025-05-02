import random

def randomized_partition(arr, left, right):
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

def randomized_select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = randomized_partition(arr, left, right)
    rank = pivot_index - left + 1
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return randomized_select(arr, left, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, right, k - rank)

# Example usage
arr = [9, 3, 2, 7, 5, 6, 1, 8, 4]
k = 3  # Find the 3rd smallest element
result = randomized_select(arr[:], 0, len(arr)-1, k)


print(result)

