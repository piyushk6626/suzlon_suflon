<!-- image -->

## RP 817 Wind Turbine Nacelle Process Parameter Monitoring

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee .

Committee Chairs: Bruce Hamilton, Navigant Consulting Jim Turnbull, SKF Principal Author: Dan Doan, GE Energy

## Purpose and Scope

The scope of 'Wind Turbine Nacelle Process Parameter Monitoring' discusses the methods and procedures to facilitate nacelle process parameter modeling for condition based monitoring. The process parameters are available from the OEM controls system (SCADA) and provides an early warning indicator for degraded operation of bearings, gearboxes, blade controls, generators, motors, and control components in the turbine.

## Introduction

There are many methods with which to monitor and utilize the supervisory control and data acquisition systems (SCADA) data collected around the processes within a wind turbine and wind plant. The issue is the high variability in the data and getting a sense of the data compared to the plant and historical operations. One proven method is using empirical non-parametric modeling of process parameters to complement traditional condition based maintenance techniques. The process parameters provide drivers and responses for modeling methodologies to detect 'normalized' departures from historical behavior that could be early indicators of degraded conditions around the equipment in the Nacelle.

The industry description of this methodology is referred to as advanced pattern recognition (APR) and has been used successfully in the wind industry over all manufacturers and designs of wind turbine generators. The understating of relationships between performance and mechanical systems has been known since the origins of condition based maintenance. When a bearing temperature increases, the technician looks at trends in the data for the variable of concern: local ambient temperatures, oil supply temperatures, speed of the rotating system, load changes, cooling system operations, etc. These correlations were, and are, performed manually, by some simple data extractions and X/Y plots, or simply by visual comparison of trends against the one in question.

1

## Introduction

(continued)

This 'validation' is performed in relationship to hard alarms. With little or no warning, hard alarms placed the technician at disadvantage, having to react to the equipment alarm conditions. By the end of the 1990s, computer hardware and software systems had advanced sufficiently in order to perform statistical modeling using stand-alone computer systems. The advanced pattern recognition algorithms were commercialized to take advantage of 'online data mining', that is, running advanced statistical models in real-time on process parameters.

The key to successfully using process parameters in condition based maintenance is ensuring that there is a known, good historical reference data set to use for comparison with current process parameters.

The APR methodologies are very robust and accurate in determining the behavior of an asset. They are very sensitive to changes in single instrument behavior that are clear indicators of degradation, i.e. small deviation in bearing metal temperature (&lt;10% of normal span of operation) while taking into many other environmental factors affecting the bearing temperature, such as load, speed, and ambient temperature.

Statistical models are used to compare the same components, for similar assets across a wind plant, detecting changes in the components behavior as compared to the other assets. This analysis, which can be automated, identifies the outliers and focuses resources where and when they are needed.

Areas where statistical models and APR can be used for condition monitoring include, but are not limited to the following asset components:

-  Hub system
-  Main bearing
-  Blades
-  Gearbox
-  Bearings
-  Oil sump
-  Gears
-  Oil system
-  Online oil particulates
-  Oil cooler
-  Generator
-  Bearings
-  Windings
-  Slip rings
-  Controls
-  Cooling systems

2

<!-- image -->

## Introduction

(continued)

## Asset components list continued:

-  Transformers
-  Converters
-  Yaw
-  Controls
-  Position
-  Wind
-  Power
-  Efficiency
-  Direction
-  Speed

## The different assets include all physical measurements and calculations associated with these assets:

-  Pressures
-  Temperatures
-  Vibrations, including deterministic characteristic: kurtosis, crest factor, spike energy, stress wave, etc.
-  Voltage
-  Current
-  Torque
-  Strain
-  Moment
-  Particle count
-  Wind direction
-  Wind speed
-  Wind deviation
-  Blade tip speed ratio
-  Ambient temperatures
-  Ambient pressures
-  Power
-  Position
-  Set points
-  Control demand signals
-  Etc.

The more parameters around a component the better the detection of potential effects from degradation.

Fleet comparison of parameters for a component, e.g. localized models looking at all similar gearbox parameters, typically takes the form of a correlation matrix or statistical modeling.

3

## Advance Pattern Recognition and Statistical Analysis Condition Monitoring Procedures

