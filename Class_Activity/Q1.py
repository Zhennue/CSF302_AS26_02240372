import time
import matplotlib.pyplot as plt

print("Prime Number Testing")
print("--------------------")

numbers372 = input("Enter at least 10 numbers separated by spaces: ").split()

naive_steps372 = []
optimized_steps372 = []

for n372 in numbers372:

    n372 = int(n372)

    # Naive Method
    steps_naive372 = 0
    start_naive372 = time.time()

    prime_naive372 = True

    if n372 < 2:
        prime_naive372 = False

    for i372 in range(2, n372):
        steps_naive372 += 1

        if n372 % i372 == 0:
            prime_naive372 = False
            break

    end_naive372 = time.time()


    # Optimized Method
    steps_opt372 = 0
    start_opt372 = time.time()

    prime_opt372 = True

    if n372 < 2:
        prime_opt372 = False

    i372 = 2

    while i372 * i372 <= n372:
        steps_opt372 += 1

        if n372 % i372 == 0:
            prime_opt372 = False
            break

        i372 += 1

    end_opt372 = time.time()


    # Save steps for graph
    naive_steps372.append(steps_naive372)
    optimized_steps372.append(steps_opt372)


    # Results
    print("\nNumber:", n372)

    if prime_naive372:
        print("Naive: Prime")
    else:
        print("Naive: Not Prime")

    print("Naive Steps:", steps_naive372)
    print("Naive Time:", end_naive372 - start_naive372)

    if prime_opt372:
        print("Optimized: Prime")
    else:
        print("Optimized: Not Prime")

    print("Optimized Steps:", steps_opt372)
    print("Optimized Time:", end_opt372 - start_opt372)

    print("--------------------")


# Graph
plt.plot(numbers372, naive_steps372, marker="o", label="Naive")
plt.plot(numbers372, optimized_steps372, marker="o", label="Optimized")

plt.xlabel("Input Numbers")
plt.ylabel("Number of Steps")
plt.title("Prime Number Testing: Naive vs Optimized")

plt.legend()
plt.grid()
plt.show()