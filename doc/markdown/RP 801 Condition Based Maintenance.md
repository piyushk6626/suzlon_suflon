<!-- image -->

## RP 801 Condition Based Maintenance (CBM)

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee .

Committee Chair: Junda Zhu, NRG Systems

Principal Author: Junda Zhu, NRG Systems

## Purpose and Scope

The scope of 'Condition Based Maintenance (CBM)' provides an overview of the condition based maintenance strategy and examples of some of the existing technologies utilized to perform condition monitoring on wind turbines. This document serves as the introduction and foundation for the rest of the 800 series of recommended practice chapters. For further detail on any of the specific technologies mentioned in this chapter, please look into the rest of the RP 800 series.

## Introduction

Following in the footsteps of other industries, the wind energy industry operations and maintenance have been evolving towards predictive maintenance strategies to maximize the turbine availability while minimizing the production interruption due to operational failures. A conventional event-based maintenance strategy is recognized to be not as optimal due to unexpected shutdowns and potential safety concerns related to the catastrophic failures with no early warnings. On the other hand, scheduled based maintenance, while it significantly improves the turbine availability, still falls short on cost optimization since failure occurs in between the maintenance cycles.

1

## Introduction

(continued)

As the wind industry is exploring territories that are much more remote, drive train operational situation awareness is considered crucial for turbine availability and maintenance cost optimization. Predictive maintenance strategy based on condition monitoring technologies is considered the direction where the industry is moving. Predictive maintenance is scheduling maintenance action based on the actual or projected condition of a single component or the overall turbine operational health condition. Hence, this is also referred to as condition based maintenance. The maintenance activities at the site are only carried out when it is necessary or convenient. The condition of the component can be assessed through a variety of condition monitoring technologies, such as those commonly seen in vibrations analysis and particle counters, among others.

With the help of properly instrumented condition monitoring hardware and algorithms, the operator will have full situational awareness and overview of the operational condition down to critical components of the turbine. With the information available from these systems, the maintenance team can optimize the maintenance activity and decide the right time to service the right component. Hence, the maintenance cost along with the turbine downtime can be greatly reduced. Establishing the right maintenance strategy and practices for your fleet can make the difference between a profitable operation versus one that is not.

Traditionally speaking, a properly deployed condition monitoring system involves many aspects including hardware instrumentation, data collection and storage system configuration, fault detection, diagnostic, severity assessment, prognostics, action recommendation, inspection/repair, and knowledge preservation. It is important for the end user of a condition monitoring system to understand these aspects in order to select a system that is capable and effective when deployed. The following list provides the end user a checklist to go over when choosing a system that fits their budget and needs.

## Condition Based Maintenance Selection Checklist

## 1. Hardware Instrumentation

The hardware deployed should be carefully selected to match the section of components which the condition monitoring system is supposed to cover. The mounting location is also crucial for effective and accurate diagnostics. Orientation of the sensor, sensitivity of the sensor, and the measurement capability, e.g. spectrum range, should all be well selected for wind application.

2

<!-- image -->

## 2. Data Collection, Transfer, and Storage

Modern condition monitoring systems take measurements much more frequently than ever before. On one hand, data can provide insight of fault location and modes. On the other hand, if not careful, data accumulates in an uncontrolled manner and will result in high data storage cost. Collecting data more frequently than necessary will also increase the load on the data bus, which can potentially affect other critical information from being transmitted.

## 3. System/Sensor Configuration

The sensor needs to sample at the right frequency for the component it is monitoring and have sufficient resolution for the proper analysis. The configuration should also take into account the component kinematic if the information is needed for further analysis. The data collection triggering condition sometimes needs to be pre-defined as well.

## 4. Fault Detection

Early fault detection is one of the major advantages of instrumenting condition monitoring systems. To be able to achieve early fault detection, the proper algorithm needs to be integrated to capture early signs of degradation. The algorithm implemented should be designed specifically for wind applications that cope with the operational characteristics of a wind turbine. The correct fault detection algorithm should be able to provide consistent and stable readings of the fault signature in advance, allowing the operator enough time to react.

## 5. Diagnostics

Diagnostics, commonly referred to as fault localization and fault mode identification, is the analysis procedure to find the fault location as well as the type of fault. There are multiple algorithms developed using a variety of instruments to determine the fault mode. Different fault modes result in different maintenance priorities. For example, widespread scuffing damage should be treated more carefully compared to localized spalling. The user of the CMS system should also contact the supplier about what type of fault the system is capable of detecting.

## 6. Severity Assessment

Upon successful detection of the fault, the next question is the severity of the fault. There are multiple ways to assess the degradation level of the component. Some of the CMS suppliers use absolute references, like ISO 10816, while others set up statistical thresholding methodology among the fleet. The choice of methodology for severity assessment should be evaluated together with the corresponding measurement and its characteristics.

3

## 7. Prognostics

