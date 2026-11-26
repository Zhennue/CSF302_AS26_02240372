import csv
import random
import time

import matplotlib.pyplot as plt_372

from Assignment2_AS26.Assignment2_ClosestPair import closest_pair_372, closest_pair_brute_372


def run_benchmark_372():
    sizes_372 = [1000, 2000, 4000, 8000, 16000, 32000, 64000]
    time_limit_372 = 60
    random_generator_372 = random.Random(42)
    all_points_372 = [
        (random_generator_372.randint(0, 1000000),
         random_generator_372.randint(0, 1000000))
        for _372 in range(64000)
    ]
    results_372 = []
    brute_stopped_372 = False

    for n_372 in sizes_372:
        points_372 = all_points_372[:n_372]
        start_372 = time.perf_counter()
        closest_pair_372(points_372)
        divide_time_372 = time.perf_counter() - start_372

        brute_time_372 = None
        if not brute_stopped_372:
            start_372 = time.perf_counter()
            try:
                closest_pair_brute_372(points_372, time_limit_372)
                brute_time_372 = time.perf_counter() - start_372
            except TimeoutError:
                brute_time_372 = time.perf_counter() - start_372
                brute_stopped_372 = True

        results_372.append((n_372, divide_time_372, brute_time_372))
        brute_display_372 = (
            f"{brute_time_372:.3f}s" if brute_time_372 is not None else "skipped"
        )
        print(f"n={n_372:>6}: divide and conquer {divide_time_372:.3f}s; "
              f"brute force {brute_display_372}")

    with open("Q2_Timing_Results.csv", "w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow([
            "Number of Points", "Divide and Conquer (seconds)",
            "Brute Force (seconds)"
        ])
        writer_372.writerows(results_372)

    crossover_372 = next(
        (n_372 for n_372, divide_372, brute_372 in results_372
         if brute_372 is not None and divide_372 < brute_372),
        None
    )
    if crossover_372 is not None:
        print(f"First measured crossover: n={crossover_372}")
    else:
        print("No measured crossover in the completed brute-force sizes.")

    divide_sizes_372 = [row_372[0] for row_372 in results_372]
    divide_times_372 = [row_372[1] for row_372 in results_372]
    brute_sizes_372 = [row_372[0] for row_372 in results_372
                       if row_372[2] is not None]
    brute_times_372 = [row_372[2] for row_372 in results_372
                       if row_372[2] is not None]

    plt_372.figure(figsize=(9, 6))
    plt_372.loglog(divide_sizes_372, divide_times_372, marker="o",
                   label="Divide and conquer")
    plt_372.loglog(brute_sizes_372, brute_times_372, marker="s",
                   label="Brute force")
    plt_372.xlabel("Number of points (n)")
    plt_372.ylabel("Execution time (seconds)")
    plt_372.title("Closest pair algorithm performance")
    plt_372.legend()
    plt_372.grid(True, which="both")
    plt_372.tight_layout()
    plt_372.savefig("Q2_Performance_Graph.png", dpi=300)
    plt_372.close()
    print("Saved Q2_Timing_Results.csv and Q2_Performance_Graph.png")


if __name__ == "__main__":
    run_benchmark_372()
