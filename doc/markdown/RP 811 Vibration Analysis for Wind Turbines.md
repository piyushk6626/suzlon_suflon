<!-- image -->

## RP 811 Vibration Analysis for Wind Turbines

The following recommended practice (RP) is subject to the disclaimer at the front of this manual. It is important that users read the disclaimer before considering adoption of any portion of this recommended practice.

This recommended practice was prepared by a committee of the AWEA Operations and Maintenance (O&amp;M) Committee.

Committee Chair: Junda Zhu, NRG Systems Principal Authors: Junda Zhu, NRG Systems

## Purpose and Scope

The scope of 'Vibration Analysis for Wind Turbines' introduces wind energy professionals to vibration analysis methods used to detect and analyze machine component failures. This guide does not intend to make the reader an analysis expert. It merely informs the reader about common vibration analysis strategies and methods and lays the foundation for understanding vibration analysis concepts for the primary rotating components on the drivetrain of a wind turbine.

This recommended practice focuses specifically on the use of vibration analysis and encourages the consideration of additional condition monitoring technologies as part of a comprehensive proactive maintenance strategy.

## Introduction

The production cost of wind energy has decreased significantly, especially in recent years. According to the Department of Energy, the cost of wind energy has decreased more than 90% since the early 1980s. According to the American Wind Energy Association (AWEA), the cost of wind energy has dropped 66% in the past 6 years. One major factor behind the wind energy production cost reduction is that the maintenance strategy of the industry is evolving from schedule based maintenance to condition based maintenance, also known as predictive maintenance.

1

## Introduction

(continued)

Vibration analysis is one of the most commonly implemented condition based monitoring solutions in the wind energy industry. The fundamental theory of analyzing vibration data was established in the 1960s, and vibration signal processing algorithms have been developing ever since. Back in the 1990s, time synchronous averaging algorithms were implemented which significantly increased the fault diagnostics capability on non-stationary machineries similar to a wind turbine drivetrain.

Due to the stochastic nature of wind, the wind turbine drivetrain operational speed and load is always fluctuating. Traditional fast Fourier transform (FFT) based analysis techniques are not as effective when it comes to components with frequent speed variation. Additionally, FFT techniques are not capable of detecting non-periodical impacts in noisy environments such as gear fault signatures. The advantages of a well-instrumented vibration analysis, when compared with other practices, is the capability of early fault detection and fault localization in an online, real-time manner.

There are several key aspects of vibration analysis for wind turbines including:

-  Component coverage
-  Sensor selection and configuration
-  Sensor mounting
-  Signal processing techniques
-  Alarm setting or thresholding techniques
-  Data interpretation
-  Severity assessment

On top of these, there are several vibration standards commonly referenced by the industry. This article will discuss them in the following sections.

## Component Coverage

Normal commercial condition monitoring systems have the capability of covering most of the drivetrain components. The bearing components include: the main bearing, carrier bearing, planetary bearing, low-speed shaft (LSS) bearings, intermediate speed shaft (ISS) bearings, high-speed shaft (HSS) bearings, and generator bearings. A list of component shafts include: the main shaft, carrier shaft, planetary shaft, LSS, ISS, HSS, and generator shafts. The geared components include: the ring gear, planetary gear, intermediate pinion, intermediate gear, high-speed gear, and high-speed pinion. All of the components mentioned above are shown in Figure A. Normally, one vibration sensor is assigned to monitoring an assembly.

2

AWEA

<!-- image -->

3 - stage Gearbox with

Single Main Bearing

Main Bearing

Nacelle XY

AAX

Sensor 15

Sensor

AA

Main Shaft

Sensor

Planetary Section

Carrier Plate

C

GR7

High Speed Shaft

GEN1

Figure A: Typical Wind Turbine Drivetrain Layout and Sensor Coverage.

<!-- image -->

## Sensor Selection, Configuration, and Mounting

## 1. Sensor Selection

Not all vibration sensors are the same. Accelerometers are the most commonly applied vibration sensor. However, they have different sensitivity, signal to noise ratio, spectrum range, frequency response, dynamic range, etc. When combined with the proper sensor configuration and algorithm, the sensor should have enough sensitivity and resolution to monitor gear mesh and bearing fault peaks with a high signal-to-noise ratio. For a slow moving section of a wind turbine drivetrain, a low spectrum range, high sensitivity accelerometer should be applied. While in the high-speed section, the spectrum range should be relatively high to cover the bearing fault frequency locations or the resonance band. A vibration condition monitoring sensor system precisely selected for wind applications can provide accurate diagnostics and be cost effective at the same time.

3

A

Tach

Generator

## 1. Sensor Selection

(continued)

Velocity sensors are also relatively common in the industry. Typically, velocity measurements are utilized to monitor low frequency rotational faults (imbalance, alignment, etc.). Some practices also use velocity to help with bearing fault detection in later failure stages. As modern technology evolves, dynamic range is no longer a limiting factor. Accelerometers are becoming more popular in comparison to velocity transducers. Mathematically speaking, the best velocity transducer is an accelerometer and integrator. Velocity is good for broadband evaluations such as ISO 10816, but not necessary for frequency spectra since it represents a change in the slope of the spectrum.

