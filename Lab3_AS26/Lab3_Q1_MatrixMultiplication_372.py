"""
Lab 3 - Q1: Traditional vs Strassen Matrix Multiplication
Student suffix: 372

Analysis/Conclusion:
Traditional multiplication uses O(n^3) time. Strassen uses about O(n^2.807).
The program checks that both methods return the same result and prints timings.
"""

import random as random_372
import time as time_372


def add_matrix_372(matrix_a_372, matrix_b_372):
    size_372 = len(matrix_a_372)
    return [[matrix_a_372[row_372][col_372] + matrix_b_372[row_372][col_372]
             for col_372 in range(size_372)] for row_372 in range(size_372)]


def subtract_matrix_372(matrix_a_372, matrix_b_372):
    size_372 = len(matrix_a_372)
    return [[matrix_a_372[row_372][col_372] - matrix_b_372[row_372][col_372]
             for col_372 in range(size_372)] for row_372 in range(size_372)]


def traditional_multiply_372(matrix_a_372, matrix_b_372):
    size_372 = len(matrix_a_372)
    result_372 = [[0 for col_372 in range(size_372)] for row_372 in range(size_372)]
    for row_372 in range(size_372):
        for col_372 in range(size_372):
            for inner_372 in range(size_372):
                result_372[row_372][col_372] += (
                    matrix_a_372[row_372][inner_372] * matrix_b_372[inner_372][col_372]
                )
    return result_372


def strassen_multiply_372(matrix_a_372, matrix_b_372):
    size_372 = len(matrix_a_372)
    if size_372 == 1:
        return [[matrix_a_372[0][0] * matrix_b_372[0][0]]]

    half_372 = size_372 // 2
    a11_372 = [row_372[:half_372] for row_372 in matrix_a_372[:half_372]]
    a12_372 = [row_372[half_372:] for row_372 in matrix_a_372[:half_372]]
    a21_372 = [row_372[:half_372] for row_372 in matrix_a_372[half_372:]]
    a22_372 = [row_372[half_372:] for row_372 in matrix_a_372[half_372:]]
    b11_372 = [row_372[:half_372] for row_372 in matrix_b_372[:half_372]]
    b12_372 = [row_372[half_372:] for row_372 in matrix_b_372[:half_372]]
    b21_372 = [row_372[:half_372] for row_372 in matrix_b_372[half_372:]]
    b22_372 = [row_372[half_372:] for row_372 in matrix_b_372[half_372:]]

    p1_372 = strassen_multiply_372(add_matrix_372(a11_372, a22_372), add_matrix_372(b11_372, b22_372))
    p2_372 = strassen_multiply_372(add_matrix_372(a21_372, a22_372), b11_372)
    p3_372 = strassen_multiply_372(a11_372, subtract_matrix_372(b12_372, b22_372))
    p4_372 = strassen_multiply_372(a22_372, subtract_matrix_372(b21_372, b11_372))
    p5_372 = strassen_multiply_372(add_matrix_372(a11_372, a12_372), b22_372)
    p6_372 = strassen_multiply_372(subtract_matrix_372(a21_372, a11_372), add_matrix_372(b11_372, b12_372))
    p7_372 = strassen_multiply_372(subtract_matrix_372(a12_372, a22_372), add_matrix_372(b21_372, b22_372))

    c11_372 = add_matrix_372(subtract_matrix_372(add_matrix_372(p1_372, p4_372), p5_372), p7_372)
    c12_372 = add_matrix_372(p3_372, p5_372)
    c21_372 = add_matrix_372(p2_372, p4_372)
    c22_372 = add_matrix_372(add_matrix_372(subtract_matrix_372(p1_372, p2_372), p3_372), p6_372)

    top_372 = [c11_372[row_372] + c12_372[row_372] for row_372 in range(half_372)]
    bottom_372 = [c21_372[row_372] + c22_372[row_372] for row_372 in range(half_372)]
    return top_372 + bottom_372


def main_372():
    size_372 = int(input("Enter matrix size (power of 2, e.g. 2, 4, 8, 16): "))
    if size_372 < 1 or (size_372 & (size_372 - 1)) != 0:
        print("Please enter a positive power of 2.")
        return

    matrix_a_372 = [[random_372.randint(1, 9) for col_372 in range(size_372)] for row_372 in range(size_372)]
    matrix_b_372 = [[random_372.randint(1, 9) for col_372 in range(size_372)] for row_372 in range(size_372)]

    start_372 = time_372.perf_counter()
    traditional_result_372 = traditional_multiply_372(matrix_a_372, matrix_b_372)
    traditional_time_372 = time_372.perf_counter() - start_372

    start_372 = time_372.perf_counter()
    strassen_result_372 = strassen_multiply_372(matrix_a_372, matrix_b_372)
    strassen_time_372 = time_372.perf_counter() - start_372

    print("\\nMatrix A:")
    for row_372 in matrix_a_372:
        print(row_372)
    print("\\nMatrix B:")
    for row_372 in matrix_b_372:
        print(row_372)
    print("\\nTraditional result:")
    for row_372 in traditional_result_372:
        print(row_372)
    print("\\nStrassen result:")
    for row_372 in strassen_result_372:
        print(row_372)
    print("\\nResults match:", traditional_result_372 == strassen_result_372)
    print(f"Traditional time: {traditional_time_372:.6f} seconds")
    print(f"Strassen time:    {strassen_time_372:.6f} seconds")


if __name__ == "__main__":
    main_372()