Prognostics, or remaining useful life prediction, is considered one of the most challenging topics in the industry and academia. Given the fault mode and severity, predicting the end of life for a component is always a difficult task. Various kinds of faults develop dramatically differently. While some of the faults may exist for years without interrupting production, others fail catastrophically in a very short period of time resulting in massive asset damage. Some algorithms that are specialized for prognostics are the Kalman/particle filtering algorithm and other statistical intensive methodologies. The prognostics algorithms are also subject to various measured parameters along with frequency of measurements.

## 8. Action Recommendation

The actionable information is one of the most valuable outputs a condition monitoring system can provide to the operator of a wind farm. Once the fault mode, severity, and the predicted remaining useful life have been estimated, it is the job of the CMS or the analyst to offer the operator some recommended action. Commonly given suggestions include: keep monitoring, inspect when convenient, inspect soon, etc. If the degraded component is not accessible for inspections, then repair or replacement should be considered.

## 9. Inspection/Repair

Once a recommendation is offered, the site team should inspect the affected component or service the component if inspection is not possible. This is normally done at the site level. If the component is replaced, it is sometimes quite helpful to let the CMS supplier know the make and model of the new component that was installed. On top of that, inspection pictures on the failed components can be very helpful for fine tuning the condition monitoring system.

## 10. Knowledge Preservation

No condition monitoring system is perfect. The diagnostics, as well as the severity assessment, should have the option to be fine-tuned using the feedback from the site team. Therefore, the inspection report along with the input from the inspection team ought to be reviewed in detail. Only by working with the maintenance team and communicating with the operator can a CMS be harnessed to its full potential.

4

<!-- image -->

## 10. Knowledge Preservation

(continued)

Condition monitoring solutions, when applied in the wind energy industry, must address some unique issues. Due to the stochastic nature of wind, the incoming wind speed and direction are almost always changing. This leads to fluctuating drive train speed and load. Combined with the complicated design of turbine components such as gearbox planetary section, it is crucial that a deployed condition monitoring solution can overcome such issues and provide accurate and consistent readings that can be interpreted to evaluate the health of the component. There are multiple commercial condition monitoring solutions available. RP 801 focuses on some of the key technologies in the wind energy industry.

## Condition Monitoring Technologies

## 1. Vibration Analysis

Vibration analysis is one of the most commonly available condition monitoring solutions in the industry. The technology of using vibration to perform nondestructive evaluation has been implemented by a selection of industries since the 1960s. The hardware, along with the algorithm, has been refined over the years. Typical measurements are acceleration and velocity. The collected signal will be processed by time, frequency, or time-frequency domain analysis techniques to extract mechanical fault signatures. The conventional vibration signal processing method is designed for stationary machinery. When applied to the wind energy industry, it is crucial that the system compensates for the drivetrain speed fluctuation in order to obtain consistent results. RP 811 'Vibration Analysis for Wind Turbines' focuses on vibration based condition monitoring techniques and explains vibration analysis in detail.

## 2. Acoustic Emission

Acoustic emission, or AE, is the phenomenon of transient elastic wave generation due to a rapid release of strain energy caused by structural alteration in a solid material under mechanical or thermal stress. It is a solution for incipient fault detection using much higher sampling rate than vibration signals. There are also quite a few publications proving that this technology can provide early fault detection when compared with vibration analysis. However, due to the cost and high data sampling induced storage cost, the AE is not as widely implemented.

5

## 3. Debris Monitoring

Oil debris counter is one of the most commonly encountered CMS solutions. Recently, these measurements are normally taken in real-time. When fault occurs, metals are normally ground off the surface of the contacting surfaces. By monitoring the debris count in the oil flow, one can perform monitoring and fault detection of the drive train. RP 818 'Wind Turbine On-line Gearbox Debris Condition Monitoring' discusses this technique in detail.

## 4. Lubrication Oil Monitoring

Different from oil debris monitoring, lubrication oil condition monitoring monitors the oil health condition instead of the mechanical components. Oil analysis normally measures the cleanliness, water content, oxidation level, particle contamination, additive depletion, and many other key performance indicators. These indicators ensure that the oil is operating at its optimal condition. Lubrication oil health is crucial to a wind turbine gearbox. RP 819 'Online Oil Condition Monitoring' covers this topic.

## 5. Grease Monitoring

Apart from the oil-lubricated components in the gearbox, components like generator bearings, pitch bearings, and main bearings are normally grease lubricated. One of the solutions to monitor the health of these components is by monitoring the grease condition. The detailed procedure to collect and analyze the grease sample from components and the wind turbine drive train can be found in RP 812 'Wind Turbine Main Bearing Grease Sampling Procedures' and RP 815 'Wind Turbine Grease Analysis Test Methods'.

## 6. Temperature Measurement

Temperature is one of earliest developed indicators of component health. Bearing manufacturers have long been aware of the relationship between bearing temperature and bearing life. Because of this relationship, temperature can be used to monitor bearing conditions or other temperature sensitive components, such as generators. For further information please refer to RP 816 'Wind Turbine Temperature Measurement Procedures.'

