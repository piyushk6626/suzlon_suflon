<!-- image -->

## RP 502 Smart Grid Data Reporting

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Bruce Hamilton, Navigant

Principal Author: Benjamin Karlson, Sandia National Laboratories

## Purpose and Scope

The scope of 'Smart Grid Data Reporting' focuses on generating, collecting, and serving up wind farm data for smart grid operation. This data can also be useful for power purchaser and owner/operator reporting.

## Introduction

It is important that readers understand what is meant by smart grid in this context. A smart grid is a modernized electric grid that uses information and communication technology to gather and act on information in an automated fashion to improve the efficiency, reliability, economics, and sustainability of the production and distribution of electricity.

## Smart Grid Data Reporting

## 1. Data Requirements

The most important characteristic of a smart grid is the ubiquity of communication devices and the flow of information between all aspects of the grid including the generation, transmission, distribution, and end use. Under the current grid operations scheme (non-smart grid), grid operators need to know certain operating information of all generation. This includes, but may not be limited to, real power, reactive power, and bus voltage at the point-of-interconnection. Additionally, grid operators need to communicate to generators operation commands such as how much power the grid can accept, what voltage schedule to follow, etc.

1

## 1. Data Requirements

(continued)

The following was taken from NERC's ' Interconnection Requirements for Variable Generation ' report:

The following signals should be sampled at the normal SCADA (supervisory control and data acquisition) update rate:

-  Active power (MW)
-  Reactive power (Mvar)
-  Voltage at the point-of-interconnection

The following wind plant status signals are also recommended but may be sampled at a slower rate:

-  Number of turbines available (or total MW rating of available turbines)
-  Number of turbines running and generating power (or total MW rating of turbines online and generating power)
-  Number of turbines not running due to low wind speed
-  Number of turbines not running due to high-speed cutout
-  Maximum and minimum reactive power capability of plant (for some plants in weak grid locations, it would also be prudent to know how much of the total range is dynamic, as opposed to switched capacitors or reactors)
-  Total available wind power (equal to production unless curtailed)
-  Average plant wind speed (when wind speeds are high and increasing, operators could anticipate high-speed cutout actions)
-  Plant main breaker (binary status)
-  Plant in voltage regulation mode (binary status)
-  Plant in curtailment (binary status)
-  Plant up ramp rate limiter on (binary status)
-  Plant down ramp rate limiter on (binary status)
-  Plant frequency control function on (binary status)
-  Plant auto-restart blocked (on/off)

A fully realized smart grid will incorporate a two-way flow of real-time information from generation to consumption.

Current data requirements needed from wind power plants to grid operators are clarified under the IEC 61400-25 communication standards. This standard provides a basis for the interoperability of SCADA systems and addresses the communication between SCADA systems installed on wind power plants and the grid operations centers that can benefit from the SCADA data.

2

<!-- image -->

## 1. Data Requirements

(continued)

The IEC 61400-25 Edition 1 (2008) standard has not been widely adopted yet; however, as smart grid initiatives move forward, grid operators should adopt this standard as a means of facilitating communication and interoperability. Wind power plants interconnecting to the grid will have different data requirements as defined by the specific transmission owner with which the wind power plant is interconnected.

## 1.1. Phasor Measurement Units

Phasor measurement units (PMUs) are devices that measure the signals on the bulk electric grid using a synchronized common time source. If installed, they are installed on the grid side of a wind power plant point-of-interconnect (POI) and monitor in real-time the state of the electric grid. These units monitor voltage and current many times a second, typically 30 samples/second, allowing for fast response dynamic adjustments to be made on the grid providing for stability and reliability. This high frequency monitoring of wind power plants will enable better regulation and coordination of all interconnected generation.

Because PMUs are connected to the grid side of the POI of a wind power plant, they are typically owned and maintained by transmission operators, though any wind power plant that opts to purchase and install a PMU should provide access to this data to grid operators.

## 1.2. Forecasting

Because the power output of a wind power plant is a direct function of the wind speed and the weather is an ever-changing system, the wind forecast, and thus the wind power plant generation forecast, play an important role in grid system operations. This forecast combined with the load forecast enables grid operators to commit generation resources on a day-ahead schedule allowing the system to be maintained economically and securely.

For detailed information regarding wind power plant forecasts see RP 504 on Wind Forecasting Data.

3

## 1.3. Active Wind Plant Control

As the smart grid initiative progresses it will become imperative that wind power plant's control systems are able to respond to signals sent from grid operators to actively control the operation of the wind plant. This might include reducing or increasing real power or reactive power, controlling the ramp-rate of the plant, or providing frequency regulation as requested by the grid. However, because today's wind power plants are typically operated to maximize power output, they may face an economic penalty for operating in a different state.

## References

- [1] 'The Smart Grid: An Introduction,' Litos Strategic Communication, New Bedford, MA, USA, Prepared for the U.S. Department of Energy under contract No. DE-AC26-04NT41817, Subtask 560.01.04, 2008.
- [2] 'A Smart Grid Strategy for Assuring Reliability of the Western Grid', The Western Electricity Coordinating Council, 2011.
- [3] 'Advancement of Synchrophasor Technology' Oak Ridge National Laboratory, Oak Ridge, TN, USA, Prepared for the U.S. Department of Energy's Office of Electricity Delivery and Energy Reliability, 2016.
- [4] '2012 Special Assessment, Interconnection Requirements for Variable Generation', NERC, Atlanta, GA, USA, 2012.
- [5] K. Johansen, 'Presentation of IEC 61400-25 work: 'A generic communication solution for Wind Power Plants'', presented at JWPA, Denmark, 2009.

4