---
title: Power electronics and electrical machines
meta: KTH EJ2301 & EJ2201 · 2024–2025
summary: >
  Hardware-level coursework behind the systems work — converter component selection from
  datasheets, and machine parameter estimation from laboratory measurements.
tags: [MATLAB, Simulink, PSpice, Parameter estimation]
---

The forecasting and market work is what I do day to day, but it sits on top of physical
equipment, and I think it matters to understand that equipment properly rather than treat it
as an abstraction. Three pieces of coursework where the answer had to match measured
reality:

## Buck converter design

A step-down DC-DC converter designed from a specification — 500–580 V input, 20 A maximum
load current. Component selection worked from real datasheets: allowing voltage margin for
switching overshoot ruled out everything below a 1200 V rating, which selected the
APT20GF120BR IGBT at 20 A continuous at 90 °C. Then filter design, loss calculation,
thermal sizing and simulation.

[Read the report (PDF)](../files/projects/ej2301-buck-converter-design.pdf)

## DC machine parameter estimation

A 3 kW, 1500 rpm DC machine characterised from laboratory measurements of the armature and
excitation circuits, with the estimated parameters used to build a Simulink model whose
steady-state torque–speed behaviour was verified against theory.

The detail I enjoyed: a sharp voltage drop appears across the diode at the start of the
discharge phase when the switch opens, because the measurement contains a real diode rather
than an ideal component. Small discrepancies between measurement and model usually mean
something physical, not noise.

[Read the report (PDF)](../files/projects/ej2201-dc-machine-parameter-estimation.pdf)

## AC machines and control

Synchronous and induction machine modelling and control — parameter identification from lab
data, the induction machine represented with an inverse-Γ model, and torque analysis of an
IPMSM including the maximum-torque-per-ampere trajectory, aimed at energy-efficient
operation.

[Read the report (PDF)](../files/projects/ej2201-ac-machines-control.pdf)
