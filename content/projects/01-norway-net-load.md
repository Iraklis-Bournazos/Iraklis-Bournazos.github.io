---
title: Municipal-scale net load forecasting for Norway
meta: MSc thesis · rebase.energy & KTH · 2026
summary: >
  Day-ahead net load forecasts for all 350 Norwegian municipalities, disaggregated by
  consumer segment and built entirely on open data. The most useful result is a negative one.
tags: [Python, LightGBM, Elhub AMI, ERA5, GeoPandas]
report: msc-thesis-net-load-forecasting-norway.pdf
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/norway-net-load-forecasting
---

## The problem

Distribution system operators, traders and flexibility providers all need to know what
tomorrow's load looks like at the grid boundary. That boundary is moving. Norway's
*Plusskunde* net-metering scheme lets households with installations up to 100 kW export
surplus generation, and rooftop solar has spread quickly.

The consequence is the **behind-the-meter invisibility problem**. What a DSO measures is
net load — gross consumption minus whatever the roof produced and the household consumed
on site. Self-consumed solar never crosses any metering point the operator owns, so it is
structurally unobservable from the operator's own data. The DSO sees only the difference
and cannot decompose it.

My question: can you forecast that net load, at municipal resolution, across an entire
country, using nothing but public data?

## The data

Elhub publishes hourly AMI metering for Norway, already split by consumer category —
private residential, commercial and industrial — along with solar export records and daily
installed-capacity snapshots. Weather comes from ERA5 reanalysis, matched to each
municipality by a weather-station selection procedure that picks the most representative
grid cell. No proprietary data anywhere, so the results are reproducible.

## Three stages, not one model

1. **National weather feature ablation** across all 350 municipalities, to find which
   weather variables actually earn their place.
2. **Six-fold expanding-window walk-forward evaluation** on eight municipalities chosen to
   span the full solar-penetration spectrum, comparing several model formulations.
3. **Three-fold national validation** over the unseen 2025 calendar year.

Forecasting runs per consumer segment, because the three segments turn out to be different
problems rather than three instances of one.

## What the results say

Temperature dominates everything. The ablation puts its contribution at **+5.74 percentage
points** of MAPE reduction for residential load, +4.21 pp for commercial and +2.00 pp for
industrial.

The weather-based LightGBM model became the national default. For residential net load it
reaches a mean annual municipality MAPE of **6.69%**, beating the seasonal naive benchmark
in **347 of 350 municipalities** and the best linear-regression baseline in 246 of 350.
Commercial load reaches 9.66% MAPE, winning in 313 of 350 against naive.

The linear baseline is not merely worse — it *collapses* on industrial load, at 63.3%
annual mean MAPE. That is the cleanest evidence in the thesis that the non-linear
architecture is a structural necessity here rather than a fashionable choice.

## The negative result, which is the useful one

The prosumer-aware model — the one given solar capacity and export features — produced no
systematic national improvement. Its mean gain was **−0.03 pp** across 350 municipalities.
No penetration tier showed a robust win.

The obvious conclusion is that the model is inadequate. A controlled synthetic experiment
says otherwise: given exact, noiseless capacity information, the same architecture improves
consistently across every growth scenario and every fold, by **+0.16 to +0.37 pp**.

So the architecture is sound and the failure is in the data. Three causes, all structural:
behind-the-meter invisibility, solar penetration that is still low, and contamination in the
registry itself — Elhub's E19 metering category pools residential, commercial, agricultural
and industrial generation together, each with different self-consumption ratios and diurnal
profiles, so using it as a residential-solar proxy imports noise that cannot be removed
without disaggregating the registry.

**This matters for anyone deciding where to spend money.** If a DSO is choosing between
better forecasting models and better visibility of distributed generation, this says: fix
the visibility first. The models are already ahead of the data.

The operational answer under current conditions is a conservative portfolio: deploy the
prosumer-aware model only in the 48 municipalities (13.7%) where it improves consistently
across every fold, and the weather-based model everywhere else. That never underperforms
the weather-based model anywhere in the portfolio.

## Industrial load is a different problem

Norwegian industrial consumption concentrates in large energy-intensive facilities running
on production schedules that have little to do with weather or calendars. Weather-and-calendar
features reach their generalisation limit, and the win rate against naive sits near 50%.
The recommendation is a two-category hybrid — seasonal naive for continuous-process
municipalities, and the weather model with spot-price features for heterogeneous urban ones.

## Being honest about the ceiling

The reported accuracy is an **upper bound**, not an operational figure. Weather features come
from ERA5 reanalysis — historically observed conditions, not forecasts. In production, NWP
forecast error would degrade this. ERA5's ~31 km grid also cannot resolve sub-municipal
variation, so municipalities where the load centre sits away from the assigned cell — fjord
microclimates, elevation differences, spatially concentrated industry — carry a systematic
mismatch.

## Context

Carried out at [rebase.energy](https://www.rebase.energy/) as my KTH degree project.
Supervisors: Valgerður Jónsdóttir, Ilias Dimoulkas and Sebastian Haglund. Examiner: Lars
Nordström.
