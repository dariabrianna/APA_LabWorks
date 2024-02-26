import random
import time
import matplotlib.pyplot as plt
import sys

# Increase the maximum recursion depth
sys.setrecursionlimit(10000)  # Adjust if necessary for very large datasets

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

# Define the datasets
small_dataset = random.sample(range(1, 101), 50)  # 50 unique values between 1 and 100
large_random_dataset = random.sample(range(1, 20001), 5000)  # 5000 unique values between 1 and 20000
nearly_sorted_dataset = list(range(1, 1001)) + random.sample(range(1001, 1101), 50)  # Mostly sorted 1050 values
repeated_elements_dataset = [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]  # 2000 elements with 5 possible values

datasets = {
    "Small dataset": small_dataset,
    "Large random dataset": large_random_dataset,
    "Nearly sorted dataset": nearly_sorted_dataset,
    "Repeated elements dataset": repeated_elements_dataset
}

# Sort datasets by size (ascending order)
sorted_dataset_info = sorted(datasets.items(), key=lambda item: len(item[1]))
sorted_dataset_names = [info[0] for info in sorted_dataset_info]
sorted_dataset_sizes = [len(info[1]) for info in sorted_dataset_info]

# Record the time taken for sorting each sorted dataset
sorted_times = []
for _, data in sorted_dataset_info:
    start_time = time.time()
    quick_sort(data.copy())  # Use copy to avoid altering original dataset
    sorted_times.append(time.time() - start_time)

# Plotting the performance in ascending order of dataset size
plt.figure(figsize=(10, 6))
plt.plot(sorted_dataset_sizes, sorted_times, marker='o', linestyle='-', color='b')
plt.title('Quick Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(sorted_dataset_sizes, labels=sorted_dataset_names)  # Use sorted sizes and labels
plt.grid(True)
plt.show()
