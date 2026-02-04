<!-- image -->

## RP 204 Converter Maintenance

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Kevin Alewine, Shermco Industries

Principal Author: Aaron Lawson, PSI Repair Services

Contributing Author: Kevin Alewine, Shermco Industries

## Safety Notice

The American Wind Energy Association (AWEA) cannot determine or prescribe how industry employers should evaluate their compliance obligation under the Occupational Safety and Health Administration's (OSHA) regulations. Each employer must make its own determinations depending on the condition of the worksite.

AWEA strongly encourages its members to develop their own written program to address worker safety and health procedures, programs, and hazard assessments, as well as provide training for their workers in these areas. Elements to consider when creating a program:

1. Ensure workers utilize appropriate personal protective equipment (PPE) including but not limited to flame resistant (FR) rated clothing, Arc Flash suit and hood, and electrical gloves rated to the electrical hazard present.
2. Follow all electrical safety codes including but not limited to NFPA70E, OSHA, ANSI, etc.
3. Ensure proper Lock Out Tag Out (LOTO) procedures are followed.
4. Allow adequate time for capacitors to discharge before opening converter cabinets. Capacitor discharge times should be provided by the converter OEM. If unknown, wait a MINIMUM of 30 minutes!
5. Ensure there is no dangerous voltage present at the converter by measuring the voltage at the capacitor banks, input and/or output phase terminals.

1

RP 204

## Purpose and Scope

The scope of 'Converter Maintenance' provides an introduction to the operation of converters commonly used in wind turbines. It also addresses basic maintenance and troubleshooting related to the converters. It is not machine specific; OEM documentation should be used where available. Variations to this recommended practice may be necessary in some instances.

## Introduction

Converters are used to synchronize the output from a generator to the frequency of the grid. There are various topologies used in wind turbines such as doubly fed induction generators or full power conversion from permanent magnet generators. The converters used are similar and have the same basic components. The maintenance and troubleshooting for these converters are similar and can be applied with a basic knowledge of the converter being used.

Note: The terms converter and inverter are commonly used interchangeably. For the purpose of this document, the term converter will be used. Only qualified and properly trained personnel should be allowed to perform maintenance on converters.

## Converter Maintenance Procedures

1. Filter

Inspect the filter for contamination and replace when necessary. The filter should be replaced every year or sooner depending on the dustiness of the environment. Clogged filters will cause cooling fans to work harder, which shortens their lifetime, and will also increase the temperature of the converter, which will lead to a shorter converter lifetime.

## 2. Electrical Connections

Inspect terminals for loose connections, corrosion, and damage from high temperature. Inspect wiring for cracked insulation, abrasions, and discoloration. Inspect the condition of all wire crimps. Repair or replace any cables or terminals that show damage. Terminals on the phase connections as well as the DC link connections should be inspected. Ensure that no insulation is trapped under terminals. Verify all connections are tightened using the specified torque ratings. Improperly tightened electrical connections will heat up and eventually fail.

2

<!-- image -->

## 3. Fiber Optic Cables, If Equipped

When fiber optic cables are removed, care should be taken to ensure dust and debris are not allowed to come in contact with the cable or transceiver ports. Use clean and dry compressed air to blow off dust from the cables, connectors, and transceiver ports. Isopropyl alcohol and lens paper can be used to clean off cables and connectors. Never use dry lens paper as it is extremely abrasive when dry. Never insert any foreign object into a transceiver port. Install covers or plugs to prevent dust from contaminating cleaned fiber optics. Commercial optical cable cleaning kits are also available; follow their instructions for proper use.

## 4. Heat Sink

Inspect heat sink for dirt or debris. Heat sink fins will pick up dust and dirt from the cooling air. Dirty or clogged heat sinks will not allow heat to be efficiently removed from power electronic components and cause a shortened lifetime. Heat sinks should be inspected and cleaned at least annually but more often if the environment is excessively dusty. Cleaning can be accomplished by blowing clean and dry compressed air through the heat sink and capturing dust using a vacuum cleaner at the outlet. Care must be taken to prevent dust from entering adjoining equipment. Oil or grease contamination must also be removed from heat sink surfaces and fins.

## 5. Fans

Test for proper operation of the cooling fans. If the heat sink temperature gradually rises over time, this may be an indication of a failing fan. A handheld anemometer can be used to verify the proper airspeed. If the airspeed is low, the fan should be repaired or replaced. Increased noise or vibration from a fan is an indication of bearing failure and the fan should be repaired or replaced before complete failure. Clean the fan blades and guard of any accumulated dust and debris or other obstructions.

## 6. Liquid Cooling System, If Equipped

