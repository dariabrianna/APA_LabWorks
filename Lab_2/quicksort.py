import random
import time
import matplotlib.pyplot as plt
import sys

# Increase the maximum recursion depth
sys.setrecursionlimit(10000)  # Set this to a higher number as needed


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

dataset_sizes = [5, 15, 1000, 10]  
sort_times = [0.001, 0.002, 0.2, 0.01] 


small_dataset = random.sample(range(1, 101), 50)  # 50 unique values between 1 and 100
large_random_dataset = random.sample(range(1, 20001), 5000)  # 5000 unique values between 1 and 20000
nearly_sorted_dataset = list(range(1, 1001)) + random.sample(range(1001, 1101), 50)  # Mostly sorted 1050 values
repeated_elements_dataset = [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]  # 2000 elements with 5 possible values

# Record the time taken for sorting each dataset
dataset_sizes = ['Small dataset', 'Large random dataset', 'Nearly sorted dataset', 'Repeated elements dataset']
datasets = [small_dataset, large_random_dataset, nearly_sorted_dataset, repeated_elements_dataset]
# Correcting dataset_sizes for plotting
numerical_dataset_sizes = [len(dataset) for dataset in datasets]  # This should be numerical values

# Record the time taken for sorting each dataset again with corrected times
sort_times = []  # Resetting sort times to fill with actual measured times
for dataset in datasets:
    start_time = time.time()
    quick_sort(dataset.copy())  # Sort the dataset
    sort_times.append(time.time() - start_time)

# Plotting the corrected performance
plt.figure(figsize=(10, 6))
plt.plot(numerical_dataset_sizes, sort_times, marker='o', linestyle='-', color='b')
plt.title('Quick Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(numerical_dataset_sizes)  # Use numerical sizes here
plt.grid(True)
plt.show()
