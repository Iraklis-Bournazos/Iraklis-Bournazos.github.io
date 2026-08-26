---
title: Intraday electricity price forecasting, six European markets
meta: Nitor Energy quantitative trading competition · 2026
summary: >
  A competition solution for intraday price forecasting across six European markets, built
  around the part that actually drives the error: spikes.
tags: [Python, LightGBM, Ensembles]
links:
  - label: Code on GitHub
    url: https://github.com/Iraklis-Bournazos/nitor-energy-forecasting
---

## The problem

Intraday electricity prices across six European markets. Forecasting the median hour is not
especially hard; almost any reasonable model does it. The difficulty is concentrated in a
small number of hours.

Price spikes are rare, extreme, and responsible for a disproportionate share of total error.
A model that treats every hour as equally important will optimise for the boring majority and
be badly wrong exactly when being wrong is expensive.

## Approach

The pipeline is therefore built around detecting and handling spikes rather than treating
them as outliers to be smoothed away. Gradient boosting with ensemble combination across
markets, with feature engineering aimed at the conditions that precede extreme prices —
tight margins, unusual cross-border flows, forecast errors in renewables.

## Context

Entered in the Nitor Energy quantitative energy trading competition (Denmark), February 2026.
