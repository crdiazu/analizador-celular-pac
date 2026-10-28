# Mobile Signal Tester – iPhone and Android - SignalTester

Mobile Signal Tester – iPhone and Android - SignalTester

[Signal Tester](https://signaltester.co.uk/)

[Signal Testing ▼](https://signaltester.co.uk/4g-signal-tester/) [4G Signal Tester](https://signaltester.co.uk/4g-signal-tester/) [5G Signal Tester](https://signaltester.co.uk/5g-signal-tester/) [NB-IoT Signal Tester](https://signaltester.co.uk/nb-iot-signal-tester/) [5G RedCap Signal Tester](https://signaltester.co.uk/5g-redcap-signal-tester/) [Signal Analyser](https://signaltester.co.uk/signal-analyser/) [Mobile Signal Tester](https://signaltester.co.uk/mobile-signal-tester/)

[Check Signal ▼](https://signaltester.co.uk/check-mobile-signal-strength/) [Check Signal Strength](https://signaltester.co.uk/check-mobile-signal-strength/) [iPhone Field Test Mode](https://signaltester.co.uk/mobile-signal-tester/) [CellMapper Guide](https://signaltester.co.uk/cell-mapper-guide/) [Coverage Checkers](https://signaltester.co.uk/coverage-checker-resources/)

[Guides ▼](https://signaltester.co.uk/understanding-signal-metrics/) [Signal Metrics Guide](https://signaltester.co.uk/understanding-signal-metrics/) [Antenna Selection Guide](https://signaltester.co.uk/antenna-selection-guide/) [Antenna Buyers Guide](https://signaltester.co.uk/antenna-buyers-guide/) [IoT SIM Cards](https://signaltester.co.uk/iot-sim-cards/) [eSIM and eUICC](https://signaltester.co.uk/esim-euicc-guide/) [SGP.32 Explained](https://signaltester.co.uk/sgp32-iot-esim/) [Starlink and IoT](https://signaltester.co.uk/starlink-lte-iot/) [Best Practices](https://signaltester.co.uk/iot-installation-best-practices/)

[CellTester ▼](https://signaltester.co.uk/celltester-platform/) [The Platform](https://signaltester.co.uk/celltester-platform/) [How It Works](https://signaltester.co.uk/how-it-works/) [Pricing](https://signaltester.co.uk/pricing/) [Mobile App](https://signaltester.co.uk/mobile-app/) [Free IP Scanner](https://security.celltester.co.uk/)

[Blog](https://signaltester.co.uk/blog/)

[Contact](https://signaltester.co.uk/contact/)

[Try CellTester Free](https://app.celltester.co.uk/)

Signal Testing [4G Signal Tester](https://signaltester.co.uk/4g-signal-tester/) [5G Signal Tester](https://signaltester.co.uk/5g-signal-tester/) [NB-IoT Signal Tester](https://signaltester.co.uk/nb-iot-signal-tester/) [5G RedCap](https://signaltester.co.uk/5g-redcap-signal-tester/) [Signal Analyser](https://signaltester.co.uk/signal-analyser/) [Mobile Signal Tester](https://signaltester.co.uk/mobile-signal-tester/) Check Signal [Check Signal Strength](https://signaltester.co.uk/check-mobile-signal-strength/) [iPhone Field Test Mode](https://signaltester.co.uk/mobile-signal-tester/) [CellMapper Guide](https://signaltester.co.uk/cell-mapper-guide/) [Coverage Checkers](https://signaltester.co.uk/coverage-checker-resources/) Guides [Signal Metrics](https://signaltester.co.uk/understanding-signal-metrics/) [Antenna Selection](https://signaltester.co.uk/antenna-selection-guide/) [IoT SIM Cards](https://signaltester.co.uk/iot-sim-cards/) [eSIM & eUICC](https://signaltester.co.uk/esim-euicc-guide/) [Best Practices](https://signaltester.co.uk/iot-installation-best-practices/) CellTester [The Platform](https://signaltester.co.uk/celltester-platform/) [How It Works](https://signaltester.co.uk/how-it-works/) [Pricing](https://signaltester.co.uk/pricing/) [Free IP Scanner](https://security.celltester.co.uk/) Company [Blog](https://signaltester.co.uk/blog/) [Contact](https://signaltester.co.uk/contact/) [About](https://signaltester.co.uk/about/) [Try CellTester Free](https://app.celltester.co.uk/)

[Home](https://signaltester.co.uk/) › Mobile Signal Tester – iPhone and Android

# Mobile Signal Tester – iPhone and Android

How to test mobile signal strength on iPhone and Android. Field Test Mode step-by-step, Android engineering codes, third-party apps and the SignalTester mobile app coming soon.

Testing mobile signal strength from your phone is useful for pre-site surveys and quick coverage checks. This guide covers every method on iOS and Android, what readings mean, and where phone-based testing ends and professional router-based commissioning with CellTester must begin.

## iPhone - Field Test Mode in detail

Dial `*3001#12345#*` → Call. iOS 16+: Field Test app opens directly with full menu. iOS 15 and earlier: press Home after dialling to display numeric dBm in the status bar.

**Key readings to find on iOS 16+:**

LTE → Serving Cell Meas → RSRP, RSRQ, SINR, RSSI

5G NR → NR Serving Cell Info → SS-RSRP, SS-RSRQ, SS-SINR

LTE → Neighbour Cell Info → signals from adjacent cells (useful for interference diagnosis)

LTE → Timing Advance → distance estimate to serving tower

Physical Cell ID → PCI for CellMapper cross-referencing

**Switching operators on iPhone for comparison:** Settings → Mobile Data → Network Selection → Manual. Select each operator, return to Field Test Mode, note RSRP. This is slow (30-60 seconds per operator) compared to CellTester's automated sweep, but useful for a quick pre-site check.

## Android - engineering modes

**Samsung (*#0011#):** Opens Service Mode showing RSRP, RSRQ, RSSNR, band and EARFCN in real time. Most useful quick-access Android engineering tool.

**Settings (all Android):** About Phone → Status → SIM Status → Signal Strength. Updates slowly - allow 30 seconds for stabilisation at each location.

**Network Cell Info (app, Android):** Shows RSRP, RSRQ, RSSNR, CQI, band, EARFCN and cell location on a map. Includes logging for walking surveys. Best free option for pre-site work.

## The consumer vs professional testing distinction

Phone-based signal testing - whether iPhone Field Test Mode or Android engineering mode - measures what the phone receives with its internal antenna. This is categorically different from what the Teltonika router being installed will receive with its external antenna in its final mounting position. Differences of 10-20 dB are common. Use phone testing for planning. Use CellTester for commissioning.

📱

**The SignalTester mobile app is in development.** It will provide consumer-grade signal checking with a bundled roaming eSIM for multi-operator comparison. Important: the app tests what your phone receives - not representative of installed router hardware. [Join the waiting list →](https://signaltester.co.uk/mobile-app)

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