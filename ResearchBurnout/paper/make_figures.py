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
    ax.text(0.252, 0.45, "Small A (5) vs. Small B (8)\nBroad C (13) vs. Broad D (23)",
            ha="center", va="center", fontsize=7.5)
    ax.text(0.748, 0.565, "High-symptom warnings", ha="center", va="center", weight="bold")
    ax.text(0.748, 0.45, "Workload only (1)\nvs. Small B (8)",
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
    labels = ["Workload only", "Small B forest", "Matched\nrandom"]
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


def score_errors():
    # Aggregate values from the ridge reproduction in research/06-data-analysis-and-experiment-history.md.
    labels = ["Primary · Small A/B", "Primary · Broad C/D",
              "Secondary · Small A/B", "Secondary · Broad C/D"]
    without = np.array([0.6183, 0.6145, 0.6001, 0.5874])
    with_genai = np.array([0.5883, 0.5933, 0.5528, 0.5578])
    assert np.all(with_genai < without)

    fig, ax = plt.subplots(figsize=(3.5, 1.77))
    fig.subplots_adjust(left=0.37, bottom=0.26, right=0.97, top=0.80)
    rows = np.arange(len(labels))
    ax.hlines(rows, with_genai, without, color=GRAY, linewidth=0.9)
    ax.scatter(without, rows, s=21, facecolor="white", edgecolor=GRAY,
               label="Without GenAI", zorder=3)
    ax.scatter(with_genai, rows, s=21, color=BLUE, label="With GenAI", zorder=3)
    for row, before, after in zip(rows, without, with_genai):
        ax.annotate(f"{before:.4f}", (before, row), xytext=(5, 0),
                    textcoords="offset points", va="center", fontsize=7)
        ax.annotate(f"{after:.4f}", (after, row), xytext=(-5, 0),
                    textcoords="offset points", ha="right", va="center", fontsize=7)
    ax.set(xlim=(0.52, 0.654), ylim=(3.5, -0.5), xticks=[0.53, 0.56, 0.59, 0.62, 0.65],
           xlabel="Mean absolute error (points)")
    ax.set_yticks(rows, labels, fontsize=7)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.tick_params(axis="x", length=2)
    ax.grid(axis="x", color="#d9e0e3", linewidth=0.5)
    fig.legend(loc="upper center", frameon=False, ncol=2, fontsize=7.5)
    fig.savefig(FIGURES / "genai-score-errors.pdf")
    plt.close(fig)


def warning_differences(comparisons, intervals):
    metrics = ["recall", "precision", "balanced_accuracy"]
    names = ["Recall", "Precision", "Balanced accuracy"]
    paired = "selected_rf minus workload_logistic"
    bounds = 100 * np.array([intervals[paired, metric] for metric in metrics])
    means = 100 * np.array([float(comparisons["selected_rf"][metric])
                           - float(comparisons["workload_logistic"][metric])
                           for metric in metrics])
    lower, upper = bounds.T
    assert np.all((lower <= means) & (means <= upper))

    fig, ax = plt.subplots(figsize=(3.5, 1.59))
    fig.subplots_adjust(left=0.33, bottom=0.27, right=0.97, top=0.96)
    rows = np.arange(len(metrics))
    ax.axvline(0, color=INK, linestyle="--", linewidth=0.8)
    ax.errorbar(means, rows, xerr=(means - lower, upper - means),
                fmt="o", color=BLUE, linewidth=1.1, markersize=3.8, capsize=3)
    labels = [f"{name}\n{lo:.1f} to {hi:.1f}".replace("-", "−")
              for name, lo, hi in zip(names, lower, upper)]
    ax.set(xlim=(-22, 6), ylim=(2.5, -0.5), xticks=[-20, -15, -10, -5, 0, 5],
           xlabel="Forest minus workload (percentage points)")
    ax.set_yticks(rows, labels, fontsize=7.2)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.tick_params(axis="x", length=2)
    ax.grid(axis="x", color="#d9e0e3", linewidth=0.5)
    fig.savefig(FIGURES / "paired-warning-intervals.pdf")
    plt.close(fig)


if __name__ == "__main__":
    with (RESULTS / "25-model-comparison-summary.csv").open(newline="") as source:
        comparisons = {row["method"]: row for row in csv.DictReader(source)}
    with (RESULTS / "25-shuffled-label-test-results.csv").open(newline="") as source:
        shuffled = np.array([float(row["balanced_accuracy"]) for row in csv.DictReader(source)])
    with (RESULTS / "25-conditional-student-uncertainty-intervals.csv").open(newline="") as source:
        intervals = {(row["comparison"], row["metric"]): (float(row["lower"]), float(row["upper"]))
                     for row in csv.DictReader(source)}
    observed = float(comparisons["selected_rf"]["balanced_accuracy"])
    assert len(shuffled) == 199 and shuffled.max() < observed
    assert float(comparisons["workload_logistic"]["fp"]) == float(comparisons["selected_rf"]["fp"])

    FIGURES.mkdir(exist_ok=True)
    study_design()
    warning_counts(comparisons)
    permutation_accuracy(observed, shuffled)
    score_errors()
    warning_differences(comparisons, intervals)
