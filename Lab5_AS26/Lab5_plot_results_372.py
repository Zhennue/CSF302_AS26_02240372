import csv
from pathlib import Path
import matplotlib.pyplot as plt


def read_csv_372(path_372):
    with path_372.open(newline="", encoding="utf-8") as file_372:
        return list(csv.DictReader(file_372))


def plot_q1_372(folder_372):
    rows_372 = read_csv_372(folder_372 / "q1_results.csv")
    for kind_372 in sorted(set(row_372["input_type"] for row_372 in rows_372)):
        figure_372, axis_372 = plt.subplots()
        for algorithm_372 in sorted(set(row_372["algorithm"] for row_372 in rows_372)):
            selected_372 = [row_372 for row_372 in rows_372 if row_372["input_type"] == kind_372 and row_372["algorithm"] == algorithm_372]
            selected_372.sort(key=lambda row_372: int(row_372["n"]))
            axis_372.plot([int(row_372["n"]) for row_372 in selected_372],
                          [float(row_372["time_seconds"]) for row_372 in selected_372],
                          marker="o", label=algorithm_372)
        axis_372.set(title=f"Q1 execution time - {kind_372}", xlabel="Input size (n)", ylabel="Time (seconds)")
        axis_372.legend()
        axis_372.grid(True)
        figure_372.tight_layout()
        figure_372.savefig(folder_372 / f"q1_{kind_372}_time.png")
        plt.close(figure_372)


def plot_q2_372(folder_372):
    rows_372 = read_csv_372(folder_372 / "q2_results.csv")
    figure_372, axis_372 = plt.subplots()
    for algorithm_372 in sorted(set(row_372["algorithm"] for row_372 in rows_372 if row_372["algorithm"] != "Counting")):
        selected_372 = [row_372 for row_372 in rows_372 if row_372["algorithm"] == algorithm_372]
        selected_372.sort(key=lambda row_372: int(row_372["n"]))
        axis_372.plot([int(row_372["n"]) for row_372 in selected_372],
                      [float(row_372["time_seconds"]) for row_372 in selected_372],
                      marker="o", label=algorithm_372)
    axis_372.set(title="Q2 radix sort and merge sort", xlabel="Input size (n)", ylabel="Time (seconds)")
    axis_372.legend()
    axis_372.grid(True)
    figure_372.tight_layout()
    figure_372.savefig(folder_372 / "q2_radix_merge_time.png")
    plt.close(figure_372)

    counting_372 = [row_372 for row_372 in rows_372 if row_372["algorithm"] == "Counting"]
    figure_372, axis_372 = plt.subplots()
    axis_372.plot([int(row_372["k_or_maximum"]) for row_372 in counting_372],
                  [float(row_372["time_seconds"]) for row_372 in counting_372], marker="o")
    axis_372.set(title="Q2 counting sort with n=100,000", xlabel="Maximum key (k)", ylabel="Time (seconds)")
    axis_372.set_xscale("log")
    axis_372.legend(["Counting sort"])
    axis_372.grid(True)
    figure_372.tight_layout()
    figure_372.savefig(folder_372 / "q2_counting_k_time.png")
    plt.close(figure_372)


def plot_q3_372(folder_372):
    rows_372 = read_csv_372(folder_372 / "q3_results.csv")
    figure_372, axis_372 = plt.subplots()
    for algorithm_372 in sorted(set(row_372["algorithm"] for row_372 in rows_372)):
        selected_372 = [row_372 for row_372 in rows_372 if row_372["algorithm"] == algorithm_372]
        selected_372.sort(key=lambda row_372: int(row_372["n"]))
        axis_372.plot([int(row_372["n"]) for row_372 in selected_372],
                      [float(row_372["time_seconds"]) for row_372 in selected_372],
                      marker="o", label=algorithm_372)
    axis_372.set(title="Q3 inversion counting performance", xlabel="Input size (n)", ylabel="Time (seconds)")
    axis_372.set_xscale("log")
    axis_372.set_yscale("log")
    axis_372.legend()
    axis_372.grid(True)
    figure_372.tight_layout()
    figure_372.savefig(folder_372 / "q3_inversion_time.png")
    plt.close(figure_372)


if __name__ == "__main__":
    folder_372 = Path(__file__).parent / "outputs"
    for required_372 in ["q1_results.csv", "q2_results.csv", "q3_results.csv"]:
        if not (folder_372 / required_372).exists():
            raise SystemExit(f"Missing {required_372}. Run the corresponding question program first.")
    plot_q1_372(folder_372)
    plot_q2_372(folder_372)
    plot_q3_372(folder_372)
    print(f"Plots saved in {folder_372}")
