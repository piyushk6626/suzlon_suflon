<!-- image -->

## RP 508 Oil Analysis Data Collection and Reporting Procedures

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Bruce Hamilton, Navigant

Principal Author: Allison Toms, Gastops

## Purpose and Scope

The scope of 'Oil Analysis Data Collection and Reporting Procedures' describes best practices in oil analysis data collection and reporting procedures for optimal information on the condition of the monitored component and proper maintenance actions.

## Introduction

Experience has shown that premature gearbox failures are a leading maintenance cost driver of wind turbine operation. Premature gearbox failures reduce turbine availability, result in lost production and downtime, and can add significantly to project lifecycle cost of operation. Oil debris and oil condition monitoring, used in conjunction with prognostics and health management (PHM) monitoring to assess and monitor the health of a wind turbine gearbox, should be part of a comprehensive condition monitoring program.

Oil debris and oil condition analysis techniques offer the potential for detecting early component damage and lubricant degradation, trending the severity of such damage, estimating the time to reach pre-defined damage limits, and providing key information for proactive maintenance decisions, often prior to other monitoring techniques.

Oil debris RP 818 'Wind Turbine On-line Gearbox Debris Condition Monitoring' and oil condition RP 819 'Online Oil Condition Monitoring' monitoring can be accomplished through continuous online sensors or traditional offline 'point-intime' oil and grease RP 815 'Wind Turbine Grease Analysis Test Methods' analysis sampling [1] .

1

## Data Collection

Data collection methods for offline periodic monitoring and online continuous monitoring are summarized below.

## 1. Offline Periodic Monitoring

Offline periodic 'point-in-time' oil, grease, and filter samples, typically taken every six months for wind turbines, are sent to a laboratory for analysis. The laboratory analysis provides details on the oil's physical properties and contaminants utilizing a wide variety of laboratory tests and instruments. The data generated from all these instruments should be automatically transferred to a laboratory information management system (LIMS) which also contains the sample collection and machinery component information. Manual transcription of data should be avoided.

## 2. Online Continuous Monitoring

Online sensors provide continuous monitoring for each component being monitored at regular intervals, for example daily. This near real-time data is exported automatically by a variety of methods, such as general packet radio service (GPRS) cellular modem, supervisory control and data acquisition (SCADA), or Ethernet, to a central monitoring location where the data is automatically processed to assess the health of the component.

## Data Variability

Oil analysis data is impacted by a wide variety of factors which need to be taken into account for repeatable and reproducible oil analysis data interpretation [2] .

## 1. Operational and Maintenance Actions

Operational and maintenance actions impact data in predictable ways and these actions should be provided with each sample.

1.1. Operational intensity can impact how quickly a component wears and how rapidly a fault progresses. A relevant indicator of machine usage should be included in any limit and trend calculations.

1.2. Sampling, maintenance, filter, and oil changes are rarely performed at precise intervals. These irregular, opportunistic intervals have a profound effect on measurement data and interfere with trending techniques. Consequently, they need to be taken into account for accurate limit and trend calculations.

2

<!-- image -->

## 2. Sample Collection Techniques

Proper sample collection techniques play a large role in providing representative data. The recommended procedures in RP 102 'Wind Turbine Gearbox Oil Sampling Procedure' and RP 815 'Wind Turbine Grease Analysis Test Methods' should be followed.

## 3. Laboratories and Test Instruments

Laboratories and test instruments also impact data. This section provides examples of factors that impact oil analysis data interpretation. Online sensors have the benefit of overcoming some of these factors. The following should be adhered to for improved repeatability and reproducibility of data:

- 3.1. Variations in laboratory analytical instruments impact data reliability. Ideally, trending should only be performed on results obtained from the same make and model of test instrument.
- 3.2. If samples are analyzed at more than one laboratory, the laboratories should be in a quality assurance program demonstrating a correlation in results obtained from each laboratory and each instrument.
- 3.3. Laboratories utilized should be certified to ISO 17025 [3] to enhance confidence in the results.

