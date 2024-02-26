import random
import time
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Define the datasets
datasets = {
    'Small dataset': random.sample(range(1, 101), 50),
    'Large random dataset': random.sample(range(1, 20001), 5000),
    'Nearly sorted dataset': list(range(1, 1001)) + random.sample(range(1001, 1101), 50),
    'Repeated elements dataset': [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]
}

# Sort datasets by their size (ascending order)
sorted_datasets_info = sorted(datasets.items(), key=lambda item: len(item[1]))

# Record the time taken for sorting each dataset
sorted_times = []
sorted_sizes = []
sorted_labels = []

for name, data in sorted_datasets_info:
    start_time = time.time()
    heap_sort(data.copy())  # Use copy to avoid altering original dataset
    end_time = time.time()
    time_taken = end_time - start_time
    sorted_times.append(time_taken)
    sorted_sizes.append(len(data))
    sorted_labels.append(name)
    print(f"{name} sorted in {time_taken:.6f} seconds.")

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.plot(sorted_sizes, sorted_times, marker='o', linestyle='-', color='b')
plt.title('Heap Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(sorted_sizes, labels=sorted_labels)  # Use sorted dataset names for x-ticks
plt.grid(True)
plt.show()
