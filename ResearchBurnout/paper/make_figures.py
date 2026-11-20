"""Build the IEEE-column figures from the recorded aggregate results."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


PAPER = Path(__file__).resolve().parent
RESULTS = PAPER.parent / "results"
FIGURES = PAPER / "tex" / "figures"
BLUE = "#235a85"
INK = "#21272b"
GRAY = "#66757c"

plt.rcParams.update(
    {
        "font.size": 8,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": GRAY,
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": INK,
        "ytick.color": INK,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "pdf.fonttype": 42,
    }
)


def study_design():
    fig, ax = plt.subplots(figsize=(3.5, 1.58))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.set_axis_off()

    for column in (0.252, 0.748):
        ax.plot([0.5, 0.5, column, column], [0.84, 0.75, 0.75, 0.64], color=GRAY, lw=0.7)
        ax.plot([column, column, 0.5, 0.5], [0.36, 0.25, 0.25, 0.19], color=GRAY, lw=0.7)

    ax.text(0.5, 0.915, "97 university student surveys", ha="center", va="center", weight="bold")
    ax.axhspan(0.36, 0.64, xmin=0.025, xmax=0.48, color="#eaf0f4")
    ax.axhspan(0.36, 0.64, xmin=0.52, xmax=0.975, color="#eaf0f4")
    ax.text(0.252, 0.565, "Score estimation", ha="center", va="center", weight="bold")
    ax.text(0.252, 0.45, "5 study questions\nvs. 5 study + 3 GenAI",
            ha="center", va="center", fontsize=7.5)
    ax.text(0.748, 0.565, "High-symptom warnings", ha="center", va="center", weight="bold")
    ax.text(0.748, 0.45, "Workload alone\nvs. 5 study + 3 GenAI",
            ha="center", va="center", fontsize=7.5)
    ax.text(0.5, 0.13, "Repeated nested cross-validation", ha="center", va="center", weight="bold")
    ax.text(0.5, 0.045, "Inner folds tune · Outer folds test on held-out students",
            ha="center", va="center", fontsize=7.5)
    fig.savefig(FIGURES / "study-design.pdf")
    plt.close(fig)


def warning_counts(comparisons):
    fig, axes = plt.subplots(1, 2, figsize=(3.5, 1.43), sharey=True)
    fig.subplots_adjust(left=0.27, bottom=0.2, right=0.96, top=0.85, wspace=0.32)
    methods = ["workload_logistic", "selected_rf", "random_same_warning_count"]
    labels = ["Workload only", "Eight-question\nforest", "Matched\nrandom"]
    rows = np.arange(len(methods))
    for ax, key, title, limit, ticks in zip(
        axes,
        ("tp", "fp"),
        ("High detected / 17", "False warnings / 80"),
        (19.5, 80),
        ([0, 5, 10, 15], [0, 20, 40, 60, 80]),
    ):
        counts = [float(comparisons[method][key]) for method in methods]
        ax.barh(rows, counts, height=0.46, color=[INK, BLUE, GRAY], zorder=2)
        for row, count in zip(rows, counts):
            ax.annotate(f"{count:.1f}", (count, row), xytext=(3, 0),
                        textcoords="offset points", va="center", fontsize=7.5)
        ax.set(xlim=(0, limit), xticks=ticks)
        ax.set_title(title, fontsize=8, pad=3)
        ax.grid(axis="x", color="#d9e0e3", linewidth=0.5)
        ax.tick_params(axis="y", length=0, pad=3)
        ax.tick_params(axis="x", length=2)
    axes[0].set_yticks(rows, labels)
    axes[0].set_ylim(len(rows) - 0.5, -0.5)
    fig.savefig(FIGURES / "warning-counts.pdf")
    plt.close(fig)


def permutation_accuracy(observed, shuffled):
    fig, ax = plt.subplots(figsize=(3.5, 1.57))
    fig.subplots_adjust(left=0.14, bottom=0.27, right=0.97, top=0.96)
    ax.hist(shuffled * 100, bins=np.arange(40, 68, 2), color="#aec2d2",
            edgecolor=BLUE, linewidth=0.5)
    ax.axvline(observed * 100, color=INK, linestyle="--", linewidth=1.1)
    ax.annotate(f"Observed\n{observed:.1%}", (observed * 100, 0.91),
                xycoords=("data", "axes fraction"), xytext=(-5, 0),
                textcoords="offset points", ha="right", va="top", weight="bold")
    ax.set(xlim=(40, 80), xticks=range(40, 81, 10),
           xlabel="Balanced accuracy (%)", ylabel="Shuffled runs")
    ax.tick_params(length=2)
    fig.savefig(FIGURES / "permutation-accuracy.pdf")
    plt.close(fig)


if __name__ == "__main__":
    with (RESULTS / "25-model-comparison-summary.csv").open(newline="") as source:
        comparisons = {row["method"]: row for row in csv.DictReader(source)}
    with (RESULTS / "25-shuffled-label-test-results.csv").open(newline="") as source:
        shuffled = np.array([float(row["balanced_accuracy"]) for row in csv.DictReader(source)])
    observed = float(comparisons["selected_rf"]["balanced_accuracy"])
    assert len(shuffled) == 199 and shuffled.max() < observed
    assert float(comparisons["workload_logistic"]["fp"]) == float(comparisons["selected_rf"]["fp"])

    FIGURES.mkdir(exist_ok=True)
    study_design()
    warning_counts(comparisons)
    permutation_accuracy(observed, shuffled)