## 2. Sensor Configuration

The configuration of the sensor is also crucial and should be tailored to the section of the gearboxes one is monitoring. Normally, for an online retrofitted system, these are preset and can be changed by the condition monitoring system specialist. Each sensor is selected and configured based on the section it is monitoring.

For a handheld system, these settings need to be constrained for the logger to function or to increase the fault detection capability. These configurations need to be changed based on which sections the sensor is collecting data from. The configurations should be logged precisely so that the next time a technician performs testing, they can use the same setup to ensure reading consistency. Common sensor configurations are listed as follows:

-  Sampling time
-  Sampling duration
-  Spectrum resolution or number of spectral lines
-  Order tracking
-  Frequency range (fmax or low cutoff frequency)
-  Band pass filter selection
-  Tachometer setting
-  With or without averages, number of averages
-  Detection method (peak-to-peak, RMS, etc.)

4

<!-- image -->

## 2. Sensor Configuration

(continued)

For handheld systems in general, it is recommended that the acceleration measurement fmax should be higher than three times the focused gear mesh frequency and that the acceleration enveloping fmax should be higher than five times the targeted bearing damage frequency. Data acquisition duration should be long enough to ensure at least 10 to 15 shaft rotations are acquired. Since the number of spectral lines, together with the fmax setting, determine the data acquisition duration, it may be difficult in some cases to satisfy both requirements with a single measurement (data acquisition duration and spectral line resolution).

Note: Signal averaging is not recommended for a variable speed machine. Not only will random noise be reduced, signals related to the speed, such as defect frequencies, will be affected.

## 3. Sensor Mounting

Ideally, the vibration should be measured for all three axes, including vertical, horizontal, and radial. These measurements can be done if a handheld system is instrumented as long as the monitored locations are consistent from test to test. However, due to cost restraint, only one direction of vibration can be measured in online retrofitted commercial applications. Typically this direction is the radial direction. The tachometer is normally mounted on the high-speed section of the drivetrain, typically between the gearbox downwind side and the generator. The rotating speed of the other shafts of the gearbox can be obtained from the gear ratio.

The sensor mounting location can be different since the turbine and gearbox manufacturer are not always the same. The general guideline is that the sensor should be mounted at, or adjacent to, the loading zone.

## Signal Processing

Vibration analysis in simple terms is to detect machine abnormality based on changes in vibration waveform in time domain or frequency domain. Statistics can be extracted from the waveform, such as condition indicators or descriptors. These condition indicators are designed to detect different fault modes of the monitored component.

However, in practice, a proper vibration analysis sequence is quite complicated and includes noise reduction, speed change compensation, fault mode detection algorithm, and fault feature extraction.

5

## 1. Noise Reduction and Speed Compensation

Speed compensation and noise cancellation are crucial for a robust and effective condition monitoring system. Noise cancellation is straight forward. Complicated drivetrains, like wind turbines, consistently produce mechanical noises. An effective noise cancellation algorithm can ensure the fault signature is isolated and greatly helps with fault isolation, which greatly reduces the effort for up tower inspection. Speed compensation is also quite critical when it comes to improving signal-to-noise ratio and improving reading consistency.

## 1.1. Time Synchronous Averaging (TSA)

TSA is designed and developed to detect shaft and gear faults with nonstationary signals that operate in noisy environments, which is ideal for wind applications. To successfully implement TSA, a tachometer reference signal is often necessary. The advantages of implementing TSA are noise reduction and speed compensation. Theoretically, noises or tunes that are not synchronous with the target shaft rotating frequency will be greatly reduced. The level of noise reduction correlates with the number of revolutions of the target shaft during the data collection timeframe. TSA can significantly enhance the shaft and gear mesh vibration signature signal-to-noise ratio while coping with speed variation.

## 1.2. Time Synchronous Re-sampling (TSR)

TSR, like TSA, is used to compensate for speed variation. However, TSR does not average out the non-synchronous vibration signals. This algorithm only re-samples the vibration signal based on tachometer reference. The typical application of TSR is for bearing diagnostics. The implementation of TSR allows the system to sample for a longer period to increase the signal-to-noise ratio and spectrum resolution. This is especially useful when it comes to the slow speed end of the drivetrain, since its rotation takes longer and normally involves quite a bit of speed variation, especially if one samples longer.

6

<!-- image -->

## 2. Fault Mode Detection

## 2.1. Frequency Domain Analytics

Frequency domain analysis on rotating machineries allows the user to quickly identify potential faults on mechanical components, especially bearings. With each type of bearing fault triggering excitations at a different location of the spectrum, depending on the bearing kinematic, along with modulations on the fault frequency location peaks, frequency domain analysis is one the most commonly used diagnostics algorithms available. It can also be used for shaft imbalance, misalignment analysis, generator related issues, etc. Fast Fourier transform (FFT) is one of the most commonly used time to frequency domain conversion algorithm. Other similar algorithms that are also explored by vibration analysts include: power density spectrum, Welch's method, and others.

