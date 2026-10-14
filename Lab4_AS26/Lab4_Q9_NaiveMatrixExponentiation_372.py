from Lab4_Q7_MatrixMultiplicationModulo_372 import MatrixMultiplicationModulo_372
from Lab4_Q8_IdentityMatrix_372 import IdentityMatrix_372

def NaiveMatrixExponentiation_372(matrix_372, exponent_372, modulus_372):
    if exponent_372 < 0 or modulus_372 <= 0:
        raise ValueError("Exponent must be non-negative and modulus positive.")
    result_372 = IdentityMatrix_372(len(matrix_372))
    for _372 in range(exponent_372):
        result_372 = MatrixMultiplicationModulo_372(result_372, matrix_372, modulus_372)
    return result_372

if __name__ == "__main__":
    print(NaiveMatrixExponentiation_372([[1, 1], [1, 0]], 5, 100))
