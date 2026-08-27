---
title: Multicriteria load control for a domestic water heater
meta: KTH EI2525 · 2025 
summary: >
  A plug-in box that decides when a household water heater should run. Forecasting,
  optimisation and real-time control in one loop — built, wired and tested on a bench.
tags: [Python, Linear programming, Raspberry Pi 5, Arduino, Triac, Nord Pool · SMHI]
report: ei2525-multicriteria-load-control.pdf
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/multicriteria-load-control
---

## Scope

A plug-in controller deciding when a domestic water heater runs, optimising electricity cost
against PV self-consumption while respecting comfort limits. The tank is thermal storage, so
heating can be shifted without the user noticing.

Two market changes made it worth building: Nord Pool moved to **quarter-hourly** prices on
1 October 2025, and Swedish network operators apply power-based tariffs penalising monthly
peaks.

## What I built

- **Day-ahead optimisation** — a linear program on a 15-minute grid. The tank is modelled as
  finite thermal storage with standing losses and the heater's 2.2 kW rating as a hard cap,
  with comfort constraints on state of charge and a peak-avoidance term.
- **Real-time supervision** — a loop running every ten seconds on live smart-meter data,
  detecting unexpected PV surplus and overriding the schedule, then rebalancing later to stay
  inside the daily energy budget.
- **Hardware** — Raspberry Pi 5 driving an Arduino over USB serial, with a triac power stage
  and zero-crossing detector for duty-cycle modulation. Prices from Nord Pool SE3, PV from
  Forecast.Solar, weather from SMHI, live consumption over the smart meter's HAN interface.

## Results

Run on 30 November 2025 to schedule the following day. The optimiser pre-heated through the
cheap early-morning hours to ~17.6 kWh, drew down across the expensive middle of the day,
and never fell below the 6 kWh comfort threshold — slack zero in every interval, so all
hot-water demand was met. The heater was forced off during the three highest-load intervals
and modulated between 1.4 and 2.2 kW elsewhere.

Bench testing validated the full chain: the oscilloscope trace shows the zero-crossing
square wave, the Arduino trigger pulse and the truncated sine feeding the load, running
autonomously.

## Limitations

Not yet tested on a real water heater — thermal results are simulation, and without a
temperature sensor the controller runs on a placeholder state of charge. Current sensing was
not built, so triac firing is open loop. Testing used a resistive light bulb rather than a
heating element.
