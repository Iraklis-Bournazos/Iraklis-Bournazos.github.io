---
title: Multicriteria load control for a domestic water heater
meta: KTH EI2525 · 2025 · with Dio Randa Damara and Hadrien Guillaud
summary: >
  A plug-in box that decides when a household water heater should run. Forecasting,
  optimisation and real-time control in one loop — built, wired and tested on a bench.
tags: [Python, Linear programming, Raspberry Pi 5, Arduino, Triac, Nord Pool · SMHI]
report: ei2525-multicriteria-load-control.pdf
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/multicriteria-load-control
---

## Why a water heater

A domestic water heater is close to an ideal flexibility resource. The tank is thermal
storage: heat the water early and it is still hot later. Nobody notices *when* the heating
happened, only whether there is hot water when they want it.

Two things made this worth building in 2025. Nord Pool day-ahead prices moved from hourly
to **quarter-hourly** resolution on 1 October, and Swedish network operators increasingly
apply power-based tariffs that penalise monthly peaks. Meanwhile compensation for exporting
PV to the grid is modest. Shifting heating into cheap or high-PV periods is worth real
money — provided something is making that decision.

## Three layers

**Screening** looks several days out for favourable conditions — low prices, high expected
PV — to inform strategic pre-heating.

**Day-ahead optimisation** is a linear program on a **15-minute** grid, matching the new
market resolution. The tank is modelled as finite thermal storage with standing losses and
the heater's 2.2 kW rating as a hard cap. The objective trades grid cost against PV
self-consumption, subject to comfort constraints on the tank state of charge, plus a
peak-avoidance term that forces the heater off during the household's highest-load
intervals.

**Real-time supervision** runs every ten seconds against live smart-meter data over the home
area network. When it sees unexpected solar surplus in the export measurement it boosts
heater power to absorb it rather than exporting at a poor price, then reduces heating in
expensive periods later to stay inside the daily energy budget. This is the layer that
handles the gap between the forecast and what the day actually did.

## What it does on a real day

The full pipeline ran on 30 November 2025 at 11:55 to produce the schedule for 1 December —
the same sequence a deployed system would follow.

The optimiser pre-heated the tank through the cheap early-morning hours, reaching about
17.6 kWh of stored energy, then let it draw down through the expensive middle of the day
(07:00–16:00), never dropping below the 6 kWh comfort threshold. The slack variable stayed
at zero for every interval, meaning all hot-water demand was met. During the three
highest-load intervals the heater was forced off entirely; elsewhere it modulated between
1.4 and 2.2 kW.

It was a Swedish winter day, so PV surplus was zero and the heater ran on grid energy
throughout. The saving came purely from *when* it ran. That is the honest version of the
result — the machinery worked, but December in Sweden is not where PV self-consumption pays.

## The hardware, and that it actually ran

Raspberry Pi 5 running optimisation and supervision, talking over USB serial to an Arduino
driving a **triac power stage** with a **zero-crossing detector** for duty-cycle modulation
of the resistive load. Prices from Nord Pool SE3, PV forecasts from Forecast.Solar, weather
from SMHI, live consumption and export from the smart meter's HAN interface.

We assembled the zero-crossing detector on perfboard, put it in an enclosure, and tested the
full chain on the bench. The final validation was an oscilloscope trace showing three
signals together: the detector's square wave, the Arduino's trigger pulse, and the truncated
sine feeding the load — a light bulb visibly changing brightness under the optimiser's
decisions, running autonomously.

## What it does not do yet

The report is explicit about this, and it is worth repeating:

- **Never tested on a real water heater.** All thermal results are simulation. Without a
  temperature sensor or a state-of-charge estimator, the real-time controller runs on a
  placeholder SOC value, so comfort constraints cannot be genuinely enforced.
- **Open-loop actuation.** The current-sensing stage was not built in the time available, so
  triac firing assumes a linear relationship between delay angle and delivered power — an
  approximation that will not hold under a distorted mains waveform.
- **The zero-crossing detector dissipates more power than expected** and needs a redesign for
  long-term use.
- **Tested on a light bulb**, not a high-power heating element, and not over extended periods.

## Why I like this one

Most student projects stop at the simulation. This one had to close the loop: a forecast
feeds an optimiser, the optimiser produces a schedule, the schedule becomes a triac firing
pattern, and the triac heats something — and then reality diverges from the forecast and
something has to notice and react within ten seconds. Every layer had to be right for the
last one to work, and the failure modes were physical rather than statistical.

Supervised by Nathaniel Taylor, examined by Lina Bertling Tjernberg.
