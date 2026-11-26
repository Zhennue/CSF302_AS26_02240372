def optimal_bst_372(p_372, q_372):
    n_372 = len(p_372)
    cost_372 = [[0.0] * (n_372 + 2) for _ in range(n_372 + 2)]
    weight_372 = [[0.0] * (n_372 + 2) for _ in range(n_372 + 2)]
    root_372 = [[0] * (n_372 + 1) for _ in range(n_372 + 1)]
    for i_372 in range(1, n_372 + 2):
        cost_372[i_372][i_372 - 1] = q_372[i_372 - 1]
        weight_372[i_372][i_372 - 1] = q_372[i_372 - 1]
    for length_372 in range(1, n_372 + 1):
        for i_372 in range(1, n_372 - length_372 + 2):
            j_372 = i_372 + length_372 - 1
            cost_372[i_372][j_372] = float("inf")
            weight_372[i_372][j_372] = weight_372[i_372][j_372 - 1] + p_372[j_372 - 1] + q_372[j_372]
            for r_372 in range(i_372, j_372 + 1):
                candidate_372 = cost_372[i_372][r_372 - 1] + cost_372[r_372 + 1][j_372] + weight_372[i_372][j_372]
                if candidate_372 < cost_372[i_372][j_372]:
                    cost_372[i_372][j_372] = candidate_372
                    root_372[i_372][j_372] = r_372
    return cost_372[1][n_372], root_372

def tree_string_372(root_372, i_372, j_372):
    if i_372 > j_372:
        return "None"
    r_372 = root_372[i_372][j_372]
    return f"k{r_372}({tree_string_372(root_372, i_372, r_372 - 1)}, {tree_string_372(root_372, r_372 + 1, j_372)})"

if __name__ == "__main__":
    p_372 = [0.15, 0.10, 0.05, 0.10, 0.20]
    q_372 = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    cost_372, root_372 = optimal_bst_372(p_372, q_372)
    print(f"Expected search cost: {cost_372:.2f}")
    print("Optimal BST structure:")
    print(tree_string_372(root_372, 1, len(p_372)))
