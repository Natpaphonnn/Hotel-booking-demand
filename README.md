# Hotel Booking Demand — Revenue Strategy & Analytics

> Data-driven insights for hospitality revenue optimization using 119,390 hotel bookings (2015–2017)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-red)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-9B59B6)

[![Presentation](https://img.shields.io/badge/Presentation-View%20Slides-FF2800?style=for-the-badge)](https://natpaphonnn.github.io/Hotel-booking-demand/presentation.html)
[![Revenue Presentation](https://img.shields.io/badge/Revenue%20Presentation-Interactive%20Charts-2D2D2D?style=for-the-badge)](https://natpaphonnn.github.io/Hotel-booking-demand/revenue-presentation.html)

---

## Business Problem

Hotels face significant revenue loss from booking cancellations, suboptimal pricing, and undifferentiated customer strategies. This project addresses three critical business questions:

1. **Can we predict which bookings will be canceled?** — Enable strategic overbooking and revenue protection
2. **How should room rates adapt to demand patterns?** — Optimize pricing across lead times and seasons
3. **Who are our most valuable customers?** — Segment customers for targeted marketing and retention

## Key Findings

### Cancellation Prediction
- Built an **XGBoost model** achieving strong ROC-AUC performance for cancellation prediction
- **Lead time** is the single strongest predictor — bookings made 365+ days in advance have dramatically higher cancellation rates
- Recommended a **risk-tiered overbooking strategy** that could recover significant lost revenue

### Dynamic Pricing Insights
- **Short lead-time bookings** (0–7 days) command the highest ADR — last-minute travelers are less price-sensitive
- **Resort Hotels** show 2–3x seasonal price variation vs City Hotels' stable rates
- Identified **optimal pricing windows** by season and booking channel

### Customer Segmentation
- Identified **4 distinct customer segments** using RFM-adapted K-Means clustering
- **High-Value segment** (long stays, high ADR) generates disproportionate revenue
- Mapped each segment to **actionable marketing strategies** — from VIP loyalty programs to direct booking conversion campaigns

## Project Structure

```
Hotel-booking-demand/
├── README.md
├── hotel_bookings.csv                         # Raw dataset (119,390 rows)
├── requirements.txt
├── notebooks/
│   ├── 01_EDA_Revenue_Analysis.ipynb          # EDA & Revenue Insights
│   ├── 02_Cancellation_Prediction.ipynb       # ML Prediction Model
│   ├── 03_Dynamic_Pricing_Insight.ipynb       # Pricing Optimization
│   └── 04_Customer_Value_Segmentation.ipynb   # Customer Clustering
├── src/
│   ├── config.py                              # Color palette & constants
│   ├── data_cleaning.py                       # Reusable cleaning pipeline
│   ├── feature_engineering.py                 # Feature creation
│   └── viz_style.py                           # Custom visualization theme
└── outputs/
    └── figures/                               # Exported plots
```

## Methodology

| Notebook | Technique | Key Output |
|----------|-----------|------------|
| 01 — EDA | Revenue analysis, cancellation patterns | Business insights dashboard |
| 02 — Prediction | Logistic Regression → Random Forest → XGBoost | Overbooking strategy with optimal threshold |
| 03 — Pricing | Lead time/seasonal analysis, price elasticity | Dynamic pricing recommendations |
| 04 — Segmentation | RFM-adapted K-Means clustering | 4 customer segments with targeted strategies |

## Tech Stack

- **Data:** Pandas, NumPy
- **ML:** Scikit-Learn, XGBoost
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Theme:** Custom Ferrari Red palette (`#FF2800`)

## How to Reproduce

```bash
# Clone the repository
git clone https://github.com/yourusername/Hotel-booking-demand.git
cd Hotel-booking-demand

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook notebooks/01_EDA_Revenue_Analysis.ipynb
```

## Dataset

Source: [Hotel Booking Demand](https://www.sciencedirect.com/science/article/pii/S2352340918315191) — Nuno Antonio, Ana de Almeida, Luis Nunes (2019)

- **119,390 bookings** across 2 hotel types (Resort Hotel, City Hotel)
- **32 features** including lead time, ADR, market segment, customer type, and cancellation status
- **Time period:** July 2015 – August 2017

---

*Built as a Data Science portfolio project showcasing Revenue Strategy & Analytics in Hospitality.*
