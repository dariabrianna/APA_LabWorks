import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Define datasets
datasets = {
    "Small dataset": random.sample(range(1, 101), 50),
    "Large random dataset": random.sample(range(1, 20001), 5000),
    "Nearly sorted dataset": list(range(1, 1001)) + random.sample(range(1001, 1101), 50),
    "Repeated elements dataset": [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]
}

# Sort datasets by size (ascending order)
sorted_datasets_info = sorted(datasets.items(), key=lambda item: len(item[1]))

# Record the time taken for sorting each sorted dataset
sorted_times = []
sorted_sizes = []
sorted_labels = []

for name, data in sorted_datasets_info:
    start_time = time.time()
    merge_sort(data.copy())
    sorted_times.append(time.time() - start_time)
    sorted_sizes.append(len(data))
    sorted_labels.append(name)

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.plot(sorted_sizes, sorted_times, marker='o', linestyle='-', color='b')
plt.title('Merge Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(sorted_sizes, labels=sorted_labels)  # Set x-ticks to be the names of the sorted datasets
plt.grid(True)
plt.show()
