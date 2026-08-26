---
title: Wind farm feasibility study, central Sweden
meta: KTH EG2340 · 2025 · team project
summary: >
  Technical and economic assessment of an 80 MW wind farm in a mountainous site in bidding
  zone SE3 — turbine selection through to battery sizing and LCOE.
tags: [MATLAB, Python, LCOE / NPV, BESS sizing]
links:
  - label: Code on GitHub
    url: https://github.com/tilfra/WindProject_Team2
---

## Scope

A full feasibility study for an **80 MW wind farm** on a mountainous site near Idre fjäll, in
bidding zone **SE3**. Not a modelling exercise in isolation — the question was whether this
particular project should be built.

## Turbine technology

The study starts by comparing the four generator concepts — the fixed-speed Danish concept,
variable resistance, doubly-fed induction generator, and full converter — and then narrows by
wind class, turbine size, cold-climate package and sound emissions, which matter a great deal
at a mountainous Swedish site.

The selected turbine was the **Vestas V136-3.45**, arranged in a **staggered formation** with
an **open-ring electrical layout** after comparing several topological and electrical
alternatives.

## Grid connection and economics

Grid connection options were explored and costed. Net present value and levelised cost of
energy were then calculated across a range of investment costs rather than a single point
estimate.

That range is where the study earns its keep. **At the lower bound of investment cost the
project is profitable; at the upper bound it is not.** The feasibility of the project is
decided by an assumption, not by the wind resource — which is a more useful conclusion than
a single confident NPV figure would have been.

## Storage

Finally, a hybrid battery energy storage system was evaluated against SE3 price data. Adding
storage increases total revenue, and the optimal battery size shifts with the assumed
investment cost — so the storage decision is coupled to the same uncertainty as the farm
itself.

## Team

Team 2: Iraklis Bournazos, Tilde Franzén, Victor Pettersson, Berzan Uyar and Mingyu Xie.
