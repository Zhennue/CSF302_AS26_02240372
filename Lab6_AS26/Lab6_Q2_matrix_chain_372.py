import random

def matrix_chain_372(dims_372):
    count_372 = len(dims_372) - 1
    cost_372 = [[0] * count_372 for _ in range(count_372)]
    split_372 = [[0] * count_372 for _ in range(count_372)]
    for length_372 in range(2, count_372 + 1):
        for start_372 in range(count_372 - length_372 + 1):
            end_372 = start_372 + length_372 - 1
            cost_372[start_372][end_372] = float("inf")
            for mid_372 in range(start_372, end_372):
                candidate_372 = (cost_372[start_372][mid_372] +
                    cost_372[mid_372 + 1][end_372] +
                    dims_372[start_372] * dims_372[mid_372 + 1] * dims_372[end_372 + 1])
                if candidate_372 < cost_372[start_372][end_372]:
                    cost_372[start_372][end_372] = candidate_372
                    split_372[start_372][end_372] = mid_372
    return cost_372[0][-1], split_372

def parenthesize_372(split_372, i_372, j_372):
    if i_372 == j_372:
        return f"A{i_372 + 1}"
    mid_372 = split_372[i_372][j_372]
    return f"({parenthesize_372(split_372, i_372, mid_372)}{parenthesize_372(split_372, mid_372 + 1, j_372)})"

def left_to_right_372(dims_372):
    total_372 = 0
    rows_372, cols_372 = dims_372[0], dims_372[1]
    for index_372 in range(2, len(dims_372) - 1 + 1):
        next_cols_372 = dims_372[index_372]
        total_372 += rows_372 * cols_372 * next_cols_372
        cols_372 = next_cols_372
    return total_372

def brute_force_372(dims_372):
    def solve_372(i_372, j_372):
        if i_372 == j_372:
            return 0
        best_372 = float("inf")
        for mid_372 in range(i_372, j_372):
            value_372 = (solve_372(i_372, mid_372) + solve_372(mid_372 + 1, j_372) +
                         dims_372[i_372] * dims_372[mid_372 + 1] * dims_372[j_372 + 1])
            best_372 = min(best_372, value_372)
        return best_372
    return solve_372(0, len(dims_372) - 2)

def show_372(label_372, dims_372):
    best_372, split_372 = matrix_chain_372(dims_372)
    expression_372 = parenthesize_372(split_372, 0, len(dims_372) - 2)
    print(f"\n{label_372}: dimensions={dims_372}")
    print(f"Optimal scalar multiplications: {best_372:,}")
    print(f"Optimal parenthesisation: {expression_372}")
    print(f"Left-to-right cost: {left_to_right_372(dims_372):,}")
    if len(dims_372) - 1 <= 8:
        brute_372 = brute_force_372(dims_372)
        print(f"Brute-force cost: {brute_372:,} (verification {'passed' if brute_372 == best_372 else 'FAILED'})")
        assert brute_372 == best_372

if __name__ == "__main__":
    show_372("Provided test 1", [30, 35, 15, 5, 10, 20, 25])
    show_372("Provided test 2", [5, 4, 6, 2, 7])
    rng_372 = random.Random(372)
    print("\nFive random chains")
    for test_372 in range(1, 6):
        matrix_count_372 = rng_372.randint(3, 8)
        dims_372 = [rng_372.randint(2, 30) for _ in range(matrix_count_372 + 1)]
        show_372(f"Random chain {test_372}", dims_372)
