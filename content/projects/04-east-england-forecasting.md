---
title: Probabilistic renewable forecasting, East England
meta: KTH EG2140 · 2025 · IEEE competition sponsored by Ørsted and rebase.energy
summary: >
  Day-ahead probabilistic forecasts of combined wind and solar output for Hornsea 1 and East
  England solar, submitted as quantiles and scored on pinball loss.
tags: [Python, LightGBM, CatBoost, Random forest, Pinball loss]
---

## The task

An IEEE Power & Energy Society competition, sponsored by Ørsted and rebase.energy: forecast
the combined wind and solar generation of **Hornsea 1** — a 1.2 GW offshore wind farm 120 km
off the Yorkshire coast — together with East England's solar capacity.

Forecasts were day-ahead, for each half-hour period, submitted as **quantiles in 10%
increments from 10% to 90%** and scored on pinball loss. Models were trained and tested on
2020–2023 data, with the explicit aim of beating previous competitors' results.

## Why probabilistic

A point forecast of wind output answers the wrong question. If you are deciding how much
reserve to hold, or what to bid, you need to know how wrong the forecast might be and in
which direction. Pinball loss rewards exactly that: a model that is confident when it should
be and uncertain when it should be.

This was my first serious work with quantile forecasting, and the technique is the direct
ancestor of what I now do professionally on imbalance volumes.

## Approach

Random forest regression, LightGBM and CatBoost, each trained on generation-site data, then
combined into an **ensemble producing a weighted combination of their predictions**.
Evaluated across several error measures in addition to the competition metric.

The ensemble was the strongest model, which is the expected result but worth confirming
empirically — it inherits each component's strengths and averages out their individual
failure modes.

## Context

Team project with Tilde Franzén and Victor Pettersson. Supervised by Xavier Weiss, with
Sebastian Haglund as industry mentor.
