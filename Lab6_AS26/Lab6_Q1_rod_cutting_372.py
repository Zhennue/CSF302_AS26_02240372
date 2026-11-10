import csv
import time
from pathlib import Path

PRICES_372 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def price_372(length_372):
    return PRICES_372[length_372] if length_372 < len(PRICES_372) else 3 * length_372

def naive_rod_cut_372(n_372):
    calls_372 = 0
    def solve_372(size_372):
        nonlocal calls_372
        calls_372 += 1
        if size_372 == 0:
            return 0, []
        best_372, pieces_372 = -1, []
        for first_372 in range(1, size_372 + 1):
            rest_value_372, rest_pieces_372 = solve_372(size_372 - first_372)
            candidate_372 = price_372(first_372) + rest_value_372
            if candidate_372 > best_372:
                best_372, pieces_372 = candidate_372, [first_372] + rest_pieces_372
        return best_372, pieces_372
    value_372, pieces_372 = solve_372(n_372)
    return value_372, pieces_372, calls_372

def memo_rod_cut_372(n_372):
    calls_372, memo_372 = 0, {0: (0, [])}
    def solve_372(size_372):
        nonlocal calls_372
        calls_372 += 1
        if size_372 in memo_372:
            return memo_372[size_372]
        best_372, pieces_372 = -1, []
        for first_372 in range(1, size_372 + 1):
            rest_value_372, rest_pieces_372 = solve_372(size_372 - first_372)
            candidate_372 = price_372(first_372) + rest_value_372
            if candidate_372 > best_372:
                best_372, pieces_372 = candidate_372, [first_372] + rest_pieces_372
        memo_372[size_372] = (best_372, pieces_372)
        return memo_372[size_372]
    value_372, pieces_372 = solve_372(n_372)
    return value_372, pieces_372, calls_372

def bottom_up_rod_cut_372(n_372):
    values_372, first_piece_372 = [0] * (n_372 + 1), [0] * (n_372 + 1)
    calls_372 = 0
    for size_372 in range(1, n_372 + 1):
        best_372 = -1
        for first_372 in range(1, size_372 + 1):
            calls_372 += 1
            candidate_372 = price_372(first_372) + values_372[size_372 - first_372]
            if candidate_372 > best_372:
                best_372, first_piece_372[size_372] = candidate_372, first_372
        values_372[size_372] = best_372
    pieces_372, remaining_372 = [], n_372
    while remaining_372:
        chosen_372 = first_piece_372[remaining_372]
        pieces_372.append(chosen_372)
        remaining_372 -= chosen_372
    return values_372[n_372], pieces_372, calls_372

def benchmark_372():
    folder_372 = Path(__file__).parent / "outputs"
    rows_372 = []
    methods_372 = [("Naive recursion", naive_rod_cut_372),
                   ("Top-down memoized", memo_rod_cut_372),
                   ("Bottom-up tabulated", bottom_up_rod_cut_372)]
    for n_372 in [5, 10, 15, 20, 25]:
        for name_372, method_372 in methods_372:
            start_372 = time.perf_counter()
            value_372, pieces_372, calls_372 = method_372(n_372)
            elapsed_372 = time.perf_counter() - start_372
            rows_372.append([name_372, n_372, calls_372, f"{elapsed_372:.8f}", value_372])
            print(f"{name_372:22} n={n_372:2} calls={calls_372:12} time={elapsed_372:.6f}s revenue={value_372}")
    with (folder_372 / "q1_rod_cutting_results.csv").open("w", newline="", encoding="utf-8") as f_372:
        writer_372 = csv.writer(f_372)
        writer_372.writerow(["algorithm", "n", "calls", "time_seconds", "maximum_revenue"])
        writer_372.writerows(rows_372)
    print("Saved outputs/q1_rod_cutting_results.csv")

if __name__ == "__main__":
    print("Maximum revenue and optimal pieces for n = 1 to 10")
    for n_372 in range(1, 11):
        value_372, pieces_372, _ = bottom_up_rod_cut_372(n_372)
        print(f"n={n_372:2} maximum revenue={value_372:2} pieces={pieces_372}")
    print("\nBenchmarking n = 5, 10, 15, 20, 25")
    benchmark_372()
