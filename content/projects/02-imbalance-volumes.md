---
title: Imbalance volume forecasting for the Swedish bidding zones
meta: rebase.energy · 2026
summary: >
  An end-to-end pipeline forecasting imbalance volumes across the Swedish bidding zones,
  with dedicated models per lead time and probabilistic output built for the tails.
tags: [Python, Quantile regression, Conformal prediction, Time-series transformers]
muted_tags: [Internal work]
---

## Why imbalance is a different problem

System imbalance is not load. It is the residual of everything that did not go according to
plan — forecast error, outages, market behaviour — and it is dominated by the hours when
something unusual happened. A model tuned to minimise average error will be excellent on the
quiet hours that nobody cares about and useless on the ones that cost money.

That shapes every decision in the pipeline.

## Structure

The pipeline forecasts imbalance volumes across the Swedish bidding zones with **dedicated
models per lead time** rather than one model asked to cover every horizon. What is knowable
about hour *h+1* is not what is knowable about hour *h+36*, and collapsing those into a
single model quietly wastes information at short horizons.

The whole thing is built to be **leakage-free**: at every horizon, the model sees only what
would genuinely have been available at that moment. This is less trivial than it sounds when
market data, forecasts and settlement values all arrive on different schedules.

## Probabilistic output

The output is a distribution, not a number:

- **Quantile regression** for the shape of the distribution
- **Conformal calibration** so the intervals mean what they claim to mean
- **Tail-exceedance spike detection** for the extreme hours specifically
- **Directional probabilities** — the probability that the system is long or short, which is
  often the decision-relevant quantity rather than the magnitude

## Feature selection

Feature selection uses a **Boruta-style shadow-feature pipeline**: real features must
outperform randomised copies of themselves to survive. Alongside that, per-horizon
correlation studies across numerical weather prediction models, intraday market data and
day-ahead market data, since which sources matter changes substantially with lead time.

I also implemented **transformer time-series foundation models** as an input generator,
using their outputs as features to improve short-term accuracy.

## Note

This is internal work at [rebase.energy](https://www.rebase.energy/) and the code is not
public. I am happy to talk about the approach in general terms.
