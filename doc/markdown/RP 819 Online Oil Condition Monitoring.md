<!-- image -->

## RP 819 Online Oil Condition Monitoring

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

## Committee Chairs:

Bruce Hamilton, Navigant Consulting Jim Turnbull, SKF

Principal Author: Ryan Brewer, Poseidon Systems

## Purpose and Scope

The scope of 'Online Oil Condition Monitoring' discusses the utilization of online oil condition monitoring to assess the health of a wind turbine gearbox lubricant.

Gearbox lubricants are designed to provide a protective layer between contact surfaces, thereby significantly reducing friction and wear. They also transfer heat, contaminants, and debris out of the gearbox. Due to the extreme conditions wind turbines operate under (temperature swings, high torque, frequent start/stops, humidity swings), gearbox lubricants are specially formulated with additives such as oxidation inhibitors, corrosion inhibitors, extreme pressure protection, and anti-foam agents.

Maintaining a healthy lubricant is of critical importance to maximizing the operating life of a wind turbine gearbox. Over time, and as a lubricant is exposed to debris or contamination, temperature swings, and extreme loads, its ability to provide the expected level of protection degrades. Ineffective or improper lubrication can lead to highly accelerated wear rates, development of corrosion, reduced efficiency, and ultimately functional failure.

In addition to traditional offline sampling and analysis, many online oil condition monitoring technologies exist which can provide users early warning of lubricant degradation. This recommended practice provides a summary of available technologies and their use for effective lubricant health monitoring.

1

## Introduction

Traditionally, the condition of lubricating oils has been determined through periodic oil sampling and laboratory testing. The methods for collecting gearbox oil samples and recommended analyses are discussed in detail in RP 102 and RP 104. A full laboratory oil analysis of an oil sample provides a detailed report of a lubricant's physical properties, quantitative analysis of key contaminants, and an indication of its remaining useful life. However, offline analysis methods provide limited early warning of lubricant degradation due to a combination of the limited number of oil samples from a given component, the significant time between sampling, typically 6 months or more, variability in lab analysis techniques, and contaminants which can rapidly fluctuate in concentration, such as wear debris and water.

Online oil condition sensors help to fill these information gaps and provide improved situational awareness when used with conventional offline methods. The real-time data provided by online sensing devices allows operators to identify and correct lubrication issues early, leading to improved long-term reliability and reduced lifecycle cost.

## Online Oil Condition Monitoring

## 1.  Sensing Technologies

A multitude of online oil condition sensors are available from several different manufacturers. The sensing technologies used can be grouped into the following categories:

-  Impedance spectroscopy
-  Conductivity sensing
-  Infrared spectroscopy
-  Moisture sensing
-  Viscosity

The following sections describe the principles of operation of these devices and how they can be applied for wind turbine oil condition monitoring. Operators are encouraged to seek specific equipment recommendation and instructions from their selected device manufacturers.

2

<!-- image -->

## 1.1. Impedance Spectroscopy

Impedance spectroscopy methods utilize a set of electrodes immersed in the lubricant to measure the fluid's impedance over a range of frequencies. Impedance measurements consist of a magnitude and phase angle and are frequency dependent. Contaminants, additives, and oxidation byproducts influence portions of the impedance spectrum. Properties such as anti-wear additive health, detergent/dispersant additive health, and dissolved/free water contamination can be detected and trended using impedance spectroscopy based devices.

Impedance based devices can provide the following fluid condition monitoring benefits:

## 1.1.1. Trend Analysis

Monitor impedance measurements to detect abnormal levels or patterns indicative of contamination or poor health.

## 1.1.2. Contamination and Remaining Useful Life Estimation

Some manufacturers provide data interpretation algorithms capable of providing remaining useful life estimates (estimate of time until oil properties reach unacceptable levels) and alarms for specific contaminations.

## 1.1.3. Additive Depletion Monitoring

Impedance-based devices are particularly sensitive to changes in additive levels in a lubricant. Some devices can even distinguish between surface protection additive loss and detergent/dispersant loss.

## 1.2. Conductivity

Conductivity-based devices operate on a similar measurement principle to impedance-based devices, using a set of electrodes immersed in the lubricant and measuring the electrical properties of the fluid between the electrodes. Conductivity measurements are performed at a fixed frequency and represent the inverse of the measured resistance at that frequency.

The measurement capabilities of a conductivity sensor are dependent upon the frequency at which conductivity is measured. They provide value in trending and alarming, but are limited in their capability by only measuring a single property of the fluid.

