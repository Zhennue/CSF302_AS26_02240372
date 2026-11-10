import csv
import random
import time
from pathlib import Path

def lcs_table_372(x_372, y_372):
    table_372 = [[0] * (len(y_372) + 1) for _ in range(len(x_372) + 1)]
    for i_372 in range(1, len(x_372) + 1):
        for j_372 in range(1, len(y_372) + 1):
            if x_372[i_372 - 1] == y_372[j_372 - 1]:
                table_372[i_372][j_372] = table_372[i_372 - 1][j_372 - 1] + 1
            else:
                table_372[i_372][j_372] = max(table_372[i_372 - 1][j_372], table_372[i_372][j_372 - 1])
    return table_372

def reconstruct_lcs_372(x_372, y_372, table_372):
    i_372, j_372, result_372 = len(x_372), len(y_372), []
    while i_372 and j_372:
        if x_372[i_372 - 1] == y_372[j_372 - 1]:
            result_372.append(x_372[i_372 - 1])
            i_372 -= 1
            j_372 -= 1
        elif table_372[i_372 - 1][j_372] >= table_372[i_372][j_372 - 1]:
            i_372 -= 1
        else:
            j_372 -= 1
    return "".join(reversed(result_372))

def lcs_two_rows_372(x_372, y_372):
    if len(y_372) > len(x_372):
        x_372, y_372 = y_372, x_372
    previous_372 = [0] * (len(y_372) + 1)
    for char_x_372 in x_372:
        current_372 = [0] * (len(y_372) + 1)
        for j_372, char_y_372 in enumerate(y_372, 1):
            if char_x_372 == char_y_372:
                current_372[j_372] = previous_372[j_372 - 1] + 1
            else:
                current_372[j_372] = max(previous_372[j_372], current_372[j_372 - 1])
        previous_372 = current_372
    return previous_372[-1]

def brute_lcs_372(x_372, y_372):
    best_372 = 0
    for mask_372 in range(1 << len(x_372)):
        subsequence_372 = "".join(x_372[i_372] for i_372 in range(len(x_372)) if mask_372 & (1 << i_372))
        matched_372 = 0
        for char_372 in y_372:
            if matched_372 < len(subsequence_372) and subsequence_372[matched_372] == char_372:
                matched_372 += 1
        if matched_372 == len(subsequence_372):
            best_372 = max(best_372, len(subsequence_372))
    return best_372

def print_table_372(x_372, y_372, table_372):
    print("    " + "  ".join(["-"] + list(y_372)))
    for i_372, char_372 in enumerate(["-"] + list(x_372)):
        print(f"{char_372:>3} " + "  ".join(str(v_372) for v_372 in table_372[i_372]))

def benchmark_372():
    rng_372 = random.Random(372)
    rows_372 = []
    for n_372 in range(5, 19):
        x_372 = "".join(rng_372.choice("ABCD") for _ in range(n_372))
        y_372 = "".join(rng_372.choice("ABCD") for _ in range(n_372))
        start_372 = time.perf_counter()
        dp_372 = lcs_two_rows_372(x_372, y_372)
        dp_time_372 = time.perf_counter() - start_372
        start_372 = time.perf_counter()
        brute_372 = brute_lcs_372(x_372, y_372)
        brute_time_372 = time.perf_counter() - start_372
        assert dp_372 == brute_372
        rows_372.append([n_372, dp_372, f"{dp_time_372:.8f}", f"{brute_time_372:.8f}"])
        print(f"n={n_372:2} LCS={dp_372:2} DP={dp_time_372:.6f}s brute force={brute_time_372:.6f}s")
    folder_372 = Path(__file__).parent / "outputs"
    with (folder_372 / "q3_lcs_timing.csv").open("w", newline="", encoding="utf-8") as f_372:
        writer_372 = csv.writer(f_372)
        writer_372.writerow(["string_length", "lcs_length", "dp_time_seconds", "brute_force_time_seconds"])
        writer_372.writerows(rows_372)
    print("Saved outputs/q3_lcs_timing.csv")

def line_diff_372(file_a_372, file_b_372):
    a_372 = Path(file_a_372).read_text(encoding="utf-8").splitlines()
    b_372 = Path(file_b_372).read_text(encoding="utf-8").splitlines()
    table_372 = lcs_table_372(a_372, b_372)
    i_372, j_372, changes_372 = len(a_372), len(b_372), []
    while i_372 and j_372:
        if a_372[i_372 - 1] == b_372[j_372 - 1]:
            changes_372.append((" ", a_372[i_372 - 1])); i_372 -= 1; j_372 -= 1
        elif table_372[i_372 - 1][j_372] >= table_372[i_372][j_372 - 1]:
            changes_372.append(("-", a_372[i_372 - 1])); i_372 -= 1
        else:
            changes_372.append(("+", b_372[j_372 - 1])); j_372 -= 1
    while i_372:
        changes_372.append(("-", a_372[i_372 - 1])); i_372 -= 1
    while j_372:
        changes_372.append(("+", b_372[j_372 - 1])); j_372 -= 1
    print(f"\nLine diff: {file_a_372} -> {file_b_372}")
    for marker_372, line_372 in reversed(changes_372):
        print(f"{marker_372} {line_372}")

if __name__ == "__main__":
    x_372, y_372 = "ABCBDAB", "BDCABA"
    table_372 = lcs_table_372(x_372, y_372)
    print(f"X = {x_372}\nY = {y_372}\n\nLCS table:")
    print_table_372(x_372, y_372, table_372)
    print(f"\nOne LCS: {reconstruct_lcs_372(x_372, y_372, table_372)}")
    print(f"LCS length: {table_372[-1][-1]}")
    print(f"Two-row LCS length: {lcs_two_rows_372(x_372, y_372)}")
    print("\nTiming for lengths 5 to 18:")
    benchmark_372()
    folder_372 = Path(__file__).parent
    if (folder_372 / "sample_a.txt").exists() and (folder_372 / "sample_b.txt").exists():
        line_diff_372(folder_372 / "sample_a.txt", folder_372 / "sample_b.txt")
