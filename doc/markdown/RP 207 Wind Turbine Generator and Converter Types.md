<!-- image -->

## RP 207 Wind Turbine Generator and Converter Types

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Kevin Alewine, Shermco Industries

Principal Author: Kevin Alewine, Shermco Industries

Contributing Author: Aaron Lawson, PSI Repair Services

## Purpose and Scope

The scope of 'Wind Turbine Generator and Converter Types' provides an introduction for managers and technicians new to wind energy to some of the most common generator and converter technologies utilized in wind turbines. These are not manufacturer specific and several variations are found, but these types make up the majority of the North American fleet. It is hoped that this can provide some common terms and nomenclature for use when addressing generic issues and solutions as well as design-specific concerns.

## Introduction

As the wind energy industry continues to grow and the reliability of turbine fleets becomes more critical, manufacturers have focused on generator designs that have proven successful in this severe application. While traditional generator designs have been used, there are several technologies utilized that are less common in utility or industrial applications. A typical engine driven generator, as an example, is designed using a salient pole generator where the frequency generated is dependent on the rotating speed and drive torque is managed to match the load. Constant speed is a real problem in wind generation, so more innovative solutions are required. The variability inherent with the wind has led to the development of complex control systems and high power electronics. These devices work in conjunction with the generator to maximize the power output and the useful wind speed range. They also stabilize the output frequency and power factor regardless of mechanical input.

1

## Wind Turbine Overview

The two basic types of drivetrains used in current designs are the traditional rotor/gearbox/generator style or the direct drive design where the rotor is directly connected to a relatively large diameter generator. In the traditional design, the gearbox increases the relatively low input speed, typically 17-20 RPM, to a highspeed output shaft connected to a 4 or 6 pole generator. Newer designs developed for large off-shore machines will probably use a simpler, more robust gearbox with a medium speed output to an 8 pole generator.

The early versions of the direct drive turbines used generators with many pole pieces, often nearly 100, much like a hydro turbine. Although some of these models are still in production, other configurations are more popular as output ranges increase. Newer direct drive turbines typically utilize permanent magnets rather than individual pole pieces.

With rare exception, wind turbines generate electricity at 690VAC and utilize internal or external step-up transformers to match project distribution requirements. This low voltage, high amperage configuration has proven to be reliable and cost-effective in nearly all wind turbines regardless of manufacturer. One reason for this specific voltage level has been the limits to the maximum operating voltage of power electronic devices used in wind converters. Insulated gate bipolar transistors (IGBTs) have been limited to maximum voltages of 1200V1700V in the past. Currently, device manufacturers have IGBTs with maximum voltage ratings of 3.3kV-6.5kV [1] . These higher voltage IGBTs have the downside of being much more expensive than the more common IGBTs in the 1200V -1700V range.

In addition to these higher voltage IGBTs, converter manufacturers are developing multilevel converters which further expand the possible output voltage for wind generator applications. For example, a medium-voltage converter can be designed with modern 6.5kV IGBTs in a seven-level topology with maximum voltages up to 11kV [2] . One downside to multilevel converters is that the high number of IGBTs requires a very complex control system.

## Fully Converted Generator Design Types

Most modern wind generators utilize one of three basic induction generator types: asynchronous induction (squirrel cage), permanent magnet rotor, and doubly-fed induction (DFIG). In this overview, these types of generators are briefly described, the benefits and shortcomings of each are explained, and the types of electronic controls necessary for excitation, frequency conversion, and synchronization with the grid are covered.

2

<!-- image -->

## Traditional Synchronous Generators

The traditional salient-pole generators common to general industrial and commercial applications have been used in just a few designs of wind turbines. The output compared to their weight and complexity has not proven popular. Their need to run at a constant speed to synchronize with the grid also complicates their use. One of the few successful designs required the use of not only a gear box but also a fluid drive to maintain generating frequency, making the weight, cost, and maintenance   complexity of the entire drivetrain generally undesirable.

## Asynchronous Induction Generators

This design was one of the earliest used in wind generation where all of the output was converted to DC and used to charge batteries, similar to automotive applications. As the size of turbines grew dramatically and the cost of large power converter components fell, these machines have been scaled to operate in the 2-3MW range. In this design, power is supplied to the stator windings to induce current in the already rotating squirrel-cage rotor. This excitation current supplies the rotating magnetic field that generates AC current from those same windings. This is a very simple generator, but not-so-simple power conversion equipment. Effectively, an AC/DC-DC/AC convertor is used on the output current with the frequency matched to the grid by high power semiconductor inverters that maintain the synchronization necessary.

Most of the generators used in this application generate 690VAC over a wide speed and current range. The converter is the key to grid stabilization, power factor, and reliability. The benefit of this design is that uptower maintenance is simplified, but the risk is that it can be very expensive to replace failed electronic components, even if they are easier to access.

## Permanent Magnet Generators

These generator designs were once thought to be the solution for many of the maintenance costs, and they are, in fact, proving to be very reliable machines in general. However, the costs associated with manufacturing these units can negatively impact the financial strategy of developers, so they remain less popular in many areas. In these designs, the excitation is supplied by the magnets on the rotating element. Like the standard induction generators, the AC output is fully converted by the electronics, which are simpler in design than either the induction generators or the doubly-fed induction generators discussed below.

