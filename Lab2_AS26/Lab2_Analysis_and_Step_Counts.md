# Lab 2: Analysis and Step/Frequency Counts

## Q1: Prime Number Testing

The program was tested with the 10 numbers shown in `Screenshots/Q1.png`. The naive method checks divisors from 2 up to `n - 1`, while the optimized method checks divisors only up to the square root of the number.

| Number | Prime? | Naive steps | Optimized steps |
|---:|:---:|---:|---:|
| 3 | Yes | 1 | 0 |
| 7 | Yes | 5 | 1 |
| 54 | No | 1 | 1 |
| 6 | No | 1 | 1 |
| 8 | No | 1 | 1 |
| 3 | Yes | 1 | 0 |
| 5 | Yes | 3 | 1 |
| 7 | Yes | 5 | 1 |
| 10 | No | 1 | 1 |
| 34 | No | 1 | 1 |

**Analysis:** Both algorithms gave the same prime/non-prime result for all 10 inputs. The optimized method used fewer checks for the prime inputs in this test. For composite numbers, the number of checks depends on how soon a divisor is found.

| Method | Time complexity | Explanation |
|---|---|---|
| Naive method | O(n) | In the worst case, it checks possible divisors up to `n - 1`. |
| Optimized method | O(√n) | It only needs to check divisors up to the square root of `n`. |

**Conclusion:** The optimized method is more efficient for larger inputs because it avoids checking divisors beyond the square root. The graph saved in `Graphs/Lab2_Q1_PrimeTesting_Graph.png` compares the step counts for these inputs.

## Q2: Merge Sort Analysis

The program was tested using the menu options shown in `Screenshots/Q2.1.png` to `Screenshots/Q2.5.png`.

### Sorting result

The ascending sort screenshot shows the following sorted array:

`[6, 11, 24, 29, 40, 57, 63, 79, 82, 93]`

The merge comparison count for this sort was **21**.

### Step counts and execution times

| Experiment | Input size (n) | Merge comparisons (step count) | Execution time (seconds) |
|---|---:|---:|---:|
| Random data (option 5) | 10 | 24 | 0.00004630 |
| Already sorted data (option 6) | 7 | 10 | 0.00002090 |
| Descending-sorted data (option 7) | 4 | 4 | 0.00002150 |

*Note: Execution times are copied from the screenshots and may change between runs or computers. The experiments used different input sizes, so their times should not be compared as a perfectly controlled performance test.*

**Analysis:** Merge sort divides the array into smaller parts, sorts those parts, and merges them. Its expected time complexity is **O(n log n)** for random, already sorted, and descending-sorted input. The number of comparisons depends on the input values and input size. Option 4 uses selection sort to arrange an array in descending order; selection sort has **O(n²)** time complexity.

## Q3: Square Matrix Multiplication

The program was tested with two randomly generated 2 × 2 matrices, as shown in `Screenshots/Q3.png`.

**Matrix A**

| 7 | 5 |
|---:|---:|
| 5 | 6 |

**Matrix B**

| 7 | 5 |
|---:|---:|
| 7 | 3 |

**Resultant matrix (A × B)**

| 84 | 50 |
|---:|---:|
| 77 | 43 |

### Operation counts

| Matrix size | Multiplications | Additions | Total counted operations |
|---|---:|---:|---:|
| 2 × 2 (screenshot result) | 8 | 4 | 12 |
| 4 × 4 (theoretical count) | 64 | 48 | 112 |
| 8 × 8 (theoretical count) | 512 | 448 | 960 |

For an `n × n` matrix, standard matrix multiplication performs `n³` multiplications and `n²(n − 1)` additions. Therefore, the total counted operations in this program are `n³ + n²(n − 1)`, and the time complexity is **O(n³)**.

**Analysis:** The result matrix is calculated by multiplying each row of Matrix A by each column of Matrix B and adding the products. For the 2 × 2 example, the program counted 8 multiplications and 4 additions, giving 12 counted operations.

## Overall Conclusion

This lab compared naive and optimized prime testing, measured merge sort on different input types, and counted the operations used in square matrix multiplication. The results show that optimized prime testing reduces unnecessary divisor checks, merge sort has **O(n log n)** time complexity, and standard matrix multiplication has **O(n³)** time complexity. Execution times are small and can vary, so step counts are also useful for comparing algorithm performance.
