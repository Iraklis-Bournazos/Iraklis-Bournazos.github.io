---
title: Electrical machines — parameter estimation and control
meta: KTH EJ2201, Electrical Machines and Drives · 2024
summary: >
  DC, synchronous and induction machines, combining laboratory measurements, parameter
  identification, mathematical modelling and simulation in MATLAB/Simulink.
tags: [MATLAB, Simulink, Parameter estimation, MTPA]
reports:
  - label: DC machines report (PDF)
    file: ej2201-dc-machine-parameter-estimation.pdf
  - label: AC machines report (PDF)
    file: ej2201-ac-machines-control.pdf
---

The first part builds a DC machine model directly from experimental data. The second extends
the analysis to AC machines — torque modelling, Maximum Torque Per Ampere operation and
magnetic saturation effects.

## DC machine parameter estimation

I characterised a 3 kW, 1500 rpm DC machine using laboratory measurements from its armature and excitation circuits. The raw voltage and current signals were first processed to remove measurement offsets and separate steady-state and transient regions before estimating the machine parameters.

From the measurements, I estimated the armature and field resistances and inductances, as well as the machine flux constant. In particular, the inductances were obtained from the relationship between current and integrated flux linkage, using regression to extract the slope of the resulting characteristics.

These parameters were then used to build a dynamic DC machine model in Simulink, representing the armature, excitation and mechanical subsystems. I validated the model by comparing its simulated torque–speed characteristic against theoretical MATLAB calculations, obtaining closely matching behaviour across multiple operating points.

## AC machines and control

The second part focused on interior permanent-magnet synchronous machines (IPMSMs) and induction machines.

For the IPMSM, I modelled electromagnetic torque in the d–q reference frame and generated iso-torque maps across the operating current range. I then derived and plotted the Maximum Torque Per Ampere trajectory to identify the current combinations that produce the required torque with minimum stator current.

For the induction machine, I reformulated the torque equations using an inverse-Γ equivalent model and derived the corresponding MTPA trajectory. The calculated rated torque was consistent with the machine nameplate data.

I also investigated magnetic saturation by modelling the magnetising inductance as a nonlinear function of stator current. Comparing the linear and nonlinear cases showed how saturation changes the iso-torque characteristics while having relatively little effect on the MTPA trajectory in the analysed operating range.