3

## 1.3. Infrared Spectroscopy

Infrared (IR) spectroscopy, or Fourier transform infrared spectroscopy (FTIR), has been used for many years to provide rapid, low cost, offline analyses of oil samples. The technology passes an infrared light source through a lubricant sample to an infrared detector. The light passing through the oil is influenced by oil contaminants and additives which absorb infrared radiation at specific frequencies. By comparing the frequency spectrum of new and used oil samples, it is possible to determine the lubricant properties, such as water, oxidation, glycol levels, and other breakdown products.

Through advances in electronics manufacturing techniques, IR technology is beginning to make its way into online sensing devices. Current technology does not have the refined measurement capabilities of laboratory devices; however, they do offer multi-parameter trending capabilities which can provide valuable, real-time insight into fluid condition.

## 1.4. Moisture Sensors

Water contamination has many detrimental effects on the performance of a lubricant, including accelerating oxidation, promoting corrosion, decreasing film strength, and increasing foaming. Water is also a difficult contaminant to control, particularly in gearbox applications which endure frequent temperature cycling, changes in atmospheric humidity, and do not experience high enough temperatures to evaporate water contamination. Online moisture sensors, often referred to as oil relative humidity (RH) or water activity sensors, can detect and trend water contamination in an oil lubrication system.

Nearly all online moisture sensors utilize a capacitive sensing element with a hydrophilic dielectric. As moisture is absorbed and desorbed by the lubricant and sensor, the measured capacitance value will change. These devices track moisture while it is present in its dissolved state and will not continue increasing as free water forms in a system.

Benefits of this technology to wind turbine gearbox lubricant monitoring include:

-  Real-time tracking of dissolved water contamination during temperature and humidity swings that are missed by periodic offline analyses.
-  Identifying turbines that have faulty desiccants.
-  Identifying turbines that show potential for free water formation to allow prompt corrective actions.

4

<!-- image -->

## 1.5. Viscosity

Through monitoring the viscosity of the oil in a lubrication system, mechanical shear, as well as contamination, can be indicated. Reduced viscosity results in reduced film strength and increases the likelihood of excessive friction, wear, and heat generation. Elevated viscosity can result in reduced cold-start lubrication and oil filtration performance and decreased efficiency due to increased fluid friction.

There are several types of online viscosity sensing techniques including rotational, vibrational, and displacement based sensors. Each method has its own advantages and disadvantages which should be discussed with the respective monitoring equipment manufacturers. Due to the very high temperature sensitivity of viscosity measurements and the temperature swings experienced by wind turbine oils, devices capable of providing a temperature compensated output or trending measurements from a specific operating temperature are recommended.

## 2. Installation Considerations

Proper installation of an online oil sensing device is critical to ensuring reliable operation and expected sensor performance. The following sections detail the considerations required when selecting an installation location and plumbing the unit into the system. Always consult with the device manufacturer before installing a device.

## 2.1. Location Selection

The following considerations should be used to determine the optimal location for device:

-  The device should be placed in a section of the lubrication system with sufficient flow to ensure a representative fluid sample is observed by the device.
-  Ensure that the flow rate in the installation location does not exceed manufacturer recommendations.
-  The device should not be placed at the bottom of a fluid reservoir or low point of a kidney loop as sludge and deposits may prevent accurate readings.

5

## 2.1. Location Selection

(continued)

-  For many online condition monitors, post filtration installation locations are preferred to prevent electrode shorting or damage to moving parts. Wear debris monitors should be installed prefilter.
-  Ensure that the device's maximum ambient temperature will not be exceeded.
-  Orient the device and/or design the device manifold in a manner that avoids entrapment of air bubbles or debris.

## 2.2. Plumbing

When installing the device into a system, consider the following:

-  If using a manifold, ensure it is free of machining chips and any burrs have been removed.
-  Lubricate any threads and/or O-rings prior to installation.
-  Tighten all fittings per the recommended torque specification.
-  After installation, engage the lubrication system and check for leaks.

## Summary

Online condition monitoring enhances lubrication maintenance practices to help maintain healthy lubricant and ultimately extend gearbox life. Many online sensing devices are available which offer insight into a variety of oil condition parameters. The selection of an appropriate device depends on the monitoring objective, historical lubrication issues, site location, and the operator's budget. Regardless of the sensing method chosen, these technologies provide significant enhancement to a standalone offline sampling and analysis program by providing continuous data between the typical 6-month sampling intervals.

6