import csv
import random
import time
from pathlib import Path

SIZES_372 = [1000, 2000, 4000, 8000, 16000]
INPUT_TYPES_372 = ["random", "sorted", "reverse", "duplicates"]


def make_data_372(size_372, kind_372, seed_372=372):
    rng_372 = random.Random(seed_372 + size_372)
    if kind_372 == "random":
        return [rng_372.randint(0, size_372 * 10) for _ in range(size_372)]
    if kind_372 == "sorted":
        return list(range(size_372))
    if kind_372 == "reverse":
        return list(range(size_372, 0, -1))
    if kind_372 == "duplicates":
        return [rng_372.randint(0, 9) for _ in range(size_372)]
    raise ValueError("Unknown input type")


def quicksort_lomuto_372(values_372):
    arr_372 = values_372.copy()
    comparisons_372 = 0

    def partition_372(low_372, high_372):
        nonlocal comparisons_372
        pivot_372 = arr_372[high_372]
        boundary_372 = low_372
        for scan_372 in range(low_372, high_372):
            comparisons_372 += 1
            if arr_372[scan_372] <= pivot_372:
                arr_372[boundary_372], arr_372[scan_372] = arr_372[scan_372], arr_372[boundary_372]
                boundary_372 += 1
        arr_372[boundary_372], arr_372[high_372] = arr_372[high_372], arr_372[boundary_372]
        return boundary_372

    def sort_372(low_372, high_372):
        while low_372 < high_372:
            pivot_index_372 = partition_372(low_372, high_372)
            if pivot_index_372 - low_372 < high_372 - pivot_index_372:
                sort_372(low_372, pivot_index_372 - 1)
                low_372 = pivot_index_372 + 1
            else:
                sort_372(pivot_index_372 + 1, high_372)
                high_372 = pivot_index_372 - 1

    sort_372(0, len(arr_372) - 1)
    return arr_372, comparisons_372


def quicksort_hoare_372(values_372):
    arr_372 = values_372.copy()
    comparisons_372 = 0

    def partition_372(low_372, high_372):
        nonlocal comparisons_372
        pivot_372 = arr_372[(low_372 + high_372) // 2]
        left_372, right_372 = low_372 - 1, high_372 + 1
        while True:
            left_372 += 1
            while True:
                comparisons_372 += 1
                if not (arr_372[left_372] < pivot_372):
                    break
                left_372 += 1
            right_372 -= 1
            while True:
                comparisons_372 += 1
                if not (arr_372[right_372] > pivot_372):
                    break
                right_372 -= 1
            if left_372 >= right_372:
                return right_372
            arr_372[left_372], arr_372[right_372] = arr_372[right_372], arr_372[left_372]

    def sort_372(low_372, high_372):
        while low_372 < high_372:
            split_372 = partition_372(low_372, high_372)
            if split_372 - low_372 < high_372 - split_372:
                sort_372(low_372, split_372)
                low_372 = split_372 + 1
            else:
                sort_372(split_372 + 1, high_372)
                high_372 = split_372

    sort_372(0, len(arr_372) - 1)
    return arr_372, comparisons_372


def quicksort_random_372(values_372, seed_372=372):
    arr_372 = values_372.copy()
    comparisons_372 = 0
    rng_372 = random.Random(seed_372)

    def partition_372(low_372, high_372):
        nonlocal comparisons_372
        chosen_372 = rng_372.randint(low_372, high_372)
        arr_372[chosen_372], arr_372[high_372] = arr_372[high_372], arr_372[chosen_372]
        pivot_372 = arr_372[high_372]
        boundary_372 = low_372
        for scan_372 in range(low_372, high_372):
            comparisons_372 += 1
            if arr_372[scan_372] <= pivot_372:
                arr_372[boundary_372], arr_372[scan_372] = arr_372[scan_372], arr_372[boundary_372]
                boundary_372 += 1
        arr_372[boundary_372], arr_372[high_372] = arr_372[high_372], arr_372[boundary_372]
        return boundary_372

    def sort_372(low_372, high_372):
        while low_372 < high_372:
            pivot_index_372 = partition_372(low_372, high_372)
            if pivot_index_372 - low_372 < high_372 - pivot_index_372:
                sort_372(low_372, pivot_index_372 - 1)
                low_372 = pivot_index_372 + 1
            else:
                sort_372(pivot_index_372 + 1, high_372)
                high_372 = pivot_index_372 - 1

    sort_372(0, len(arr_372) - 1)
    return arr_372, comparisons_372


def quicksort_three_way_372(values_372):
    arr_372 = values_372.copy()
    comparisons_372 = 0

    def sort_372(low_372, high_372):
        nonlocal comparisons_372
        while low_372 < high_372:
            pivot_372 = arr_372[(low_372 + high_372) // 2]
            less_372, scan_372, greater_372 = low_372, low_372, high_372
            while scan_372 <= greater_372:
                comparisons_372 += 1
                if arr_372[scan_372] < pivot_372:
                    arr_372[less_372], arr_372[scan_372] = arr_372[scan_372], arr_372[less_372]
                    less_372 += 1
                    scan_372 += 1
                else:
                    comparisons_372 += 1
                    if arr_372[scan_372] > pivot_372:
                        arr_372[scan_372], arr_372[greater_372] = arr_372[greater_372], arr_372[scan_372]
                        greater_372 -= 1
                    else:
                        scan_372 += 1
            if less_372 - low_372 < high_372 - greater_372:
                sort_372(low_372, less_372 - 1)
                low_372 = greater_372 + 1
            else:
                sort_372(greater_372 + 1, high_372)
                high_372 = less_372 - 1

    sort_372(0, len(arr_372) - 1)
    return arr_372, comparisons_372


def run_benchmarks_372():
    algorithms_372 = {
        "Lomuto": quicksort_lomuto_372,
        "Hoare": quicksort_hoare_372,
        "Randomized": quicksort_random_372,
        "Three-way": quicksort_three_way_372,
    }
    output_372 = Path(__file__).parent / "outputs"
    output_372.mkdir(exist_ok=True)
    result_file_372 = output_372 / "q1_results.csv"
    with result_file_372.open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow(["algorithm", "input_type", "n", "comparisons", "time_seconds"])
        for kind_372 in INPUT_TYPES_372:
            for size_372 in SIZES_372:
                data_372 = make_data_372(size_372, kind_372)
                for name_372, algorithm_372 in algorithms_372.items():
                    start_372 = time.perf_counter()
                    sorted_data_372, count_372 = algorithm_372(data_372)
                    elapsed_372 = time.perf_counter() - start_372
                    assert sorted_data_372 == sorted(data_372)
                    writer_372.writerow([name_372, kind_372, size_372, count_372, f"{elapsed_372:.8f}"])
                    print(f"{name_372:12} {kind_372:10} n={size_372:5} comparisons={count_372:12} time={elapsed_372:.6f}s")
    print(f"\nSaved results to: {result_file_372}")


if __name__ == "__main__":
    run_benchmarks_372()
