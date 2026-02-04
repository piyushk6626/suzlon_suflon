<!-- image -->

## RP 831 Condition Monitoring of Electrical and Electronic Components of Wind Turbines

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chairs:

Bruce Hamilton, Navigant Consulting Jim Turnbull, SKF Principal Author: Wenxian Yang, Newcastle University, UK

## Purpose and Scope

The scope of 'Condition Monitoring of Electrical and Electronic Components of Wind Turbines' discusses the condition monitoring techniques used for detecting emergent failures occurring in the electrical and electronic components of wind turbines. It will cover the condition monitoring of wind turbine generator, power electronics, transformer, and cables.

## Introduction

Wind industry practice shows that for onshore wind turbines, 75% of faults cause 5% of downtime and 25% of faults cause 95% of downtime. The majority of those 25% of faults are due to the failures of electrical and electronic components of wind turbines [1] . Considering the wet and corrosive environment of offshore sites and the difficulties of accessing offshore equipment, it is believed that above figure will be more undesirable offshore. Therefore, the reliability and availability of wind turbine electrical and electronic components are critical to minimize life-cycle energy cost and benefit project financials [2] . This highlights the importance of condition monitoring for electrical and electronic components of wind turbines, both onshore and offshore. In the following sections, condition monitoring techniques for detecting emergent failures in wind turbine generators, power electronics, turbine and substation transformers, and cables will be discussed.

1

## Condition Monitoring of Electrical and Electronic Components of Wind Turbines

## 1. Condition Monitoring of Wind Turbine Generators

Since doubly-fed induction generators (DFIG) are the most common type in the wind turbine fleet, this section will focus on condition monitoring techniques for DFIG. The failure modes of permanent magnet generators, which are increasing in market share, are different from those of DFIG but still have many similarities.

The failure modes of DFIG include:

-  Mechanical: bearing failure, rotor mechanical integrity failure, stator mechanical integrity failure, and cooling system failure
-  Electrical: core insulation failure, rotor winding or insulation failure, stator winding or insulation failure, brush gear failure, slip ring failure, commutator failure, and electrical trip

The root causes of these failures are various, such as defective design or manufacture, poor installation, inadequate maintenance, heavy cyclic operation, severe ambient conditions, overload, over speed, low cycle fatigue, shock loading, high cycle fatigue, component failure, excessive temperature in windings, excessive temperature in bearings, steady or transient excessive dielectric stress, debris, dirt, corrosion, etc. Electrical current, flux, and power monitoring techniques have been well developed and are now successfully applied to the condition monitoring of wind turbine generators. Many characteristic frequencies have been identified from stator current signals for diagnosing those electrical failures occurring in the stator and rotor. The relevant information can be found from many openly published literatures.

## 1.1. Bearing

Since bearings account for over 40% of failures in generators, condition monitoring practice should concentrate on generator bearings. This can be achieved by onboard vibration monitoring and analysis, often in combination with temperature measurement. As the relevant techniques and monitoring procedures have already been introduced in AWEA O&amp;M RP 811 and RP 815, they will not be repeated again in this section. Nonetheless, bearing faults may also be detectable from an analysis of generator electrical current and power signals. Bearings approaching failure contribute to changes in air-gap eccentricity, resulting in measurable effects on magnetic field.

2

<!-- image -->

## 1.2. Earth/Ground Fault Detection

While generator rotors, stators, and bearings are responsible for over 80% of failures of the generator, and usually stators exhibit more problems than rotors [3] , detection of other electrical faults in the generator cannot be ignored. For example, a single earth/ground leakage fault in a generator rotor winding is not serious in itself because the leakage current is relatively limited and cannot cause significant damage. But if multiple earth/ground leakage faults occur, higher current flows may eventually lead to the damage of winding, insulation, and even the rotor forging. To detect this type of fault early, a rotor earth/ground fault detector is required, which applies a DC bias voltage to the rotor winding and monitors the current flowing to the rotor body via an alarm relay. Should an alarm occur, it is essential to shut down the generator for further investigation and to prevent additional damage.

## 1.3. Electrical Discharge Monitoring

Electrical discharge monitoring is another important technique that is often adopted in the condition monitoring practice of wind turbine generators. The discharge behavior of a generator is complex but can be categorized in an ascending order of energy and potential damage as: corona discharge, partial discharge, spark discharge, and arc discharge. Electrical discharge is an early indicator of many electrical faults occurring in the generator that are usually related to integrity and the residual life of insulation. Today, many commercial on-line discharge monitoring systems have been developed and are used extensively in the condition monitoring of wind turbine generators.

