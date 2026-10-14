"""
Lab 3 - Q2: Traditional vs Karatsuba Large Integer Multiplication
Student suffix: 372

Analysis/Conclusion:
Traditional digit multiplication takes O(n^2) time. Karatsuba takes about
O(n^1.585) time. Python integers are used for the final exact value, while
the inputs are accepted as strings to support very long numbers.
"""

import random as random_372
import time as time_372


def traditional_multiply_372(number_a_372, number_b_372):
    digits_a_372 = [int(digit_372) for digit_372 in number_a_372[::-1]]
    digits_b_372 = [int(digit_372) for digit_372 in number_b_372[::-1]]
    result_372 = [0] * (len(digits_a_372) + len(digits_b_372))

    for index_a_372, digit_a_372 in enumerate(digits_a_372):
        for index_b_372, digit_b_372 in enumerate(digits_b_372):
            result_372[index_a_372 + index_b_372] += digit_a_372 * digit_b_372

    for index_372 in range(len(result_372) - 1):
        result_372[index_372 + 1] += result_372[index_372] // 10
        result_372[index_372] %= 10

    while len(result_372) > 1 and result_372[-1] == 0:
        result_372.pop()
    return "".join(str(digit_372) for digit_372 in result_372[::-1])


def karatsuba_multiply_372(number_a_372, number_b_372):
    number_a_372 = str(int(number_a_372))
    number_b_372 = str(int(number_b_372))
    if len(number_a_372) == 1 or len(number_b_372) == 1:
        return str(int(number_a_372) * int(number_b_372))

    size_372 = max(len(number_a_372), len(number_b_372))
    if size_372 % 2 == 1:
        size_372 += 1
    number_a_372 = number_a_372.zfill(size_372)
    number_b_372 = number_b_372.zfill(size_372)
    half_372 = size_372 // 2

    high_a_372, low_a_372 = number_a_372[:-half_372], number_a_372[-half_372:]
    high_b_372, low_b_372 = number_b_372[:-half_372], number_b_372[-half_372:]

    product_high_372 = int(karatsuba_multiply_372(high_a_372, high_b_372))
    product_low_372 = int(karatsuba_multiply_372(low_a_372, low_b_372))
    product_middle_372 = int(karatsuba_multiply_372(str(int(high_a_372) + int(low_a_372)),
                                                     str(int(high_b_372) + int(low_b_372))))
    combined_372 = (
        product_high_372 * (10 ** (2 * half_372))
        + (product_middle_372 - product_high_372 - product_low_372) * (10 ** half_372)
        + product_low_372
    )
    return str(combined_372)


def make_number_372(digit_count_372):
    first_digit_372 = str(random_372.randint(1, 9))
    remaining_372 = "".join(str(random_372.randint(0, 9)) for _ in range(digit_count_372 - 1))
    return first_digit_372 + remaining_372


def main_372():
    digit_count_372 = int(input("Enter digit count (e.g. 8, 16, 32, 64, 128): "))
    if digit_count_372 < 1:
        print("Digit count must be positive.")
        return

    number_a_372 = make_number_372(digit_count_372)
    number_b_372 = make_number_372(digit_count_372)
    print("\\nNumber A:", number_a_372)
    print("Number B:", number_b_372)

    start_372 = time_372.perf_counter()
    traditional_result_372 = traditional_multiply_372(number_a_372, number_b_372)
    traditional_time_372 = time_372.perf_counter() - start_372

    start_372 = time_372.perf_counter()
    karatsuba_result_372 = karatsuba_multiply_372(number_a_372, number_b_372)
    karatsuba_time_372 = time_372.perf_counter() - start_372

    print("\\nTraditional result:", traditional_result_372)
    print("Karatsuba result:  ", karatsuba_result_372)
    print("Results match:", traditional_result_372 == karatsuba_result_372)
    print(f"Traditional time: {traditional_time_372:.6f} seconds")
    print(f"Karatsuba time:   {karatsuba_time_372:.6f} seconds")


if __name__ == "__main__":
    main_372()
