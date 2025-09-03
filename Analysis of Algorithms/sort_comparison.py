import time
import random
import statistics

def time_algorithm(algo, arr):
    start = time.time()
    algo(arr.copy())
    return time.time() - start

# Starter code
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def insertion_sort(arr): 
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  
        j = i - 1    

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def random_array(array_size):
    random.seed(50)
    array = list(range(1, array_size + 1))
    random.shuffle(array)
    return array

def inversely_sorted_array(array_size):
    return list(range(array_size, 0, -1))

def sorted_array(array_size):
    return list(range(1, array_size + 1))

n = 10000 #change for array size
times = []

for _ in range(5):
    arr = sorted_array(n) #change for sorted/inverse/random 
    run_time = time_algorithm(insertion_sort, arr) #change based on algorithm
    times.append(run_time)

mean_time = statistics.mean(times)
median_time = statistics.median(times)
sd_time = statistics.stdev(times)

print(f"n = {n}:")
for i, t in enumerate(times, 1):
    print(f"{t:.6f} seconds")
 
print(f"\nMean Time: {mean_time:.6f} seconds")
print(f"Median Time: {median_time:.6f} seconds")
print(f"SD: {sd_time:.6f} seconds")