Inspect the heat exchanger for dust and debris and clean if necessary. The coolant pump should be tested for proper operation. Many pumps will have a pressure gauge that should indicate the pump is operating correctly. Excessive noise from the pump may be an indicator of a failing pump or motor. The entire coolant system should be inspected for leaks and repaired as necessary.

3

RP 204

## 6. Liquid Cooling System, If Equipped (continued)

Coolant should be tested for proper refractive index and adjusted as necessary. A refractometer should be used with the proper scale; an automotive hydrometer is not acceptable for converter coolant testing. Distilled water should be used with the specified antifreeze; potable water should never be used due to its mineral and chemical content variation. Coolant level and refractive index should be tested every 6 months unless otherwise specified by the manufacturer. Coolant should be completely replaced (to renew the corrosion inhibitors) every 5 years unless otherwise specified by the manufacturer.

## 7. Seals

Inspect enclosure and door seals for condition. Damage to seals will allow dirt and contamination to enter the enclosure. Proper airflow can also be affected by damaged seals. Replace if damaged. Cable glands should also be inspected for proper sealing or damage.

## 8. Enclosure

Inspect all enclosures and remove any loose hardware, insects, or any other foreign objects. Vacuum any accumulated dirt or debris that may be present inside the enclosure.

## 9. Converter Control Unit

Depending on the type of converter control unit, a memory backup battery may be used. This battery should be replaced as recommended by the manufacturer,or at least every 5 years. Care should be taken when replacing this battery to prevent electrostatic discharge (ESD) damage to the electronics. Proper replacement procedures should be followed to prevent memory data loss.

## 10. Thermographic Inspection

Thermal cameras can be used to inspect converter equipment when under load for abnormal heating of components and electrical terminals. Proper training is required when using thermal cameras. Consulting with a certified and experienced thermographer is recommended. Proper PPE is required when accessing a converter cabinet under load as there is an extreme danger of arc flash and hazardous voltages are present.

4

<!-- image -->

## 10. Thermographic Inspection

(continued)

Baseline thermal images may be required to ensure abnormal conditions are properly identified. Areas to inspect include electrical terminals, insulated gate bipolar transistors (IGBTs), capacitors, control circuit boards, and heat sinks/ cooling systems. Loose terminals will show up hotter than properly torqued terminals. Failing IGBTs, capacitors, or components on circuit boards may appear hotter than other components in the system. Improperly functioning heat sinks or coolant lines may appear cooler than when they are properly operating.

## 11. DC Link Capacitors

Two main types of capacitors are used in converters: aluminum electrolytic and film capacitors. Aluminum electrolytic capacitors have a shorter lifetime than film capacitors. Many newer converters use film capacitors for this reason. The lifetimes of both types of capacitors are dependent on the ambient temperature, operating time, and loading of the converter. Testing DC link capacitors are difficult without the proper equipment. Standard equivalent series resistance (ESR) meters are not able to test high capacitance and voltage of DC link capacitors.

Visually inspect capacitors for bulges, dents, burns, or other abnormal marking and replace any that have damage. Large aluminum electrolytic capacitors commonly have a vent plug that will pop out in the case of an over voltage or over temperature event. Replace any capacitors that have a missing vent plug. Clean DC link capacitors and bus bars of any dust and debris as this can cause arcing across their terminals.

## 12. Insulated Gate Bipolar Transistors (IGBTs)

Inspect IGBTs for dust and debris. Clean any contamination on or near their terminals as this can cause arcing. A digital multimeter can be used to check IGBTs for shorts across their collector and emitter terminals.

## Troubleshooting

Most wind turbine control systems deliver codes when a fault occurs. These codes give important information that can aid the troubleshooting process.

5

RP 204

## Troubleshooting

(continued)

## 1. Possible causes of common failures codes:

## 1.1. Over Temperature:

-  Defective temperature sensor/switch or thermostat
-  Dirty or clogged heat sink
-  Dirty or clogged filters
-  Failure of cooling fan
-  Low coolant level
-  Kinked coolant hoses
-  Exceeding converters ambient operating temperature

## 1.2. Over Current:

-  Phase-to-phase short
-  Phase-to-ground short
-  Shorted IGBT
-  Faulty current transformer/transducer
-  Faulty converter control unit
-  Shorted generator
-  Shorted cabling
-  Faulty crowbar circuit, if equipped

## 1.3. Switching Frequency:

-  Faulty rotor converter
-  Loose or damaged rotor cables
-  Faulty slip ring brushes

## 1.4. DC Overvoltage:

-  Static or transient overvoltage on grid
-  Failed converter
-  Faulty line side converter contactor

## 1.5. DC Undervoltage:

-  Open grid supply fuse
-  Open DC fuse
-  Faulty converter

6