## 2.2. Time Doman Analytics

Time domain analysis is also one of the most commonly used techniques for vibration analysis on stationary machineries. It is sometimes used for gear fault detection, since non-periodical impact, like damaged gear tooth impact, will not show up in frequency spectrum but will in time domain waveforms. Time domain analysis is also used for rough estimation of overall vibration level for simple systems. Time synchronous averaging is one of the most sophisticated time domain analytical methodologies.

## 2.3. Time-Frequency Domain Analytics

Time-frequency analysis is quite powerful when it comes to gear analysis. The basic idea is to convert the signal to frequency domain, filter the signals by only looking at a certain area of the spectrum, or remove the undesirable frequency elements. Afterwards, the signal is transformed back to time domain for assessment. This can be especially useful for gear analysis using narrowband, FM, and AM analysis, among others.

## 3. Fault Feature Extraction

After the signal goes through frequency, time, or time-frequency analysis, a waveform will be extracted from the original signal. These waveforms need to be summarized by statistics so the user can easily assess the waveform by only looking at the key indicators extracted from the waveform.

7

## 3. Fault Feature Extraction

(continued)

These indicators are commonly called condition indicators, descriptors, or similar. In simple terms, these are statistics of the processed waveform of some sort. Commonly seen statistics are: root mean square (RMS), mean, median, kurtosis, peak-to-peak (P2P), crest factor (peak over RMS), skewness, and so on and so forth.

## Thresholding or Severity Assessment

Currently, there is no established and well recognized standard for the wind turbine drivetrain vibration level assessment. Some references, like ISO 10816, were not specifically developed for wind applications. Standards, such as VDI, are specifically developed for wind application; however, like ISO standards, they are focused on specific bands regardless of the operating condition or load of the turbine. The reason that these stand for vibration severity assessment is that the fundamental frequency of the gear meshing or bearing fault signatures is a function of shaft speed. Even if the band can successfully capture the bearing fault frequency at any opening speed, the drawbacks are inconsistent readings since the operational speed varies and the spectrum will be dominated by gear mesh frequency peaks. These standards also acknowledge that they are only good for general vibration level assessment. For modern CMS, the severity threshold should be set based on the condition indicators calculated by the systems and based on statistics.

While moving the statistics based threshold setting procedures forward, the threshold should be set based on the indicators' distributions. For example, if we set the alarm threshold to be mean plus three sigma, the false alarm rate of a normal distribution can be quite different from that of a Rayleigh or Weibull distribution. Most of the condition indicators, based on publications, are heavily tailed like Rayleigh. Hence, it is crucial to take into account the actual reading distribution when setting the alarm threshold statistically. Always assuming that all of the CI readings are normally distributed will sometimes lead to frequency false alarms, which will lead to the user ignoring the alarms.

Threshold setting is a delicate balance between false alarm and miss detection. Different companies offer different solutions. However, it is recommended to check with the supplier of the thresholding methodology to make sure the alarm setting is effective and robust.

8

<!-- image -->

## Summary

Vibration analysis techniques have been refined over the years. Vibration based diagnostics for wind applications have their challenges. The speed and load are always fluctuating because of stochastic wind speed and direction. On top of that, the front end of the turbine moves at a relatively slow speed. These issues have a great impact on the vibration based signal processing techniques which are quite different from stationary machines. There have been a series of publications and algorithms developed to cope with these challenges. Further information can be found in the following references if the reader would like to investigate deeper into the algorithmic details or mathematical processing.

## References

- [1] AWEA.org. AWEA, 'The Cost of Wind Energy in the U.S.,' 2017, [Online] Available: www.awea.org/falling-wind-energy-costs. [Accessed ].
- [2] J. Zhu, T. Nostrand, C. Spiegel, and B. Morton, 'Survey of Condition Indicators for Condition Monitoring Systems,' in Annu. Conf. of the PHMS , 2014.
- [3] E. Bechhoefer and M. Kingsley, 'A review of time synchronous average algorithms,' in Annu. Conf. of the PHMS , 2009.
- [4] E. Bechhoefer, D. He, and P Dempsey, 'Gear health threshold setting based on a probability of false alarm,' in Annu. Conf. of the PHMS , 2011.
- [5] Mechanical vibration -- Evaluation of Machine Vibration by Measurements on Non-rotating Parts -- Part 8: Reciprocating Compressor Systems , ISO 10816 -8:2014, 2014
- [6] Measurement and Evaluation of the Mechanical Vibration of Wind Turbines and Their Components - Wind Turbines with Gearbox , VDI 3834 Blatt 1, 2015.
- [7] Guideline for the Certification of Wind Turbines Edition 2010 , 2010 ed., Germanischer Lloyd, Hamburg, Germany, 2010.

9