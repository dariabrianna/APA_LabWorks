import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr.pop()
    
    lower, higher = [], []
    
    for x in arr:
        if x <= pivot:
            lower.append(x)
        else:
            higher.append(x)
    
    return quick_sort(lower) + [pivot] + quick_sort(higher)

# Test the function
test_array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(test_array)
print(sorted_array)

# Defining the small and large datasets
small_dataset = [29, 10, 14, 37, 13]
large_dataset = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 55, 31, 47, 82, 38]

# Applying Quick Sort to both datasets
sorted_small_dataset = quick_sort(small_dataset)
sorted_large_dataset = quick_sort(large_dataset)

print((sorted_small_dataset, sorted_large_dataset))

large_dataset = [random.randint(1, 10000) for _ in range(1000)]

# Timing the Quick Sort for the large dataset
start_time = time.time()
sorted_large_dataset = quick_sort(large_dataset)
end_time = time.time()

# Calculate the time taken
time_taken = end_time - start_time
print(time_taken)

dataset_sizes = [5, 15, 1000]
sort_times = [0.00001, 0.0001, 0.0156]  # Estimated times based on previous discussions

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, sort_times, marker='o', linestyle='-', color='b')
plt.title('Quick Sort Performance Analysis')
plt.xlabel('Dataset Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.xscale('log')  # Using a logarithmic scale for better visualization of wide-ranging sizes
plt.yscale('log')  # Log scale for time to accommodate the exponential nature of time complexity
plt.xticks(dataset_sizes, labels=[str(size) for size in dataset_sizes])
plt.show()