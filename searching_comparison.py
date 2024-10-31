import time
import random

# Binary Search Implementation
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1 
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Ternary Search Implementation
def ternary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1  # Target not found
    third = (right - left) // 3
    mid1 = left + third
    mid2 = right - third
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)

# Performance testing function
def test_search_algorithms(arr, target):
    results = {}
    
    # Testing Binary Search 
    start_time = time.time()
    result_binary = binary_search(arr, target)
    time_for_binary = time.time() - start_time
    results['Binary Search'] = {'index': result_binary, 'time': time_for_binary}
    
    # Testing Ternary Search
    start_time = time.time()
    result_ternanry = ternary_search(arr, target)
    time_for_ternary = time.time() - start_time
    results['Ternary Search'] = {'index': result_ternanry, 'time': time_for_ternary}
    
    return results


data_sizes = [10000, 100000, 1000000]
results = {}

#generate data for different data sizes
for size in data_sizes:
    # For Sorted data
    sorted_list = sorted(random.sample(range(size * 10), size))
    target = random.choice(sorted_list)
    results[('Sorted', size)] = test_search_algorithms(sorted_list, target)

    # For Reverse Sorted data
    reverse_sorted_list = sorted(random.sample(range(size * 10), size), reverse=True)
    target = random.choice(reverse_sorted_list)
    results[('Reverse Sorted', size)] = test_search_algorithms(reverse_sorted_list, target)

    # For Random data
    random_list = random.sample(range(size * 10), size)
    sorted_random_list = sorted(random_list)  
    target = random.choice(sorted_random_list)
    results[('Random', size)] = test_search_algorithms(sorted_random_list, target)

# Display results for each case
for (data_type, size), result in results.items():
    print(f"\nData Type: {data_type}, Data Size: {size}")
    for algo, res in result.items():
        print(f"{algo} - Index: {res['index']}, Time: {res['time']} seconds")