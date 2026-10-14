# Lab 2 - Q2: Merge Sort Analysis (Menu-Driven)
# Conclusion: Merge sort has O(n log n) time complexity for random, sorted, and
# reverse-sorted inputs. The measured step count can vary with input order and size.

import random
import time


def Merge_372(left_372, right_372, steps_372):
    result_372 = []
    left_index_372 = 0
    right_index_372 = 0

    while left_index_372 < len(left_372) and right_index_372 < len(right_372):
        steps_372[0] += 1
        if left_372[left_index_372] <= right_372[right_index_372]:
            result_372.append(left_372[left_index_372])
            left_index_372 += 1
        else:
            result_372.append(right_372[right_index_372])
            right_index_372 += 1

    result_372.extend(left_372[left_index_372:])
    result_372.extend(right_372[right_index_372:])
    return result_372


def MergeSort_372(array_372, steps_372):
    if len(array_372) <= 1:
        return array_372[:]
    middle_372 = len(array_372) // 2
    left_372 = MergeSort_372(array_372[:middle_372], steps_372)
    right_372 = MergeSort_372(array_372[middle_372:], steps_372)
    return Merge_372(left_372, right_372, steps_372)


def SelectionSortDescending_372(array_372):
    result_372 = array_372[:]
    steps_372 = 0
    for index_372 in range(len(result_372)):
        largest_372 = index_372
        for scan_372 in range(index_372 + 1, len(result_372)):
            steps_372 += 1
            if result_372[scan_372] > result_372[largest_372]:
                largest_372 = scan_372
        result_372[index_372], result_372[largest_372] = result_372[largest_372], result_372[index_372]
    return result_372, steps_372


def Measure_372(data_372):
    steps_372 = [0]
    start_372 = time.perf_counter()
    sorted_data_372 = MergeSort_372(data_372, steps_372)
    elapsed_372 = time.perf_counter() - start_372
    return sorted_data_372, steps_372[0], elapsed_372


def Main_372():
    array_372 = []
    print("Lab 2 Q2 - Merge Sort Analysis")
    while True:
        print("\n1. Generate n random numbers")
        print("2. Display array")
        print("3. Sort ascending using Merge Sort")
        print("4. Sort descending using Selection Sort")
        print("5. Analyze random data")
        print("6. Analyze already sorted data")
        print("7. Analyze descending-sorted data")
        print("0. Exit")
        choice_372 = input("Choose an option: ").strip()

        if choice_372 == "1":
            try:
                size_372 = int(input("Enter number of integers (n): "))
                if size_372 < 1:
                    print("Please enter n >= 1.")
                    continue
                array_372 = [random.randint(1, 100) for _ in range(size_372)]
                print("Array generated.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice_372 == "2":
            print("Array:", array_372 if array_372 else "No array yet. Choose option 1.")
        elif choice_372 == "3":
            if not array_372:
                print("Generate an array first.")
                continue
            steps_372 = [0]
            array_372 = MergeSort_372(array_372, steps_372)
            print("Ascending array:", array_372)
            print("Merge comparisons (step count):", steps_372[0])
        elif choice_372 == "4":
            if not array_372:
                print("Generate an array first.")
                continue
            array_372, steps_372 = SelectionSortDescending_372(array_372)
            print("Descending array:", array_372)
            print("Selection-sort comparisons (step count):", steps_372)
        elif choice_372 in ("5", "6", "7"):
            try:
                size_372 = int(input("Enter n for this experiment: "))
                if size_372 < 1:
                    print("Please enter n >= 1.")
                    continue
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if choice_372 == "5":
                data_372 = [random.randint(1, 100) for _ in range(size_372)]
                label_372 = "Random data"
            elif choice_372 == "6":
                data_372 = list(range(1, size_372 + 1))
                label_372 = "Already sorted data"
            else:
                data_372 = list(range(size_372, 0, -1))
                label_372 = "Descending-sorted data"

            sorted_data_372, count_372, elapsed_372 = Measure_372(data_372)
            print(f"\n{label_372}")
            print("Input sample:", data_372[:20], "..." if size_372 > 20 else "")
            print("Sorted output sample:", sorted_data_372[:20], "..." if size_372 > 20 else "")
            print("Merge comparisons (step count):", count_372)
            print(f"Execution time: {elapsed_372:.8f} seconds")
            print("Expected time complexity: O(n log n)")
        elif choice_372 == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    Main_372()
