import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]       # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

small_dataset = random.sample(range(1, 101), 50)  # 50 unique values between 1 and 100
large_random_dataset = random.sample(range(1, 20001), 5000)  # 5000 unique values between 1 and 20000
nearly_sorted_dataset = list(range(1, 1001)) + random.sample(range(1001, 1101), 50)  # Mostly sorted 1050 values
repeated_elements_dataset = [random.choice([3, 7, 8, 12, 15]) for _ in range(2000)]  # 2000 elements with 5 possible values

# Apply Merge Sort to each dataset
sorted_small_dataset = merge_sort(small_dataset)
sorted_large_random_dataset = merge_sort(large_random_dataset)
sorted_nearly_sorted_dataset = merge_sort(nearly_sorted_dataset)
sorted_repeated_elements_dataset = merge_sort(repeated_elements_dataset)

# Print sorted arrays
print("Sorted small dataset:", sorted_small_dataset)
print("Sorted large random dataset (first 10 elements):", sorted_large_random_dataset[:1000])
print("Sorted nearly sorted dataset:", sorted_nearly_sorted_dataset)
print("Sorted repeated elements dataset:", sorted_repeated_elements_dataset)

def calculate_sorting_time(dataset, algorithm, name):
    start_time = time.time()
    sorted_data = algorithm(dataset.copy())  # Sort the copy of the dataset
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"{name} sorted in {time_taken:.6f} seconds")
    return time_taken

datasets = {
    "Small dataset": small_dataset,
    "Large random dataset": large_random_dataset,
    "Nearly sorted dataset": nearly_sorted_dataset,
    "Repeated elements dataset": repeated_elements_dataset
}

sort_times = []
dataset_sizes = [len(datasets[name]) for name in datasets]

for name, data in datasets.items():
    start_time = time.time()
    merge_sort(data.copy())  # Use copy to avoid altering original data
    sort_times.append(time.time() - start_time)

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, sort_times, marker='o', linestyle='-', color='b')
plt.title('Merge Sort Performance')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.xticks(dataset_sizes)  # Set x-ticks to be the sizes of the datasets
plt.grid(True)
plt.show()