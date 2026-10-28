# Understanding Signal Metrics - SignalTester

Understanding Signal Metrics - SignalTester

[Signal Tester](https://signaltester.co.uk/)

[Signal Testing ▼](https://signaltester.co.uk/4g-signal-tester/) [4G Signal Tester](https://signaltester.co.uk/4g-signal-tester/) [5G Signal Tester](https://signaltester.co.uk/5g-signal-tester/) [NB-IoT Signal Tester](https://signaltester.co.uk/nb-iot-signal-tester/) [5G RedCap Signal Tester](https://signaltester.co.uk/5g-redcap-signal-tester/) [Signal Analyser](https://signaltester.co.uk/signal-analyser/) [Mobile Signal Tester](https://signaltester.co.uk/mobile-signal-tester/)

[Check Signal ▼](https://signaltester.co.uk/check-mobile-signal-strength/) [Check Signal Strength](https://signaltester.co.uk/check-mobile-signal-strength/) [iPhone Field Test Mode](https://signaltester.co.uk/mobile-signal-tester/) [CellMapper Guide](https://signaltester.co.uk/cell-mapper-guide/) [Coverage Checkers](https://signaltester.co.uk/coverage-checker-resources/)

[Guides ▼](https://signaltester.co.uk/understanding-signal-metrics/) [Signal Metrics Guide](https://signaltester.co.uk/understanding-signal-metrics/) [Antenna Selection Guide](https://signaltester.co.uk/antenna-selection-guide/) [Antenna Buyers Guide](https://signaltester.co.uk/antenna-buyers-guide/) [IoT SIM Cards](https://signaltester.co.uk/iot-sim-cards/) [eSIM and eUICC](https://signaltester.co.uk/esim-euicc-guide/) [SGP.32 Explained](https://signaltester.co.uk/sgp32-iot-esim/) [Starlink and IoT](https://signaltester.co.uk/starlink-lte-iot/) [Best Practices](https://signaltester.co.uk/iot-installation-best-practices/)

[CellTester ▼](https://signaltester.co.uk/celltester-platform/) [The Platform](https://signaltester.co.uk/celltester-platform/) [How It Works](https://signaltester.co.uk/how-it-works/) [Pricing](https://signaltester.co.uk/pricing/) [Mobile App](https://signaltester.co.uk/mobile-app/) [Free IP Scanner](https://security.celltester.co.uk/)

[Blog](https://signaltester.co.uk/blog/)

[Contact](https://signaltester.co.uk/contact/)

[Try CellTester Free](https://app.celltester.co.uk/)

Signal Testing [4G Signal Tester](https://signaltester.co.uk/4g-signal-tester/) [5G Signal Tester](https://signaltester.co.uk/5g-signal-tester/) [NB-IoT Signal Tester](https://signaltester.co.uk/nb-iot-signal-tester/) [5G RedCap](https://signaltester.co.uk/5g-redcap-signal-tester/) [Signal Analyser](https://signaltester.co.uk/signal-analyser/) [Mobile Signal Tester](https://signaltester.co.uk/mobile-signal-tester/) Check Signal [Check Signal Strength](https://signaltester.co.uk/check-mobile-signal-strength/) [iPhone Field Test Mode](https://signaltester.co.uk/mobile-signal-tester/) [CellMapper Guide](https://signaltester.co.uk/cell-mapper-guide/) [Coverage Checkers](https://signaltester.co.uk/coverage-checker-resources/) Guides [Signal Metrics](https://signaltester.co.uk/understanding-signal-metrics/) [Antenna Selection](https://signaltester.co.uk/antenna-selection-guide/) [IoT SIM Cards](https://signaltester.co.uk/iot-sim-cards/) [eSIM & eUICC](https://signaltester.co.uk/esim-euicc-guide/) [Best Practices](https://signaltester.co.uk/iot-installation-best-practices/) CellTester [The Platform](https://signaltester.co.uk/celltester-platform/) [How It Works](https://signaltester.co.uk/how-it-works/) [Pricing](https://signaltester.co.uk/pricing/) [Free IP Scanner](https://security.celltester.co.uk/) Company [Blog](https://signaltester.co.uk/blog/) [Contact](https://signaltester.co.uk/contact/) [About](https://signaltester.co.uk/about/) [Try CellTester Free](https://app.celltester.co.uk/)

[Home](https://signaltester.co.uk/) › Understanding Signal Metrics

# Understanding Signal Metrics

RSRP, RSRQ and SINR explained for IoT and M2M installations. Signal metric threshold tables, the full bars but slow internet problem, and what CQI means.

What is RSRP, RSRQ and SINR in cellular signal testing?

RSRP (Reference Signal Received Power) measures the strength of the signal from the serving cell tower in dBm - it is the primary coverage indicator. RSRQ (Reference Signal Received Quality) measures signal quality relative to interference and noise. SINR (Signal to Interference plus Noise Ratio) is the most direct predictor of achievable data throughput. For 4G LTE IoT installations in the UK, target RSRP of -80 dBm or better, RSRQ of -10 dB or better, and SINR of +6 dB or better for reliable data connectivity.

## Why signal metrics matter for IoT installations

Consumer devices show signal strength as bars. Bars are not a measurement - they are a visual representation derived from RSRP, and different devices use different conversion algorithms. Two phones showing full bars can have very different actual signal levels. For IoT and M2M installations, bars are irrelevant. You need RSRP, RSRQ and SINR from the actual installed hardware.

## RSRP - Reference Signal Received Power

RSRP measures the average power of the LTE Cell-Specific Reference Signals received from the serving cell, measured per Resource Element in dBm. It is always negative - closer to zero means stronger signal. RSRP is measured independently of channel bandwidth, making it directly comparable across different bands and channel widths.

|   |   |   |

| --- | --- | --- |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

## RSRQ - Reference Signal Received Quality

RSRQ = N x RSRP / RSSI, where N is the number of Resource Blocks. It captures the ratio of the wanted reference signal to the total received power including interference from other cells and users. A device can have strong RSRP (good signal from its serving cell) but poor RSRQ (because of high interference from neighbouring cells). This is particularly common in dense urban areas and industrial sites near large cell tower clusters.

Target: -10 dB or better. Acceptable: -10 to -15 dB. Poor: below -15 dB. If RSRQ is poor while RSRP is good, the solution is typically a directional antenna pointed directly at the serving cell to reduce off-axis interference, or a band lock to a less congested frequency.

## SINR - Signal to Interference plus Noise Ratio

SINR is the ratio of the wanted signal power to the sum of interference and thermal noise. It directly determines which modulation scheme the network assigns to the device.

|   |   |   |   |

| --- | --- | --- | --- |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

## Full bars but slow internet - the SINR explanation

This is one of the most common IoT installation problems. A device shows strong signal (high RSRP, full bars) but delivers poor throughput. The cause is almost always low SINR. The device is close to the tower and receives a strong signal, but the cell is congested or there is significant co-channel interference from neighbouring cells. The network has no choice but to assign low-order modulation, and throughput collapses regardless of RSRP.

Solution: try a different operator (some cells are less congested), use band locking to move to a less loaded frequency, or test at a different time of day if traffic load is the cause.

## RSSI, CQI and other metrics

**RSSI** (Received Signal Strength Indicator) is the total received power including noise and interference. It is less useful than RSRP for commissioning decisions because it does not isolate the wanted signal. High RSSI with low RSRP indicates a noisy RF environment.

**CQI** (Channel Quality Indicator, scale 0-15) is reported by the modem to the base station to indicate the highest modulation order it can currently support. CQI 15 = 256-QAM maximum rate. CQI below 5 = QPSK only, very poor efficiency. Target CQI 10 or above for reliable IoT performance.

**PCI** (Physical Cell Identity) and **EARFCN** (Evolved Absolute Radio Frequency Channel Number) identify which cell and frequency the device is connected to. Useful for cross-referencing with CellMapper to understand the physical cell tower the router is using.

[Related 4G Signal Tester RSRP thresholds and MIMO analysis for 4G LTE installations.](https://signaltester.co.uk/4g-signal-tester/)

[Related Antenna Selection Guide Which antenna type solves which signal problem.](https://signaltester.co.uk/antenna-selection-guide/)

[Signal Tester](https://signaltester.co.uk/)

Professional cellular signal testing for IoT and M2M installers. Guides on 4G, 5G, NB-IoT and 5G RedCap, plus the CellTester platform for professional commissioning.

[✉ sales@signaltester.co.uk](mailto:sales@signaltester.co.uk)

Platform

[How It Works](https://signaltester.co.uk/how-it-works/)

[Pricing](https://signaltester.co.uk/pricing/)

[Free IP Scanner](https://security.celltester.co.uk/)

[Launch CellTester](https://app.celltester.co.uk/)

Signal Testing

[4G Signal Tester](https://signaltester.co.uk/4g-signal-tester/)

[5G Signal Tester](https://signaltester.co.uk/5g-signal-tester/)

[NB-IoT Signal Tester](https://signaltester.co.uk/nb-iot-signal-tester/)

[5G RedCap](https://signaltester.co.uk/5g-redcap-signal-tester/)

[Mobile Signal Tester](https://signaltester.co.uk/mobile-signal-tester/)

[Signal Analyser](https://signaltester.co.uk/signal-analyser/)

[Check Signal Strength](https://signaltester.co.uk/check-mobile-signal-strength/)

Guides

[Signal Metrics](https://signaltester.co.uk/understanding-signal-metrics/)

[Antenna Selection](https://signaltester.co.uk/antenna-selection-guide/)

[Antenna Buyers Guide](https://signaltester.co.uk/antenna-buyers-guide/)

[Best Practices](https://signaltester.co.uk/iot-installation-best-practices/)

[CellMapper Guide](https://signaltester.co.uk/cell-mapper-guide/)

[Starlink and IoT](https://signaltester.co.uk/starlink-lte-iot/)

SIM & eSIM

[IoT SIM Cards](https://signaltester.co.uk/iot-sim-cards/)

[Roaming SIM Cards](https://signaltester.co.uk/roaming-sim-cards/)

[Multi-Network SIMs](https://signaltester.co.uk/multi-network-sim-cards/)

[eSIM and eUICC](https://signaltester.co.uk/esim-euicc-guide/)

[SGP.32 Explained](https://signaltester.co.uk/sgp32-iot-esim/)

© 2026 SignalTester. All rights reserved. Powered by [CellTester](https://celltester.co.uk/).

[Privacy Policy](https://signaltester.co.uk/privacy-policy/) [Terms](https://signaltester.co.uk/terms/) [About](https://signaltester.co.uk/about/) [Contact](https://signaltester.co.uk/contact/)

We respect your privacy

Cookies help us improve your experience, deliver personalized content, and analyze traffic. You can choose which cookies to allow by clicking **Customize**. Click **Accept All** to consent or **Reject All** to decline non-essential cookies.

Customize Reject All Accept All

[Powered by](https://cookieadmin.net/?utm_source=wpplugin&utm_medium=footer)

Personalize Your Cookie Preferences ✖

We use cookies to ensure smooth navigation and enable essential site functions. You can view detailed information about each cookie category below.

Cookies marked as **Necessary** are stored in your browser because they are essential for basic site functionality. **These cookies do not require your consent under GDPR.**

We also use third-party cookies to analyze site usage, remember your preferences, and deliver relevant content and ads. These will only be activated with your consent. You can choose to enable or disable these cookies, but please note that turning off some types may affect your browsing experience.

► Necessary Cookies Always Active

Necessary cookies enable essential site features like secure log-ins and consent preference adjustments. They do not store personal data.

None

► Functional Cookies Remark [-]

Functional cookies support features like content sharing on social media, collecting feedback, and enabling third-party tools.

None

► Analytical Cookies Remark [-]

Analytical cookies track visitor interactions, providing insights on metrics like visitor count, bounce rate, and traffic sources.

None

► Advertisement Cookies Remark [-]

Advertisement cookies deliver personalized ads based on your previous visits and analyze the effectiveness of ad campaigns.

None

► Unclassified Cookies Remark

Unclassified cookies are cookies that we are in the process of classifying, together with the providers of individual cookies.

None

Reject All Save Preferences Accept All

[Powered by](https://cookieadmin.net/?utm_source=wpplugin&utm_medium=footer) 