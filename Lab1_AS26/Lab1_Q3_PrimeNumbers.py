import time

# Input sizes
sizes_372 = [10000, 50000, 100000, 500000, 1000000]


# Naive Prime Checking using Trial Division
def naive_prime_372(number_372):
    if number_372 < 2:
        return False

    for i_372 in range(2, number_372):
        if number_372 % i_372 == 0:
            return False

    return True


# Optimized Trial Division
def optimized_prime_372(number_372):
    if number_372 < 2:
        return False

    i_372 = 2

    while i_372 * i_372 <= number_372:
        if number_372 % i_372 == 0:
            return False

        i_372 += 1

    return True


# Sieve of Eratosthenes
def sieve_372(number_372):
    prime_372 = [True] * (number_372 + 1)

    prime_372[0] = False
    prime_372[1] = False

    i_372 = 2

    while i_372 * i_372 <= number_372:

        if prime_372[i_372]:
            for j_372 in range(i_372 * i_372, number_372 + 1, i_372):
                prime_372[j_372] = False

        i_372 += 1

    return prime_372


# Testing each input size
for size_372 in sizes_372:

    # Naive Prime Checking
    start_372 = time.time()

    for number_372 in range(2, size_372 + 1):
        naive_prime_372(number_372)

    end_372 = time.time()

    naive_time_372 = end_372 - start_372


    # Optimized Trial Division
    start_372 = time.time()

    for number_372 in range(2, size_372 + 1):
        optimized_prime_372(number_372)

    end_372 = time.time()

    optimized_time_372 = end_372 - start_372


    # Sieve of Eratosthenes
    start_372 = time.time()

    sieve_372(size_372)

    end_372 = time.time()

    sieve_time_372 = end_372 - start_372


    # Results
    print("Input size:", size_372)
    print("Naive Trial Division:", naive_time_372)
    print("Optimized Trial Division:", optimized_time_372)
    print("Sieve of Eratosthenes:", sieve_time_372)
    print("-----------------------------")