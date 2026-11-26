from Lab4_Q9_NaiveMatrixExponentiation_372 import NaiveMatrixExponentiation_372
from Lab4_Q10_BinaryMatrixExponentiation_372 import BinaryMatrixExponentiation_372

if __name__ == "__main__":
    matrices_372 = [[[1, 1], [1, 0]], [[2, 1], [1, 1]]]
    for matrix_372 in matrices_372:
        for exponent_372, modulus_372 in [(0, 7), (5, 100), (8, 13)]:
            naive_372 = NaiveMatrixExponentiation_372(matrix_372, exponent_372, modulus_372)
            binary_372 = BinaryMatrixExponentiation_372(matrix_372, exponent_372, modulus_372)
            print(f"Matrix={matrix_372}, exponent={exponent_372}, modulus={modulus_372}, match={naive_372 == binary_372}")
