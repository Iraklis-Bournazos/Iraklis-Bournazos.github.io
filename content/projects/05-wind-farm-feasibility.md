---
title: Wind farm feasibility study, Skärvagshållan
meta: KTH EG2340 · 2025 · team project
summary: >
  Technical and economic assessment of an 80 MW wind farm in mountainous central Sweden.
tags: [MATLAB, Python, Jensen wake model, LCOE / NPV, BESS sizing]
report: eg2340-wind-farm-feasibility.pdf
links:
  - label: Code on GitHub
    url: https://github.com/tilfra/WindProject_Team2
---

## Scope

An 80 MW onshore wind farm at Skärvagshållan, a mountainous site in central Sweden inside
bidding zone **SE3**. The question was whether the project should be built.

## What I investigated

- **Turbine technology** — the four generator concepts, then wind class, cold-climate
  package, turbulence and transport into complex terrain
- **Layout and wake losses** — modelled with the Jensen wake model, validated against the
  Renewables.ninja benchmark
- **Grid connection** — nine candidate buses, voltage rise, reactive power capability
- **Economics** — NPV and LCOE across the investment-cost range over a 25-year lifetime
- **Storage** — hybrid BESS sizing against SE3 prices under a constrained export connection

## What came out

**Vestas V136** full converter, two-row staggered layout. The ridge-aligned arc at 7D
spacing yields more energy, but needs 13.9 × 12.8 km — more than the site allows, and at 4D
its advantage disappears.

**Grid connection decides more than cost.** Ignoring line impedance, all nine buses accept
80 MW and the 10 kV node looks cheapest. Including it, voltage rise makes 10 kV and 20 kV
infeasible; only the 70 kV side of the 20/70 kV transformer stays inside grid-code limits.

**Profitability turns on the investment cost**, not the wind resource: NPV +109 MSEK at
0.852 BSEK (LCOE 361.6 SEK/MWh), −622 MSEK at 1.58 BSEK (573.2 SEK/MWh).

**A 45 MWh battery** raises annual net revenue by about 4.6% by recovering curtailed energy.
133 MWh shows clear diminishing returns.
