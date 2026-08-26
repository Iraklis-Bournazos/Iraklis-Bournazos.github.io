---
title: Wind farm feasibility study, Skärvagshållan
meta: KTH EG2340 · 2025 · team project
summary: >
  Technical and economic assessment of an 80 MW wind farm in mountainous central Sweden,
  where two of the obvious answers turned out to be wrong once the details were modelled.
tags: [MATLAB, Python, Jensen wake model, LCOE / NPV, BESS sizing]
report: eg2340-wind-farm-feasibility.pdf
links:
  - label: Code on GitHub
    url: https://github.com/tilfra/WindProject_Team2
---

## Scope

A full feasibility study for an **80 MW onshore wind farm** at Skärvagshållan, a mountainous
site in central Sweden inside bidding zone **SE3**. Turbine technology, layout, grid
connection, economics and storage — the question being whether this project should be built,
not whether it could be modelled.

The headline finding is that **technical feasibility was never the constraint**. Economics
and the grid connection dominated the assessment. Two specific results changed the answer
from what the obvious approach would have given.

## Turbine and siting

After comparing the four generator concepts — fixed-speed Danish, variable resistance, DFIG
and full converter — the **Vestas V136 with a full converter** was selected on wind class,
cold-climate package, turbulence tolerance and transportability into complex terrain.

Production was modelled with the manufacturer power curve and the **Jensen wake model**, then
validated against the independent **Renewables.ninja** benchmark, which agreed closely on
capacity factor. The Enercon alternative required a cubic approximation of its power curve,
and that approximation systematically overestimated yield — a reminder that turbine choice
and data quality shape the credibility of everything downstream.

## First surprise: the better layout does not fit

An arced, ridge-aligned configuration at 7D spacing gives higher annual energy production
and lower wake losses than a staggered layout — exactly what theory predicts for turbines
following the prevailing wind along an exposed ridge.

It needs roughly **13.9 km by 12.8 km** of site to do it. That does not fit. Compress the
spacing to 4D so it does fit, and wake losses rise until production falls *below* the
staggered layout.

So the two-row staggered arrangement won — not because it is aerodynamically superior but
because it is the best thing that fits inside the property boundary. Layout optimisation
without land constraints produces an answer you cannot build.

## Second surprise: the cheapest grid connection is infeasible

Nine candidate connection buses were assessed. Ignore line impedance, and all nine
comfortably accommodate 80 MW — and the low-voltage 10 kV node looks best, because
connection charges scale with voltage level.

Include realistic line impedance and the ranking inverts. Voltage rise from the wind
injection pushes the 10 kV point far past its limit, and even the 20 kV bus hits the ceiling
at minimum load. Only the **70 kV side of the 20/70 kV transformer** stays inside grid-code
limits.

Reactive power capability helps — operating at 0.95 capacitive raises the admissible
capacity at every node — but at 80 MW it was never the binding constraint. The impedance
was.

## Economics: the assumption decides the project

Net present value and LCOE across the investment-cost range, over a 25-year lifetime:

| Investment cost | NPV | LCOE |
|---|---|---|
| ≈ 0.852 BSEK (low) | **+109.11 MSEK** | 361.6 SEK/MWh — below captured price |
| ≈ 1.58 BSEK (high) | **−622.02 MSEK** | 573.2 SEK/MWh — above captured price |

The grid connection alone contributes about 187 MSEK. The project is profitable or it is a
disaster depending on which end of the cost range materialises — which is a far more useful
conclusion than a single confident NPV would have been.

## Storage

A hybrid BESS was evaluated against SE3 prices under a constrained 20 MW export connection.
A **45 MWh battery** — a little over half an hour of full farm output — raises annual net
revenue by about **4.6%** net of its own investment cost, mostly by rescuing energy that
would otherwise be curtailed.

Tripling it to 133 MWh raises revenue further but by much less than three times: clear
diminishing returns past a size set by the grid constraint, not by the wind. Larger
batteries only make sense if cell costs fall to around 300 000 SEK/MWh.

## Team

Iraklis Bournazos, Tilde Franzén, Victor Pettersson, Berzan Uyar and Mingyu Xie.
