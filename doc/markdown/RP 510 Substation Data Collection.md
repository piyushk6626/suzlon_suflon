<!-- image -->

## RP 510 HV Substation Data Collection

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Bruce Hamilton, Navigant

Principal Author: Bill Young, Electrical Consultants Inc.

## Purpose and Scope

The scope of 'HV Substation Data Collection' focuses on wind farm data collection recommendations specific to the high voltage (HV) substation.

## Substation Data Reporting Recommendations

## 1. Identity Data Off-takers

The first step in setting up telemetry for any new site is to identify all of the internal and external data off-takers' telemetry requirements. This includes what data points are needed, what protocols and circuits are required, and when the data is needed. Often the interconnecting transmission owner and/or the independent system operator (ISO) will have strict data requirements which require certain live supervisory control and data acquisition (SCADA) telemetry to be flowing to their SCADA system before substation energization and plant synchronization. Once this step is completed, the particular telemetry requirements of each identified data off-taker can be examined to determine the required SCADA tags.

## 2. Common Substation Components and Recommended Data Tags

## 2.1. Substation Network/IED Connections

Typically, all of the substation relays, control building equipment, and alarms are tied into an remote terminal unit (RTU)/SCADA gateway/data concentrator. Devices can be connected various ways, including using serial cables, Ethernet cables, or fiber cables. Some RTUs include dedicated programmable logic controllers (PLC), Windows or Linux computers with SCADA software, or other proprietary devices.

1

## 2.1. Substation Network/IED Connections (continued)

Some RTUs are very simple and can pull all the various SCADA tags together and serve them up to a master device, while some RTUs can do many extra things, such as math operations, custom logic functions, send emails, etc.

## 2.2. Transformer(s)

Table A: Typical Transformer Tags

| Tag                  | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| LOR TRIP             | Trip status of the lockout relay associated with this transformer             |
| LOR Coil Fail        | Coil failure monitoring of the lockout relay associated with this transformer |
| Winding Temp         | Depending on transformer, there may be multiple temperature alarms available. |
| Oil Level            | Low oil level alarm                                                           |
| Sudden Pressure      |                                                                               |
| Sudden Oil Flow Trip |                                                                               |
| 87 TRIP              | Transformer differential relay TRIP indication                                |
| Loss of AC Power     | Loss of AC power for fans, etc.                                               |
| Loss of DC Power     | Loss of DC control power                                                      |

2

<!-- image -->

## 2.3. Breaker(s)

The table below is a set of recommended SCADA tags associated with each high voltage breaker. Other switching devices such as circuit switchers, MODs, etc., will have a smaller subset of these points, potentially only a status feedback.

Table B: Typical Breaker Tags

| Tag                                   | Description                                              |
|---------------------------------------|----------------------------------------------------------|
| VA                                    | A phase voltage of associated BUS                        |
| VB                                    | B phase voltage of associated BUS                        |
| VC                                    | C phase voltage of associated BUS                        |
| IA                                    | A phase current through breaker                          |
| IB                                    | B phase current through breaker                          |
| IC                                    | C phase current through breaker                          |
| P                                     | Real power through breaker                               |
| Q                                     | Reactive power through breaker                           |
| Breaker\Circuit Switch- er\MOD Status | 52a Status of breaker\circuit switch- er\MOD             |
| Loss of Close or Trip Volt- age Alarm |                                                          |
| Loss of Heater Voltage Alarm          |                                                          |
| Spring Charge Alarm                   |                                                          |
| Trip Coil 1 Fail                      | Indication that trip coil 1 has failed                   |
| Trip Coil 2 Fail                      | Indication that trip coil 2 has failed                   |
| Trip Indication                       | Trip indication from associated breaker protective relay |
| Local/Remote Status                   | Any local/remote switch status                           |

3

## 2.4. Meter(s)

The tags needed from the substation meters can vary depending on site specific PPA, GIA, ISO, and other requirements. Below is an example typical tag list for a substation check meter. Other tags such as detailed harmonic measurements, line and transformer compensation, etc. may and are often included as well depending on the site requirements.

Table C: Typical Meter Tags

