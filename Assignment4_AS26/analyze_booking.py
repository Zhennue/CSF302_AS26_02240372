import csv
import random
from pathlib import Path

from booking import (
    best_schedule_372,
    greedy_earliest_finish_372,
    greedy_highest_fee_372,
)


def make_random_requests_372(random_generator_372, count_372):
    requests_372 = []
    for _372 in range(count_372):
        start_372 = random_generator_372.randint(0, 100)
        finish_372 = random_generator_372.randint(start_372 + 1,
                                                   start_372 + 20)
        fee_372 = random_generator_372.randint(100, 10000)
        requests_372.append((start_372, finish_372, fee_372))
    return requests_372


def main_372():
    counterexamples_372 = {
        "Earliest finish": [(0, 4, 12), (0, 2, 5), (2, 4, 5)],
        "Highest fee": [(0, 3, 10), (0, 1, 6), (1, 3, 6)],
    }
    print("Small counterexamples:")
    for rule_372, requests_372 in counterexamples_372.items():
        optimal_372 = best_schedule_372(requests_372)
        if rule_372 == "Earliest finish":
            greedy_372 = greedy_earliest_finish_372(requests_372)
        else:
            greedy_372 = greedy_highest_fee_372(requests_372)
        print(f"{rule_372}: requests={requests_372}")
        print(f"  greedy={greedy_372}; optimal={optimal_372}")

    random_generator_372 = random.Random(372)
    ratio_totals_372 = {"Earliest finish": 0.0, "Highest fee": 0.0}
    ratio_worst_372 = {"Earliest finish": 1.0, "Highest fee": 1.0}
    worst_case_372 = {"Earliest finish": None, "Highest fee": None}
    trial_count_372 = 1000

    for trial_372 in range(trial_count_372):
        requests_372 = make_random_requests_372(random_generator_372, 50)
        optimal_fee_372 = best_schedule_372(requests_372)[0]
        for rule_372, rule_function_372 in [
            ("Earliest finish", greedy_earliest_finish_372),
            ("Highest fee", greedy_highest_fee_372),
        ]:
            greedy_fee_372 = rule_function_372(requests_372)[0]
            ratio_372 = greedy_fee_372 / optimal_fee_372
            ratio_totals_372[rule_372] += ratio_372
            if ratio_372 < ratio_worst_372[rule_372]:
                ratio_worst_372[rule_372] = ratio_372
                worst_case_372[rule_372] = trial_372

    output_folder_372 = Path(__file__).parent / "outputs"
    output_folder_372.mkdir(exist_ok=True)
    output_path_372 = output_folder_372 / "Greedy_Revenue_Ratios.csv"
    with output_path_372.open("w", newline="", encoding="utf-8") as file_372:
        writer_372 = csv.writer(file_372)
        writer_372.writerow([
            "Rule", "Trials", "Average revenue ratio", "Worst revenue ratio",
            "Worst trial"
        ])
        for rule_372 in ratio_totals_372:
            average_372 = ratio_totals_372[rule_372] / trial_count_372
            print(f"{rule_372}: average={average_372:.4f}, "
                  f"worst={ratio_worst_372[rule_372]:.4f} "
                  f"(trial {worst_case_372[rule_372]})")
            writer_372.writerow([
                rule_372, trial_count_372, f"{average_372:.8f}",
                f"{ratio_worst_372[rule_372]:.8f}", worst_case_372[rule_372]
            ])
    print("Saved", output_path_372)


if __name__ == "__main__":
    main_372()
