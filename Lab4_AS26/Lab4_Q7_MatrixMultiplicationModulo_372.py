def MatrixMultiplicationModulo_372(matrix_a_372, matrix_b_372, modulus_372):
    if modulus_372 <= 0:
        raise ValueError("Modulus must be positive.")
    size_372 = len(matrix_a_372)
    if size_372 == 0 or len(matrix_b_372) != size_372:
        raise ValueError("Matrices must be non-empty square matrices of the same size.")
    if any(len(row_372) != size_372 for row_372 in matrix_a_372 + matrix_b_372):
        raise ValueError("Matrices must be square.")
    result_372 = [[0 for _372 in range(size_372)] for _372 in range(size_372)]
    for row_372 in range(size_372):
        for col_372 in range(size_372):
            for inner_372 in range(size_372):
                result_372[row_372][col_372] += matrix_a_372[row_372][inner_372] * matrix_b_372[inner_372][col_372]
            result_372[row_372][col_372] %= modulus_372
    return result_372

if __name__ == "__main__":
    print(MatrixMultiplicationModulo_372([[1, 2], [3, 4]], [[5, 6], [7, 8]], 10))
