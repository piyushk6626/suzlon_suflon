<!-- image -->

## RP 818 Wind Turbine On-Line Gearbox Debris Condition Monitoring

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chairs: Kevin Dinwiddie, AMSOIL Erik Smith, Moventas Bruce Hamilton, Navigant Consulting

Principal Author: Andrew German, GasTOPS

## Purpose and Scope

The scope of 'Wind Turbine On-Line Gearbox Debris Condition Monitoring' discusses the use of oil debris monitoring to assess and monitor the health of a wind turbine gearbox as part of a comprehensive condition monitoring program.

Experience has shown that premature gearbox failures are a leading maintenance cost driver of a wind turbine operation. Premature gearbox failures reduce turbine availability, result in lost production and downtime, and can add significantly to project lifecycle cost of operation.

Oil debris monitoring used in conjunction with prognostics and health management (PHM) techniques offers the potential of detecting early gearbox damage, tracking the severity of such damage, estimating the time to reach pre-defined damage limits, and providing key information for proactive maintenance decisions. Experience has shown that major damage modes in wind turbine gearboxes are typically bearing spall and gear teeth pitting, both of which release metallic debris particles into the oil lubrication system [1-3] . Oil debris monitoring is well suited to provide an early indication and quantification of surface damage to bearings and gears of a wind turbine gearbox.

An oil debris sensor is used to detect and count metallic debris particles in the lube oil as it flows through the bore of the sensor. The amount of debris detected and the trend in particle counts can be used as an indication of component wear and damage. These sensors may employ inductive coils to detect debris resulting from early gearbox damage and are capable of detecting both ferromagnetic and non-ferromagnetic metallic debris.

1

HS H

Ban Inian Splise

## Introduction

- Ring Cer

Plus Hearing

Figure A shows the arrangement of a wind turbine gearbox, which typically consists of three stages of gearing: a high-speed stage, an intermediate stage, and a planetary stage. The majority of wind turbine gearbox problems that cause outages are due to bearing spall and/or gear pitting [1-3] .

Figure A

<!-- image -->

Employing an oil debris sensor installed in the gearbox lube oil system provides the capability of detecting bearing and gear damage at an early stage and giving insight into the extent of the damage and its impact on the remaining life of the gearbox. Increasing particle counts have been successfully used as a notification to perform additional borescope inspection of the gearbox to better localize and assess the progression of damage.

Inductive oil debris sensors can be installed in either a full-flow or partial-flow configuration. In the full-flow configuration, 100% of the oil flow is passed through the sensor along with 100% of the debris particles. In a partial-flow configuration, the oil flow is divided and a portion of the flow is passed through the oil debris sensor while the rest is diverted, as shown in Figure B. In a partial-flow configuration, a number of factors can influence the amount of oil debris passing through the sensor. These factors include flow rate, sensor location, and sensor plumbing arrangement. It is recommended that some tests be performed to correlate the fraction of oil debris passing through the sensor as a function of oil flow rate for a given type of partial-flow sensor configuration.

Both full-flow and partial-flow configurations are suitable for wind turbine gearbox condition monitoring, as both provide comparable data trends.

2

Flow I

AWEA

Cil

Cooler

<!-- image -->

Partial Flow

All of the oil flow

Gearboo is passed through

sensor

## Introduction (continued)

Figure B

<!-- image -->

Whether a full-flow or partial-flow configuration is used, the oil debris sensor is installed in the lube system at a point downstream of the gearbox oil return port and upstream of the filtration system. Typically only a single sensor is used, and it can be installed in either a return line or a supply line as long as it is upstream of the filtration system.

## On-Line Condition Monitoring (Debris Monitoring) Procedures

## 1. Site Survey and Installation Planning

- 1.1. Review the lube oil system to determine the most suitable location to install the debris monitoring sensor. The sensor must be located at a point downstream of the gearbox oil return port and upstream of the filtration system and can be installed either before or after the pump. ( See Figure C )

Figure C

<!-- image -->

3

Flow

Fi =

1.2. If using a full-flow sensor, select a sensor bore that matches the lube oil line bore as closely as possible. This will ensure that the pressure drop across the sensor is minimized. If there is a difference between the oil debris sensor bore and the lube oil line bore, then a pressure drop analysis should be conducted prior to the sensor installation in order to confirm that the pressure drop across the sensor is acceptable.

