"""Project configuration — Luxury Hotel Gold theme color palette and constants."""

# === Color Palette (Luxury Hotel Gold Theme) ===
COLORS = {
    "primary": "#B8945F",       # Warm Gold
    "dark": "#2C2C2C",          # Charcoal
    "white": "#FFFFFF",
    "light_gray": "#F5F0EB",    # Warm cream
    "accent": "#D4B896",        # Light tan
    "grid": "#EDE8E2",          # Warm grid
    "text": "#3D3D3D",          # Dark text
    "muted": "#9E9E9E",         # Muted text
    "deep_gold": "#8B7242",     # Deep gold for emphasis
    "navy": "#1C2541",          # Dark navy accent
}

# Sequential palette for charts (gold gradient)
GOLD_PALETTE = ["#8B7242", "#B8945F", "#C9A96E", "#D4B896", "#E2CCAE", "#F0E0C8"]

# Categorical palette
CATEGORY_PALETTE = ["#B8945F", "#2C2C2C", "#D4B896", "#1C2541", "#8B7242", "#6B6B6B"]

# === Month Mapping ===
MONTH_ORDER = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
MONTH_TO_NUM = {m: i + 1 for i, m in enumerate(MONTH_ORDER)}

# === Season Mapping ===
HIGH_SEASON_MONTHS = [7, 8, 12, 1]  # Jul, Aug, Dec, Jan
MID_SEASON_MONTHS = [3, 4, 5, 6, 9, 10]
LOW_SEASON_MONTHS = [2, 11]

# === Lead Time Buckets ===
LEAD_TIME_BINS = [0, 7, 30, 90, 180, 365, 800]
LEAD_TIME_LABELS = ["0-7d", "8-30d", "31-90d", "91-180d", "181-365d", "365d+"]

# === File Paths ===
DATA_PATH = "../hotel_bookings.csv"
FIGURES_PATH = "../outputs/figures/"
