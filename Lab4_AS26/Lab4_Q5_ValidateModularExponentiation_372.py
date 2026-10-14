def ValidatedModularExponentiation_372(a_372, b_372, m_372):
    if not all(isinstance(value_372, int) for value_372 in (a_372, b_372, m_372)):
        raise ValueError("Enter whole numbers only.")
    if b_372 < 0:
        raise ValueError("Negative exponents are not supported.")
    if m_372 <= 0:
        raise ValueError("Modulus must be a positive integer.")
    result_372 = 1 % m_372
    a_372 %= m_372
    while b_372 > 0:
        if b_372 & 1:
            result_372 = (result_372 * a_372) % m_372
        a_372 = (a_372 * a_372) % m_372
        b_372 >>= 1
    return result_372

if __name__ == "__main__":
    try:
        a_372 = int(input("Enter base (negative bases are allowed): "))
        b_372 = int(input("Enter exponent (zero is allowed): "))
        m_372 = int(input("Enter positive modulus: "))
        print("Result:", ValidatedModularExponentiation_372(a_372, b_372, m_372))
    except ValueError as error_372:
        print("Input error:", error_372)
