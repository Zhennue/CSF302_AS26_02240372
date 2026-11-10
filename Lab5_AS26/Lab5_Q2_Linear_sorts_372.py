import csv
import random
import time
from array import array
from pathlib import Path


def counting_sort_372(values_372, maximum_372=None):
    if not values_372:
        return []
    if any(value_372 < 0 for value_372 in values_372):
        raise ValueError("Counting sort accepts non-negative integers only")
    if maximum_372 is None:
        maximum_372 = max(values_372)
    if maximum_372 < max(values_372):
        raise ValueError("maximum is smaller than an input value")
    counts_372 = array("Q", [0]) * (maximum_372 + 1)
    for value_372 in values_372:
        counts_372[value_372] += 1
    for index_372 in range(1, len(counts_372)):
        counts_372[index_372] += counts_372[index_372 - 1]
    output_372 = [0] * len(values_372)
    for value_372 in reversed(values_372):
        counts_372[value_372] -= 1
        output_372[counts_372[value_372]] = value_372
    return output_372


def counting_sort_digit_372(values_372, exponent_372, base_372):
    counts_372 = [0] * base_372
    output_372 = [0] * len(values_372)
    for value_372 in values_372:
        digit_372 = (value_372 // exponent_372) % base_372
        counts_372[digit_372] += 1
    for index_372 in range(1, base_372):
        counts_372[index_372] += counts_372[index_372 - 1]
    for value_372 in reversed(values_372):
        digit_372 = (value_372 // exponent_372) % base_372
        counts_372[digit_372] -= 1
        output_372[counts_372[digit_372]] = value_372
    return output_372


def radix_sort_372(values_372, base_372=10):
    if base_372 < 2:
        raise ValueError("Base must be at least 2")
    if any(value_372 < 0 for value_372 in values_372):
        raise ValueError("This LSD implementation accepts non-negative integers only")
    if not values_372:
        return []
    output_372 = values_372.copy()
    exponent_372 = 1
    maximum_372 = max(output_372)
    while maximum_372 // exponent_372 > 0:
        output_372 = counting_sort_digit_372(output_372, exponent_372, base_372)
        exponent_372 *= base_372
    return output_372


def merge_sort_372(values_372):
    if len(values_372) <= 1:
        return values_372.copy()
    middle_372 = len(values_372) // 2
    left_372 = merge_sort_372(values_372[:middle_372])
    right_372 = merge_sort_372(values_372[middle_372:])
    result_372 = []
    left_index_372 = right_index_372 = 0
    while left_index_372 < len(left_372) and right_index_372 < len(right_372):
        if left_372[left_index_372] <= right_372[right_index_372]:
            result_372.append(left_372[left_index_372])
            left_index_372 += 1
        else:
            result_372.append(right_372[right_index_372])
            right_index_372 += 1
    result_372.extend(left_372[left_index_372:])
    result_372.extend(right_372[right_index_372:])
    return result_372


def stable_pair_demo_372():
    pairs_372 = [(2, 0), (1, 1), (2, 2), (0, 3), (1, 4), (2, 5)]
    keys_372 = [pair_372[0] for pair_372 in pairs_372]
    sorted_keys_372 = counting_sort_372(keys_372, 2)
    # Stable pair counting sort: place original pairs using cumulative positions.
    counts_372 = [0, 0, 0]
    for key_372 in keys_372:
        counts_372[key_372] += 1
    for index_372 in range(1, len(counts_372)):
        counts_372[index_372] += counts_372[index_372 - 1]
    output_372 = [None] * len(pairs_372)
    for pair_372 in reversed(pairs_372):
        key_372 = pair_372[0]
        counts_372[key_372] -= 1
        output_372[counts_372[key_372]] = pair_372
    print("Original (key, index) pairs:", pairs_372)
    print("Sorted keys:", sorted_keys_372)
    print("Stable sorted pairs:", output_372)
    assert output_372 == sorted(pairs_372, key=lambda pair_372: pair_372[0])


def timed_372(function_372, data_372, *args_372):
    start_372 = time.perf_counter()
    result_372 = function_372(data_372, *args_372)
    return result_372, time.perf_counter() - start_372


def run_benchmarks_372():
    rng_372 = random.Random(372)
    output_dir_372 = Path(__file__).parent / "outputs"
    output_dir_372.mkdir(exist_ok=True)
    rows_372 = []

    print("Counting sort: n=100,000; varying k")
    for maximum_372 in [10, 10**3, 10**5, 10**7]:
        data_372 = [rng_372.randint(0, maximum_372) for _ in range(100_000)]
        result_372, elapsed_372 = timed_372(counting_sort_372, data_372, maximum_372)
        assert result_372 == sorted(data_372)
        rows_372.append(["Counting", 100_000, maximum_372, elapsed_372])
        print(f"k={maximum_372:>9} time={elapsed_372:.6f}s")

    print("\nRadix sort and merge sort: k=1,000,000,000; varying n")
    for size_372 in [10_000, 100_000, 250_000, 500_000, 1_000_000]:
        data_372 = [rng_372.randint(0, 10**9) for _ in range(size_372)]
        for base_372 in [10, 256]:
            result_372, elapsed_372 = timed_372(radix_sort_372, data_372, base_372)
            assert result_372 == sorted(data_372)
            rows_372.append([f"Radix base {base_372}", size_372, 10**9, elapsed_372])
            print(f"Radix base {base_372:3} n={size_372:>7} time={elapsed_372:.6f}s")
        result_372, elapsed_372 = timed_372(merge_sort_372, data_372)
        assert result_372 == sorted(data_372)
        rows_372.append(["Merge sort", size_372, 10**9, elapsed_372])
        print(f"Merge sort     n={size_372:>7} time={elapsed_372:.6f}s")

    with (output_dir_372 / "q2_results.csv").open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow(["algorithm", "n", "k_or_maximum", "time_seconds"])
        writer_372.writerows(rows_372)
    stable_pair_demo_372()
    print(f"\nSaved results to: {output_dir_372 / 'q2_results.csv'}")


if __name__ == "__main__":
    run_benchmarks_372()
