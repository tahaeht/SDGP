"""
Waste Analysis Module — Pink Café Demand Forecasting Dashboard
Author: Ahmed
Sprint: Week 2

Calculates production recommendations, old-method estimates,
and waste avoided using AI-based forecasting vs traditional ordering.
"""

import math
import pandas as pd


def recommend_production(predicted_qty: float, buffer_pct: float) -> int:
    raw = predicted_qty * (1 + buffer_pct / 100)
    return math.ceil(round(raw, 4))


def old_method_estimate(series: pd.Series, window: int = 4) -> float:
    if len(series) == 0:
        return 0.0
    return series.tail(window).mean()


def waste_avoided(old_estimate: float, new_recommendation: int) -> dict:
    units = max(0, math.ceil(old_estimate) - new_recommendation)
    pct = (units / old_estimate * 100) if old_estimate > 0 else 0.0
    return {"units": units, "pct": round(pct, 2)}


def generate_waste_summary(products: list, series_dict: dict, predictions: dict, buffer: float) -> pd.DataFrame:
    rows = []
    for product in products:
        series = series_dict.get(product, pd.Series(dtype=float))
        predicted_qty = predictions.get(product, 0.0)
        old_est = old_method_estimate(series)
        new_rec = recommend_production(predicted_qty, buffer)
        avoided = waste_avoided(old_est, new_rec)
        rows.append({
            "Product": product,
            "Old Estimate": math.ceil(old_est),
            "AI Recommendation": new_rec,
            "Waste Avoided (units)": avoided["units"],
            "Waste Avoided (%)": avoided["pct"],
        })
    return pd.DataFrame(rows)
