# Waste Analysis Methodology

**Project:** Pink Café Demand Forecasting Dashboard

---

## 1. Objective

The purpose of this waste analysis is to quantify:

- **Overproduction waste** — units produced but not sold
- **Underproduction loss** — missed revenue from unmet demand
- **Financial impact** of forecasting errors

The system uses predicted demand from an **Exponential Smoothing (ETS)** time series model to guide daily production decisions.

---

## 2. Key Variables

| Symbol | Description |
|--------|-------------|
| F<sub>t</sub> | Forecasted demand for day *t* |
| A<sub>t</sub> | Actual demand for day *t* |
| B | Manager safety buffer percentage |
| C | Cost per unit (£) |
| P | Selling price per unit (£) |

---

## 3. Production Target Formula

Managers apply a safety buffer to reduce the likelihood of stockouts:

> **Production<sub>t</sub> = F<sub>t</sub> × (1 + B)**

### Example

| Parameter | Value |
|-----------|-------|
| Forecast | 100 croissants |
| Buffer (B) | 10% (0.10) |
| **Production** | **100 × 1.10 = 110** |

---

## 4. Waste Calculation (Overproduction)

If actual sales are **lower** than production:

> **Waste Units = Production<sub>t</sub> − A<sub>t</sub>**
>
> **Financial Waste = Waste Units × C**

### Example

| Parameter | Value |
|-----------|-------|
| Production | 110 |
| Actual Sales | 100 |
| Cost per unit (C) | £1.50 |
| **Waste Units** | **10** |
| **Financial Waste** | **£15.00** |

---

## 5. Underproduction (Missed Revenue)

If demand **exceeds** production:

> **Missed Sales = A<sub>t</sub> − Production<sub>t</sub>**
>
> **Lost Revenue = Missed Sales × P**

This captures the **opportunity cost** — revenue the café could have earned if sufficient stock had been produced.

---

## 6. Forecast Accuracy Metrics

### Forecast Error

> **Error<sub>t</sub> = A<sub>t</sub> − F<sub>t</sub>**

### Mean Absolute Error (MAE)

> **MAE = (1 / n) × Σ |A<sub>t</sub> − F<sub>t</sub>|**

MAE provides an average magnitude of forecasting errors across all evaluated days, independent of error direction.

### Waste Percentage

> **Waste % = (Waste Units / Production<sub>t</sub>) × 100**

This metric expresses waste as a proportion of total production, enabling comparison across products and time periods.

---

## 7. Business Impact

This analysis enables Pink Café to:

- **Reduce food waste** — minimising overproduction through data-driven targets
- **Improve profitability** — balancing production costs against lost revenue
- **Make data-driven production decisions** — replacing intuition with statistical forecasting
- **Compare forecasting models objectively** — using MAE and waste percentage as benchmarks

---

## 8. Summary Table

| Scenario | Condition | Metric | Formula |
|----------|-----------|--------|---------|
| Overproduction | Production > Actual | Financial Waste | (Production − Actual) × Cost |
| Underproduction | Actual > Production | Lost Revenue | (Actual − Production) × Price |
| Accuracy | All days | MAE | Mean of absolute forecast errors |
| Efficiency | All days | Waste % | (Waste Units / Production) × 100 |