| Tag           | Description                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA            | A phase to neutral voltage                                                                                                                                                                                     |
| VB            | B phase to neutral voltage                                                                                                                                                                                     |
| VC            | C phase to neutral voltage                                                                                                                                                                                     |
| VAB           | A phase to B phase line-to-line voltage                                                                                                                                                                        |
| VBC           | B phase to C phase line-to-line voltage                                                                                                                                                                        |
| VCA           | C phase to A phase line-to-line voltage                                                                                                                                                                        |
| Vll AVG       | Average line-to-line voltage                                                                                                                                                                                   |
| IA            | A phase current                                                                                                                                                                                                |
| IB            | B phase current                                                                                                                                                                                                |
| IC            | C phase current                                                                                                                                                                                                |
| MW            | Megawatts. Typically with the convention that the wind farm producing power is shown as positive.                                                                                                              |
| MVAR          | Megavars. Typically with the convention that the wind farm producing VARS is shown as positive.                                                                                                                |
| PF            | Power factor                                                                                                                                                                                                   |
| F             | System frequency                                                                                                                                                                                               |
| kWH Delivered | A counter of kilowatt hours delivered. Typically with the convention that the wind farm producing power is delivering to the grid. This convention can change site-to-site depend- ing on other requirements.  |
| kWH Received  | A counter of kilowatt hours received. Typically with the con- vention that the wind farm consuming power from the grid is received. This convention can change site-to-site de- pending on other requirements. |
| kVh Delivered | A counter of kilovar hours delivered. Typically with the con- vention that the wind farm exporting VARS to the grid is de- livered. This convention can change site-to-site depending on other requirements.   |
| kVH Received  | A counter of kilovar hours received. Typically with the con- vention that the wind farm has received. This convention can change site to site depending on other requirements.                                 |

4

<!-- image -->

## 2.5. Control House/Enclosure

Data from the control enclosure provides some critical alarms, such as indication of loss of AC power, a fire, etc. It is important to properly monitor these alarms so that site operations can respond in a timely manner before larger problems happen.

Table D: Typical Control Enclosure Tags

| Tag                                    | Description                                                                                                                                                              |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Panel or Summary Alarm                 | Any panel summary or other sum- mary alarms or protective relay alarms that may be available in the control enclosure. Alarms may be brought in individually or grouped. |
| Building Smoke Alarm                   |                                                                                                                                                                          |
| Building Hydrogen 1% Alarm             | The hydrogen concentration near the batteries has reached 1%.                                                                                                            |
| Building Hydrogen 2% Alarm             | The hydrogen concentration near the batteries has reached 2%.                                                                                                            |
| Building Door Alarm                    | The door to the control enclosure has been opened.                                                                                                                       |
| Building Battery Charger Summary Alarm | An alarm associated with the battery charger.                                                                                                                            |
| Building Battery Charger AC Fail       | The AC source to the battery charger has failed.                                                                                                                         |
| ATS Normal Source Indication           | The automatic transfer switch for the control enclosure is using the normal AC source.                                                                                   |
| ATS Emergency Source Indication        | The automatic transfer switch for the control enclosure is using the emergency AC source.                                                                                |
| HVAC Lockout Or Loss of Power          |                                                                                                                                                                          |
| HVAC Low Or High-Temperature Alarm     |                                                                                                                                                                          |

5

## 3. Typical Wind Farm SCADA Components that Tie into the Substation

## 3.1. Turbine Network

The various sensors in each turbine connect to a PLC or some type of computer. These devices are typically connected to network switches that all connect back to a central switch. This allows all of the individual turbines to communicate with the wind farm management system/wind farm power plant controller (WFMS/PPC). The wind turbine network is typically a fiber optic connected Ethernet network running between all of the turbines and the turbine manufacturer's overall power plant control system, which may be located in the substation control building/enclosure, its own enclosure, or in a separate operations building. This network is often isolated from the substation network. Data from the turbine network is often not  pulled directly from the Substation SCADA System, but turbine data is exposed via an OLE (object linking and embedding) for process control (OPC) server that can be read into the plant historian.

## 3.2. Wind Farm Power Plant Controller

The wind farm power plant controller is typically a server or combination of servers that control the wind park. Often these are provided by the turbine manufacturer, but there are also setups with third party controllers as well. The PPC is the eyes into the wind farm system. It allows the operations group to see the status of the park or individual turbines, see the various sensor readings on the turbines, control the turbines, and it also keeps the wind park producing in an acceptable range in terms of both MW and MVAR output as defined by any interconnection agreements, ISO curtailments, etc.

6

<!-- image -->

## 3.2. Wind Farm Power Plant Controller

(continued)

Table E shows typical data that the WFMS/PPC may receive from the Substation SCADA System.

Table E: Tags to PPC

| Tag                                                                                      | Description                                                                                                                                                                         |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MWCurtailment Set Point                                                                  | PlantMW curtailment signals from the ISO, market participant, plant owner, or other may come through the substation RTU or be directly entered into the plant turbine SCADA system. |
| Voltage Set Point                                                                        | If the plant is operating on a voltage schedule, this set point may come through the substation RTU or be directly entered into the plant tur- bine SCADA system.                   |
| VAR Set Point                                                                            | This set point may come through the substation RTU or be directly entered into the plant turbine SCADA system.                                                                      |
| Substation Analog and Digital Values (Power, Energy, Breaker Status, Alarm Status, etc.) | If the plant SCADA system is acting to aggregate all of the alarms and provide a single interface there may be many points coming from the substation RTU.                          |

7

## 3.2. Wind Farm Power Plant Controller

(continued)

Table F below shows typical data and commands that the PPC may send to the substation RTU.

Table E: Tags from PPC

