---
name: Iraklis Bournazos
tagline: Electrical engineer — energy forecasting and power systems
location: Stockholm, Sweden
email: bournazosiraklis@gmail.com
phone: "+46 70 498 45 95"
linkedin: linkedin.com/in/iraklis-bournazos
github: github.com/Iraklis-Bournazos
site: iraklis-bournazos.github.io

summary: >
  Electrical and computer engineer with an MSc in Electric Power Engineering from KTH,
  specialising in power system operation, planning and electricity markets. I build
  forecasting systems for net load, renewable generation, prices and imbalance — and I am
  equally at home in the power system engineering underneath them.

experience:
  - when: Jun 2026 — present
    role: Data Scientist Intern
    org: rebase.energy
    place: Stockholm, Sweden
    bullets:
      - Built an end-to-end, leakage-free imbalance volume forecasting pipeline for the
        Swedish bidding zones, with dedicated models for each forecast lead time.
      - Produced probabilistic forecasts using quantile regression with conformal
        calibration, adding tail-exceedance spike detection and directional probabilities
        of system imbalance.
      - Designed a Boruta-style shadow-feature importance pipeline and per-horizon
        correlation studies across weather prediction models and intraday and day-ahead
        market data, and implemented transformer time-series foundation models as an
        input generator for short-term accuracy.

  - when: Jan 2026 — Aug 2026
    role: MSc Thesis Project
    org: rebase.energy
    place: Stockholm, Sweden
    bullets:
      - Designed and implemented a modular end-to-end machine learning framework for
        day-ahead net load forecasting across 350 Norwegian municipalities, using
        LightGBM, CatBoost, XGBoost and ensemble modelling on open Elhub AMI metering
        data and ERA5 weather reanalysis.
      - Disaggregated forecasting by consumer segment — residential, commercial and
        industrial — and showed that industrial net load is a structurally different
        problem requiring a hybrid deployment strategy.
      - Investigated behind-the-meter solar PV penetration and grid observability, and
        established through a controlled synthetic experiment that the limiting factor is
        data visibility rather than model architecture.
      - Built the preprocessing and feature pipelines, with residual analysis, bias
        correction and drift handling for robustness under changing conditions.

  - when: Nov 2023 — Apr 2024
    role: Lab & Research Assistant
    org: Electric Devices and Decision Systems Lab, NTUA
    place: Athens, Greece
    bullets:
      - Researched artificial intelligence techniques for smart grids and power forecasting.
      - Worked with LSTM, Bi-LSTM, GRU, random forest and XGBoost models for wind power
        forecasting, and designed stacked meta-learning architectures.

  - when: Sep 2021 — May 2023
    role: Platform Administrator
    org: Climate Change Hub
    place: Athens, Greece
    bullets:
      - Contributed to the development of the organisation's platform, and integrated
        corporate social responsibility data from partner organisations.

education:
  - when: Aug 2024 — Aug 2026
    degree: MSc, Electric Power Engineering
    org: KTH Royal Institute of Technology
    place: Stockholm, Sweden
    notes:
      - "Two-year degree, 120 ECTS. Specialisation: power system operation, planning,
        control and electricity markets."
      - "Degree project: A Municipal-Scale Net Load Forecasting Framework for Norway,
        carried out at rebase.energy."

  - when: Dec 2018 — Apr 2024
    degree: Diploma, Electrical and Computer Engineering
    org: National Technical University of Athens
    place: Athens, Greece
    notes:
      - "Five-year integrated degree, 300 ECTS. Major in Electric Power and Energy Systems,
        grade 8.01/10. Thesis: Wind Turbine Energy Forecasting with Machine Learning and
        Meta-Learning Methods."

  - when: Sep 2021 — Apr 2024
    degree: Minor, Leadership and Management
    org: American College of Greece
    place: Athens, Greece — GPA 3.68/4, taken alongside the NTUA diploma

projects:
  - when: 2025
    title: Multicriteria Load Control — price-responsive water heater controller
    org: KTH EI2525, Electric Power Engineering Project
    text: >
      Linear-programming scheduler running a domestic water heater against spot prices and PV
      forecasts, with a real-time supervisory loop on live smart-meter data. Raspberry Pi 5,
      Arduino triac stage, zero-crossing detector.

  - when: 2025
    title: Probabilistic renewable generation forecasting, East England
    org: KTH EG2140 — IEEE competition sponsored by Ørsted and rebase.energy
    text: >
      Day-ahead probabilistic forecasts for Hornsea 1 and East England solar, submitted as
      quantiles and scored on pinball loss. Random forest, LightGBM and CatBoost ensemble.

  - when: 2025
    title: Wind farm feasibility and techno-economic study, bidding zone SE3
    org: KTH EG2340, Wind Power Systems
    text: >
      80 MW wind farm in central Sweden — turbine selection, layout and electrical topology,
      grid connection costing, LCOE and NPV across an investment range, BESS sizing on SE3 prices.

  - when: 2025
    title: Hydro scheduling and power system planning
    org: KTH EG2240, Power System Planning
    text: >
      Deterministic and stochastic short-term and long-term hydro scheduling for a cascaded
      four-plant river system in GAMS, with Monte Carlo valuation of flexibility across SE1–SE4.

skills:
  - group: Programming
    items: Python, MATLAB, GAMS, Octave, Git/GitHub
  - group: Data & machine learning
    items: pandas, polars, NumPy, xarray, GeoPandas, scikit-learn, LightGBM, CatBoost,
      XGBoost, PyTorch, Hugging Face Chronos, conformal prediction (puncc)
  - group: Power system tools
    items: PandaPower, PowerFactory, Simulink, ARISTO, PSpice, LTspice, PLECS, FEMM, pvlib
  - group: Energy data
    items: Elhub, ENTSO-E, Nord Pool, ERA5, SMHI, Kartverket

languages: "English — fluent (C2) · Greek — native · French — intermediate (B2) ·
  Swedish — beginner (A2), actively learning"

awards:
  - "Stavros Niarchos Foundation Scholarship for Academic Excellence, 2021–2024"
  - "Deree Merit Scholarship for Academic Excellence, 2021–2024"
  - "Award of Democracy and Oratory Award, Model Hellenic Parliament, 2021"
  - "Elected member of student council, NTUA, 2019–2020"
---
