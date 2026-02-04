<!-- image -->

## RP 506 Wind Turbine Key Performance Indicator Data Reporting Procedures

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: David Zeglinski, OSIsoft, LLC

Principal Author: Dave Ippolito, Versify Solutions

## Purpose and Scope

The scope of 'Wind Turbine Key Performance Indicator Data Reporting Procedures ' describes best practices in reporting key performance indicators (KPIs) including recommended data granularity, frequency, and methods for capturing and collecting data required to produce recommended KPIs.

## Introduction

This document assumes the reader has working knowledge of SCADA, data capture, and data collection and historian technologies. While this document does not recommend specific technologies, it assumes that SCADA data may be captured and collected using some method of historian technology. Also, this document assumes that integrated values for any underlying data point that is captured may be extracted from the data historian at the described levels of frequency.

Presentation of key performance metrics and any technologies associated with data reporting are also beyond the scope of this document, but is recommended that any reporting or presentation tool or application used allow for both high level "dashboard reporting" that may be tailored for senior management as well as the ability to drill down into granular details as needed by engineers, plant managers, and operators.

1

RP 506

## Procedures (Detailed Descriptions)

Data should be collected from the plant at various levels of granularity and frequencies based on how the data is to be applied in calculating key performance indicators described below. As a best practice, data should be read from a plant's SCADA system and collected in the data historian utilizing industry standard protocols such as OPC or MODBUS. Depending on the KPI, calculations may be completed as the data is read from SCADA, or may occur after integrated data has been collected over a period of time.

Table A lists operational data that must be collected in order to produce key performance indicators described within this document.

Table A

| MW                 | BOP / Turbine   | Hour / Minute   |
|--------------------|-----------------|-----------------|
| Turbine Available  | BOP / Turbine   | Hour / Minute   |
| Turbine Online     | BOP / Turbine   | Hour / Minute   |
| Turbine Fault Code | Turbine         | Minute          |
| Wind Speed         | Turbine         | Minute          |
| Wind Direction     | BOP             | Minute          |
| Curtailment Events | Turbine         | Start / Stop    |

Key performance metrics may be calculated as data is collected or tabulated periodically as needed. The following describes KPIs that should be collected for turbines and the balance of the plant.

## 1. Total MWh

Integrated MWh values for the plant and for each turbine describe plant output and are used for other metrics.

## 2. Available MW

Hourly metric based on each turbine's nameplate capacity and the total amount of time that the turbine is available.

Available MW = Sum(turbine available * turbine capacity)

2

<!-- image -->

## 3. Availability

Percentage of plant or turbine that is available for given hour.

Availability = Available MW / Nameplate Capacity

## 4. Potential Energy

Turbine capability based on design curve and meteorological conditions

Potential Energy = Design Curve(wind speed, RH, BP, etc.)

## 5. Capacity Factor

Percent of plant or turbine capacity that is producing power

Capacity Factor = Total MWh / Nameplate Capacity

## 6. Curtailment Hours or Minutes

The total number or minutes or fraction of an hour during which there has been a curtailment event

Curtailment Time = Total minutes between curtailment event start and stop

## 7. Curtailment MWh

Total MWh lost during curtailment events. Note that it may be desirable to track curtailment MWh for different types of curtailment events. Curtailment MWh is estimated using minute level integrated potential energy, the actual MW for each minute of a curtailment event. This is best computed on a minute level basis and totaled for any given hour.

## 8. Turbine Faults

The number of distinct turbine fault events should be tracked for each turbine, as well as the total number of faults for the balance of the wind farm. A turbine fault event begins when a turbine fault code is recorded and ends when the turbine is reset and the fault status indicates the turbine is back online.

## 9. Turbine Fault Lost Energy

Lost energy due to turbine faults may be estimated by subtracting actual energy from potential energy during a given fault event. It may be desirable to track lost energy by fault code, category, and plant levels.

3