## 1.4. Other Practices

Besides the aforementioned techniques, some other techniques are often adopted in practice for various condition monitoring purposes. For example, turn-to-turn faults in rotor or stator windings may lead to local overheating thereby increasing the temperature of the stator and rotor. Stator and rotor temperature is often measured as an indicator of overall condition.

In addition, the deteriorating performance of the brush gear in the generator can be detected by measuring brush or brush-holder temperature. A more advanced technique involves detecting the radio frequency energy generated by brush sparking, but this technique has not been commercially used in practice.

3

## 2. Condition Monitoring of the Power Electronics of Wind Turbines

Power electronics have been identified as the components that are most prone to fail, particularly in the wet, salty, and corrosive environment experienced offshore. However, condition monitoring techniques for power electronics have not been fully developed. The reasons are various, but the major ones include:

-  The failures of power electronics develop quickly, not allowing sufficient time to implement condition monitoring.
-  Power electronic systems have a compact structural design that does not leave enough space to install condition monitoring transducers.
-  The power electronic components are relatively cheap in price and easy to replace so there is no need to monitor their health condition online if the system can be easily accessed.

However, power electronics have a wide range of failure modes, which can be caused by excessive temperature, excessive current and voltage, corrosion, thermal fatigue, ionizing radiation, mechanical shock, stress or impact, etc. A recent survey based on 200 power electronics products from 80 companies shows that failures in the converter are 30% due to capacitors, 26% due to PCBs, 21% due to semiconductors, e.g. insulated gate bipolar transistor (IGBT), and 13% due to poorly soldered connections [4] . Clearly, semiconductors and DC link capacitors are the most fragile components in wind turbine power electronics.

## 2.1. IGBTs

Temperature measurement is commonly used for monitoring the operation and health of wind turbine power electronic converters and inverters, but more advanced techniques are being researched today. The latest generation of IGBT products has been equipped with built-in thermocouples so that variations in IGBT temperature can be readily tracked. However, measured temperature is reliant on many factors, such as ambient temperature and load, thus, diagnosis of an IGBT high temperature condition still requires further investigation.

4

<!-- image -->

## 2.2. Capacitors

Two kinds of capacitors are being used in the wind industry as DC link capacitors in power electronic converters:  the aluminum electrolytic capacitor and the metallized polypropylene film capacitor. The former is characterized by a high power density at a relatively low price, but is prone to fail in practical application. By contrast, the latter is more reliable and is able to withstand higher voltages and currents with a trade-off of comparatively lower power density. The condition of electrolytic capacitors can be approximated by trending three characteristic aging indicators: capacitance, equivalent series resistance, and the dissipation factor, and comparing the measured values of these parameters with recommended service thresholds. Although film capacitors are generally more reliable than electrolytic capacitors due to their self-healing capability, they are not free from failures. In contrast to the three aging indicators of an electrolytic capacitor, the film capacitor has only one ageing indicator: capacitance. Online condition monitoring of the capacitance of the film capacitor is exactly the same as that used for monitoring the electrolytic capacitor. Since temperature is the main ageing accelerator of capacitors, temperature measurement is also applied to condition monitoring for capacitors, although the result derived from temperature monitoring could be less reliable.

## 3. Condition Monitoring of Wind Turbine and Substation Transformers

Wind turbine and substation transformers are critical to the operation of wind farms. Their safety and reliability is critical to profitable power generation, transmission, and distribution. As the transformers are subject to very high mechanical, electrical, and thermal stresses during operation, failures and aging issues often occur in their windings, bushings, tap changers, insulation, and auxiliary equipment. Although consistent failure rates for these components have not been established in surveys conducted by different organizations, winding, bushing, and insulation systems have been identified as the three most fragile components in transformers. Moreover, these components are responsible for over 50% of plant downtime [5] .

5

## 3. Condition Monitoring of Wind Turbine and Substation Transformers (continued)

