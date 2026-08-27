---
title: Imbalance volume forecasting for the Swedish bidding zones
meta: rebase.energy · 2026
summary: >
  An end-to-end pipeline forecasting imbalance volumes across the Swedish bidding zones,
  with dedicated models per lead time and probabilistic output built for the tails.
tags: [Python, Quantile regression, Conformal prediction, Time-series transformers]
muted_tags: [Internal work]
---

## Scope

Forecasting the 15-minute system imbalance volume in SE3, from 15 minutes up to 12 hours ahead, using probabilistic machine-learning models built around the information that would actually have been available at each prediction time.

The target is the signed balancing volume activated by the TSO: positive values indicate a short system requiring up-regulation, while negative values indicate a long system requiring down-regulation.

## Modelling approach

I built 15 independent single-horizon XGBoost models, one for each lead time from 15 minutes to 12 hours. Each horizon has its own feature set because the useful information changes substantially with lead time. Also a pooled strategy was tested and evaluated.

The pipeline was designed to be fully leakage-safe. Measured quantities, forecasts and market data were shifted according to their real publication delays, so every model only sees information that would genuinely have existed at issue time.

## Probabilistic forecasts

For each horizon it produces:

- **Quantile regression** for the shape of the distribution
- **Conformal calibration** so the intervals mean what they claim to mean
- **Tail-exceedance spike detection** for the extreme hours specifically
- **Directional probabilities** — the probability that the system is long or short, which is
  often the decision-relevant quantity rather than the magnitude
- **SHAP**-based feature attributions

This makes the forecast useful for both expected imbalance magnitude and risk around extreme or directional outcomes.

## Feature engineering and selection

The project combined 4,800+ candidate features from grid, market, weather and forecast data. Sources included ENTSO-E, Nord Pool, JAO, Rebase grid and weather data, together with internally generated driver forecasts.


Feature selection uses a **Boruta-style shadow-feature pipeline**: real features must
outperform randomised copies of themselves to survive. Alongside that, extensive per-horizon
correlation analysis between every candidate input and the target, across numerical weather
prediction models and intraday and day-ahead market data.

I also implemented **transformer time-series foundation models** as an input generator,
using their outputs as features to improve short-term accuracy in different lead times of forecasting.

## Note

This is internal work at [rebase.energy](https://www.rebase.energy/) and the code is not
public. I am happy to talk about the approach in general terms.
