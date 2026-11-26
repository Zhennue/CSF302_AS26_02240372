# Lab 2 - Q3: Square Matrix Multiplication
# Matrices must have power-of-two dimensions (2, 4, 8, 16, ...).
# Conclusion: Standard matrix multiplication uses n^3 multiply operations and
# approximately n^3 additions for an n x n matrix, so its time complexity is O(n^3).

import random


def IsPowerOfTwo_372(number_372):
    return number_372 > 0 and (number_372 & (number_372 - 1)) == 0


def MultiplyMatrices_372(matrix_a_372, matrix_b_372):
    size_372 = len(matrix_a_372)
    result_372 = [[0 for column_372 in range(size_372)] for row_372 in range(size_372)]
    multiply_count_372 = 0
    addition_count_372 = 0

    for row_372 in range(size_372):
        for column_372 in range(size_372):
            total_372 = 0
            for inner_372 in range(size_372):
                total_372 += matrix_a_372[row_372][inner_372] * matrix_b_372[inner_372][column_372]
                multiply_count_372 += 1
                if inner_372 > 0:
                    addition_count_372 += 1
            result_372[row_372][column_372] = total_372

    return result_372, multiply_count_372, addition_count_372


def ReadMatrix_372(size_372, matrix_name_372):
    matrix_372 = []
    print(f"Enter values for {matrix_name_372}, one row at a time.")
    print(f"Enter {size_372} integers per row, separated by spaces.")
    for row_372 in range(size_372):
        while True:
            try:
                values_372 = [int(value_372) for value_372 in input(f"Row {row_372 + 1}: ").split()]
                if len(values_372) != size_372:
                    print(f"Please enter exactly {size_372} values.")
                    continue
                matrix_372.append(values_372)
                break
            except ValueError:
                print("Use integers separated by spaces.")
    return matrix_372


def PrintMatrix_372(matrix_372):
    for row_372 in matrix_372:
        print(" ".join(f"{value_372:5}" for value_372 in row_372))


def Main_372():
    print("Lab 2 Q3 - Square Matrix Multiplication")
    while True:
        try:
            size_372 = int(input("Enter matrix size (2, 4, 8, 16, ...): "))
            if IsPowerOfTwo_372(size_372) and size_372 >= 2:
                break
            print("Size must be a power of 2 and at least 2.")
        except ValueError:
            print("Please enter a valid integer.")

    choice_372 = input("Enter M to input matrices manually or R for random matrices: ").strip().upper()
    if choice_372 == "M":
        matrix_a_372 = ReadMatrix_372(size_372, "Matrix A")
        matrix_b_372 = ReadMatrix_372(size_372, "Matrix B")
    else:
        matrix_a_372 = [[random.randint(1, 9) for column_372 in range(size_372)] for row_372 in range(size_372)]
        matrix_b_372 = [[random.randint(1, 9) for column_372 in range(size_372)] for row_372 in range(size_372)]

    print("\nMatrix A:")
    PrintMatrix_372(matrix_a_372)
    print("\nMatrix B:")
    PrintMatrix_372(matrix_b_372)

    result_372, multiply_count_372, addition_count_372 = MultiplyMatrices_372(matrix_a_372, matrix_b_372)
    print("\nResultant Matrix (A x B):")
    PrintMatrix_372(result_372)
    print("\nOperation counts:")
    print("Multiplications:", multiply_count_372)
    print("Additions:", addition_count_372)
    print("Total counted operations:", multiply_count_372 + addition_count_372)
    print(f"Time complexity: O(n^3), where n = {size_372}.")


if __name__ == "__main__":
    Main_372()
