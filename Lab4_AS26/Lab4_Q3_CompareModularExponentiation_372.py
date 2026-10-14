from Lab4_Q1_NaiveModularExponentiation_372 import NaiveModularExponentiation_372
from Lab4_Q2_BinaryModularExponentiation_372 import BinaryModularExponentiation_372

if __name__ == "__main__":
    cases_372 = [(2, 10, 7), (3, 15, 11), (5, 20, 13), (-2, 8, 9), (7, 0, 5)]
    for a_372, b_372, m_372 in cases_372:
        naive_372 = NaiveModularExponentiation_372(a_372, b_372, m_372)
        binary_372 = BinaryModularExponentiation_372(a_372, b_372, m_372)
        print(f"a={a_372}, b={b_372}, m={m_372}: naive={naive_372}, binary={binary_372}, match={naive_372 == binary_372}")
