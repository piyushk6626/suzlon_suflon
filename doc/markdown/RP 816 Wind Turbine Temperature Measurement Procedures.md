<!-- image -->

## RP 816 Wind Turbine Temperature Measurement Procedures

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chairs:

Bruce Hamilton, Navigant Consulting Jim Turnbull, SKF

Principal Author: Eric Bechhoefer, NRG System

## Purpose and Scope

The scope of 'Wind Turbine Temperature Measurement Procedures' discusses the methods and procedures to facilitate temperature based condition monitoring. Temperature is available from most supervisory control and data acquisition systems (SCADA) and provides a low cost, late warning indicator for bearing, generators, and motor components in the turbine.

## Introduction

Temperature is an age old indicator of component health. Bearing manufacturers have long been aware of the relationship between bearing temperature and bearing life. Because of this relationship, temperature can be used to monitor bearing condition or for other temperature sensitive components, such as motors and generators.

If temperature is a reliable method for component life prediction, why is its use not cited more often as an indicator of fault? While there are subtle changes in temperature due to wear, there are many other environmental factors that affect bearing temperatures, such as load, speed, and ambient temperature.

The key to successfully use temperature for component life prediction is to remove the environmental factors so that differences in temperature between the same components on similar turbines reflect actual bearing faults or other component faults where temperature can signify failures.

1

## Introduction

(continued)

Potential areas where temperature can be used for condition monitoring include, but is not limited to:

-  Main bearing
-  Generator bearings
-  Generator windings
-  Gearbox oil sump
-  Gearbox bearings
-  Yaw motors
-  Pitch motors
-  Slip ring
-  Hydraulic pumps

## Temperature Condition Monitoring Procedures

In general, the temperature sensor must be attached in close proximity to the bearing/component under analysis.

## 1. Simple Troubleshooting Rules for Bearings

The temperature should be no more than 82°C on the bearing housing. The bearing outer ring can be up to 11°C hotter than the housing. Note that lubricants are typically selected to run at lower temperatures and a temperature rise of 28°C may cause oil viscosity to drop by 50% or more.

## 2. Simple Troubleshooting Rules for Electric Motors and Generators

The National Electrical Manufactures Association (NEMA) has defined temperature rise for electric motors and generators in MG 1-1998. This standard outlines the normal maximum temperature rise based on a maximum ambient temperature of 40°C, power/load, service factor rating, and insulation class. For example, for a 1.5 MW generator with a service factor of 1.15 and insulation class B, the maximum allowable temperature rise would be 95°C. Thus, the machine should alert a warning condition when the winding temperature is greater than 135°C.

## 3. The Use of SCADA for Temperature Condition Monitoring

SCADA systems can be used to alert for high temperature conditions on bearings, generators, and motors. As noted, successful temperature diagnostics requires reducing the effect of environmental factors.

2

<!-- image -->

- 3.1. Define a component temperature rise (CTR), which is the difference of the sensor temperature and ambient temperature.
- 3.2. Define a threshold for CTR. Since the operating temperature can be a function of load/power output, consider developing threshold bins by wind speed/power output to reduce variation. Additionally, threshold should be set for similar machine configuration, e.g. the combination of model, gearbox, and generator represent one type of machine configuration.
- 3.2.1. Use a minimum of 6 nominal machines, with a minimum of 21 acquisitions per machine, to generate test statistics (mean and standard deviation).
- 3.2.2. Assuming near Gaussian distributions, set the threshold for each power bin as CTR mean + 3*CTR standard deviation, which will give an approximate probability of false of 1e-3.
- 3.3. Set alarm alerts for hot bearings at 82°C.
- 3.4. Set generator/motor alerts based on NEMA MG 1-1998, as appropriate.

## Summary

Temperature can be a powerful indicator of component health. That said, temperature of components is also affected by environmental factors such as ambient temperature, load, and speed. By reducing the effect of these environmental factors (monitoring temperature rise, binning by power), temperature can be used to diagnose component wear. For bearings, the absolute temperature should not exceed 82°C. For motors/generators, NEMA MG 1-1998 should be consulted for absolute temperature limits.

3