---
title: Step-down (buck) DC-DC converter design
meta: KTH EJ2301, Power Electronics · 2024
summary: >
  A full operational design of a buck DC-DC converter, with components selected from real
  datasheets, through to thermal design, feedback control and dynamic simulation.
tags: [MATLAB, PSpice, IGBT selection, Thermal design]
report: ej2301-buck-converter-design.pdf
---

Designed and analysed a high-power buck DC–DC converter for a 500–580 V input range, a regulated 260 V output and loads up to 20 A. The project covered the complete converter design process, from semiconductor and passive-component selection to thermal design, feedback control and dynamic simulation.

I selected the IGBT and freewheeling diode based on voltage/current ratings, switching behaviour, thermal limits and cost, and calculated their conduction and switching losses from manufacturer datasheets. I determined a 7 kHz switching frequency and sized the LC output filter to satisfy the converter's voltage- and current-ripple constraints.

I also designed the thermal management system by deriving the required sink-to-ambient thermal resistance and dimensioning a heat sink for the semiconductor losses.

For the control system, I modelled the converter power stage and PWM dynamics, designed a compensated voltage-feedback controller using the K-factor approach, and evaluated the frequency response in MATLAB. The controller was then implemented and tested in PSpice.

Finally, I compared open- and closed-loop operation and performed a 15 A → 20 A load-step test. The closed-loop system improved voltage regulation and successfully recovered the output voltage to approximately 260 V following the load disturbance.

**Tools & methods:** PSpice · MATLAB · Power Electronics · DC–DC Converters · PWM · Feedback Control · Frequency-Domain Analysis · Thermal Design
