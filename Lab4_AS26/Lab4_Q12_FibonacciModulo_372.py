from Lab4_Q10_BinaryMatrixExponentiation_372 import BinaryMatrixExponentiation_372

def FibonacciModulo_372(n_372, modulus_372):
    if n_372 < 0 or modulus_372 <= 0:
        raise ValueError("n must be non-negative and modulus positive.")
    result_372 = BinaryMatrixExponentiation_372([[1, 1], [1, 0]], n_372, modulus_372)
    return result_372[0][1]

if __name__ == "__main__":
    print("Fibonacci(10) mod 100 =", FibonacciModulo_372(10, 100))
