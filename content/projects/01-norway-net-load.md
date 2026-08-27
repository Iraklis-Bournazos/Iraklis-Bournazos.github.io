---
title: Municipal-scale net load forecasting for Norway
meta: MSc thesis · rebase.energy & KTH · 2026
summary: >
  Day-ahead net load forecasts for all 350 Norwegian municipalities, disaggregated by
  consumer segment.
tags: [Python, LightGBM, Elhub AMI, ERA5, GeoPandas]
report: msc-thesis-net-load-forecasting-norway.pdf
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/norway-net-load-forecasting
---

## The problem

What a DSO measures at the grid boundary is net load — consumption minus behind-the-meter
generation consumed on site. Self-consumed solar never crosses a metering point the operator
owns, so it is structurally unobservable. Norway's *Plusskunde* scheme, which lets households
export from installations up to 100 kW, has made this grow quickly.

**Main question:** how efficiently can net load be forecast at municipal resolution, across
an entire country, using nothing but public data?

## Data

Elhub hourly AMI metering, already split into private residential, commercial and industrial,
with solar export records and daily installed-capacity snapshots. ERA5 reanalysis weather,
matched to each municipality by a weather-station selection algorithm.

## Framework

1. **National weather feature ablation** across all 350 municipalities
2. **Six-fold expanding-window walk-forward evaluation** on eight municipalities spanning the
   solar-penetration spectrum
3. **Three-fold national validation** on the unseen 2025 calendar year

Forecasting runs per consumer segment, because the three behave as different problems.

## Results

The weather-based LightGBM model became the national default. Residential net load reaches a
mean annual municipality MAPE of **6.69%**, beating the benchmark in **347 of 350
municipalities** and the linear-regression baseline in 246 of 350. Commercial reaches 9.66%,
winning in 313 of 350.

Industrial is structurally different: production schedules are uncorrelated with weather and
calendar, and the win rate sits near 50%. The recommendation is a two-category hybrid.

## The synthetic experiment

The prosumer-aware model — given solar capacity and export features — produced **no**
systematic national improvement: mean gain −0.03 pp across 350 municipalities.

A controlled synthetic experiment isolates why. Given exact, noiseless capacity information,
the same architecture improves consistently across every growth scenario and fold, by
**+0.16 to +0.37 pp**. The architecture is sound; the limit is in the data — behind-the-meter
invisibility, low penetration, and contamination in the registry, since Elhub's E19 category
pools residential, commercial, agricultural and industrial generation together.

The operational answer is a conservative portfolio: deploy the prosumer-aware model only in
the 48 municipalities (13.7%) where it improves across every fold, and the weather-based
model elsewhere. For a DSO choosing between better models and better visibility of
distributed generation, this says: fix the visibility first.
