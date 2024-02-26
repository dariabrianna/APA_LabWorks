import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Define the datasets
datasets = {
    'Small dataset': random.sample(range(1, 101), 50),  # 50 unique values
    'Large random dataset': random.sample(range(1, 20001), 5000),  # 5000 unique values
    'Nearly sorted dataset': list(range(1, 1001)) + random.sample(range(1001, 1101), 50),  # Mostly sorted 1050 values
    'Repeated elements dataset': [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]  # 2000 elements with limited variety
}

# Sort datasets by their size (ascending order)
sorted_datasets_info = sorted(datasets.items(), key=lambda item: len(item[1]))

# Record the time taken for sorting each dataset
sorted_times = []
sorted_sizes = []

for name, data in sorted_datasets_info:
    start_time = time.time()
    bubble_sort(data.copy())  # Use copy to avoid altering original dataset
    end_time = time.time()
    time_taken = end_time - start_time
    sorted_times.append(time_taken)
    sorted_sizes.append(len(data))
    print(f"{name} sorted in {time_taken:.6f} seconds.")

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.plot(sorted_sizes, sorted_times, marker='o', linestyle='-', color='b')
plt.title('Bubble Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(sorted_sizes, labels=[name for name, _ in sorted_datasets_info])  # Set x-ticks to be the names of the sorted datasets
plt.grid(True)
plt.show()
