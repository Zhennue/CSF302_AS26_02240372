# Assignment 4: Booking the Hall

**Student number ending:** 372  
**AI tool statement:** I used OpenAI Codex to review the assignment requirements, implement and check the booking algorithms, and help prepare the analysis. I compared dynamic programming with brute force on 500 random inputs and ran the requested greedy-ratio experiment.

## Greedy counterexamples

### Earliest-finish rule

Requests: `[(0, 4, 12), (0, 2, 5), (2, 4, 5)]`.

Earliest finish chooses request indices `[1, 2]`, earning `10`. The optimal schedule chooses index `[0]`, earning `12`. The rule maximizes the number of compatible events, but the longer event pays more than the two short events combined.

### Highest-fee rule

Requests: `[(0, 3, 10), (0, 1, 6), (1, 3, 6)]`.

Highest fee chooses index `[0]`, earning `10`. The optimal schedule chooses `[1, 2]`, earning `12`. Choosing the single highest fee first blocks two compatible requests whose combined fee is greater.

## Why the dynamic-programming recurrence works

Sort requests by finish time. For a request `j`, let `p(j)` be the number of earlier sorted requests that finish no later than `j` starts. An optimal schedule either leaves out `j`, earning `OPT(j - 1)`, or includes it. If it includes `j`, all other selected requests must finish by its start, so their best possible fee is `OPT(p(j))`. Therefore:

```text
OPT(0) = 0
OPT(j) = max(OPT(j - 1), fee_j + OPT(p(j)))
```

The two cases cover every possible optimal schedule. The DP records which choice wins and follows those choices backward to recover original request indices.

## Revenue-ratio experiment

I generated 1,000 seeded random inputs, each with 50 requests. Start times ranged from 0 to 100, durations from 1 to 20, and fees from 100 to 10,000. For each input, I divided each greedy rule's revenue by the optimal dynamic-programming revenue.

| Rule | Average ratio | Worst ratio |
|---|---:|---:|
| Earliest finish | 0.7990 | 0.4481 |
| Highest fee | 0.8709 | 0.5296 |

The highest-fee rule earned more on average in this sample, but neither greedy rule always earned the maximum. The ratios are empirical results from these generated inputs, not guarantees for every set of bookings. Full results are saved in `outputs/Greedy_Revenue_Ratios.csv`.

## Time complexity

| Function | Time complexity | Reason |
|---|---:|---|
| `greedy_earliest_finish_372` | `O(n log n)` | Sort requests, then scan once. |
| `greedy_highest_fee_372` | `O(n²)` | Sort, then check each request against the already accepted schedule. |
| `best_schedule_372` | `O(n log n)` | Sort once, then find each predecessor by binary search and fill the DP table. |
| `brute_force_372` | `O(2ⁿ n log n)` | Enumerate subsets and sort/check each subset; intended only for `n ≤ 15`. |

## Critical reflection

Passing tests does not prove that a greedy rule is correct. Tests check selected cases, and a rule can appear successful until an input exposes the choice that blocks a better combination. The small counterexamples were useful because they show exactly how each local choice can lose revenue.

The manager could use earliest finish when all fees are equal, because selecting the largest number of compatible events then also maximizes total fees. When fees differ, the 1,000-input experiment found average revenue ratios of 0.7990 for earliest finish and 0.8709 for highest fee, with worst ratios of 0.4481 and 0.5296. Those results suggest highest fee did better on this sample, but both rules can give up a large share of the optimum. For revenue decisions, the DP algorithm is the reliable choice.

Codex helped draft and review the implementation. I checked its output against brute force on 500 seeded random inputs, tested the listed edge cases and equal-fee property, and confirmed the supplied sample. The counterexamples and revenue ratios provide additional checks beyond ordinary passing cases.