## Data Analysis

A significant amount of data is generated by oil analysis monitoring. This data needs to be reduced to useful information regarding component health. Level limits are established to indicate different stages of a fault in progress. Finite limits are typically utilized for parameters, such as allowable water contamination [4] . However, in addition to level limits, trending the rate of progression of a failure is also very important. A significant change in trend is indicative of the rate of damage progression towards level limits of defined failure stages [5] . Identifying a failure in the early stages is much more cost effective than allowing it to progress to later failure stages of the machine. Condition monitoring information should clearly and consistently indicate machinery condition from normal through various stages of failure.

3

## Results Reports

Reports for offline periodic monitoring are obtained from oil sample analysis laboratories and reports for online continuous monitoring from automated data processing algorithms.

## 1. Laboratory Analysis Results

Laboratory analysis results of an oil, grease, or filter sample provide a detailed report of a lubricant's physical properties and quantitative analysis of key contaminants. Figure A is a typical report that provides:

-  Customer information
-  Component information
-  Sample information
-  Current sample data
-  Two or more prior samples of data for comparison
-  New oil data for comparison
-  Limit values, if available, for each applicable parameter measured
-  Trend values or trend charts, if available, for each applicable parameter measured
-  Laboratory comments
-  Laboratory recommendations

Limits utilized in the report should state if they were derived based on customers' historical data specific to their components or if they are generic to machine and oil type.

Note that not all parameters measured are applicable to the component. Thus, for non-relevant parameters, level limits and trends are not assigned. Numerous laboratory tests are available. Not all of them provide useful information on component health or can be linked to a failure mode.

4

Wear Metals

Addtives

Contaminants

Wind Farm X

AWEA

Component Information

Machine Type:

ubricant:

Machine MFG:

Machine MOD:

Excossive Particle Count

Date Sampled

Lab No

Machinc / Lube Cond.

Industria Gear

Sump Size: Linknowr

<!-- image -->

Analysis Report

Sample Information

Roccived:

09/15/2016

## 1. Laboratory Analysis Results (continued)

abrasive car and damage internal components. Reducing particle levols will significandy extond component life.

CUSTOMER NOTES

9.14:2016

3/10.2016

17/6399

5Л/2015

1512385

NEW OIL

1708048

1653045

N/M

M/ M

N/M

