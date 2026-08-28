---
title: Probabilistic renewable forecasting, East England
meta: KTH EG2140 · 2025 
summary: >
  Day-ahead probabilistic forecasting for the Hornsea 1 offshore wind farm and an East England solar farm.
tags: [Python, CatBoost, LightGBM, Quantile stacking, Pinball loss]
report: eg2140-east-england-forecasting.pdf
---

## The task

An IEEE Power & Energy Society competition sponsored by Ørsted and rebase.energy: forecast
the combined wind and solar generation of **Hornsea 1** — a 1.2 GW offshore wind farm off the
Yorkshire coast — together with East England's solar output.

Day-ahead, per half-hour period, submitted as **quantiles from 10% to 90%** and scored on
pinball loss. Trained and tested on 2020–2023.

## Approach

Three base models — random forest, LightGBM and CatBoost — combined in a **stacked
ensemble**. For each quantile level separately, the base models' validation predictions
become input features to a meta-model trained with `QuantileRegressor` under pinball loss,
so the ensemble can weight the base models differently per quantile.

## Results

| Model | MAE (MWh) | R² | Pinball (MWh) |
|---|---|---|---|
| Naive benchmark | 146.28 | 0.459 | 73.14 |
| LightGBM | 131.02 | 0.604 | 30.45 |
| Random forest | 79.40 | 0.836 | 34.21 |
| CatBoost | 74.65 | 0.841 | 30.08 |
| **Ensemble** | 75.85 | **0.844** | **29.39** |

Pinball loss down roughly **60% against the benchmark**, R² from 0.46 to 0.84. The
competition's top fifteen entries scored between **22.18 and 33.92 MWh**, so 29.39 sits
within the range of the leading entries.

