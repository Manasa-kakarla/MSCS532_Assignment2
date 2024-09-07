import timeit
import tracemalloc
import random

def quick_sort(arr):
    """Implementation of the quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_data(size):
    """Generate a list of random integers."""
    return [random.randint(0, 100000) for _ in range(size)]

def measure_performance(size):
    """Measure execution time and memory usage of quicksort."""
    data = generate_random_data(size)

    # Time the execution
    start_time = timeit.default_timer()
    sorted_data = quick_sort(data)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    # Track memory usage
    tracemalloc.start()
    quick_sort(data)  # Run quick_sort to measure memory usage
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