| Tag                              | Description                                                                                                                                                                     |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of turbines online        | Number of turbines producing power                                                                                                                                              |
| Number of turbines offline       | Number of turbines not producing power                                                                                                                                          |
| Number of turbines state unknown | Number of turbines with loss of communication                                                                                                                                   |
| Number of turbines available     | Number of turbines that may or may not be running but are available if there is sufficient wind                                                                                 |
| GrossMW                          |                                                                                                                                                                                 |
| Gross MVAR                       |                                                                                                                                                                                 |
| Wind Speed                       |                                                                                                                                                                                 |
| Temperature                      |                                                                                                                                                                                 |
| Pressure                         |                                                                                                                                                                                 |
| Wind Direction                   |                                                                                                                                                                                 |
| Open/Close Capacitor or Reactor  | If there are one or several static reactive devices such as fixed capacitor(s) and reactor(s) there may be one or more tags related to the status and control of these devices. |

8

<!-- image -->

## 3.3. Substation HMI

A human machine interface (HMI) is typically just a computer with software the reads SCADA tags from a data concentrator or RTU and displays the data in a meaningful  way on a screen. HMIs can also allow an operator to have remote control of breakers and other devices. HMIs can replace annunciator functionality by including 'virtual' annunciators and alarms. HMIs can be used to view historical data. Many modern HMI systems allow both local viewing on a dedicated monitor as well as remote viewing through a web page or other mechanism. An HMI is not a required device and many substations do not have them, but if included they can provide quick visibility of what the site is doing as well as summarize any alarms.

## 3.4. Interface to POI Utility

The interconnecting utility will often require various SCADA tags from the wind farm and the wind farm owner will want data from the utility, such as revenue meter data. This connection may be done in various ways, such as over optical ground wire (OPGW) as a direct fiber connect between the utility RTU and the wind farm RTU, a dedicated private phone line, point-to-point virtual private network (VPN) between customer and utility, etc. THIS CONNECTION IS OFTEN REQUIRED TO BE FULLY OPERATIONAL BEFORE PERMISSION TO BACK FEED IS GRANTED!

Questions to ask about the point of interconnection (POI) utility's data requirements:

-  What SCADA tags do they require?
-  What SCADA tags will the site want from them?
-  Will they require any control?
-  When do they require SCADA to be fully functional?
-  What type of SCADA testing do they require?
-  What protocol do they wish to use to communicate?
-  How do they want to communicate physically (e.g. direct fiber, microwave, leased line, etc.)?
-  Do they require any equipment, rack space, or floor space in the control building?

9

## 3.5. Interface to ISO

Depending on the location of the wind farm, there may be additional independent system operator (ISO) requirements related to SCADA. For example, wind farms in California will be in CAISO territory and wind farms in Texas in ERCOT territory. CAISO, ERCOT, PJM, SPP, MISO, etc. all have varying telemetry requirements, some much stricter than others and some requiring information to be finalized many months ahead of when a new plant will energize. It is very important to understand early on what ISO requirements may be applicable on any given project . ISOs have various SCADA connection requirements as it pertains to the method, protocol, required security and segregation, etc. ISOs take their data very seriously. For example, in some cases a wind farm can be shut down if all of the required meteorological data is not being properly transmitted to the ISO.

Questions to ask about independent system operator's (ISO) data requirements:

-  What SCADA tags do they require?
-  What SCADA tags will we want from them?
-  Will they be issuing any curtailment signals?
-  When do they require SCADA to be fully functional?
-  What type of SCADA testing do they require?
-  What protocol do they wish to use to communicate?
-  How do they want to communicate physically (e.g. direct fiber, microwave, leased line, etc.)?
-  Do they require any equipment, rack space, or floor space in the control building?

## 3.6. Interface to Owner

Typically the owner will have some type of external data connection to the plant. This is commonly a dedicated T1/MPLS or other circuits. Often there will be a router and a firewall device between the substation network and the outside world. The firewall helps secure the substation network and meet NERC requirements.

10

<!-- image -->

## 3.6. Interface to Owner

(continued)

Questions to ask about owner SCADA data requirements for the substation:

-  What SCADA tags do you require?
-  Do you require remote breaker control?
-  What type of SCADA testing do you require?
-  What protocol do you wish to use?
-  How do they want to communicate physically (e.g. direct fiber, microwave, leased line, etc.)?
-  What additional floor space will you need for IT or telecom equipment?
-  How often is this data needed?
-  How will this data be used?
-  How will critical alarms be separated from non-critical alarms?

## Conclusion

The SCADA tags listed throughout this recommended practice give a good overview of the tags needed to effectively monitor a high voltage substation, as well as some of the common tags needed for the various data off-takers that typically connect to the substation. It is important to review the particular requirements on a site-by-site basis as there are many factors that can play into the different data requirements. What makes sense for one site does not always fit for another.

11

AMERICAN

WIND ENERGY

ASSOCIATION

AWEAT

<!-- image -->

## Chapter 6 Balance of Plant

<!-- image -->

Operations and Maintenance Recommended Practices version 2013