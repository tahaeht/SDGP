````

````python
<vscode_codeblock_uri>vscode-remote://ssh-remote%2Bcsctcloud.uwe.ac.uk/home/ahmed2.deraz/SDGP/services/waste_analysis.py</vscode_codeblock_uri>"""
Waste Analysis Module — Pink Café Demand Forecasting Dashboard
Author: Ahmed
Sprint: Week 2

Calculates production recommendations, old-method estimates,
and waste avoided using AI-based forecasting vs traditional ordering.
"""

import math
import pandas as pd


def recommend_production(predicted_qty: float, buffer_pct: float) -> int:
    """
    Calculate recommended production quantity with safety buffer.
    
    Uses round(..., 4) before math.ceil() to avoid floating-point
    precision errors (e.g., 100 * 1.10 = 110.00000000000001 → ceil = 111).
    
    Args:
        predicted_qty: Forecasted demand (units)
        buffer_pct: Safety buffer as a percentage (e.g., 10 for 10%)
    
    Returns:
        Integer production target
    """
    raw = predicted_qty * (1 + buffer_pct / 100)
    return math.ceil(round(raw, 4))


def old_method_estimate(series: pd.Series, window: int = 4) -> float:
    """
    Estimate what the café would order without AI — simple mean