If using a partial-flow sensor, select or install a bypass flow stream that supports the sensor manufacturer's recommended flow rate. Bypass filtration systems and oil sampling ports are typical install points. Consult with the sensor manufacturer for specific instructions. Ensure the bypass configuration maintains a suitable oil flow in the supply line to the gearbox lubrication points.

1.3. Ensure that there are no interferences and/or conflicts of space between the oil debris sensor and existing components.

1.4. Locate and mark the position where the sensor will be installed, as well as any bolts, brackets, and tubes that need to be replaced or repositioned.

1.5. Ensure that there is suitable power available for the oil debris sensor. Ensure that the power source has a switch or circuit breaker that can be turned off during sensor installation.

1.6. Ensure that all required tools and consumable materials are available and are on-site.

## 2. Sensor Electrical Installation

2.1. Connect the oil debris sensor to the SCADA or control/monitoring system (CMS) according to the instructions from the sensor manufacturer.

2.2. Ensure the switch or circuit breaker from the sensor power supply source is turned off.

2.3. Connect the oil debris sensor to the power supply according to the instructions from the sensor manufacturer.

2.4. Switch on the power to the sensor.

2.5. Perform a signal check by passing a metal particle through the sensor bore. Ensure that the sensor detects the particle and conveys this information to SCADA/CMS. When available, perform a sensor self-test to verify functionality and communications. Consult with the manufacturer for specific instructions.

4

<!-- image -->

## 3. Sensor Installation in Fluid Line

- 3.1. Ensure the switch or circuit breaker from the sensor power supply source is turned off.
- 3.2. Install the sensor in the lube oil line location that was marked during the site survey. Replace hoses, bolts, brackets, tubes, etc. as required.
- 3.3. Perform a leak check for all installed lube system components, including sensor, hoses, and fittings/adapters.
- 3.4. Perform a physical mounting integrity check to ensure that the sensor and all installed lube system components will remain secure without leaking, becoming damaged, or suffering degraded service life or performance.

## 4. Warning and Alarm Limit Configuration

Although all stages of gearing have experienced bearing problems, it is noteworthy that feedback from field experience suggests that high-speed shaft bearings and planet gear bearings are especially problematic. The former can be repaired in-situ whereas the latter requires gearbox replacement. This suggests that damaged high-speed shaft bearings should be replaced early in the damage cycle while damaged planet gear bearings should be run to the damage limit that maximizes production and minimizes secondary damage in the gearbox. Hence, gearbox damage inspection limits will be set on the basis of bearing damage. These same limits will also provide valid inspection points for gearing, since surface fatigue phenomena for bearings and gears progress in a similar manner.

The recommended parameters for indicating severity of bearing damage are:

-  The total accumulated particle counts detected by the oil debris monitoring sensor
-  An increasing rate of particle generation

A correlation can be defined between the accumulated particle counts detected by the sensor and the spall size on a damaged rolling element bearing. Thus, the maximum severity of damage can be defined as an alarm limit.

5

## Summary

Condition monitoring is an effective technique for managing gearbox failures. Oil debris sensors, when installed within the gearbox lube system, provide reliable information regarding the health of the gearbox. Sensor data can be interpreted easily as a condition indicator that provides an early warning of bearing spall and gear pitting damage and quantifies the severity and rate of damage progression towards failure.

Oil debris sensors are a proven technology and have been in operation since the early 1990s. There are now thousands of these devices operating in a wide variety of machinery applications accruing millions of operational hours.

## References

- [1] J. V. Rensselaer, 'The Elephant in the Wind Turbine,' Tribology &amp; Lubrication Technology , pp. 38-48, June, 2010.
- [2] W. Musial, S. Butterfield, and B. McNiff, 'Improving Wind Turbine Gearbox Reliability', NREL, Golden, Colorado, USA, NREL/CP-500-41548, 2007.
- [3] T. Jonsson, 'Gearbox Repair Experiences,' presented at Sandia 2006 Wind Turbine Reliability Workshop, Albuquerque, New Mexico, USA, 2006.

6