Modern transformer bushings are generally designed with closely stepped capacitive stress control layers. The basic insulating systems of capacitive stress controlled, high voltage bushings are classified as: resin-bonded paper bushing, resin-impregnated paper bushing, and oil-impregnated paper bushing. Despite the different types of bushings, bushing capacitance and dielectric dissipation factor are two key indicators of their operational condition. This is because both indicators are dependent on ageing, although they are also affected by the external environment, e.g. moisture, dirt, etc. Dielectric dissipation factor is a function of bushing capacitance. An increase in bushing capacitance for all bushing types indicates partial breakdowns between the control layers. A short-circuit between two control layers could have little influence on the general health condition of a bushing, but an increasing number of defective control layers can result in a complete breakdown of the insulation. Storm conditions (lightning, high winds, etc.) and/or routine switching actions may cause a transient overvoltage condition that could damage the insulating layer of the bushing. Tracking and reporting transient overvoltage conditions in transformers is recommended as an additional tool in the evaluation of transformer and bushing condition.

## 3.1. Other Practices

Besides monitoring bushing capacitance, dielectric dissipation factor, and transient overvoltage, the following techniques are often useful for condition monitoring of wind turbine and substation transformers:

## 3.1.1. Dissolved Gas Analysis

Over time, high electrical and thermal stresses in the transformer will cause breakdown of insulating materials and release gases due to localized overheating, corona, and arcing. Different concentrations of gases will appear depending on the intensities of energy dissipated by various faults, and the analysis of dissolved gases is very helpful for the identification of the root causes of the faults.

## 3.1.2. Partial Discharge Monitoring

PD is also an important means for detecting the deterioration of the insulation system of a transformer. Once a defect has developed on the insulator, partial discharge pulses will be generated at its point of origin. Hence, the initiation and development of an insulation defect can be identified if partial discharge pulses are detectable.

6

<!-- image -->

## 3.1.3. Temperature

Temperature measurement is used as an indicator of the operational and health/aging condition of transformer windings. Now, several approaches have been adopted for the measurement of transformer temperature. Among them, the most promising device is an optical fiber transmitter connected to a crystal sensor. The sensor converts an incoming light beam into an optical signal that can be correlated to sensor temperature. Currently, these devices have been tested but are not widely in service.

## 3.1.4. Vibration Analysis

Vibration sensors magnetically attached to the sides and top of the transformer tank may help detect changes in the mechanical integrity of transformer windings, e.g. winding looseness, and the tap changer. But the practice has shown that vibration analysis of transformers is quite complicated due to the many vibration sources, such as primary excitation, leakage flux, mechanical interaction, switching operations, etc.

## 3.1.5. Leakage Flux

This is a traditional method popularly used for detecting changes in winding geometry. It is known that any mechanical displacement of the windings can result in changes to the radial component of leakage flux. By using search coils that are installed in the transformer, these changes can be readily detected.

## 3.1.6. Analysis of Current Signals

This is a very popular approach used in the condition monitoring practice of transformers. This method can be used to detect the undesirable conditions in single phase or three phase transformers. Usually, all three phases of current signals are used together for either comparison or comprehensive analysis, e.g. Park's vector pattern analysis, to detect the early malfunction of transformers.

## 3.1.7. Monitoring of Bushing Oil Pressure

For oil-filled bushings, it is  possible to measure bushing oil pressure, thereby checking for possible oil leaks. Since changes to bushing oil pressure can also be affected by the thermal overload or partial discharges, it is recommended that careful onsite investigation be conducted once a significant drop in bushing oil pressure is observed.

7

## 4. Condition Monitoring of Electric Cables

Power cables used on wind farms represent a large capital investment. They are usually reliable but are critical to the overall performance of the facility. Failures not only affect the power generation of individual wind turbines, but the production of the whole wind farm could be impacted. For this reason, monitoring and maintaining the condition of electric cables is of great significance to assure the profitable production of wind farms, particularly for those where cable installation and repair are difficult to carry out.

Different types of electric cables, e.g. paper/oil and extruded cables, are produced for different purposes. Cable systems used on wind farms are predominately insulated with solid dielectric insulation, e.g. plastic and rubber based materials. Electric cable systems can fail for a number of reasons [6] . The most common reason for failure on wind farms is poor installation technique. Low voltage cable systems (less than 1kV) commonly fail at the connectors due to overheating. One of the most effective tests for low voltage cable systems is the infrared assessment. See RP 601 and 602 Secondary Cables for more information.

Medium and high voltage cable systems can fail due to overheating at the connection points, but the predominant issue is insulation failure. Failure occurs when the local electric stress exceeds the insulation strength, e.g. a sharp metal protrusion in the insulation, a gas or air void is introduced where solid insulation should be, e.g. a lack of dielectric grease on a joint interface, or, as is most common, a more subtle mixture of these two cases. In either case, partial discharge arises and begins erosion process. The erosion process only advances during voltage stresses which are sufficiently high to turn on the PD ionization process. Voltage transients, which are very common at wind farms, intermittently turn on PD sites and cause sporadic erosion.