## 7. Nacelle Process Parameters

Nacelle process parameter data is taken from process variables of the control system. Whether real-time data or data stored in a plant historian, this data provides valuable insight into the holistic condition of the turbine. For further information please refer to RP 816 'Wind Turbine Nacelle Process Parameter Monitoring'.

6

<!-- image -->

## 8. Electric Current Analysis

The reliability and availability of wind turbine electrical and electronic components are critical to minimize life-cycle energy cost and benefit project financials. From up tower generators to substations, electrical current analysis can be widely used for the health indicator of mechanical or non-mechanical components. RP 831 'Condition Monitoring of Electrical and Electronic Components of Wind Turbines' discusses electrical current analysis in detail.

## 9. Summary

The above mentioned condition monitoring technologies are merely a portion of what is available on the market today. Some of the other solutions have been mentioned in the rest of the recommended practice chapters. Systems tailored for the wind energy industry can ensure real-time health condition assessment coverage from the blades all the way to the non-drive end generator bearings. Most of the available systems take measurements periodically under certain operating conditions. For example, some of the measurements are only taken when the turbine is operating at a certain speed or at a certain section of the power curve. The frequency of measurement and the amount of data collected have to be balanced between necessity, the load on the data bus, and data storage cost, among other considerations.

Different systems provide different health information regarding the turbine. There is no one technology that is superior to the others. It is the responsibility of the owners and operators to evaluate the need of their wind farm and choose among all of the available solutions.

While acknowledging the advantages of implementing condition monitoring technologies for the wind energy industry, the challenges should also be discussed. When it comes to slow-moving sections of the traditional planetary gearboxes, the early fault detection of the planetary section, as well as the main bearing, has always been a difficult task for many CMS suppliers. The issue is caused by slow rotating speed and poor vibration transmission path. Hence, it is important to carefully select hardware and algorithm combinations for these sections.

The properly deployed CMS can provide vital information on the wind farm site operating status. When fully integrated into the site maintenance logistics, maintenance actions can be coordinated across the farm and service calls can be better planned and optimized. This will increase the turbine uptime while reducing the maintenance cost, hence maximizing the profit margin of the entire operation. Moreover, with early detection of degraded components or drivetrains, fewer catastrophic failures will occur, which increases the operational safety. Components are most likely to be operating at their optimal condition, which directly leads to improved annual energy production.

7

## Summary

The production cost is vital to the survival of wind energy as a viable future renewable energy source. Condition based maintenance plays a critical role in the significant reduction of operational cost. A correctly and properly instrumented wind turbine condition monitoring system can offer full operational situational awareness to the operator. With the help of the CMS, maintenance action can be performed only when it is necessary or convenient. Some of the costintensive down tower repairs can be avoided by detecting the fault in the early stage and quick up tower servicing. Unplanned shutdowns can also be reduced to a minimum. The operator can optimize the fleet-wide maintenance activities by consolidating services with the health information of all of the similarly degraded components at hand. There is an initial investment on the CMS; however, the return on investment is becoming  easier to justify due to the increased capability and reduced cost of modern condition monitoring technologies. Due to a wide range of available solutions in the market, it is crucial for the operator to select a system that is designed and tailored for the wind energy industry given its special needs.

## Acknowledgement

A special thank you to Shawn Sheng from NREL for his contribution throughout the drafting stages of this document, which would not have been completed without Shawn's inputs as a condition monitoring specialist in wind applications.

## References

- [1] S. Sheng, ed., 'Wind Turbine Gearbox Condition Monitoring Round Robin Study - Vibration Analysis', NREL, Golden, CO, USA, NREL/TP-500054530, 2012.
- [2] F. P. G. Márquez, A. M. Tobias, J. Pinar, and M. Papaelias, 'Condition Monitoring of Wind Turbines: Techniques and Methods,' Renewable Energy , vol. 46, pp. 169-178, October, 2012.
- [3] S. Sheng and P. Veers, 'Wind Turbine Drivetrain Condition Monitoring - An Overview,' presented at Applied Systems Health Management, Virginia Beach, Virginia, USA, NREL/CP-5000-50698, 2011.
- [4] R. B. Randall, Vibration-based Condition Monitoring: Industrial, Aerospace, and Automotive Applications , Hoboken, New Jersey, USA: Wiley, 2011.
- [5] S. Sheng and W. Yang, 'Wind Turbine Drivetrain Condition Monitoring, An Overview,' presented at ASME Turbo Expo, San Antonio, Texas, USA, NREL/PR-5000-58774, 2013.
- [6] S. Sheng, 'Wind Turbine Gearbox Oil Filtration and Condition Monitoring,' presented at Tribology Frontiers Conference, Denver, Colorado, USA, NREL/PR-5000-65388, 2015.

8