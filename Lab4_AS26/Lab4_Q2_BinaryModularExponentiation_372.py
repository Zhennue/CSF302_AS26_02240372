def BinaryModularExponentiation_372(a_372, b_372, m_372):
    if b_372 < 0 or m_372 <= 0:
        raise ValueError("Exponent must be non-negative and modulus must be positive.")
    result_372 = 1 % m_372
    a_372 %= m_372
    while b_372 > 0:
        if b_372 & 1:
            result_372 = (result_372 * a_372) % m_372
        a_372 = (a_372 * a_372) % m_372
        b_372 >>= 1
    return result_372

if __name__ == "__main__":
    print("2^10 mod 7 =", BinaryModularExponentiation_372(2, 10, 7))
