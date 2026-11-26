import csv
import random
import time
from pathlib import Path


def brute_force_inversions_372(values_372):
    count_372 = 0
    for left_372 in range(len(values_372)):
        for right_372 in range(left_372 + 1, len(values_372)):
            if values_372[left_372] > values_372[right_372]:
                count_372 += 1
    return count_372


def merge_inversions_372(values_372):
    def sort_count_372(items_372):
        if len(items_372) <= 1:
            return items_372, 0
        middle_372 = len(items_372) // 2
        left_372, left_count_372 = sort_count_372(items_372[:middle_372])
        right_372, right_count_372 = sort_count_372(items_372[middle_372:])
        merged_372 = []
        left_index_372 = right_index_372 = 0
        cross_count_372 = 0
        while left_index_372 < len(left_372) and right_index_372 < len(right_372):
            if left_372[left_index_372] <= right_372[right_index_372]:
                merged_372.append(left_372[left_index_372])
                left_index_372 += 1
            else:
                merged_372.append(right_372[right_index_372])
                right_index_372 += 1
                cross_count_372 += len(left_372) - left_index_372
        merged_372.extend(left_372[left_index_372:])
        merged_372.extend(right_372[right_index_372:])
        return merged_372, left_count_372 + right_count_372 + cross_count_372

    return sort_count_372(values_372)[1]


def kendall_tau_distance_372(ranking_a_372, ranking_b_372):
    if len(ranking_a_372) != len(ranking_b_372):
        raise ValueError("Both rankings must contain the same number of movies")
    if set(ranking_a_372) != set(ranking_b_372):
        raise ValueError("Both rankings must contain the same movie titles")
    positions_b_372 = {movie_372: index_372 for index_372, movie_372 in enumerate(ranking_b_372)}
    converted_372 = [positions_b_372[movie_372] for movie_372 in ranking_a_372]
    return merge_inversions_372(converted_372)


def read_ranking_372(label_372):
    print(f"\nEnter 10 movie titles for {label_372}, from rank 1 to rank 10.")
    ranking_372 = []
    for index_372 in range(10):
        movie_372 = input(f"Rank {index_372 + 1}: ").strip()
        while not movie_372 or movie_372 in ranking_372:
            print("Please enter a non-empty movie title that has not already been used.")
            movie_372 = input(f"Rank {index_372 + 1}: ").strip()
        ranking_372.append(movie_372)
    return ranking_372


def verify_random_arrays_372():
    rng_372 = random.Random(372)
    for size_372 in [0, 1, 2, 10, 50, 100, 500, 1000, 2000]:
        for _ in range(5):
            data_372 = [rng_372.randint(-100, 100) for _ in range(size_372)]
            brute_372 = brute_force_inversions_372(data_372)
            efficient_372 = merge_inversions_372(data_372)
            assert brute_372 == efficient_372
    print("Verification passed: brute force and merge-based counts match for random arrays up to n=2,000.")


def benchmark_372():
    rng_372 = random.Random(372)
    sizes_372 = [1000, 5000, 10000, 20000, 50000, 100000, 250000, 500000, 1000000]
    output_dir_372 = Path(__file__).parent / "outputs"
    output_dir_372.mkdir(exist_ok=True)
    rows_372 = []
    brute_stopped_372 = False
    for size_372 in sizes_372:
        data_372 = [rng_372.randint(0, size_372 * 10) for _ in range(size_372)]
        start_372 = time.perf_counter()
        efficient_count_372 = merge_inversions_372(data_372)
        efficient_time_372 = time.perf_counter() - start_372
        rows_372.append(["Merge-sort-based", size_372, efficient_count_372, efficient_time_372])
        print(f"Merge-based n={size_372:>7} inversions={efficient_count_372} time={efficient_time_372:.6f}s")

        if not brute_stopped_372:
            start_372 = time.perf_counter()
            brute_count_372 = brute_force_inversions_372(data_372)
            brute_time_372 = time.perf_counter() - start_372
            rows_372.append(["Brute force", size_372, brute_count_372, brute_time_372])
            print(f"Brute force n={size_372:>7} inversions={brute_count_372} time={brute_time_372:.6f}s")
            assert brute_count_372 == efficient_count_372
            if brute_time_372 > 60:
                brute_stopped_372 = True
                print("Brute force exceeded 60 seconds; it will not be run for larger arrays.")
    with (output_dir_372 / "q3_results.csv").open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow(["algorithm", "n", "inversions", "time_seconds"])
        writer_372.writerows(rows_372)
    print(f"\nSaved results to: {output_dir_372 / 'q3_results.csv'}")


if __name__ == "__main__":
    verify_random_arrays_372()
    benchmark_372()
    print("\nKendall tau distance calculator (10 movies)")
    ranking_a_372 = read_ranking_372("User A")
    ranking_b_372 = read_ranking_372("User B")
    distance_372 = kendall_tau_distance_372(ranking_a_372, ranking_b_372)
    maximum_372 = 10 * 9 // 2
    print(f"Kendall tau distance: {distance_372} discordant pairs out of {maximum_372}")
    print(f"Normalized distance: {distance_372 / maximum_372:.4f}")
