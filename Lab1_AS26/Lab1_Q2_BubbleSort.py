import random
import time

# Input sizes
sizes_372 = [100, 500, 1000, 2000, 4000, 8000]


#1/ Bubble Sort
def bubble_sort_372(data_372):
    for i_372 in range(len(data_372)):
        for j_372 in range(len(data_372) - 1 - i_372):
            if data_372[j_372] > data_372[j_372 + 1]:
                data_372[j_372], data_372[j_372 + 1] = data_372[j_372 + 1], data_372[j_372]


#2/ Merge Sort
def merge_sort_372(data_372):
    if len(data_372) <= 1:
        return data_372

    mid_372 = len(data_372) // 2

    left_372 = merge_sort_372(data_372[:mid_372])
    right_372 = merge_sort_372(data_372[mid_372:])

    return merge_372(left_372, right_372)


def merge_372(left_372, right_372):
    result_372 = []

    while left_372 and right_372:
        if left_372[0] < right_372[0]:
            result_372.append(left_372.pop(0))
        else:
            result_372.append(right_372.pop(0))

    result_372.extend(left_372)
    result_372.extend(right_372)

    return result_372


# Test each size
for size_372 in sizes_372:

    #3/ Generate random array
    data_372 = random.sample(range(size_372 * 10), size_372)


# 4/ Measure average execution time.


    # Bubble Sort average time
    total_bubble_372 = 0

    for count_372 in range(10):
        data1_372 = data_372.copy()

        start_372 = time.time()
        bubble_sort_372(data1_372)
        end_372 = time.time()

        total_bubble_372 += end_372 - start_372

    bubble_average_372 = total_bubble_372 / 10


    # Merge Sort average time
    total_merge_372 = 0

    for count_372 in range(10):
        data2_372 = data_372.copy()

        start_372 = time.time()
        merge_sort_372(data2_372)
        end_372 = time.time()

        total_merge_372 += end_372 - start_372

    merge_average_372 = total_merge_372 / 10


    # Results
    print("Dataset size:", size_372)
    print("Bubble Sort average time:", bubble_average_372)
    print("Merge Sort average time:", merge_average_372)
    print("-----------------------------")