# Assignment 4: Program Output

This page records the example output and the results from the tests and analysis script. The full explanation is in `Assignment4_Analysis_And_Reflection.md`.

## Example booking schedule

Run `booking.py` to compare the two greedy rules with dynamic programming:

```text
Requests: [(9, 12, 3000), (10, 16, 8000), (13, 17, 4000), (12, 14, 2500), (16, 18, 2000)]
Earliest finish: (7500, [0, 3, 4])
Highest fee: (10000, [1, 4])
Dynamic programming: (10000, [1, 4])
```

## Tests

`test_booking.py` checks the required edge cases, the sample and counterexamples, 500 random inputs against brute force, and the equal-fee property. All ten tests pass.

## Counterexamples and revenue ratios

Run `analyze_booking.py` to print the small counterexamples and compare both greedy rules with the optimal dynamic-programming result over 1,000 generated sets of 50 requests. The average and worst ratios are saved in `outputs/Greedy_Revenue_Ratios.csv` and summarized in the analysis report.
