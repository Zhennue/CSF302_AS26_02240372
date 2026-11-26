import random


def quicksort_basic_372(values_372):
    """Sort values in place using recursive Lomuto quicksort."""
    def sort_range_372(low_372, high_372):
        if low_372 >= high_372:
            return

        pivot_372 = values_372[high_372]
        boundary_372 = low_372
        for scan_372 in range(low_372, high_372):
            if values_372[scan_372] <= pivot_372:
                values_372[boundary_372], values_372[scan_372] = (
                    values_372[scan_372], values_372[boundary_372]
                )
                boundary_372 += 1

        values_372[boundary_372], values_372[high_372] = (
            values_372[high_372], values_372[boundary_372]
        )
        sort_range_372(low_372, boundary_372 - 1)
        sort_range_372(boundary_372 + 1, high_372)

    sort_range_372(0, len(values_372) - 1)


def quicksort_improved_372(values_372, cutoff_372=16, seed_372=None):
    """Sort in place using randomized three-way quicksort and insertion sort."""
    if cutoff_372 < 1:
        raise ValueError("cutoff must be at least 1")

    random_generator_372 = random.Random(seed_372)

    def insertion_sort_372(low_372, high_372):
        for index_372 in range(low_372 + 1, high_372 + 1):
            value_372 = values_372[index_372]
            position_372 = index_372 - 1
            while position_372 >= low_372 and values_372[position_372] > value_372:
                values_372[position_372 + 1] = values_372[position_372]
                position_372 -= 1
            values_372[position_372 + 1] = value_372

    def sort_range_372(low_372, high_372):
        while high_372 - low_372 + 1 > cutoff_372:
            pivot_372 = values_372[random_generator_372.randint(low_372, high_372)]
            less_372 = low_372
            scan_372 = low_372
            greater_372 = high_372

            while scan_372 <= greater_372:
                if values_372[scan_372] < pivot_372:
                    values_372[less_372], values_372[scan_372] = (
                        values_372[scan_372], values_372[less_372]
                    )
                    less_372 += 1
                    scan_372 += 1
                elif values_372[scan_372] > pivot_372:
                    values_372[scan_372], values_372[greater_372] = (
                        values_372[greater_372], values_372[scan_372]
                    )
                    greater_372 -= 1
                else:
                    scan_372 += 1

            left_size_372 = less_372 - low_372
            right_size_372 = high_372 - greater_372

            # Recurse only into the smaller side; loop over the larger side.
            if left_size_372 < right_size_372:
                sort_range_372(low_372, less_372 - 1)
                low_372 = greater_372 + 1
            else:
                sort_range_372(greater_372 + 1, high_372)
                high_372 = less_372 - 1

        if low_372 < high_372:
            insertion_sort_372(low_372, high_372)

    sort_range_372(0, len(values_372) - 1)


if __name__ == "__main__":
    sample_372 = [5, 3, 8, -1, 3]
    basic_sample_372 = sample_372.copy()
    improved_sample_372 = sample_372.copy()
    quicksort_basic_372(basic_sample_372)
    quicksort_improved_372(improved_sample_372, seed_372=372)
    print("Basic quicksort:", basic_sample_372)
    print("Improved quicksort:", improved_sample_372)

