# Lab 2 - Q1: Prime Number Testing
# Compare naive and optimized prime testing using step counts and execution time.
# Conclusion: The optimized method checks divisors only up to sqrt(n), so it generally
# performs fewer checks than the naive method. Both methods have O(n) and O(sqrt(n))
# time complexity respectively.

import time
import matplotlib.pyplot as plt


def IsPrimeNaive_372(n_372):
    steps_372 = 0
    if n_372 < 2:
        return False, steps_372
    for divisor_372 in range(2, n_372):
        steps_372 += 1
        if n_372 % divisor_372 == 0:
            return False, steps_372
    return True, steps_372


def IsPrimeOptimized_372(n_372):
    steps_372 = 0
    if n_372 < 2:
        return False, steps_372
    divisor_372 = 2
    while divisor_372 * divisor_372 <= n_372:
        steps_372 += 1
        if n_372 % divisor_372 == 0:
            return False, steps_372
        divisor_372 += 1
    return True, steps_372


def Main_372():
    numbers_372 = []
    print("Lab 2 Q1 - Prime Number Testing")
    print("Enter at least 10 integers.")
    for index_372 in range(10):
        while True:
            try:
                number_372 = int(input(f"Number {index_372 + 1}: "))
                numbers_372.append(number_372)
                break
            except ValueError:
                print("Please enter a whole number.")

    naive_counts_372 = []
    optimized_counts_372 = []
    naive_times_372 = []
    optimized_times_372 = []

    print("\nResults")
    print("-" * 78)
    print(f"{'Number':>10} {'Prime?':>8} {'Naive steps':>14} {'Optimized steps':>18} {'Same result?':>14}")
    print("-" * 78)

    for number_372 in numbers_372:
        start_372 = time.perf_counter()
        naive_result_372, naive_steps_372 = IsPrimeNaive_372(number_372)
        naive_time_372 = time.perf_counter() - start_372

        start_372 = time.perf_counter()
        optimized_result_372, optimized_steps_372 = IsPrimeOptimized_372(number_372)
        optimized_time_372 = time.perf_counter() - start_372

        naive_counts_372.append(naive_steps_372)
        optimized_counts_372.append(optimized_steps_372)
        naive_times_372.append(naive_time_372)
        optimized_times_372.append(optimized_time_372)

        print(f"{number_372:>10} {str(optimized_result_372):>8} {naive_steps_372:>14} "
              f"{optimized_steps_372:>18} {str(naive_result_372 == optimized_result_372):>14}")

    try:
        plt.figure(figsize=(9, 5))
        plt.plot(numbers_372, naive_counts_372, marker="o", label="Naive method")
        plt.plot(numbers_372, optimized_counts_372, marker="s", label="Optimized method")
        plt.xlabel("Input number")
        plt.ylabel("Divisibility checks (step count)")
        plt.title("Prime Testing: Step Count Comparison")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("Lab2_Q1_PrimeTesting_Graph.png")
        plt.show()
        print("\nGraph saved as Lab2_Q1_PrimeTesting_Graph.png")
    except ImportError:
        print("\nInstall matplotlib to generate the graph: pip install matplotlib")

    print("\nComplexity: Naive O(n), Optimized O(sqrt(n)).")
    print("Conclusion: The optimized method normally uses fewer divisibility checks.")


if __name__ == "__main__":
    Main_372()
