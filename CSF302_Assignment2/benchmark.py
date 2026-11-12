
import random
import time
import csv
import math
import matplotlib.pyplot as plt

from closest import closest_pair, closest_pair_brute


# Input sizes
sizes = [
    1000,
    2000,
    4000,
    8000,
    16000,
    32000,
    64000
]

results = []

# Maximum time allowed for brute force
time_limit = 60


# Generate the same random points for both algorithms
random_generator = random.Random(42)

all_points = [
    (
        random_generator.randint(0, 1000000),
        random_generator.randint(0, 1000000)
    )
    for _ in range(64000)
]

brute_stopped = False


print("Starting performance tests...\n")

for n in sizes:

    points = all_points[:n]

    # Measure divide and conquer
    start = time.perf_counter()

    closest_pair(points)

    dc_time = time.perf_counter() - start

    # Measure brute force
    brute_time = None

    if not brute_stopped:

        start = time.perf_counter()

        closest_pair_brute(points)

        brute_time = time.perf_counter() - start

        if brute_time >= time_limit:
            brute_stopped = True

    else:
        print("Brute force skipped because of the time limit.")

    results.append([
        n,
        dc_time,
        brute_time
    ])

    print(
        f"n = {n:6d} | "
        f"Divide and Conquer = {dc_time:.6f}s | "
        f"Brute Force = "
        f"{brute_time if brute_time is not None else 'Stopped'}"
    )


# Save timing results to CSV
with open("timing_results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Number of Points",
        "Divide and Conquer (seconds)",
        "Brute Force (seconds)"
    ])

    writer.writerows(results)


# Find crossover point
crossover = None

for n, dc_time, brute_time in results:

    if brute_time is not None and dc_time < brute_time:

        crossover = n
        break


print("\nCrossover Point:")

if crossover is not None:
    print(
        "Divide and conquer becomes faster "
        "at n =", crossover
    )
else:
    print(
        "No crossover was found in the measured sizes."
    )


# Create log-log graph
dc_sizes = [row[0] for row in results]
dc_times = [row[1] for row in results]

brute_sizes = [
    row[0] for row in results
    if row[2] is not None
]

brute_times = [
    row[2] for row in results
    if row[2] is not None
]

plt.figure(figsize=(9, 6))

plt.loglog(
    dc_sizes,
    dc_times,
    marker="o",
    label="Divide and Conquer"
)

plt.loglog(
    brute_sizes,
    brute_times,
    marker="s",
    label="Brute Force"
)

plt.xlabel("Number of Points (n)")
plt.ylabel("Execution Time (seconds)")

plt.title("Closest Pair Algorithm Performance")

plt.legend()
plt.grid(True, which="both")

plt.tight_layout()

plt.savefig("performance_graph.png", dpi=300)

plt.show()

print("\nFiles generated:")
print("1. timing_results.csv")
print("2. performance_graph.png")
