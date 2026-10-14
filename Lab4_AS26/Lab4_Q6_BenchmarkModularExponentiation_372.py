from time import perf_counter
from Lab4_Q1_NaiveModularExponentiation_372 import NaiveModularExponentiation_372
from Lab4_Q2_BinaryModularExponentiation_372 import BinaryModularExponentiation_372

if __name__ == "__main__":
    base_372, modulus_372 = 7, 1000003
    for exponent_372 in [1000, 10000, 100000, 500000]:
        start_372 = perf_counter()
        naive_372 = NaiveModularExponentiation_372(base_372, exponent_372, modulus_372)
        naive_time_372 = perf_counter() - start_372
        start_372 = perf_counter()
        binary_372 = BinaryModularExponentiation_372(base_372, exponent_372, modulus_372)
        binary_time_372 = perf_counter() - start_372
        print(f"Exponent {exponent_372}: results match = {naive_372 == binary_372}")
        print(f"  Naive: {naive_time_372:.6f} seconds")
        print(f"  Binary: {binary_time_372:.6f} seconds")
