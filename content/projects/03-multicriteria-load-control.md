---
title: Multicriteria load control for a domestic water heater
meta: KTH EI2525 · 2025 · with Dio Randa Damara and Hadrien Guillaud
summary: >
  A plug-in box that decides when a household water heater should run. Forecasting,
  optimisation and real-time control in one loop, on real hardware.
tags: [Python, Linear programming, Raspberry Pi 5, Arduino, SMHI · Nord Pool]
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/multicriteria-load-control
---

## The opportunity

A domestic water heater is close to an ideal flexibility resource. The tank is thermal
storage: heat the water early and it is still hot later. Nobody notices *when* the heating
happened, only whether there is hot water when they want it.

Two things made this worth building in 2025. Nord Pool day-ahead prices moved from hourly to
quarter-hourly resolution on 1 October, and many Swedish network operators now apply
power-based tariffs that penalise monthly peaks. Meanwhile compensation for exporting PV
energy to the grid is modest. Shifting heating into cheap or high-PV periods is therefore
worth real money — provided something is actually making that decision.

## The three layers

**Long-term screening** looks several days ahead for favourable conditions — low spot prices
and high expected PV — to inform strategic pre-heating.

**Day-ahead optimisation** is a linear program computing a 24-hour schedule. The tank is
modelled as finite thermal storage with standing losses and a 1 kW power cap. The objective
trades grid cost against PV self-consumption, subject to comfort constraints that keep the
tank state of charge inside its bounds at all times, so hot-water availability is never
sacrificed to save money.

**Real-time supervision** runs every ten seconds against live smart-meter data over the home
area network. When it detects unexpected solar surplus in the export measurement, it boosts
heater power to absorb it rather than exporting at a poor price; it then reduces heating
during expensive periods later to stay within the daily energy budget. This is what handles
the gap between the forecast and what the day actually did.

## The hardware

A prototype built on a Raspberry Pi 5 running the optimisation and supervision, an Arduino
microcontroller driving a **triac power stage** with a **zero-crossing detector** for
duty-cycle modulation of the resistive load. Price data from Nord Pool, weather and PV
forecasts from SMHI, live consumption and export from the smart meter's HAN interface.

The honest status at hand-in: the software chain was working and simulations showed reduced
grid cost and higher PV utilisation with the tank always inside its comfort bounds, but the
hardware still needed full laboratory testing to confirm the duty-cycle modulation approach.

## Why I like this one

Most student projects stop at the simulation. This one had to close the loop: a forecast
feeds an optimiser, the optimiser produces a schedule, the schedule drives a triac, and the
triac heats actual water — and then reality diverges from the forecast and something has to
notice and react. Every layer had to be correct for the last one to work.

Supervised by Nathaniel Taylor and examined by Lina Bertling Tjernberg.
