import csv
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt_372

from Assignment3_Sorts_372 import quicksort_basic_372, quicksort_improved_372


def time_sort_372(sort_function_372, values_372):
    result_372 = values_372.copy()
    start_372 = time.perf_counter()
    try:
        sort_function_372(result_372)
    except RecursionError:
        return None, "RecursionError"

    elapsed_372 = time.perf_counter() - start_372
    if result_372 != sorted(values_372):
        raise AssertionError("Sorting result did not match sorted()")
    return elapsed_372, "completed"


def make_values_372(size_372, kind_372, seed_372=372):
    random_generator_372 = random.Random(seed_372 + size_372)
    if kind_372 == "random":
        return [random_generator_372.randint(-100000, 100000)
                for _372 in range(size_372)]
    if kind_372 == "sorted":
        return list(range(size_372))
    if kind_372 == "duplicates":
        return [random_generator_372.randint(0, 9)
                for _372 in range(size_372)]
    raise ValueError("Unknown input type")


def run_size_benchmarks_372(output_folder_372):
    sizes_372 = [1000, 2000, 4000, 8000, 16000, 32000, 64000]
    input_types_372 = ["random", "sorted", "duplicates"]
    result_rows_372 = []

    for kind_372 in input_types_372:
        for size_372 in sizes_372:
            values_372 = make_values_372(size_372, kind_372)
            basic_time_372, basic_status_372 = time_sort_372(
                quicksort_basic_372, values_372
            )
            improved_time_372, improved_status_372 = time_sort_372(
                quicksort_improved_372, values_372
            )
            result_rows_372.append([
                kind_372, size_372, basic_time_372, basic_status_372,
                improved_time_372, improved_status_372
            ])
            basic_display_372 = (
                f"{basic_time_372:.6f}s" if basic_time_372 is not None
                else basic_status_372
            )
            print(f"{kind_372:10} n={size_372:6}: basic={basic_display_372}; "
                  f"improved={improved_time_372:.6f}s")

    csv_path_372 = output_folder_372 / "Q2_Sort_Timings.csv"
    with csv_path_372.open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow([
            "Input type", "n", "Basic time (seconds)", "Basic status",
            "Improved time (seconds)", "Improved status"
        ])
        writer_372.writerows(result_rows_372)

    for kind_372 in input_types_372:
        rows_372 = [row_372 for row_372 in result_rows_372
                    if row_372[0] == kind_372]
        basic_rows_372 = [row_372 for row_372 in rows_372
                          if row_372[2] is not None]
        plt_372.figure(figsize=(8, 5))
        if basic_rows_372:
            plt_372.plot([row_372[1] for row_372 in basic_rows_372],
                         [row_372[2] for row_372 in basic_rows_372],
                         marker="o", label="Basic quicksort")
        plt_372.plot([row_372[1] for row_372 in rows_372],
                     [row_372[4] for row_372 in rows_372],
                     marker="s", label="Improved quicksort")
        plt_372.xlabel("Input size (n)")
        plt_372.ylabel("Time (seconds)")
        plt_372.title(f"Quicksort performance: {kind_372} input")
        plt_372.grid(True)
        plt_372.legend()
        plt_372.tight_layout()
        plt_372.savefig(output_folder_372 / f"Q2_{kind_372}_Graph.png", dpi=200)
        plt_372.close()

    return result_rows_372


def run_cutoff_benchmark_372(output_folder_372):
    random_generator_372 = random.Random(372)
    values_372 = [random_generator_372.randint(-1000000, 1000000)
                  for _372 in range(100000)]
    cutoff_rows_372 = []

    for cutoff_372 in [1, 4, 8, 16, 32, 64]:
        result_372 = values_372.copy()
        start_372 = time.perf_counter()
        quicksort_improved_372(result_372, cutoff_372=cutoff_372, seed_372=372)
        elapsed_372 = time.perf_counter() - start_372
        if result_372 != sorted(values_372):
            raise AssertionError("Cutoff benchmark result did not match sorted()")
        cutoff_rows_372.append((cutoff_372, elapsed_372))
        print(f"cutoff={cutoff_372:2}: {elapsed_372:.6f}s")

    cutoff_path_372 = output_folder_372 / "Q3_Cutoff_Timings.csv"
    with cutoff_path_372.open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow(["Cutoff", "Improved quicksort time (seconds)"])
        writer_372.writerows(cutoff_rows_372)

    best_cutoff_372, best_time_372 = min(cutoff_rows_372, key=lambda row_372: row_372[1])
    return cutoff_rows_372, best_cutoff_372, best_time_372, values_372


def compare_with_sorted_372(output_folder_372, best_cutoff_372, values_372):
    improved_values_372 = values_372.copy()
    start_372 = time.perf_counter()
    quicksort_improved_372(improved_values_372, cutoff_372=best_cutoff_372,
                           seed_372=372)
    improved_time_372 = time.perf_counter() - start_372

    start_372 = time.perf_counter()
    builtin_values_372 = sorted(values_372)
    builtin_time_372 = time.perf_counter() - start_372
    if improved_values_372 != builtin_values_372:
        raise AssertionError("Improved quicksort did not match sorted()")

    compare_path_372 = output_folder_372 / "Q4_Sorted_Comparison.csv"
    with compare_path_372.open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow(["Method", "n", "Time (seconds)"])
        writer_372.writerow([f"Improved quicksort, cutoff {best_cutoff_372}",
                             len(values_372), improved_time_372])
        writer_372.writerow(["Python sorted()", len(values_372), builtin_time_372])
    print(f"Best cutoff: {best_cutoff_372}; improved={improved_time_372:.6f}s; "
          f"sorted()={builtin_time_372:.6f}s")
    return improved_time_372, builtin_time_372


def run_benchmarks_372():
    output_folder_372 = Path(__file__).parent / "outputs"
    output_folder_372.mkdir(exist_ok=True)
    run_size_benchmarks_372(output_folder_372)
    cutoff_rows_372, best_cutoff_372, best_time_372, values_372 = (
        run_cutoff_benchmark_372(output_folder_372)
    )
    compare_with_sorted_372(output_folder_372, best_cutoff_372, values_372)
    print(f"Saved benchmark data and graphs in {output_folder_372}")


if __name__ == "__main__":
    run_benchmarks_372()
