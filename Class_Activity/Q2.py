import random
import time

steps372 = 0


# Merge two parts
def merge372(a372, left372, mid372, right372):
    global steps372

    temp372 = []
    i372 = left372
    j372 = mid372 + 1

    while i372 <= mid372 and j372 <= right372:
        steps372 += 1

        if a372[i372] <= a372[j372]:
            temp372.append(a372[i372])
            i372 += 1
        else:
            temp372.append(a372[j372])
            j372 += 1

    while i372 <= mid372:
        temp372.append(a372[i372])
        i372 += 1
        steps372 += 1

    while j372 <= right372:
        temp372.append(a372[j372])
        j372 += 1
        steps372 += 1

    for i372 in range(len(temp372)):
        a372[left372 + i372] = temp372[i372]
        steps372 += 1


# Merge Sort
def merge_sort372(a372, left372, right372):
    if left372 < right372:

        mid372 = (left372 + right372) // 2

        merge_sort372(a372, left372, mid372)
        merge_sort372(a372, mid372 + 1, right372)

        merge372(a372, left372, mid372, right372)


# Descending sort
def descending_sort372(a372):
    global steps372

    n372 = len(a372)

    for i372 in range(n372):
        for j372 in range(i372 + 1, n372):

            steps372 += 1

            if a372[i372] < a372[j372]:
                a372[i372], a372[j372] = a372[j372], a372[i372]


# Generate random numbers
def generate_array372(n372):
    a372 = []

    for i372 in range(n372):
        a372.append(random.randint(1, 1000))

    return a372


# Main program
print("MERGE SORT ANALYSIS")
print("-------------------")

n372 = int(input("Enter number of elements: "))

a372 = []

while True:

    print("\nMENU")
    print("1. Generate random numbers")
    print("2. Display Array")
    print("3. Sort in Ascending Order using Merge Sort")
    print("4. Sort in Descending Order")
    print("5. Time Complexity for random data")
    print("6. Time Complexity for already sorted data")
    print("7. Time Complexity for descending data")
    print("8. Exit")

    choice372 = int(input("Enter your choice: "))

    # 1. Generate random numbers
    if choice372 == 1:

        a372 = generate_array372(n372)

        print("Random array generated.")

    # 2. Display array
    elif choice372 == 2:

        if len(a372) == 0:
            print("Please generate the array first.")
        else:
            print("Array:", a372)

    # 3. Merge Sort ascending
    elif choice372 == 3:

        if len(a372) == 0:
            print("Please generate the array first.")
        else:
            steps372 = 0

            merge_sort372(a372, 0, n372 - 1)

            print("Array sorted in ascending order.")
            print("Array:", a372)
            print("Step count:", steps372)

    # 4. Descending sort
    elif choice372 == 4:

        if len(a372) == 0:
            print("Please generate the array first.")
        else:
            steps372 = 0

            descending_sort372(a372)

            print("Array sorted in descending order.")
            print("Array:", a372)
            print("Step count:", steps372)

    # 5. Random data
    elif choice372 == 5:

        a372 = generate_array372(n372)

        steps372 = 0

        start372 = time.time()

        merge_sort372(a372, 0, n372 - 1)

        end372 = time.time()

        print("\nRandom Data")
        print("Steps:", steps372)
        print("Time:", end372 - start372, "seconds")

    # 6. Already sorted data
    elif choice372 == 6:

        a372 = list(range(1, n372 + 1))

        steps372 = 0

        start372 = time.time()

        merge_sort372(a372, 0, n372 - 1)

        end372 = time.time()

        print("\nAlready Sorted Data")
        print("Steps:", steps372)
        print("Time:", end372 - start372, "seconds")

    # 7. Descending data
    elif choice372 == 7:

        a372 = list(range(n372, 0, -1))

        steps372 = 0

        start372 = time.time()

        merge_sort372(a372, 0, n372 - 1)

        end372 = time.time()

        print("\nDescending Data")
        print("Steps:", steps372)
        print("Time:", end372 - start372, "seconds")

    # 8. Exit
    elif choice372 == 8:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")