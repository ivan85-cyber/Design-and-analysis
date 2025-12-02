import time
import random

# ------------------- Merge Sort -------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ------------------- Binary Search -------------------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    # Sample input: 10 delivery points (house numbers)
    delivery_points = [45, 12, 89, 34, 7, 23, 56, 78, 90, 3]
    print("Original delivery points:", delivery_points)

    # 1. Sorting
    sorted_points = merge_sort(delivery_points.copy())
    print("Sorted delivery points:", sorted_points)

    # 2. Searching
    target = 56
    index = binary_search(sorted_points, target)
    print(f"Search for {target}: Found at index {index}" if index != -1 else f"Search for {target}: Not found")

    # 3. Performance testing with larger input
    large_input = random.sample(range(1, 10001), 1000)
    print("\n--- Performance Test with 1000 points ---")

    start = time.time()
    sorted_large = merge_sort(large_input.copy())
    sort_time = time.time() - start
    print(f"Merge Sort time for 1000 points: {sort_time:.6f} seconds")

    start = time.time()
    binary_search(sorted_large, random.choice(sorted_large))
    search_time = time.time() - start
    print(f"Binary Search time in sorted 1000 points: {search_time:.6f} seconds")
