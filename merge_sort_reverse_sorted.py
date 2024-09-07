import timeit
import tracemalloc
import random

def merge_sort(arr):
    """Implementation of the merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted lists."""
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

def generate_reverse_sorted_data(size):
    """Generate a list of integers sorted in reverse order."""
    return [i for i in range(size, 0, -1)]

def measure_performance(size):
    """Measure execution time and memory usage of merge sort."""
    data = generate_reverse_sorted_data(size)

    # Time the execution
    start_time = timeit.default_timer()
    sorted_data = merge_sort(data)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    # Track memory usage
    tracemalloc.start()
    merge_sort(data)  # Run merge_sort to measure memory usage
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    # Calculate memory usage
    total_memory = sum(stat.size for stat in top_stats) / (1024 * 1024)  # Convert bytes to MiB

    return execution_time, total_memory

if __name__ == "__main__":
    size = 10000  # Change this size as needed
    execution_time, memory_usage = measure_performance(size)
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage:.2f} MiB")
