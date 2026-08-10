import random
import time

# Input sizes
sizes_372 = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]


#1/ Linear Search
def linear_search_372(data_372, target_372):
    for i_372 in range(len(data_372)):
        if data_372[i_372] == target_372:
            return i_372
    return -1


#2/ Binary Search
def binary_search_372(data_372, target_372):
    low_372 = 0
    high_372 = len(data_372) - 1

    while low_372 <= high_372:
        mid_372 = (low_372 + high_372) // 2

        if data_372[mid_372] == target_372:
            return mid_372
        elif data_372[mid_372] < target_372:
            low_372 = mid_372 + 1
        else:
            high_372 = mid_372 - 1

    return -1


# Testing dataset size
for size_372 in sizes_372:

    #3/ Generate random dataset
    data_372 = random.sample(range(size_372 * 10), size_372)

    #4/ Sort before Binary Search
    data_372.sort()

    # Select target
    target_372 = random.choice(data_372)


#5/ Measuring the average execution time for both algorithms.


    # Linear Search average time
    start_372 = time.time()

    for count_372 in range(10):
        linear_search_372(data_372, target_372)

    end_372 = time.time()

    linear_average_372 = (end_372 - start_372) / 10


    # Binary Search average time
    start_372 = time.time()

    for count_372 in range(10):
        binary_search_372(data_372, target_372)

    end_372 = time.time()

    binary_average_372 = (end_372 - start_372) / 10


    # Results
    print("Dataset size:", size_372)
    print("Linear Search average time:", linear_average_372)
    print("Binary Search average time:", binary_average_372)
    print("-----------------------------")