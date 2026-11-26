# Lab 3 — Analysis and Step/Frequency Counts


This report summarizes the algorithms, the measured output shown in the submitted screenshots, and the step/comparison counts. Execution times are from one run on the computer used for the screenshots, so they may change on another run or computer.

## Q1: Matrix Multiplication — Traditional vs Strassen

### Algorithm comparison

| Algorithm | How it works | Time complexity |
|---|---|---|
| Traditional multiplication | Uses three nested loops to calculate each result cell. | \(O(n^3)\) |
| Strassen's algorithm | Divides each matrix into smaller parts and uses seven recursive multiplications per split. | \(O(n^{\log_2 7}) ~ O(n^{2.807})\) |

### Result and measured time

For the screenshot test, both input matrices were \(2 \times 2\).

| Measurement | Result |
|---|---:|
| Matrix size | \(2 \times 2\) |
| Traditional execution time | 0.000014 seconds |
| Strassen execution time | 0.000102 seconds |
| Do the results match? | Yes (`True`) |

Both methods produced the same result matrix:

```text
[90, 70]
[67, 54]
```

For this small input, traditional multiplication was faster. Strassen has more recursive calls and extra matrix additions/subtractions, so its overhead can make it slower for small matrices. Its lower asymptotic complexity is more useful for sufficiently large matrices. More sizes should be tested to compare the trend.

## Q2: Large Integer Multiplication — Traditional vs Karatsuba

### Algorithm comparison

| Algorithm | How it works | Time complexity |
|---|---|---|
| Traditional multiplication | Multiplies each digit of one number by each digit of the other. | \(O(n^2)\) |
| Karatsuba's algorithm | Splits each number into high and low parts and uses three recursive multiplications per split. | \(O(n^{\log_2 3}) \approx O(n^{1.585})\) |

### Result and measured time

The screenshot test used two randomly generated **32-digit** numbers.

| Measurement | Result |
|---|---:|
| Digits in each input | 32 |
| Traditional execution time | 0.000178 seconds |
| Karatsuba execution time | 0.000739 seconds |
| Do the results match? | Yes (`True`) |

Both methods returned the same product. In this run, traditional multiplication was faster, even though Karatsuba has a better asymptotic time complexity. Recursive function calls and conversion between strings and integers add overhead, especially for inputs of only 32 digits. Testing larger digit counts would help show where Karatsuba may become faster.

## Q3: Binary Search vs Ternary Search

### Algorithm comparison

| Algorithm | Search approach | Time complexity |
|---|---|---|
| Binary search | Checks the middle item and keeps half of the remaining search range. | \(O(\log_2 n)\) |
| Ternary search | Checks two positions and keeps approximately one third of the remaining range. | \(O(\log_3 n)\) levels |

Both algorithms require a sorted array. The program records comparisons between the search key and array values. Ternary search reduces the range more per iteration, but it can make two comparisons in an iteration.

### Observed best-case demonstration

For the generated array shown in the screenshot, menu option 5 reported:

| Search algorithm | Comparisons reported |
|---|---:|
| Binary search | 5 |
| Ternary search | 3 |

This menu option searches for the first value in the array. It is the program's best-case demonstration, but it is not guaranteed to be the mathematical best case for both algorithms because the first value is not necessarily the first middle position checked.

### Observed absent-key test

Menu option 6 searches for `-1`, which is absent from the generated non-negative array.

| Search algorithm | Comparisons reported |
|---|---:|
| Binary search | 6 |
| Ternary search | 4 |

These are the counts shown for that particular generated array. An absent key is a useful unsuccessful-search test, although the exact worst-case count depends on the array length and the comparison-counting method.

### Comparison table for increasing input sizes

The screenshot from menu option 7 shows the following counts for absent-key searches on arrays of increasing size.

| Array size (\(n\)) | Binary search comparisons | Ternary search comparisons |
|---:|---:|---:|
| 8 | 6 | 4 |
| 16 | 8 | 6 |
| 32 | 10 | 6 |
| 64 | 12 | 8 |
| 128 | 14 | 10 |
| 256 | 16 | 10 |

The counts increase slowly as the array becomes larger, which is consistent with logarithmic search algorithms. In this implementation, ternary search uses fewer comparisons in the displayed absent-key tests. However, the result can vary depending on the key, array size, and how comparisons are counted; neither algorithm should be declared faster based only on one table.

### Recurrence relations

- **Binary search:** `T(n) = T(n/2) + O(1)`, giving \(O(\log n)\) time.
- **Ternary search:** `T(n) = T(n/3) + O(1)` levels, giving \(O(\log n)\) time. Each iteration may check two middle positions, so its comparison cost per iteration is higher.

## Overall conclusion

The programs verify that traditional and Strassen matrix multiplication return the same matrix, and that traditional and Karatsuba multiplication return the same large-integer product. The screenshots show that the traditional methods were faster for the tested \(2 \times 2\) matrix and 32-digit multiplication, mainly because the inputs were small and the recursive methods have extra overhead. The search experiment shows that both binary and ternary search scale logarithmically, while their comparison counts differ because they inspect the array differently. Further runs with larger matrix sizes and longer numbers would give a fairer performance comparison.