3

GEAR BOX

GENERATOR

=

## Permanent Magnet Generators (continued)

Maintenance is minimal on these machines and they may continue to be popular where long term operating costs are taken into consideration when planning the wind project, as they are in Asia and Europe. Most of the current designs utilizing permanent magnet generators are direct drive machines where an outer ring housing the magnets rotates around a wound core, which greatly improves the reliability of the windings. The ring is connected directly to the rotor and hub assembly and supported, typically, on a single, very large main bearing.

## Full-Scale Converters (FSC)

Synchronous, asynchronous, and permanent magnet generators can all be used with full-scale converters (FSC). There are two major types of FSCs used today: Rectifier Full-Scale Converters and Back-to-Back FullScale Converters.

## Rectifier Full-Scale Converters (FSC)

Rectifier FSCs use simple rectifiers on the generator stator output which reduces the number of IGBT modules and corresponding control units required. This leads to a reasonably priced and efficient converter. Some disadvantages are increased losses due to the need for induction current and harmonics caused by the uncontrolled rectifier.

Figure A: Rectifier Full-Scale Convertor

<!-- image -->

4

AWEA

<!-- image -->

•GEAR BOX

GENERATOR

## Back-to-Back Full-Scale Converters (FSCs)

Back-to-Back FSCs are becoming the most widespread topology used in the wind turbine field. These consist of two identical converters connected back-to-back to the grid side and generator side. This design is able to achieve minimum machine losses and the maximum range of control. The generator can be utilized efficiently over a wide range of speeds and the full reactive power can be made available during low wind conditions [3] . A major downside of this type of converter is the high cost due to the requirement of two identical converters using expensive power electronics.

Power can be produced at a lower cost if a wind turbine can operate within a wider range of wind speeds. This increases the profitability for the wind farm. Both types of full-scale converters allow a wide range of wind speed using modern generators and convert the full output power.

Figure B: Back-to-Back Full-Scale Converter

<!-- image -->

5

## Doubly-Fed Induction Generators (DFIG)

This type of generator is relatively rare outside of the wind industry, but they have been well accepted by many turbine OEMs as their standard design. With a fairly high power output to weight ratio, these offer a good value for the initial cost of a wind project. This design utilizes a wound, three-phase rotor with excitation power provided through a slip ring assembly. Unlike a traditional generator, where the rotor provides the rotating magnetic field and all power is generated by the stator, if these machines are operated above the synchronous speed, then a positive current flow also comes from the rotor. This allows for a much smaller machine.

Converters for doubly-fed induction generators control the slip of the generator. They supply excitation current to the rotor when the generator is below synchronous speed. When the generator is above synchronous speed, the converter will take excess current from the rotor and supply it to the grid. This increases the amount of power the generator can create at high speeds and also increases the wind speed range capable of useful power generation.

An advantage of DFIG designs is the majority of the power generated is supplied directly to the grid. The converter used is only required to convert 30% of the power from the generator. The IGBTs and other power electronic components necessary are substantially smaller and less expensive than those used in full-scale converters. These converters maximize the tradeoffs between cost and range of useful wind speed when compared with full-scale converters. One of the main disadvantages, discussed above, is the requirement for slip rings which require regular maintenance. A second disadvantage is the IGBTs must be able to cope with high peaks in current and voltage during grid faults.

6

AWEA.

Figure C: Doubly-Fed Induction Generator

<!-- image -->

<!-- image -->

## More About Convertors

In all applications, regardless of generator type, the basic construction and function of the converter are the same. They consist of IGBTs to switch the power, DC link capacitors to store energy and decouple back-to-back converters, snubber capacitors to lessen voltage spikes during switching, a bus structure with low inductance to connect the power electronics, drive electronics to provide IGBTs with the proper turn-on and turn-off signals, and control electronics to control the converter frequency and switching signals. A water or air cooled heat sink is also used to remove excess heat generated by the IGBTs during switching. The converter switches at 1200-4500Hz in a pulse width modulated (PWM) waveform. PWM is a modulation technique used by converters to generate a sine wave from a DC voltage. The converter creates a square wave with a varied duty cycle. Duty cycle is the on-time over the period of the square wave. The overall average of the PWM waveform is equivalent to an alternating current sine wave. The output is then filtered using a line reactor and power factor correction (PFC) capacitors prior to being fed into the pad mount transformer and ultimately to the grid.

7

## References

- [1] Infineon.com. 'IGBT Modules,' 2017. [Online]. Available: www.infineon.com/ cms/en/product/power/igbt/igbt-module/channel.html? channel=ff80808112ab681d0112ab69e66f0362.
- [2] M. R. Islam, Y. Guo, and J. Zhu, 'Power converters for wind turbines: Current and future development ' , in Materials and Processes for Energy: Communicating Current Research and Technological Developments , Bardoja, Spain, Formatex: 2013, pp. 559-571.
- [3] Semikron.com. 'Application Examples,' 2017. [Online]. Available: www.semikron.com/applications/wind-energy/application-examples.html.

All images courtesy of PSI Repair Services.

8