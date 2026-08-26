---
title: Municipal-scale net load forecasting for Norway
meta: MSc thesis · rebase.energy & KTH · 2026
summary: >
  Day-ahead net load forecasts for 350 Norwegian municipalities, disaggregated by consumer
  segment and built entirely on open data. The most interesting result is a negative one.
tags: [Python, LightGBM, Elhub AMI, ERA5, GeoPandas]
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/norway-net-load-forecasting
---

## The problem

Distribution system operators, traders and flexibility providers all need to know what the
next day's load looks like at the grid boundary. That boundary is moving. Norway's
*Plusskunde* net-metering scheme lets households with installations up to 100 kW export
surplus generation, and rooftop solar has been spreading quickly. What a meter records is
no longer consumption — it is consumption minus whatever the roof happened to produce.

The question I set out to answer was whether you can forecast that net load, at municipal
resolution, across an entire country, using nothing but publicly available data.

## The data

Everything comes from open sources. Elhub publishes hourly AMI metering data for Norway,
already disaggregated by consumer category — private residential, commercial and industrial
— along with solar export records and daily snapshots of installed solar capacity. Weather
comes from ERA5 reanalysis. No proprietary datasets, which means the results are
reproducible by anyone.

## The framework

The work is structured as three empirical stages rather than a single model:

1. **A national weather feature ablation** across all 350 municipalities, to establish which
   weather variables actually earn their place.
2. **A six-fold expanding-window walk-forward evaluation** on eight representative
   municipalities chosen to span the full range of solar penetration, comparing several
   modelling approaches.
3. **A three-fold national validation** on the unseen 2025 calendar year.

Forecasting is done per consumer segment, because the three segments turn out to be
genuinely different problems rather than three instances of one problem.

## What came out

For private residential net load, a conservative municipality-level assignment strategy —
deploying a prosumer-aware LightGBM model only in the 48 municipalities where improvement
was consistent across every fold, and a weather-based model in the remaining 302 — beat the
seasonal naive benchmark in 349 of 350 municipalities, and never underperformed the
weather-based model anywhere in the portfolio. Commercial load followed a similar pattern.

Industrial net load did not. It is a structurally different problem: weather-and-calendar
features hit their generalisation limit because facility-level production patterns vary too
much between municipalities to be captured by any shared representation.

## The negative result, which is the interesting one

Adding solar information to the residential model helped almost not at all. The obvious
reading is that the model architecture is inadequate. A controlled synthetic experiment says
otherwise: when the same model is given exact, noiseless capacity information, it improves
consistently, with gains of +0.16 to +0.37 percentage points across several solar growth
scenarios.

So the limit is not architectural. It is **structural behind-the-meter invisibility** —
combined with still-low penetration and a prosumer registry that is heterogeneous between
municipalities. The signal is not in the public data yet, and no amount of modelling
recovers information that was never recorded.

This matters practically. If you are a DSO deciding whether to invest in better forecasting
models or in better visibility of distributed generation, this result says: fix the
visibility first.

## Context

Carried out at [rebase.energy](https://www.rebase.energy/) in Stockholm as my KTH degree
project, supervised by Valgerður Jónsdóttir, Ilias Dimoulkas and Sebastian Haglund, and
examined by Lars Nordström.
