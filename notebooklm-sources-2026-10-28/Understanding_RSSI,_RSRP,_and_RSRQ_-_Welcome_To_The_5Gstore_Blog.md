# Understanding RSSI, RSRP, and RSRQ - Welcome To The 5Gstore Blog

Understanding RSSI, RSRP, and RSRQ - Welcome To The 5Gstore Blog

[Skip to navigation](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#site-navigation) [Skip to content](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#content)

[Home](https://5gstore.com/)

[About](https://5gstore.com/blog/about/)

[Contact 5Gstore](https://5gstore.com/site/contact_us.html)

[Shop 5Gstore](https://5gstore.com/site/shop)

Main Navigation

# Understanding RSSI, RSRP, and RSRQ

April 8, 2021 By [Pat Kline](https://5gstore.com/blog/author/pat3gstore-com/) [5G](https://5gstore.com/blog/category/5g/)

## Table of Contents

[🆕 2025 Update: Interpreting 5 G Signal Metrics](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#%F0%9F%86%95-2025-update-interpreting-5-g-signal-metrics)

[Key Metrics Added for 5 G NR](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#key-metrics-added-for-5-g-nr)

[2025 Recommended Thresholds](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#2025-recommended-thresholds)

[Practical Tips](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#practical-tips)

[Questions about improving your 5 G signal? Reach out to the 5Gstore Support team (https://5gstore.com/contact)—we measure these values every day and can recommend the right antennas and routers for your environment.](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/#questions-about-improving-your-5-g-signal-reach-out-to-the-5-gstore-support-team-https-5-gstore-com-contact-we-measure-these-values-every-day-and-can-recommend-the-right-antennas-and-routers-for-your-environment)

Whether you are going to install and manage a cellular router or deploy a cellular signal booster or amplifier system, there are a few acronyms that you'll frequently encounter. RSSI, RSRP, and RSRQ.

While these things may sound daunting at first, we'll break it down to what you need to know and provide a real-world example of how this info can be used.

RSSI is short for Received Signal Strength Indicator and is a measure of cellular signal strength. RSSI is displayed as a negative number from 0dBm (best signal) to -110dBm (weakest/no signal). RSSI is used when measuring the strength of 3G networks. A cellular router or cellular amplifier may show an RSSI of -70dBm, which would be a strong connection.

RSRP is short for Reference Signal Received Power, used when measuring 4G LTE networks. A cellular phone or another LTE-equipped device would display signal strength in RSRP, measured 0dBm (best signal) to -110dBm (weakest/no signal). An RSRP of -95dBm would be a strong signal whereas -115dBm would be very weak. Many devices show RSSI for LTE connections along with RSRP, but RSRP is a better indicator of signal strength.

RSRQ is Reference Signal Received Quality. This again only applies to 4G LTE networks and is a measure of the signal quality of a cellular connection. RSRQ is typically displayed in a range from 0dB (highest quality) to -20dB (lowest quality). Typically better signal quality results in a more reliable connection.

Say you'll be installing a Pepwave MAX BR1 for cellular backup in your home or business. To get the best performance out of the cellular connection, you will want to check its RSRP and RSRQ. If you have a weak RSRP of -105dBm and an RSRQ of -18dB, the resulting cellular network may be slow or unreliable. To improve the signal you could try to relocate the router closer to a window, or an external cellular antenna may be needed if the cellular signal is blocked or there is a metal roof on the building, for example.

Here is a quick breakdown of the numbers:

RSSI – For 3G frequencies. -70dBm is excellent, -110dBm is poor or no signal

RSRP – For LTE frequencies. -90dBm is excellent, -120dBm is poor or no signal 

RSRQ – For LTE frequencies. 0dB is no interference, -20dB is high interference

Installing or troubleshooting any cellular equipment should always include checking cellular signal strength and signal quality, and improving signal strength and quality often results in a more reliable, consistent connection.

**Finding and Interpreting RSSI, RSRP, and RSRQ**

For cellular signal boosters and amplifiers, signal information is often visible on an on-device display showing the frequencies and the gain on each. Some amplifiers have companion mobile applications or web interfaces where signal information is available. Refer to the user manual for your specific amplifier for more detailed information.

Cellular-enabled routers typically have a web user interface where cellular signal details are displayed. While all manufacturers have different locations in their web interface for signal information, it is typically found in a 'Details' or 'More Information' tab.

In a cellular-enabled Peplink or Pepwave router, log into the web interface at 192.168.50.1. From the Dashboard page, click on 'Details' to the right of the cellular interface. 

In the WAN Connection Status, you'll find the connected Band along with relevant signal information. 

In the above example the RSRP is -101dBm, and the RSRQ is -11.5dB. While the signal strength isn't bad, the signal quality is low. Moving the router to another location may provide a better signal quality, since this router is installed in a lower floor of a home. If moving the router isn't an option, an external antenna run outside to the roof would improve signal strength and quality.

For a cellular enabled Cradlepoint router, login to the web interface at 192.168.1.1 From the login page, select 'Status', 'Internet', 'Connections', and select the built in modem. 

Signal information will be displayed below, along with other device information. The above example has an RSRP of -86dBm, and an RSRQ of -9dB. This is an excellent signal strength, and while not perfect, the signal quality is within acceptable levels but should be kept in mind if cellular performance is inconsistent.

**Improving Signal Strength and Signal Quality**

As mentioned above, there are a few ways to improve cellular signal to devices like embedded routers. Let's use the [Pepwave MAX BR1 MK2](https://5gstore.com/product/7865_pepwave_max_br1_mk2.html) as an example, as a device that is commonly used for home and businesses for cellular backup to a primary connection. The included stock antennas are adequate for installations where signal is moderate to good, but in weaker signal areas, or in areas where the install location has a blocked signal, an additional antenna may be required.

A popular antenna to pair with the MAX BR1 is the [Panorama Outdoor Omni](https://5gstore.com/product/6037_panorama-wideband-mimo-3g-4g-antenna.html). This is omnidirectional, meaning it doesn't need to be aimed directly at the cell tower, simplifying installation. Since the BR1 has two cellular antenna ports, the Panorama antenna also has two 16' lengths of cable to connect directly to the router. 

The antenna can then be wall or pole mounted on the side of a home or business, on a roof, or even on a mobile command center that requires cellular connectivity.

For deployments where a router is installed in a server rack, weatherproof case, or other enclosure where signal can be blocked, other antenna options are available. Vehicles are another source of interference for cellular signal, especially since cellular routers are often installed below the dashboard or hidden away from eyes, and signal. 

The [Panorama MAKO](https://5gstore.com/product/10430_panorama-mako-5g-antenna.html) antenna is designed for vehicles, and supports up to 4×4 Cellular for Category 18 and 5G modems, WiFi, and GPS connectivity options.

5Gstore has also created a ['Guide Me'](https://5gstore.com/matching/3_cellular_wifi_gps_antenna.html) feature to help in the selection of an antenna for your deployment. Select the kind of connectivity you'll need, and we'll narrow it down to the best options for the job. Need additional assistance? [Contact the experts at 5Gstore](https://5gstore.com/site/contact_us.html) online by email or chat, or give us a call at 833-5Gstore (833-547-8673). Finally, looking for the [best 5G router](https://5gstore.com/blog/2024/10/10/best-5g-router/)?

## 🆕 2025 Update: Interpreting 5 G Signal Metrics

**Why this matters:** Since this article was first published, all major U.S. carriers have shut down their 3 G networks and dramatically expanded mid-band and mmWave 5 G coverage. Modern 5 G-capable routers and phones therefore expose additional signal metrics that complement RSSI/RSRP/RSRQ.

### Key Metrics Added for 5 G NR

**SINR (Signal-to-Interference + Noise Ratio)** – gauges how “clean” the channel is. Aim for **> 20 dB** on sub-6 GHz links and **> 25 dB** on mmWave to unlock full throughput.

**SS-RSRP (Synchronization-Signal RSRP)** – the 5 G equivalent of RSRP, measured *per beam*. Helps your modem pick the best beam when multiple 5 G sectors overlap.

**SS-RSRQ** – the quality counterpart to SS-RSRP; invaluable when fine-tuning external antennas.

### 2025 Recommended Thresholds

|   |   |   |   |   |

| --- | --- | --- | --- | --- |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

### Practical Tips

**Peplink firmware 8.4+** and **Teltonika RutOS 7.5+** surface SINR and SS-RSRP under *Status → Cellular → Details*.

When aiming external antennas for 5 G, optimize for the **highest SINR** rather than just RSRP.

**RedCap (NR-Light) IoT devices** follow the same SINR/RSRP rules but can tolerate slightly lower thresholds thanks to their smaller bandwidth.

Need deeper guidance? See our newer posts on

5 G RedCap → [https://5gstore.com/blog/2025/01/23/what-is-5g-redcap-and-why-it-matters/](https://5gstore.com/blog/2025/01/23/what-is-5g-redcap-and-why-it-matters/)

The coming 4 G shutdown → [https://5gstore.com/blog/2025/06/25/4g-shutdown/](https://5gstore.com/blog/2025/06/25/4g-shutdown/)

**5 G Router Compare Tool** → [https://5gstore.com/compare/](https://5gstore.com/compare/)

[Teltonika RSSI Info](https://wiki.teltonika-networks.com/view/RSSI)

## Questions about improving your 5 G signal? Reach out to the **5Gstore Support team** ( [https://5gstore.com/contact](https://5gstore.com/contact))—we measure these values every day and can recommend the right antennas and routers for your environment.

### Related posts:

[5G Signal Strength: What Do Signal Bars Really Mean?](https://5gstore.com/blog/2025/03/12/5g-signal-strength-meaning-of-bars/)

[How to Select the Right Donor Antenna for a Repeater System](https://5gstore.com/blog/2025/01/15/selecting-a-donor-antenna-for-repeater/)

[Best Apps for Testing Signal and Locating Cell Towers](https://5gstore.com/blog/2024/07/10/best-apps-for-testing-signal-and-locating-cell-towers/)

[How to Improve Your Cellular RSSI/ RSRP: Tips and Tricks for Better Mobile Connectivity](https://5gstore.com/blog/2023/04/10/how-to-improve-your-cellular-rssi-rsrp/)

## Post navigation

[LTE vs 5G: which router should you buy?](https://5gstore.com/blog/2021/03/23/lte-vs-5g-which-router-should-you-buy/)

[Remote Power Switch Product Overview](https://5gstore.com/blog/2021/04/20/remote-power-switch-product-overview/)

Search

Search for: Search

About This Site

Welcome to the [5Gstore](https://5Gstore.com/). We sell and support the following router manufacturers: [CradlePoint](https://5gstore.com/landing/m/cradlepoint/), [Digi](https://5gstore.com/landing/m/digi/), [Inseego](https://5gstore.com/landing/m/inseego/), [Peplink](https://5gstore.com/landing/m/peplink/), [Sierra Wireless](https://5gstore.com/landing/m/sierra_wireless/) , [Teltonika](https://5gstore.com/landing/m/teltonika/). The following antenna manufacturers: [Mobile Mark](https://5gstore.com/landing/m/mobilemark/), [Panorama](https://5gstore.com/landing/m/panorama/), [PCTel](https://5gstore.com/landing/m/pctel/), [Poynting](https://5gstore.com/landing/m/poynting/) & [Taoglas](https://5gstore.com/landing/m/taoglas/). The following cellular signal boosters: [SureCall](https://5gstore.com/landing/m/surecall/), [Wilson Connectivity](https://5gstore.com/landing/m/wilson_electronics/), [WeBoost](https://5gstore.com/landing/m/weboost/)

Powered by [MDGCS](https://www.mdgcs.com/) 

Subscribe to Our Newsletter

Stay Updated!

Once a month newsletter that summarized all of our blog posts.

First Name*

Email Address*

Subscribe

[Home](https://5gstore.com/)

[About](https://5gstore.com/blog/about/)

[Contact 5Gstore](https://5gstore.com/site/contact_us.html)

[Shop 5Gstore](https://5gstore.com/site/shop)