Manufacturer standards of modern solid dielectric components require the components to be PD free at stress levels well over the operating voltage, as they will not last long under continuous PD activity. Thus, IEEE, IEC, and ICEA standards require an off-line 50/60 Hz PD test with better than 5 pC sensitivity to determine whether or not components are in or out of specification. Since this standardized test can only be performed off-line it is typically performed during construction and then periodically during plant shutdowns. See RP 601 and RP 602 MV cable systems for more information.

8

<!-- image -->

## 4. Condition Monitoring of Electric Cables (continued)

Wind farm cable systems are presented with some extreme and unusual requirements. For example, the cable systems are typically designed for 100% loading, i.e. they can cycle from 100% to virtually zero load, they operate at more than two times the stress of typical medium voltage cable systems, and they often have relatively long cable runs (longer than 1 mile). This combination of challenges is unusual for other types of power plants and utility distribution applications that use similar cable system components. These noted challenges are usually only seen in transmission class cable systems. For this reason, many owners have specified stringent commissioning test requirements, such as the off-line 50/60 Hz PD test. In some cases, owners have installed thermocouples to spot check cable systems. While it is possible to run an optical fiber in parallel with the cable system for distributed temperature sensing (DTS), it is not a common practice.

A more common practice is to minimize the number of underground joints and use above ground junction boxes. The junction boxes can be serviced using an infrared (IR) camera, and the most common overheating point, the cable accessory, can be checked for overheating during high load conditions to prevent damage to the cable insulation. IR cameras and off-line 50/60 Hz PD tests are complementary. There is virtually no IR signature associated with PD activity and there is not any PD activity at overheating connection points until the insulation is slightly damaged. In addition, junction boxes are convenient points for fault indicators, sectionalized during failure locating and predictive off-line insulation testing.

An important issue in partial discharge testing is the level of test voltage. Using an excessive test voltage will initiate partial discharge pulses that would not exist at normal operating voltages and may cause other damage that would not occur under normal operation. Therefore, it is recommended that system test voltage not be greater than 1.5 to 2 times the operation voltage.

## Summary

Condition monitoring of electrical and power electronic components of wind turbines has long been overlooked in previous wind industry practice. It is now recognized as equally important to the condition monitoring of wind turbine drive trains, particularly with the increasing deployment of the wind turbines offshore or in remote locations.

9

## Summary

(continued)

In contrast to condition monitoring of wind turbine drive trains, condition monitoring of wind turbine electrical and power electronic components requires dedicated techniques or methods. While some methods come from traditional ideas, e.g. temperature measurement, they have been applied using more advanced technologies in order to meet special needs of wind facilities. This motivates the invention and development of even more innovative techniques in this young industry.

In this recommended practice section, a number of commercially available condition monitoring techniques for generator, power electronics, transformer, and cables are briefly discussed in order to sketch an outline of the condition monitoring of the electrical and power electronics of wind turbines. However, the selection and practical application of these techniques is still reliant on the actual situations and physical requirements at each site. Moreover, care should be taken in the application of some techniques, such as partial discharge testing, to ensure they will not introduce negative effects or additional damage to the assets being monitored.

## References

- [1] P.J. Tavner, Offshore Wind Turbines: Reliability, Availability &amp; Maintenance , Stevenage, England: IET, 2012.
- [2] W. Yang, P.J. Tavner, C. Crabtree, Y. Fen, and Y. Qiu, 'Wind Turbine Condition Monitoring: Technical and Commercial Challenges,' Wind Energy , vol. 17, no. 5, pp. 673-693, 2014.
- [3] P.J. Tavner, L. Ran, J. Penman, and H. Sedding, Condition Monitoring of Rotating Electrical Machines , Stevenage, England: IET, 2008.
- [4] E. Wolfgang, 'ECPE Tutorial: Reliability of Power Electronic Systems,' ECPE, Nuremburg, Germany, April, 2007
- [5] A. J. M. Cardoso and L. M. R. Oliveira, 'Condition Monitoring and Diagnosis of Power Transformers,' International Journal of COMADEM , vol. 2, no. 3, pp. 5-11, 1999.
- [6] J. Densley, 'Ageing Mechanism and Diagnostics for Power Cables -- An Overview,' IEEE Electrical Insulation Magazine , vol. 17, no. 1, pp. 14-22, 2001.

10