ELEMENTAL SPECTROSCOPY [ppm] ASTM D5185 Mod (-| indicates below det ection limit

Iron

Copper

Lead

Aluminum

Tin

Nickel

Chromium

Vanadium

Silver

Calcium

Magnesium

Phusphurus

7 inc

Barium

Molyb denum

Silican

Boron

Lithium

Sodium

Potassium

FTIR SPECTROSCCPY (Indexing Numbers) ASTM E2412

Oxidation

59

60

Nitration

Anti Wear

15

Other Fluid

52

PARTICLE COUNT (partides per ml) ISO 4406:99

ISO Code

18/16/13

&gt;4 Micron

-6 Micion

&gt;14 Mirron

50 Micror

&gt;100 Miemn

VISCOSITY (contistokes) ASTM D445

Viscosityi@ 40°C

327.8

ACID NUMBER (mg KCH/g) ASTM D974

Acid Number

41

18

335

24

31

35

56

15

54

18/17/13

21/8

847

63

2

328.2

1.18

67

29

540

36

15

37

11

54

15

52

17/6/12

1008

392

29

325.4

1.18

1.35

0.88

WATER (PPM) =-ASTM D6304A b-/WЛ-133 o-ASTM D6304C d-IWI-134* e-/WI-135* F-NM-136* r-Crackle h-lW1-370*

Water

Page 1 of1

100 (c)

134 (c)

140 (c)

Teating serla mad by Lat X an ISOMEC 17025:2005 astreditad aboratory LA Accredited Cardicate Number ox Teting. (*) - NotIn sope cf ascreditatan. Wihd Farm X

etume: sols respondbity ter the saplication of and rallance upen recults and recommandat'an repartad by Lib X, whose of gation la limlied to good falth perfimance.

10/29/2014

13/2947

N: M

5/15/2014

131/348

N/M

Figure A: Laboratory Oil Analysis Report

<!-- image -->

5

1446

561

43

489

49

20

411

31

37

31

15

52

19/17/14

3264

1269

96

326.2

Machine Condition

Lubricant Condition

NORMAL

MARGINAL

Machine Name: WT1 GEARBOX

Customer Information

Iron

<!-- image -->

250,000

GASTOPS

Counts

1-Dec-2008

Equipment ID

WT\_205

WT\_55

WT\_109

WT\_42

WT\_134

WT\_145

WT \_210

WT\_221

WT\_203

MetalSCAN System Status | Equipment Watch List | Fleet Summary | Contact Us | Logout

-

1-Jan-2009

Location

Farm\_14

Farm\_3

Farm\_3

Farm\_3

Farm 4

Fanm\_6

Farm\_6

Farm\_14

Farm\_14

Farm\_14

1-Feb-2009

Equipment Watch List

Equipment Model

1-Mar-2009

Date

Manufacturer

Counts

Last Count

MFR\_1S

(MFR\_16

MFR\_14

(MFR\_16

(MFR\_10

(MFR\_9

(MFR\_3

(MFR\_1S

MFR\_1S

(MFR\_1S

## 2. Online Sensor Data

IN/A

$3557

(09-SEP-2009

Online sensor data processing provides automated analysis of near real-time results for the parameters they are measuring, such as wear debris. Figure B is a typical daily sensor report for each sensor that indicates the status of each component by means of a trend plot identifying normal or alarm conditions with details on rate of damage progression for the failure mode. Figure C is a typical report that provides the status of all monitored components for the entire wind farm(s). Due to increased time reporting granularity, the real-time online sensor data provides earlier indication of a component's health status, thus allowing operators to identify and take corrective action sooner to improve long-term reliability and reduce lifecycle cost.

Figure B: Online Wear Debris Sensor Report. Trend Plot with Limits for One Gearbox.

<!-- image -->

Figure C: Online Wear Debris Sensor Report. Wind Farms by Over Limit Status.

<!-- image -->

6

WT\_164 MetalSCAN Counts with Limits

1-Apr-2009

Equipment Status

1-May-2009

<!-- image -->

## Results Integration

Oil and wear debris analysis results should be integrated with results from other sources of information that include condition monitoring results whenever possible, such as vibration and performance condition indicators. Systems can be configured to integrate various types of condition monitoring data, system configuration data, operational data, and maintenance data from different databases to provide enhanced diagnostics and prognostics information.

## Summary

Maintaining proper lubrication and early detection of oil wetted component failures is critical to maximize component life and reduce lifecycle costs of a wind turbine. Oil debris and oil condition monitoring are effective techniques to support this goal. Analysis of the significant amount of data for useful information is provided through offline laboratory or online sensor data processing and reporting tools.

## References

- [1] Standard Practice for Inductive Wear Debris Sensors in Gearbox and Drivetrain Applications , ASTM D7917-14, 2014
- [2] L. A. Toms, and A. M. Toms, Machinery Oil Analysis -- Methods, Automation and Benefits , 3rd ed., Park Ridge, IL: STLE, 2008, ch. 9.
- [3] General Requirements for the Competence of Testing and Calibration Laboratories , ISO/IEC 17025:2005, 2005.
- [4] Standard Guide for Statistically Evaluating Measurand Alarm Limits when Using Oil Analysis to Monitor Equipment and Oil for Fitness and Contamination , ASTM D7720-11, 2017.
- [5] Standard Guide for Practical Lubricant Condition Data Trend Analysis , ASTM D7669-15, 2015.

7