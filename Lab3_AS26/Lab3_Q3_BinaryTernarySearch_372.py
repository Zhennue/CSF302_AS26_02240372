"""
Lab 3 - Q3: Menu-driven Binary Search vs Ternary Search
Student suffix: 372

Analysis/Conclusion:
Binary search follows T(n)=T(n/2)+O(1), so it needs O(log2 n) comparisons.
Ternary search follows T(n)=T(n/3)+O(1), so it needs O(log3 n) levels,
but each level can make more comparisons. The measured counts show the actual
comparison count for the selected array and key.
"""

import random as random_372


def binary_search_372(array_372, key_372):
    left_372 = 0
    right_372 = len(array_372) - 1
    comparisons_372 = 0
    while left_372 <= right_372:
        middle_372 = (left_372 + right_372) // 2
        comparisons_372 += 1
        if array_372[middle_372] == key_372:
            return middle_372, comparisons_372
        comparisons_372 += 1
        if array_372[middle_372] < key_372:
            left_372 = middle_372 + 1
        else:
            right_372 = middle_372 - 1
    return -1, comparisons_372


def ternary_search_372(array_372, key_372):
    left_372 = 0
    right_372 = len(array_372) - 1
    comparisons_372 = 0
    while left_372 <= right_372:
        third_372 = (right_372 - left_372) // 3
        middle_one_372 = left_372 + third_372
        middle_two_372 = right_372 - third_372

        comparisons_372 += 1
        if array_372[middle_one_372] == key_372:
            return middle_one_372, comparisons_372
        comparisons_372 += 1
        if array_372[middle_two_372] == key_372:
            return middle_two_372, comparisons_372

        if key_372 < array_372[middle_one_372]:
            right_372 = middle_one_372 - 1
        elif key_372 > array_372[middle_two_372]:
            left_372 = middle_two_372 + 1
        else:
            left_372 = middle_one_372 + 1
            right_372 = middle_two_372 - 1
    return -1, comparisons_372


def show_counts_372(array_372):
    print("\\nn | Binary worst comparisons | Ternary worst comparisons")
    print("-" * 52)
    for size_372 in [8, 16, 32, 64, 128, 256]:
        test_array_372 = list(range(0, size_372 * 2, 2))
        binary_position_372, binary_count_372 = binary_search_372(test_array_372, -1)
        ternary_position_372, ternary_count_372 = ternary_search_372(test_array_372, -1)
        print(f"{size_372:3} | {binary_count_372:23} | {ternary_count_372:24}")


def main_372():
    array_372 = []
    while True:
        print("\\n--- SEARCH MENU ---")
        print("1. Generate n sorted random numbers")
        print("2. Display array")
        print("3. Search using Binary Search")
        print("4. Search using Ternary Search")
        print("5. Show best-case counts")
        print("6. Show worst-case counts (key absent)")
        print("7. Comparison table for increasing n")
        print("8. Exit")
        choice_372 = input("Choose an option: ").strip()

        if choice_372 == "1":
            size_372 = int(input("Enter n: "))
            if size_372 < 1:
                print("n must be positive.")
                continue
            array_372 = sorted(random_372.sample(range(0, size_372 * 10), size_372))
            print("Array generated.")
        elif choice_372 == "2":
            print(array_372 if array_372 else "Generate an array first.")
        elif choice_372 in ("3", "4"):
            if not array_372:
                print("Generate an array first.")
                continue
            key_372 = int(input("Enter key to search: "))
            if choice_372 == "3":
                position_372, count_372 = binary_search_372(array_372, key_372)
                method_372 = "Binary"
            else:
                position_372, count_372 = ternary_search_372(array_372, key_372)
                method_372 = "Ternary"
            if position_372 == -1:
                print(f"{method_372} Search: key not found.")
            else:
                print(f"{method_372} Search: key found at index {position_372}.")
            print("Number of comparisons:", count_372)
        elif choice_372 == "5":
            if not array_372:
                print("Generate an array first.")
                continue
            key_372 = array_372[0]
            print("Best case uses the first checked middle element.")
            print("Binary:", binary_search_372(array_372, key_372)[1], "comparisons")
            print("Ternary:", ternary_search_372(array_372, key_372)[1], "comparisons")
        elif choice_372 == "6":
            if not array_372:
                print("Generate an array first.")
                continue
            print("Absent-key worst-case example (key = -1):")
            print("Binary:", binary_search_372(array_372, -1)[1], "comparisons")
            print("Ternary:", ternary_search_372(array_372, -1)[1], "comparisons")
        elif choice_372 == "7":
            show_counts_372(array_372)
        elif choice_372 == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-8.")


if __name__ == "__main__":
    main_372()
