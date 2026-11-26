from time import perf_counter
from Lab4_Q9_NaiveMatrixExponentiation_372 import NaiveMatrixExponentiation_372
from Lab4_Q10_BinaryMatrixExponentiation_372 import BinaryMatrixExponentiation_372

if __name__ == "__main__":
    modulus_372 = 1000003
    for size_372 in [2, 3, 4]:
        matrix_372 = [[row_372 + col_372 + 1 for col_372 in range(size_372)] for row_372 in range(size_372)]
        for exponent_372 in [10, 100, 500]:
            start_372 = perf_counter()
            naive_372 = NaiveMatrixExponentiation_372(matrix_372, exponent_372, modulus_372)
            naive_time_372 = perf_counter() - start_372
            start_372 = perf_counter()
            binary_372 = BinaryMatrixExponentiation_372(matrix_372, exponent_372, modulus_372)
            binary_time_372 = perf_counter() - start_372
            print(f"Size={size_372}, exponent={exponent_372}, match={naive_372 == binary_372}")
            print(f"  Naive: {naive_time_372:.6f}s; Binary: {binary_time_372:.6f}s")
