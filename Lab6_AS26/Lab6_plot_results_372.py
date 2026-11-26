import csv
from pathlib import Path
import matplotlib.pyplot as plt

def read_372(path_372):
    with path_372.open(newline="", encoding="utf-8") as f_372:
        return list(csv.DictReader(f_372))

def plot_rod_372(folder_372):
    rows_372 = read_372(folder_372 / "q1_rod_cutting_results.csv")
    for field_372, filename_372, title_372, log_372 in [
        ("time_seconds", "q1_rod_cutting_time.png", "Rod Cutting Execution Time", False),
        ("calls", "q1_rod_cutting_calls.png", "Rod Cutting Calls / Iterations", True)
    ]:
        fig_372, ax_372 = plt.subplots()
        for name_372 in sorted(set(row_372["algorithm"] for row_372 in rows_372)):
            selected_372 = sorted([r_372 for r_372 in rows_372 if r_372["algorithm"] == name_372], key=lambda r_372: int(r_372["n"]))
            ax_372.plot([int(r_372["n"]) for r_372 in selected_372],
                        [float(r_372[field_372]) for r_372 in selected_372], marker="o", label=name_372)
        ax_372.set(title=title_372, xlabel="Rod length (n)", ylabel=field_372.replace("_", " ").title())
        if log_372:
            ax_372.set_yscale("log")
        ax_372.legend(); ax_372.grid(True); fig_372.tight_layout()
        fig_372.savefig(folder_372 / filename_372, dpi=300); plt.close(fig_372)

def plot_lcs_372(folder_372):
    rows_372 = read_372(folder_372 / "q3_lcs_timing.csv")
    fig_372, ax_372 = plt.subplots()
    ax_372.plot([int(r_372["string_length"]) for r_372 in rows_372], [float(r_372["dp_time_seconds"]) for r_372 in rows_372], marker="o", label="Dynamic programming")
    ax_372.plot([int(r_372["string_length"]) for r_372 in rows_372], [float(r_372["brute_force_time_seconds"]) for r_372 in rows_372], marker="o", label="Brute force")
    ax_372.set(title="LCS Execution Time", xlabel="String length", ylabel="Time (seconds)")
    ax_372.legend(); ax_372.grid(True); fig_372.tight_layout()
    fig_372.savefig(folder_372 / "q3_lcs_time.png", dpi=300); plt.close(fig_372)

if __name__ == "__main__":
    folder_372 = Path(__file__).parent / "outputs"
    if (folder_372 / "q1_rod_cutting_results.csv").exists(): plot_rod_372(folder_372)
    if (folder_372 / "q3_lcs_timing.csv").exists(): plot_lcs_372(folder_372)
    print(f"Graphs saved in {folder_372}")