In general, the greater the number of parameters monitoring a process, the better the modeling. For most APR models there needs to be, at a minimum, three (3) drivers (independent parameters): ambient temperature, rotor speed, and power output and five (5) or more response (dependent parameters): bearing vibration, bearing temperatures, oil temperatures, etc. Typically the OEM installed sensors are enough to get started. A rule of thumb is that the more sensors around a process, the better the detection of an abnormal behavior.

## 1. Where Advance Pattern Recognition (APR) Fits into Condition Monitoring for Wind Turbines

APR is an 'early' detection methodology for changes in equipment asset behavior using statistical techniques. They are typically early warning systems that gives time for the analyst to run fleet comparisons and analyze the behavior. With early detection there is some ambiguity in the actionability of the advisories that APR systems report.

These systems have low false reporting rates as compared to standard alarming systems since they use models based on each turbines unique historical behavior to determine when there has been a change that needs investigating.

APR systems increase the coverage for failure modes and effects analysis beyond traditional predictive maintenance techniques. APR correlates all the behaviors, which results in early notification in equipment degradation without having to deploy resources in the field. This helps optimize time based predictive maintenance and preventive maintenance work for up tower activities.

## 2. How Statistical Models Fit into Condition Monitoring for Wind Turbines

Most wind plants have many 'identical' turbines in a similar environment with the same operating profile. This enhances the ability to compare like assets across a large population. Statistical models are used to compare the behavior of each asset's parameters on a wind turbine to the local populations of the wind plant's similar wind turbines' parameters. This allows for detection of an outlier on one turbine in comparison to the local population of wind turbines and classifies the severity of the change in behavior.

In addition, the power profile for one turbine is compared to the plant, and degraded performance is classified and compared to the overall plant performance, which could identify control system degradation or equipment degradation that would be missed in monitoring a turbine in isolation.

4

<!-- image -->

## 3. The Use of SCADA for Time Series Data Trending and Analysis

SCADA systems can be used to provide data for all the parameters measured within the nacelle. Successful diagnostics requires eliminating the effects of operational and environmental influences. This is accomplished by statistical/APR modeling and asset model comparisons across the wind plant.

- 3.1. Since statistical and APR models are based on empirical data, the range of operation of the parameters is used to set the actionability of a change in behavior.
- 3.2. Define a threshold for APR. Since the operating parameters can be a function of load/power output, engineering and technical understanding of the normal behavior of each asset is used to set the threshold criteria. Some of the APR and statistical products allow a service threshold to be set for similar machine configurations, e.g. the combination of a motor, gearbox, and generator represent one type of machine configuration.
- 3.2.1. To build the thresholds, the user will use engineering judgement on how far from the normal range of operations that the modeled parameter can be for abnormal behavior. This can be done statistically or with engineering first principle knowledge of the wind turbines:

For example, consider a five (5) degree difference between the actual value and the statistical normal behavior (modeled) for the metal bearing temperature of a high-speed bearing on the generator that is operating well below its OEM recommended temperature. Since the model takes into account all 'known' behavior, this is an abnormal behavior that could be indicative of low oil level in the bearing cavity.

- 3.2.2. Suppliers of the different statistical and APR technologies have specific methodologies to determine the thresholds for each asset within a nacelle.
- 3.3. Alarm alerts are determined by the model, thresholds, and persistence.
- 3.4. To date, there are no industry standards for setting advisory notifications.

5

## Summary

SCADA statistical models and APR models are the best solutions of process parameters modeling for determining component health. Since these methods remove the normal behavior and emphasize the abnormal behavior across the process parameters associated with the assets within the nacelle (selfnormalizing), these solutions focus attention to actual changes in behavior that are an early indicator of a possible failure mode.

Care should be taken that the modeled behavior does not allow a parameter to exceed the OEM, best practices, or thresholds that have been established to protect the equipment and for personnel safety.

Statistical and APR theories have been around for approximately one hundred years. Since the late 1990s, the hardware and software in the industrial networks have evolved to a point where development and deployment of these solutions on real-time data feeds is acceptable. They are used extensively in the power industries, oil and gas, and mining. In the power sector, they are deployed on many thousands of wind turbines throughout the world.

## References

- [1] R. Shankar, 'Fleetwide Monitoring for Equipment Condition Assessment,' EPRI, Harriman, Tennessee, USA, Rep. 1010266, 2006.

6