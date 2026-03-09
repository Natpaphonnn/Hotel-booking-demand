"""Custom Matplotlib/Seaborn visualization theme — Luxury Hotel Gold, elegant & clean."""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from src.config import COLORS, CATEGORY_PALETTE


# Custom colormap: Gold gradient
GOLD_CMAP = mcolors.LinearSegmentedColormap.from_list(
    "luxury_gold", ["#F5F0EB", "#E2CCAE", "#D4B896", "#B8945F", "#8B7242", "#5C4A2A"]
)


def set_theme():
    """Apply the Luxury Hotel Gold custom theme to all plots."""
    plt.rcParams.update({
        # Figure
        "figure.figsize": (12, 6),
        "figure.dpi": 150,
        "figure.facecolor": COLORS["white"],
        "figure.edgecolor": COLORS["white"],

        # Axes
        "axes.facecolor": COLORS["white"],
        "axes.edgecolor": COLORS["light_gray"],
        "axes.labelcolor": COLORS["dark"],
        "axes.titlecolor": COLORS["dark"],
        "axes.labelsize": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,

        # Grid
        "grid.color": COLORS["grid"],
        "grid.linewidth": 0.6,
        "grid.alpha": 0.6,

        # Ticks
        "xtick.color": COLORS["text"],
        "ytick.color": COLORS["text"],
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        # Font
        "font.family": "sans-serif",
        "font.size": 11,

        # Legend
        "legend.frameon": False,
        "legend.fontsize": 10,

        # Savefig
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.facecolor": COLORS["white"],
    })

    sns.set_palette(CATEGORY_PALETTE)


def format_axis_currency(ax, axis="y"):
    """Format axis ticks as currency (e.g., $1.2M)."""
    import matplotlib.ticker as ticker

    def fmt(x, _):
        if abs(x) >= 1_000_000:
            return f"${x / 1_000_000:.1f}M"
        elif abs(x) >= 1_000:
            return f"${x / 1_000:.0f}K"
        return f"${x:.0f}"

    if axis == "y":
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(fmt))
    else:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(fmt))


def format_axis_pct(ax, axis="y"):
    """Format axis ticks as percentages."""
    import matplotlib.ticker as ticker
    fmt = ticker.FuncFormatter(lambda x, _: f"{x:.0%}" if x <= 1 else f"{x:.0f}%")
    if axis == "y":
        ax.yaxis.set_major_formatter(fmt)
    else:
        ax.xaxis.set_major_formatter(fmt)


def add_value_labels(ax, fmt=".0f", fontsize=9, color=None):
    """Add value labels on top of bar charts."""
    color = color or COLORS["dark"]
    for bar in ax.patches:
        val = bar.get_height()
        if val > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                val,
                f"{val:{fmt}}",
                ha="center", va="bottom",
                fontsize=fontsize, color=color, fontweight="bold"
            )
