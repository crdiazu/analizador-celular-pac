# WO2017176840A1 - Détection de signal de bande étroite pour une

# WO2017176840A1 - Détection de signal de bande étroite pour une protection de réseau - Google Patents

## Détection de signal de bande étroite pour une protection de réseau [Download PDF](https://patentimages.storage.googleapis.com/39/f2/fe/e1960dfa9f848f/WO2017176840A1.pdf)Info

Publication number   WO2017176840A1   WO2017176840A1   PCT/US2017/026069   US2017026069W   WO2017176840A1   WO 2017176840 A1   WO2017176840 A1   WO 2017176840A1   US 2017026069 W   US2017026069 W   US 2017026069W   WO 2017176840 A1   WO2017176840 A1   WO 2017176840A1   Authority   WO   WIPO (PCT)   Prior art keywords   repeater   signal   signals   band   power   Prior art date   2016-04-05   Legal status (The legal status is an assumption and is not a legal conclusion. Google has not performed a legal analysis and makes no representation as to the accuracy of the status listed.)   Ceased   Application number   PCT/US2017/026069   Other languages  [English  ( en ) ](https://www.google.com/patent/WO2017176840A1/en)Inventor   Patrick Lee COOK   Christopher Ken ASHWORTH   Vernon Alan Vanburen   Current Assignee (The listed assignees may be inaccurate. Google has not performed a legal analysis and makes no representation or warranty as to the accuracy of the list.)    Wilson Electronics LLC  Original Assignee   Wilson Electronics LLC   Priority date (The priority date is an assumption and is not a legal conclusion. Google has not performed a legal analysis and makes no representation as to the accuracy of the date listed.)   2016-04-05   Filing date   2017-04-05   Publication date   2017-10-12   2017-04-05   Application filed by Wilson Electronics LLC   filed   Critical   Wilson Electronics LLC   2017-04-05   Priority to CN201780022064.3A   priority   Critical   patent/CN109328440A/zh   2017-10-12   Publication of WO2017176840A1   publication   Critical   patent/WO2017176840A1/fr   2018-10-05   Anticipated expiration   legal-status   Critical   Status   Ceased   legal-status   Critical   Current  

## Links

[Espacenet](https://www.google.com/patent/WO2017176840A1/en)

[Global Dossier](https://www.google.com/patent/WO2017176840A1/en)

[PatentScope](https://www.google.com/patent/WO2017176840A1/en)

[Discuss](https://www.google.com/patent/WO2017176840A1/en)

## Classifications

H — ELECTRICITY  

H04 — ELECTRIC COMMUNICATION TECHNIQUE  

H04W — WIRELESS COMMUNICATION NETWORKS  

H04W52/00 — Power management, e.g. Transmission Power Control [TPC] or power classes  

H04W52/04 — Transmission power control [TPC]  

H04W52/52 — Transmission power control [TPC] using AGC [Automatic Gain Control] circuits or amplifiers  

H — ELECTRICITY  

H04 — ELECTRIC COMMUNICATION TECHNIQUE  

H04B — TRANSMISSION  

H04B7/00 — Radio transmission systems, i.e. using radiation field  

H04B7/14 — Relay systems  

H04B7/15 — Active relay systems  

H04B7/155 — Ground-based stations  

H04B7/15528 — Control of operation parameters of a relay station to exploit the physical medium  

H04B7/15535 — Control of relay amplifier gain  

## Definitions

Signal boosters and repeaters   can be used to increase the quality of wireless communication between a wireless device and a wireless communication access point, such as a cell tower. Signal boosters can improve the quality of the wireless  

the signal booster   can receive, via an antenna, downlink signals from the wireless communication access point.  

the signal booster   can amplify the downlink signal and then provide an amplified downlink signal to the wireless device.  

the signal booster   can act as a relay between the wireless device and the wireless communication access point.  

the wireless device   can receive a stronger signal from the wireless communication access point.  

uplink signals from the wireless device   e.g., telephone calls and other data  

the signal booster   can amplify the uplink signals before communicating, via an antenna, the uplink signals to the wireless communication access point.  

FIG. 1   illustrates a signal booster in communication with a wireless device and a base station in accordance with an example  

FIG. 2   illustrates a signal booster that includes a broadband signal detector in accordance with an example  

FIG. 3   illustrates a signal booster that includes a narrowband signal detector in accordance with an example  

FIG. 4   illustrates an analog narrowband detector in accordance with an example  

FIG. 5   illustrates a digital narrowband detector in accordance with an example  

FIG. 6   illustrates a wireless device in accordance with an example.  

FIG. 1   illustrates an exemplary signal booster 120 in communication with a wireless device 110 and a base station 130.  

the signal booster 120   can be referred to as a repeater.  

a repeater   can be an electronic device used to amplify (or boost) signals.  

the signal booster 120   (also referred to as a cellular signal amplifier) can improve the quality of wireless communication by amplifying, filtering, and/or applying other processing techniques via a signal amplifier 122 to uplink signals communicated from the wireless device 110 to the base station 130 and/or downlink signals communicated from the base station 130 to the wireless device 110.  

the signal booster 120   can amplify or boost uplink signals and/or downlink signals bi-directionally.  

the signal booster 120   can be at a fixed location, such as in a home or office.  

the signal booster 120   can be attached to a mobile object, such as a vehicle or a wireless device 110.  

the signal booster 120   can include an integrated device antenna 124 (e.g., an inside antenna or a coupling antenna) and an integrated node antenna 126 (e.g., an outside antenna).  

the integrated node antenna 126   can receive the downlink signal from the base station 130.  

the downlink signal   can be provided to the signal amplifier 122 via a second coaxial cable 127 or other type of radio frequency connection operable to communicate radio frequency signals.  

the signal amplifier 122   can include one or more cellular signal amplifiers for amplification and filtering.  

the downlink signal that has been amplified and filtered   can be provided to the integrated device antenna 124 via a first coaxial cable 125 or other type of radio frequency connection operable to communicate radio frequency signals.  

the integrated device antenna 124   can wirelessly communicate the downlink signal that has been amplified and filtered to the wireless device 110.  

the integrated device antenna 124   can receive an uplink signal from the wireless device 110.  

the uplink signal   can be provided to the signal amplifier 122 via the first coaxial cable 125 or other type of radio frequency connection operable to communicate radio frequency signals.  

the signal amplifier 122   can include one or more cellular signal amplifiers for amplification and filtering.  

the uplink signal that has been amplified and filtered   can be provided to the integrated node antenna 126 via the second coaxial cable 127 or other type of radio frequency connection operable to communicate radio frequency signals.  

the integrated device antenna 126   can communicate the uplink signal that has been amplified and filtered to the base station 130.  

the signal booster 120   can filter the uplink and downlink signals using any suitable analog filtering technology including, but not limited to, surface acoustic wave (SAW) filters, bulk acoustic wave (BAW) filters, film bulk acoustic resonator (FBAR) filters, ceramic filters, waveguide filters or low-temperature co-fired ceramic (LTCC) filters.  

SAW   surface acoustic wave  

BAW   bulk acoustic wave  

FBAR   film bulk acoustic resonator  

ceramic filters   ceramic filters  

waveguide filters   or low-temperature co-fired ceramic (LTCC) filters.  

LTCC   low-temperature co-fired ceramic  

the signal booster 120   can send uplink signals to a node and/or receive downlink signals from the node.  

the node   can comprise a wireless wide area network (WWAN) access point (AP), a base station (BS), an evolved Node B (eNB), a baseband unit (BBU), a remote radio head (RRH), a remote radio equipment (RRE), a relay station (RS), a radio equipment (RE), a remote radio unit (RRU), a central processing module (CPM), or another type of WWAN access point.  

WWAN   wireless wide area network  

AP   wireless wide area network  

BS   base station  

eNB   evolved Node B  

BBU   baseband unit  

RRH   remote radio head  

RRE   remote radio equipment  

RS   relay station  

RE   radio equipment  

RRU   remote radio unit  

CCM   central processing module  

the signal booster 120 used to amplify the uplink and/or a downlink signal   is a handheld booster.  

the handheld booster   can be implemented in a sleeve of the wireless device 110.  

the wireless device sleeve   can be attached to the wireless device 110, but can be removed as needed.  

the signal booster 120   can automatically power down or cease amplification when the wireless device 110 approaches a particular base station.  

the signal booster 120   can determine to stop performing signal amplification when the quality of uplink and/or downlink signals is above a defined threshold based on a location of the wireless device 110 in relation to the base station 130.  

the signal booster 120   can include a battery to provide power to various components, such as the signal amplifier 122, the integrated device antenna 124 and the integrated node antenna 126.  

the battery   can also power the wireless device 110 (e.g., phone or tablet).  

the signal booster 120   can receive power from the wireless device 110.  

the signal booster 120   can be a Federal Communications Commission (FCC)-compatible consumer signal booster.  

FCC   Federal Communications Commission  

the signal booster 120   can be compatible with FCC Part 20 or 47 Code of Federal  

the signal booster 120   can operate on the frequencies used for the provision of subscriber-based services under parts 22 (Cellular), 24 (Broadband PCS), 27 (AWS-1 , 700 MHz Lower A-E Blocks, and 700 MHz Upper C Block), and 90 (Specialized Mobile Radio) of 47 C.F.R.  

the signal booster 120   can be configured to automatically self-monitor its operation to ensure compliance with applicable noise and gain limits.  

the signal booster 120   can either self-correct or shut down automatically if the signal booster's operations violate the regulations defined in FCC Part 20.21.  

the signal booster 120   can improve the wireless connection between the wireless device 110 and the base station 130 (e.g., cell tower) or another type of wireless wide area network (WWAN) access point (AP).  

the signal booster 120   can boost signals for cellular standards, such as the Third Generation Partnership Project (3GPP) Long Term Evolution (LTE) Release 8, 9, 10, 11, 12, or 13 standards or Institute of Electronics and Electrical Engineers (IEEE) 802.16.  

3GPP   Third Generation Partnership Project  

LTE   Long Term Evolution  

IEEE   Institute of Electronics and Electrical Engineers  

the signal booster 120   can boost signals for 3 GPP LTE Release 13.0.0 (March 2016) or other desired releases.  

the signal booster 120   can boost signals from the 3GPP Technical  

the signal booster 120   can boost signals from the LTE frequency bands: 2, 4, 5, 12, 13, 17, and 25.  

the signal booster 120   can boost selected frequency bands based on the country or region in which the signal booster is used, including any of bands 1 -70 or other bands, as disclosed in ETSI TS136 104 V13.5.0 (2016-10).  

the number of LTE frequency bands and the level of signal improvement   can vary based on a particular wireless device, cellular node, or location. Additional domestic and international frequencies can also be included to offer increased functionality. Selected models of the signal booster 120 can be configured to operate with selected frequency bands based on the location of use. In another example, the signal booster 120 can automatically sense from the wireless device 110 or base station 130 (or GPS, etc.) which frequencies are used, which can be a benefit for international travelers.  

the integrated device antenna 124 and the integrated node antenna 126   can be comprised of a single antenna, an antenna array, or have a telescoping form- factor.  

the integrated device antenna 124 and the integrated node antenna 126   can be a microchip antenna.  

An example of a microchip antenna   is  

the integrated device antenna 124 and the integrated node antenna 126   can be a printed circuit board (PCB) antenna.  

PCB   printed circuit board  

An example of a PCB antenna   is TE 2118310-1.  

the integrated device antenna 124   can receive uplink (UL) signals from the wireless device 100 and transmit DL signals to the wireless device 100 using a single antenna.  

the integrated device antenna 124   can receive UL signals from the wireless device 100 using a dedicated UL antenna, and the integrated device antenna 124 can transmit DL signals to the wireless device 100 using a dedicated DL antenna.  

the integrated device antenna 124   can communicate with the wireless device 110 using near field communication.  

the integrated device antenna 124   can communicate with the wireless device 110 using far field  

the integrated node antenna 126   can receive downlink (DL) signals from the base station 130 and transmit uplink (UL) signals to the base station 130 via a single antenna.  

the integrated node antenna 126   can receive DL signals from the base station 130 using a dedicated DL antenna, and the integrated node antenna 126 can transmit UL signals to the base station 130 using a dedicated UL antenna.  

multiple signal boosters   can be used to amplify UL and DL signals.  

a first signal booster   can be used to amplify UL signals and a second signal booster can be used to amplify DL signals.  

different signal boosters   can be used to amplify different frequency ranges.  

the signal booster 120   can be configured to identify when the wireless device 110 receives a relatively strong downlink signal.  

a strong downlink signal   can be a downlink signal with a signal strength greater than approximately -80dBm.  

the signal booster 120   can be configured to automatically turn off selected features, such as amplification, to conserve battery life.  

the integrated booster   can be configured to provide amplification of the downlink signal.  

An example of a weak downlink signal   can be a downlink signal with a signal strength less than -80dBm.  

the signal booster 120   can also include one or more of: a waterproof casing, a shock absorbent casing, a flip-cover, a wallet, or extra memory storage for the wireless device.  

extra memory storage   can be achieved with a direct connection between the signal booster 120 and the wireless device 110.  

NFC   Near-Field Communications  

Bluetooth v4.0   Bluetooth Low Energy  

Bluetooth v4.1   Bluetooth v4.2  

Bluetooth 5   Ultra High Frequency  

3 GPP LTE   Institute of Electronics and Electrical Engineers (IEEE) 802.11 a, IEEE 802.11b, IEEE 802.  

IEEE 802.11 ⁇   can be used to couple the signal booster 120 with the wireless device 110 to enable data from the wireless device 110 to be communicated to and stored in the extra memory storage that is integrated in the signal booster 120.  

a connector   can be used to connect the wireless device 110 to the extra memory storage.  

the signal booster 120   can include photovoltaic cells or solar panels as a technique of charging the integrated battery and/or a battery of the wireless device 110.  

the signal booster 120   can be configured to communicate directly with other wireless devices with signal boosters.  

the integrated node antenna 126   can communicate over Very High Frequency (VHF) communications directly with integrated node antennas of other signal boosters.  

VHF   Very High Frequency  

the signal booster 120   can be configured to communicate with the wireless device 110 through a direct connection, Near-Field Communications (NFC), Bluetooth v4.0, Bluetooth Low Energy, Bluetooth v4.1, Bluetooth v4.2, Ultra High Frequency (UHF), 3 GPP LTE, Institute of Electronics and Electrical Engineers (IEEE) 802.11a, IEEE 802.11b, IEEE 802.  

ISM   industrial, scientific and medical  

Examples of such ISM bands   include 2.4 GHz, 3.6 GHz, 4.9 GHz, 5 GHz, or 5.9 GHz.  

This configuration   can allow data to pass at high rates between multiple wireless devices with signal boosters.  

This configuration   can also allow users to send text messages, initiate phone calls, and engage in video communications between wireless devices with signal boosters.  

the integrated node antenna 126   can be configured to couple to the wireless device 110. In other words, communications between the integrated node antenna 126 and the wireless device 110 can bypass the integrated booster.  

a separate VHF node antenna   can be configured to communicate over VHF communications directly with separate VHF node antennas of other signal boosters. This configuration can allow the integrated node antenna 126 to be used for simultaneous cellular communications.  

the separate VHF node antenna   can be configured to communicate with the wireless device 110 through a direct connection, Near-Field Communications (NFC), Bluetooth v4.0, Bluetooth Low Energy, Bluetooth v4.1 , Bluetooth v4.2, Ultra High Frequency (UHF), 3 GPP LTE, Institute of Electronics and Electrical Engineers (IEEE) 802.11 a, IEEE 802.11b, IEEE 802. llg, IEEE 802.11 ⁇ , IEEE 802.1 l ac, IEEE 802.11 ad, a TV White Space Band (TVWS), or any other industrial, scientific and medical (ISM) radio band.  

NFC   Near-Field Communications  

Bluetooth v4.0   Bluetooth Low Energy  

Bluetooth v4.2   Bluetooth Ultra High Frequency  

3 GPP LTE   Institute of Electronics and Electrical Engineers (IEEE) 802.11 a  

the signal booster 120   can be configured for satellite communication.  

the integrated node antenna 126   can be configured to act as a satellite communication antenna.  

a separate node antenna   can be used for satellite communications.  

the signal booster 120   can extend the range of coverage of the wireless device 110 configured for satellite communication.  

the integrated node antenna 126   can receive downlink signals from satellite communications for the wireless device 110.  

the signal booster 120   can filter and amplify the downlink signals from the satellite communication.  

the wireless device 110   can be configured to couple to the signal booster 120 via a direct connection or an ISM radio band.  

ISM bands   include 2.4 GHz, 3.6 GHz, 4.9 GHz, 5 GHz, or 5.9 GHz.  

a cellular signal booster or repeater   can include a controller operable to perform network protection in order to protect a cellular network from overload and/or noise floor increase.  

the controller   can perform network protection by adjusting a gain and/or noise power for each band in uplink transmission paths based on data from each band in downlink transmission paths.  

the data from each band in the downlink transmission paths   can include a booster station coupling loss (BSCL) or a received signal strength indication (RSSI).  

the controller   can perform network protection in accordance with the Federal Communications Commission (FCC) Consumer Booster Rules, which necessitate that uplink signal paths and downlink signal paths are to operate jointly to achieve network protection. Therefore, if the cellular signal booster includes multiple downlink signal chains and a single uplink signal chain, then each downlink signal chain can relate to or communicate with the single uplink signal chain for network protection purposes.  

FCC   Federal Communications Commission  

the controller   in order to perform network protection, can identify a received signal strength indication (RSSI) for each band in the selected number of downlink transmission paths.  

the controller   can identify one or more downlink transmission paths that correspond to a maximum RSSI as compared to other downlink transmission paths in the cellular signal booster.  

the controller   can adjust (e.g., increase or decrease) an uplink gain or noise power for each band in the selected number of uplink transmission paths based on the maximum RSSI for each band.  

the cellular signal booster   can protect a base station in the cellular network from becoming overloaded with uplink signals from the cellular signal booster that exceed a defined power threshold.  

the controller   in order to perform network protection, can identify a booster station coupling loss (BSCL) for each band in a selected number of downlink transmission paths.  

the controller   can identify one or more downlink transmission paths that correspond to a minimum BSCL for each band as compared to other downlink transmission paths in the cellular signal booster.  

the controller   can adjust (e.g., increase or decrease) an uplink gain or noise power for each band in the selected number of uplink transmission paths based on the minimum BSCL for each band.  

each band in the cellular signal booster   can be adjusted separately.  

the cellular signal booster   can protect a base station in the cellular network from becoming overloaded with uplink signals from the cellular signal booster that exceed a defined power threshold.  

the controller   can reduce the uplink gain for each band on the uplink transmission path when the BSCL is relatively low.  

a first DL path at a first band   can be associated with a first RSSI  

a second DL path at a second band   can be associated with a second RSSI.  

a maximum RSSI value   can be identified between the first RSSI and the second RSSI.  

the uplink gain or noise power on the UL signal path at a selected band   can be adjusted (e.g., increased or decreased) based on the maximum RSSI value in order to protect the base station in the cellular network.  

the RSSI for each DL path   can effectively estimate a distance between the cellular signal booster and the base station.  

the RSSI   can be relatively high, and therefore, the uplink gain or noise power on the UL signal path can be reduced for each band in order to protect the base station. If the uplink gain is not reduced, then the base station's noise floor can be raised and/or the base station can be overloaded with strong uplink signals from the cellular signal booster (i.e., uplink signals that exceed a defined power threshold). In addition, reducing the uplink gain can protect the base station's uplink receive sensitivity. In another example, if the cellular signal booster is located relatively far from the base station, then the RSSI can be relatively low, and therefore, the uplink gain or noise power on the UL signal path can be increased for each band.  

FIG. 2   illustrates an example of a bi-directional broadband cellular signal booster 200 (or repeater).  

the cellular signal booster 200   can include an outside antenna 210, an inside antenna 220 and a controller 230.  

the outside antenna 210   can send/receive signals to a base station (not shown).  

the inside antenna 220   can send/receive signals to a mobile device (not shown).  

the controller 230   can perform various functions for the cellular signal booster 200, such as automatic gain control, oscillation detection, and other network protection standards.  

the cellular signal booster 200   can include a first duplexer 212 and a second duplexer 222.  

a downlink signal path   can be communicatively coupled between the first duplexer 212 and the second duplexer 222.  

the downlink signal path   can include one or more amplifiers (e.g., A04, A05 and A06) and one or more DL bandpass filters (BPF) for amplification and filtering of downlink signals, respectively.  

amplifiers   e.g., A04, A05 and A06  

BPF   DL bandpass filters  

an uplink signal path   can be communicatively coupled between the first duplexer 212 and the second duplexer 222.  

the uplink signal path   can include one or more amplifiers (e.g., A01, A02 and A03) and one or more UL bandpass filters (BPF) for amplification and filtering of uplink signals, respectively.  

amplifiers   e.g., A01, A02 and A03  

BPF   UL bandpass filters  

the outside antenna 210   can receive a downlink signal from the base station.  

the downlink signal   can be provided to the first duplexer 212, and then to the downlink signal path for amplification and filtering.  

the downlink signal   (which has now been amplified and filtered) can be provided to the second duplexer 212, and then to the inside antenna 220 for transmission to the mobile device.  

the inside antenna 220   can receive an uplink signal from the mobile device.  

the uplink signal   can be provided to the second duplexer 222, and then to the uplink signal path for amplification and filtering.  

the uplink signal   (which has now been amplified and filtered) can be provided to the first duplexer 212, and then to the outside antenna 210 for transmission to the base station.  

the cellular signal booster 200   can include UL and DL BPFs in the uplink and downlink signal paths, respectively.  

Each UL and DL BPF   can have a defined passband, which is measured in megahertz (MHz). All signals on frequencies within a certain passband can pass through the corresponding UL or DL BPF, while signals on frequencies that are outside that certain passband are attenuated.  

the cellular signal booster 200   when the cellular signal booster 200 is a multiple-band signal booster, the cellular signal booster 200 can include a radio frequency (RF) detector on each uplink and downlink band, as the cellular signal booster 200 can always be operating on all bands.  

the downlink signal path   can include a DL RF detector 214 and the uplink signal path can include an UL RF detector 224.  

the DL and UL RF detectors 214, 224   can enable the controller 230 to perform various functions for the cellular signal booster 200, such as automatic gain control, oscillation detection, and other network protection standards.  

the DL and UL RF detectors 214, 224   can be diodes, or alternatively, the DL and UL RF detectors 214, 224 can be log-detector integrated circuits (ICs), which can achieve an increased detection range.  

the DL and UL RF detectors 214, 224   can be positioned after the DL and UL BPFs, respectively, in the cellular signal booster 200.  

the DL and UL RF detectors 214, 224   can convert a composite signal power in the respective BPF's entire passband to a proportional direct current (DC) voltage.  

DC   proportional direct current  

some network protection standards   such as the FCC  

Consumer Booster Standard   require determining a distance between the cellular signal booster 300 and a base station. This determination of the distance can allow the cellular signal booster 300 to adjust its gain and/or noise power output to protect the base station (and the cellular network as a whole).  

the cellular signal booster 300   can detect a composite downlink power in an entire passband associated with the DL BPF (via the DL RF detector 214) in order to determine the distance between the cellular signal booster and the base station.  

the composite downlink power   can be expressed as a received signal strength indication (RSSI).  

a wideband consumer signal booster   can satisfy a consumer signal booster network protection standard when a transmitted noise power in dBm/MHz of the consumer signal booster at their uplink and downlink ports does not exceed [-103 dBm/MHz - RSSI].  

the RSSI   is the downlink composite received signal power in dBm at a booster donor port for all base stations in the band of operation. RSSI is expressed in negative dB units relative to 1 mW.  

the base station transmitted power   can usually be significantly higher than the underlying assumptions made when determining the minimum power that is transmitted from the base station.  

the composite downlink power that is detected by the DL RF detector 214 in an entire passband   can include a downlink power associated with multiple base stations that are in the same area as the cellular signal booster 200.  

the composite downlink power   can be increased due to the multiple base stations in the area.  

the cellular signal booster 200   can detect the composite downlink power associated with the multiple base stations in the area (as opposed to detection of downlink power associated with individual base stations), in previous solutions, the cellular signal booster 200 would detect a stronger downlink signal (i.e., with a stronger power level), and thus the controller 230 in the cellular signal booster 200 would start reducing its gain and/or noise power in a reduced amount of time (e.g., sooner than necessary).  

FIG. 3   illustrates an example of a bi-directional broadband cellular signal booster 300 (or repeater).  

the cellular signal booster 300   can include an outside antenna 310, an inside antenna 320 and a controller 330.  

the outside antenna 310   can send/receive signals to a base station (not shown).  

the inside antenna 320   can send/receive signals to a mobile device (not shown).  

the controller 330   can perform various functions for the cellular signal booster 300, such as automatic gain control, oscillation detection, and other network protection standards.  

the cellular signal booster 300   can include a first duplexer 312 and a second duplexer 322.  

a downlink signal path   can be communicatively coupled between the first duplexer 312 and the second duplexer 322.  

the downlink signal path   can include one or more amplifiers (e.g., A04, A05 and A06) and one or more DL bandpass filters (BPF) for amplification and filtering of downlink signals, respectively.  

BPF   DL bandpass filters  

an uplink signal path   can be communicatively coupled between the first duplexer 312 and the second duplexer 322.  

the uplink signal path   can include one or more amplifiers (e.g., A01, A02 and A03) and one or more UL bandpass filters (BPF) for amplification and filtering of uplink signals, respectively.  

the cellular signal booster 300   can be a broadband or wideband detector that is operable to perform narrowband detection.  

the cellular signal booster 300   cab include a downlink narrowband (NB) detector 314 in the downlink signal path and an uplink narrowband detector 324 in the uplink signal path.  

the downlink narrowband detector 314   can detect downlink power levels associated with signals communicated from base station(s) to the cellular signal booster 300 in sub-blocks or channels or sub-bands in a defined passband.  

the downlink power levels   can be RSSI values. Higher RSSI values can correspond to signals that are transmitted from base stations that are a relatively close distance from the cellular signal booster 300, while lower RSSI values can correspond to signals that are transmitted from base stations that are a relatively far distance from the cellular signal booster 300.  

the detected downlink power levels   can be provided from the downlink narrowband detector 314 to the controller 330.  

the controller 330   can identify the downlink power levels and select one of the downlink power levels. For example, the controller 330 can select a maximum power level, which can correspond to a signal transmitted from a base station that is a shortest distance from the cellular signal booster 300 among a group of base stations.  

the controller 300   can select one of the downlink power levels using a different criterion (e.g., a minimum power level, etc.) Then, the controller 330 can adjust (e.g., increase or decrease) its gain and/or noise power in accordance with the selected downlink power level.  

the controller 330   when the controller 330 selects the maximum power level, the controller 330 can adjust its gain and/or noise power only for the nearest base station among the group of base stations, as the nearest base station can be most impacted by the cellular signal booster 300 as compared to the other base stations in the group.  

the downlink narrowband detector 314   can be in contrast to a broadband detector, which would detect a composite downlink power for signals communicated in an entire passband).  

the downlink power levels   are each associated with signals transmitted in sub-blocks or channels or sub-bands in the defined passband (as opposed to the entire passband), the downlink power levels may be smaller than a composite downlink power that would be detected by a broadband detector.  

this reduced detection bandwidth   can potentially reduce the signal power presented to the downlink narrowband detector 314, which can allow the cellular signal booster 300 to maintain a maximum gain and noise power.  

competitor signal boosters that only detect the composite downlink power   may be forced to reduce their gain and/or noise power.  

the downlink narrowband detector 314   By utilizing the downlink narrowband detector 314 to detect power levels for each sub-block or channel or sub-band, the cellular signal booster 300 can achieve increased signal coverage and customer satisfaction based on the maximum gain and noise power.  

a selected passband   can be a B25 downlink passband, which can correspond to 1930-1995 megahertz (MHz). While a broadband detector would detect a composite power level for the entire 65 MHz band, a narrowband detector can detect power levels for selected sub-blocks or channels or sub-bands in the B25 downlink passband. These selected sub-blocks or channels or sub-bands can range from 100 kilohertz (kHz) or less up to 20 MHz or more depending on network constraints.  

kHz   kilohertz  

the downlink narrowband detector 314 in the cellular signal booster 300   can detect one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band.  

the downlink narrowband detector 314   can detect the one or more power levels by sweeping the selected band.  

the power levels   can include RSSI levels.  

the controller 330   can select a signal from the one or more signals based on a power level of the selected signal.  

the power level of the selected signal   can correspond to a maximum power level of the one or more signals communicated in the selected band.  

the controller 330   can adjust a gain or output power of the cellular signal booster 300 based on the power level of the selected signal communicated in the one or more sub-bands of the selected band. In one example, the controller 330 can adjust the gain or output power of the cellular signal booster 300 to meet a network protection or government standard.  

the downlink narrowband detector 314 in the cellular signal booster 300   can detect one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band.  

the controller 330   can select a power level from the one or more power levels, and the selected power level can correspond to one of the signals communicated in the one or more sub-bands of the selected band.  

the controller 330   can adjust a gain or output power of the repeater based on the selected power level.  

the controller 330   can determine a distance between the cellular signal booster 300 and each base station that transmits the one or more signals in the selected band based on the one or more power levels that correspond to the one or more signals. In another configuration, the controller 330 can adjust one or more of: the gain, a transmitted noise power or the output power of the cellular signal booster 300 to protect a base station that is a shortest distance from the cellular signal booster 300 among a plurality of base stations. The base station that is the shortest distance from the cellular signal booster 300 among the plurality of base stations can communicate a signal with a maximum power level as compared to the one or more signals communicated from the plurality of base stations.  

the controller 330   can adjust the gain of the cellular signal booster 300 to protect a base station among a plurality of base stations, and the protected base station is not a shortest distance from the cellular signal booster 300 among the plurality of base stations.  

the controller 330   can adjust the gain (and not noise power) to protect a base station that is further way than a nearest base station.  

the gain (and not noise power)   can be adjusted in this manner when there are no users on the nearest base station.  

the downlink narrowband detector 314   can have a variable narrowband detection bandwidth depending on network conditions.  

each of the one or more sub-bands included in the selected band   can range from 100 kilohertz (KHz) to 20 megahertz (MHz) depending on network conditions.  

the frequency of the sub-bands   can be less than the frequency of the selected bands.  

the one or more sub-bands   can be associated with known cellular carriers.  

a particular cellular carrier   can own and/or operate a specific sub- band in a selected band (e.g., a particular cellular carrier can own/operate 5-10 MHz in B25, which has a frequency range of 65 MHz).  

the controller 330   can perform network protection to protect individual cellular carriers that operate in predefine sub-bands of a selected band.  

a particular cellular carrier   can operate 10 MHz in B25, which has a frequency range of 65 MHz.  

the controller 330   can use the downlink narrowband detector 314 to detect power levels corresponding to only the 10 MHz in B25 which is operated by the particular cellular carrier, as opposed to determining a composite power level that corresponds to the entire B25 (i.e., all 65 MHz of B25), which can be operated by multiple cellular carriers.  

the power levels corresponding to the 10 MHz in B25 which is operated by the particular cellular carrier   can be smaller than the composite power level corresponding to the entire B25, which can result in a more accurate reduction of a gain and/or noise power when performing network protection.  

the downlink narrowband detector 314   can scan a selected band and identify a plurality of power levels for sub-bands in the selected band.  

the frequency range of each of the sub-bands   e.g., 1 MHz  

the controller 330   can receive the plurality of power levels from the downlink narrowband detector 314.  

the controller 330   can select one of the power levels (which corresponds to a signal that is transmitted with a highest channel power), and then perform network protection for the cellular signal booster 300 based on the selected power level.  

the cellular signal booster 300   can include a broadband detector configured to measure a composite power level of the selected band.  

the cellular signal booster 300   can include a single pole double throw (SPDT) switch or a single pole single throw (SPST) switch operable to switch between the broadband detector and the downlink narrowband detector 314.  

the cellular signal booster 300   can include diode or log-detector that can be used for both narrowband and broadband detection. For example, the diode or log-detector can switch between a narrowband detection mode and a broadband detection mode.  

the downlink and uplink narrowband detectors 314, 324   can be implemented in a variety of manners.  

the downlink and uplink narrowband detectors 314, 324   can be spectrum analyzers.  

the downlink and uplink narrowband detectors 314, 324   can be variable bandwidth narrowband detectors that utilize mixers, synthesizers and intermediate frequency (IF) filters.  

IF   intermediate frequency  

the downlink and uplink narrowband detectors 314, 324   can be digital narrowband detectors, in which IF filters can be replaced with analog-to-digital (ADC) converters and processors.  

ADC   analog-to-digital  

the usage of digital narrowband detectors   can eliminate sweeping the selected band, which can achieve faster performance.  

the downlink and uplink narrowband detectors 314, 324   can include internal band pass filter (BPF) functions.  

BPF   band pass filter  

the downlink narrowband detector 314   can be utilized only for the downlink signal path, whereas the uplink narrowband detector 324 can be utilized only for the uplink signal path, which can overcome isolation concerns.  

the usage of the uplink narrowband detector 324   can enable an enhanced base station overload protection.  

the same narrowband detector   can be utilized for both the downlink and uplink signal paths.  

the cellular signal booster 300   can include single pole single throw (SPST) and/or single pole double throw (SPDT) switch to each of the uplink and/or downlink signal paths in order to increase isolation.  

SPST   single pole single throw  

SPDT   single pole double throw  

FIG. 4   illustrates an exemplary analog narrowband detector.  

a signal   can be provided to a mixer.  

the mixer   can be communicatively coupled to a synthesizer.  

the signal   can be provided from the mixer to an intermediate frequency (IF) filter.  

IF   intermediate frequency  

RF   radio frequency  

the analog narrowband detector   can be utilized in a cellular signal booster or repeater.  

FIG. 5   illustrates an exemplary digital narrowband detector.  

a signal   can be provided to a mixer.  

the mixer   can be communicatively coupled to a synthesizer.  

the signal   can be provided from the mixer to an anti-aliasing filter and then to an analog-to-digital (ADC) converter and then to a fast Fourier transform (FFT) and processor.  

ADC   analog-to-digital  

FFT   fast Fourier transform  

the digital narrowband detector   can be utilized in a cellular signal booster or repeater.  

FIG. 6   provides an example illustration of the wireless device, such as a user equipment (UE), a mobile station (MS), a mobile communication device, a tablet, a handset, a wireless transceiver coupled to a processor, or other type of wireless device.  

the wireless device   can include one or more antennas configured to communicate with a node or transmission station, such as an access point (AP), a base station (BS), an evolved Node B (eNB), a baseband unit (BBU), a remote radio head (RRH), a remote radio equipment (RRE), a relay station (RS), a radio equipment (RE), a remote radio unit (RRU), a central processing module (CPM), or other type of wireless wide area network (WWAN) access point.  

the wireless device   can communicate using separate antennas for each wireless communication standard or shared antennas for multiple wireless communication standards.  

the wireless device   can communicate in a wireless local area network (WLAN), a wireless personal area network (WPAN), and/or a WWAN.  

WLAN   wireless local area network  

FIG. 6   also provides an illustration of a microphone and one or more speakers that can be used for audio input and output from the wireless device.  

the display screen   can be a liquid crystal display (LCD) screen, or other type of display screen such as an organic light emitting diode (OLED) display.  

the display screen   can be configured as a touch screen.  

the touch screen   can use capacitive, resistive, or another type of touch screen technology.  

An application processor and a graphics processor   can be coupled to internal memory to provide processing and display capabilities.  

a non-volatile memory port   can also be used to provide data input/output options to a user.  

the non- volatile memory port   can also be used to expand the memory capabilities of the wireless device.  

a keyboard   can be with the wireless device or wirelessly connected to the wireless device to provide additional user input.  

a virtual keyboard   can also be provided using the touch screen.  

Example 1   includes a repeater, comprising: a narrowband detector configured to detect one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band; and a controller configured to: select a signal from the one or more signals based on a power level of the selected signal; and adjust a gain or output power of the repeater based on the power level of the selected signal communicated in the one or more sub-bands of the selected band.  

Example 2   includes the repeater of Example 1 , wherein the power level of the selected signal corresponds to a maximum power level of the one or more signals communicated in the selected band.  

Example 3   includes the repeater of any of Examples 1 to 2, wherein the controller is configured to determine a distance between the repeater and each base station that transmits the one or more signals in the selected band based on the one or more power levels that correspond to the one or more signals.  

Example 4   includes the repeater of any of Examples 1 to 3, wherein the controller is configured to adjust one or more of: the gain, a transmitted noise power or the output power of the repeater to protect a base station that is a shortest distance from the repeater among a plurality of base stations.  

Example 5   includes the repeater of any of Examples 1 to 4, wherein the base station that is the shortest distance from the repeater among the plurality of base stations communicates a signal with a maximum power level as compared to the one or more signals communicated from the plurality of base stations.  

Example 6   includes the repeater of any of Examples 1 to 5, wherein the controller is configured to adjust the gain of the repeater to protect a base station among a plurality of base stations, wherein the protected base station is not a shortest distance from the repeater among the plurality of base stations.  

Example 7   includes the repeater of any of Examples 1 to 6, further comprising a second narrowband detector, wherein the narrowband detector is utilized for a selected downlink band and the second narrowband detector is used for a selected uplink band.  

Example 8   includes the repeater of any of Examples 1 to 7, wherein the narrowband detector is configured to detect the one or more power levels by sweeping the selected band.  

Example 9   includes the repeater of any of Examples 1 to 8, wherein each of the one or more sub-bands included in the selected band can range from 100 kilohertz (KHz) to 20 megahertz (MHz) depending on network conditions.  

KHz   kilohertz  

MHz   megahertz  

Example 10   includes the repeater of any of Examples 1 to 9, wherein the one or more sub-bands are associated with known cellular carriers.  

Example 11   includes the repeater of any of Examples 1 to 10, wherein the controller is configured to perform one or more of: automatic gain control, oscillation detection or network protection for the repeater.  

Example 12   includes the repeater of any of Examples 1 to 11 , further comprising a broadband detector configured to measure a composite power level of the selected band.  

Example 13   includes the repeater of any of Examples 1 to 12, further comprising a single pole double throw (SPDT) switch or a single pole single throw (SPST) switch operable to switch between the broadband detector and the narrowband detector.  

SPDT   single pole double throw  

SPST   single pole single throw  

Example 14   includes the repeater of any of Examples 1 to 13, further comprising one or more signal paths to amplify and filter signals, wherein the signals include one or more of uplink signals or downlink signals.  

Example 15   includes the repeater of any of Examples 1 to 14, wherein the one or more power levels include received signal strength indicator (RSSI) levels.  

RSSI   received signal strength indicator  

Example 16   includes the repeater of any of Examples 1 to 15, wherein a narrowband detection bandwidth of the narrowband detector is variable depending on network conditions.  

Example 17   includes the repeater of any of Examples 1 to 16, wherein the controller is configured to adjust the gain or output power of the repeater to meet a network protection or government standard.  

Example 18   includes the repeater of any of Examples 1 to 17, wherein the narrowband detector is one or more of: a spectrum analyzer; a variable bandwidth narrowband detector; a digital narrowband detector; or a narrowband detector that includes a bandpass filter.  

the narrowband detector   is one or more of: a spectrum analyzer; a variable bandwidth narrowband detector; a digital narrowband detector; or a narrowband detector that includes a bandpass filter.  

Example 19   includes a signal booster, comprising: memory; and one or more processors configured to: identify one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band; select a signal from the one or more signals based on a power level of the selected signal; and perform a network protection by adjusting a gain or output power of the repeater based on the power level of the selected signal communicated in the one or more sub-bands of the selected band.  

Example 20   includes the signal booster of Example 19, wherein the power level of the selected signal corresponds to a maximum power level of the one or more signals communicated in the selected band.  

Example 21   includes the signal booster of any of Examples 19 to 20, wherein the one or more processors are configured to determine a distance between the repeater and each base station that transmits the one or more signals in the selected band based on the one or more power levels that correspond to the one or more signals.  

Example 22   includes the signal booster of any of Examples 19 to 21, wherein the one or more processors are configured to perform the network protection by adjusting the gain or output power of the repeater to protect a base station that is a shortest distance from the repeater among a plurality of base stations.  

Example 23   includes the signal booster of any of Examples 19 to 22, wherein the one or more sub-bands are associated with known cellular carriers.  

Example 24   includes the signal booster of any of Examples 19 to 23, wherein each of the one or more sub-bands included in the selected band can range from 100 kilohertz (KHz) or less to 20 megahertz (MHz) or more depending on network conditions.  

KHz   kilohertz  

MHz   megahertz  

Example 25   includes a repeater, comprising: at least one narrowband detector configured to detect one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band; and a controller configured to: select a power level from the one or more power levels, wherein the selected power level corresponds to one of the signals communicated in the one or more sub-bands of the selected band; and adjust a gain or output power of the repeater based on the selected power level.  

a repeater   comprising: at least one narrowband detector configured to detect one or more power levels that correspond to one or more signals communicated in one or more sub-bands of a selected band; and a controller configured to: select a power level from the one or more power levels, wherein the selected power level corresponds to one of the signals communicated in the one or more sub-bands of the selected band; and adjust a gain or output power of the repeater based on the selected power level.  

Example 26   includes the repeater of Example 25, wherein the selected power level corresponds to a maximum power level among the one or more power levels.  

Example 27   includes the repeater of any of Examples 25 to 26, wherein the at least one narrowband detector includes a narrowband detector for each selected uplink band and selected downlink band.  

Example 28   includes the repeater of any of Examples 25 to 27, wherein the controller is configured to adjust the gain or output power of the repeater to meet a network protection or government standard.  

Various techniques, or certain aspects or portions thereof,   can take the form of program code (i.e., instructions) embodied in tangible media, such as floppy diskettes, compact disc-read-only memory (CD-ROMs), hard drives, non-transitory computer readable storage medium, or any other machine-readable storage medium wherein, when the program code is loaded into and executed by a machine, such as a computer, the machine becomes an apparatus for practicing the various techniques.  

Circuitry   can include hardware, firmware, program code, executable code, computer instructions, and/or software.  

a non-transitory computer readable storage medium   can be a computer readable storage medium that does not include signal.  

the computing device   can include a processor, a storage medium readable by the processor (including volatile and non-volatile memory and/or storage elements), at least one input device, and at least one output device.  

the volatile and non-volatile memory and/or storage elements   can be a random-access memory (RAM), erasable programmable read only memory (EPROM), flash drive, optical drive, magnetic hard drive, solid state drive, or other medium for storing electronic data.  

the low energy fixed location node, wireless device, and location server   can also include a transceiver module (i.e., transceiver), a counter module (i.e., counter), a processing module (i.e., processor), and/or a clock module (i.e., clock) or timer module (i.e., timer).  

a transceiver module   i.e., transceiver  

a counter module   i.e., counter  

a processing module   i.e., processor  

a clock module   i.e., clock  

timer module   i.e., timer  

One or more programs that can implement or utilize the various techniques described herein   can use an application programming interface (API), reusable controls, and the like.  

API   application programming interface  

Such programs   can be implemented in a high level procedural or object oriented programming language to communicate with a computer system.  

the program(s)   can be implemented in assembly or machine language, if desired. In any case, the language can  

processor   can include general purpose processors, specialized processors such as VLSI, FPGAs, or other types of specialized processors, as well as base band processors used in transceivers to send, receive, and process wireless communications.  

modules   can be implemented as a hardware circuit comprising custom very-large-scale integration (VLSI) circuits or gate arrays, off- the-shelf semiconductors such as logic chips, transistors, or other discrete components.  

VLSI   very-large-scale integration  

a module   can also be implemented in programmable hardware devices such as field programmable gate arrays, programmable array logic, programmable logic devices or the like.  

multiple hardware circuits or multiple processors   can be used to implement the functional units described in this specification.  

a first hardware circuit or a first processor   can be used to perform processing operations and a second hardware circuit or a second processor (e.g., a transceiver or a baseband processor) can be used to communicate with other entities.  

the first hardware circuit and the second hardware circuit   can be incorporated into a single hardware circuit, or alternatively, the first hardware circuit and the second hardware circuit can be separate hardware circuits.  

Modules   can also be implemented in software for execution by various types of processors.  

An identified module of executable code   can, for instance, comprise one or more physical or logical blocks of computer instructions, which can, for instance, be organized as an object, procedure, or function. Nevertheless, the executables of an identified module need not be physically located together, but can comprise disparate instructions stored in different locations which, when joined logically together, comprise the module and achieve the stated purpose for the module.  

a module of executable code   can be a single instruction, or many instructions, and can even be distributed over several different code segments, among different programs, and across several memory devices.  

operational data   can be identified and illustrated herein within modules, and can be embodied in any suitable form and organized within any suitable type of data structure. The operational data can be collected as a single data set, or can be distributed over different locations including over different storage devices, and can exist, at least partially, merely as electronic signals on a system or network.  

the modules   can be passive or active, including agents operable to perform desired functions.  

## Landscapes

Engineering & Computer Science  ( AREA ) 

Computer Networks & Wireless Communication  ( AREA ) 

Signal Processing  ( AREA ) 

Mobile Radio Communication Systems  ( AREA ) 

Radio Relay Systems  ( AREA ) 

## Abstract

## La présente invention concerne une technologie de répéteur. Le répéteur peut comprendre un détecteur de bande étroite conçu pour détecter un ou plusieurs niveaux de puissance correspondant à un ou plusieurs signaux communiqués dans une ou plusieurs sous-bandes d'une bande sélectionnée. Le répéteur peut comprendre un dispositif de commande. Le dispositif de commande peut sélectionner un signal parmi lesdits signaux en fonction d'un niveau de puissance du signal sélectionné. Le dispositif de commande peut régler un gain ou une puissance de sortie du répéteur en fonction du niveau de puissance du signal sélectionné communiqué dans lesdites sous-bandes de la bande sélectionnée.   PCT/US2017/026069   2016-04-05   2017-04-05   Détection de signal de bande étroite pour une protection de réseau  Ceased  [WO2017176840A1  ( fr ) ](https://www.google.com/patent/WO2017176840A1/fr)Priority Applications (1)

Application Number   Priority Date   Filing Date   Title   CN201780022064.3A  [CN109328440A  ( zh ) ](https://www.google.com/patent/CN109328440A/zh)2016-04-05   2017-04-05   用于网络保护的窄带信号检测 

## Applications Claiming Priority (2)

Application Number   Priority Date   Filing Date   Title   US201662318562P   2016-04-05   2016-04-05   US62/318,562   2016-04-05  

## Publications (1)

Publication Number   Publication Date   WO2017176840A1   true  [ WO2017176840A1 ( fr ) ](https://www.google.com/patent/WO2017176840A1/fr)2017-10-12  

# Family

## ID=59961266

## Family Applications (1)

Application Number   Title   Priority Date   Filing Date   PCT/US2017/026069   Ceased  [WO2017176840A1  ( fr ) ](https://www.google.com/patent/WO2017176840A1/fr)2016-04-05   2017-04-05   Détection de signal de bande étroite pour une protection de réseau 

## Country Status (3)

## Country   Link   US  ( 1 ) [US10356732B2  ( fr ) ](https://www.google.com/patent/US10356732B2/fr)CN  ( 1 ) [CN109328440A  ( fr ) ](https://www.google.com/patent/CN109328440A/fr)WO  ( 1 ) [WO2017176840A1  ( fr ) ](https://www.google.com/patent/WO2017176840A1/fr)Cited By (1)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [US20210336652A1  ( en ) ](https://www.google.com/patent/US20210336652A1/en)*   2017-10-16   2021-10-28   Cellphone-Mate, Inc.   Signal boosters with compensation for cable loss 

## Families Citing this family (8)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [CN110138434A  ( zh ) ](https://www.google.com/patent/CN110138434A/zh)*   2019-06-04   2019-08-16   深圳市豪位科技有限公司   Nb-iot无线直放站的工作频点自适应优化方法 [DE102019208987A1  ( de ) ](https://www.google.com/patent/DE102019208987A1/de)*   2019-06-19   2020-12-24   Molex Cvs Dabendorf Gmbh   Schaltungsanordnung zur Übertragung von Funksignalen und Verfahren zum Betrieb einer Schaltungsanordnung [CN114514780B  ( zh ) ](https://www.google.com/patent/CN114514780B/zh)*   2019-07-18   2024-07-16   奥拉智能系统有限公司   用于数字雷达的节能 [US11166222B2  ( en ) ](https://www.google.com/patent/US11166222B2/en)*   2019-08-02   2021-11-02   AR & NS Investment, LLC   Communication by a repeater system including a network of radio frequency (RF) repeater devices [DE102019220166A1  ( de ) ](https://www.google.com/patent/DE102019220166A1/de)*   2019-12-19   2021-06-24   Molex Cvs Dabendorf Gmbh   Schaltungsanordnung und Verfahren zur Identifizierung eines Frequenzbands oder Kanals [EP4068634B1  ( fr ) ](https://www.google.com/patent/EP4068634B1/fr)2020-07-01   2026-03-25   Wilson Electronics, LLC   Pré-amplificateur pour un modem [CN115333598B  ( zh ) ](https://www.google.com/patent/CN115333598B/zh)*   2021-05-11   2024-05-28   维沃移动通信有限公司   信号放大器的增益控制方法、装置及网络侧设备 [CN120825728B  ( zh ) ](https://www.google.com/patent/CN120825728B/zh)*   2025-07-30   2026-06-26   浙江龙感科技有限公司   链路监测信号产生方法和电路、链路监测方法和系统 

## Citations (4)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [US20020045461A1  ( en ) ](https://www.google.com/patent/US20020045461A1/en)*   2000-10-18   2002-04-18   David Bongfeldt   Adaptive coverage area control in an on-frequency repeater [US20040156097A1  ( en ) ](https://www.google.com/patent/US20040156097A1/en)*   2003-02-06   2004-08-12   Spotwave Wireless Inc.   Intelligent gain control in an on-frequency repeater [US20100075704A1  ( en ) ](https://www.google.com/patent/US20100075704A1/en)*   2008-08-19   2010-03-25   Shared Spectrum Company   Method and System for Dynamic Spectrum Access Using Specialty Detectors and Improved Networking [US20130203403A1  ( en ) ](https://www.google.com/patent/US20130203403A1/en)*   2011-08-23   2013-08-08   Wilson Electronics, Inc.   Verifying and mitigating oscillation in amplifiers 

## Family Cites Families (42)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [US4247939A  ( en ) ](https://www.google.com/patent/US4247939A/en)1978-11-09   1981-01-27   Sanders Associates, Inc.   Spread spectrum detector [US4776032A  ( en ) ](https://www.google.com/patent/US4776032A/en)1985-05-15   1988-10-04   Nippon Telegraph And Telephone Corporation   Repeater for a same frequency with spillover measurement [US5303395A  ( en ) ](https://www.google.com/patent/US5303395A/en)1991-11-06   1994-04-12   Mitsubishi Consumer Electronics America, Inc.   Power control with a constant gain amplifier for portable radio transceivers [US5737687A  ( en ) ](https://www.google.com/patent/US5737687A/en)1995-03-01   1998-04-07   Qualcomm Incorporated   Self-attenuating RF transceiver system using antenna and modem interfaces and cable link [FI98025C  ( fi ) ](https://www.google.com/patent/FI98025C/fi)1995-05-05   1997-03-25   Nokia Mobile Phones Ltd   Langaton paikallisverkkojärjestelmä ja sellaisen vastaanotin [US6005884A  ( en ) ](https://www.google.com/patent/US6005884A/en)1995-11-06   1999-12-21   Ems Technologies, Inc.   Distributed architecture for a wireless data communications system [US5777530A  ( en ) ](https://www.google.com/patent/US5777530A/en)1996-01-31   1998-07-07   Matsushita Electric Industrial Co., Ltd.   Switch attenuator [US5835848A  ( en ) ](https://www.google.com/patent/US5835848A/en)1996-12-30   1998-11-10   Lucent Technologies Inc.   Range repeater for a transmission system [JP3877256B2  ( ja ) ](https://www.google.com/patent/JP3877256B2/ja)1998-08-11   2007-02-07   株式会社デンソー   キーレスエントリ受信機 [US6681100B1  ( en ) ](https://www.google.com/patent/US6681100B1/en)1999-03-15   2004-01-20   Teletronics International, Inc.   Smart amplifier for time division duplex wireless applications [US6711388B1  ( en ) ](https://www.google.com/patent/US6711388B1/en)2000-03-30   2004-03-23   Nokia Corporation   Distributed power level control system of transmitter for cellular communication [US7088953B2  ( en ) ](https://www.google.com/patent/US7088953B2/en)2000-10-18   2006-08-08   Spotwave Wireless Canada Inc.   Coverage area signature in an on-frequency repeater [WO2003013028A1  ( fr ) ](https://www.google.com/patent/WO2003013028A1/fr)2001-08-02   2003-02-13   Spotwave Wireless Inc.   Commande de zone de couverture adaptative dans un repeteur sur la meme frequence [WO2003044970A2  ( fr ) ](https://www.google.com/patent/WO2003044970A2/fr)2001-11-20   2003-05-30   Qualcomm Incorporated   Repeteur commande par puissance de liaison retour [US6990313B1  ( en ) ](https://www.google.com/patent/US6990313B1/en)2002-03-14   2006-01-24   Sprint Communications Company L.P.   Wireless repeater with intelligent signal display [EP1525678B1  ( fr ) ](https://www.google.com/patent/EP1525678B1/fr)2002-06-21   2008-07-30   QUALCOMM Incorporated   Repeteur de reseau local sans fil [US6697016B1  ( en ) ](https://www.google.com/patent/US6697016B1/en)2002-09-30   2004-02-24   Motorola, Inc.   Self adjustment of a frequency offset in a GPS receiver [US7526247B2  ( en ) ](https://www.google.com/patent/US7526247B2/en)2002-12-05   2009-04-28   Qualcomm Incorporated   System and method for setting the reverse link gain of repeaters in wireless communications systems [US20040146013A1  ( en ) ](https://www.google.com/patent/US20040146013A1/en)2003-01-22   2004-07-29   Hong Kong Applied Science And Technology Research Institute Co., Ltd   Wireless local area network time division duplex relay system with high speed automatic up-link and down-link detection [CA2516769A1  ( fr ) ](https://www.google.com/patent/CA2516769A1/fr)2003-02-24   2004-09-10   Qualcomm Incorporated   Prevention des oscillations de repeteur [US20040166802A1  ( en ) ](https://www.google.com/patent/US20040166802A1/en)2003-02-26   2004-08-26   Ems Technologies, Inc.   Cellular signal enhancer [US7555261B2  ( en ) ](https://www.google.com/patent/US7555261B2/en)2003-03-04   2009-06-30   O'neill Frank P   Repeater system for strong signal environments [KR20070100430A  ( ko ) ](https://www.google.com/patent/KR20070100430A/ko)2003-06-30   2007-10-11   데코링크 와이어리스 엘티디.   중계기의 알에프 출력 레벨 자동 제어 방법 [US7593689B2  ( en ) ](https://www.google.com/patent/US7593689B2/en)2003-09-16   2009-09-22   Spotwave Wireless Inc.   Method for detecting an oscillation in an on-frequency repeater [CA2459428A1  ( fr ) ](https://www.google.com/patent/CA2459428A1/fr)2004-03-03   2005-09-03   Spotwave Wireless Inc.   Reconnaissance de signal dans un repeteur accorde [US7221967B2  ( en ) ](https://www.google.com/patent/US7221967B2/en)2004-09-14   2007-05-22   Wilson Electronics, Inc.   Enhanced gain selected cell phone booster system [JP2006115149A  ( ja ) ](https://www.google.com/patent/JP2006115149A/ja)2004-10-14   2006-04-27   Pioneer Electronic Corp   デジタル受信機及びデジタル放送受信方法 [KR100997063B1  ( ko ) ](https://www.google.com/patent/KR100997063B1/ko)2006-01-27   2010-11-29   퀄컴 인코포레이티드   중계기 개방 루프 게인 측정 [JP5199261B2  ( ja ) ](https://www.google.com/patent/JP5199261B2/ja)*   2006-09-21   2013-05-15   クゥアルコム・インコーポレイテッド   リピータの間の振動を緩和するための方法および装置 [US20080081555A1  ( en ) ](https://www.google.com/patent/US20080081555A1/en)2006-10-03   2008-04-03   Wireless Data Communication Co., Ltd   Unified communication repeater [US20080096483A1  ( en ) ](https://www.google.com/patent/US20080096483A1/en)2006-10-20   2008-04-24   Wilson Electronics   Power saving circuits for time division multiple access amplifiers [US7877066B2  ( en ) ](https://www.google.com/patent/US7877066B2/en)2007-05-07   2011-01-25   Paratek Microwave Inc   Techniques to reduce the power consumption of an RF log-amp detector [JP5259174B2  ( ja ) ](https://www.google.com/patent/JP5259174B2/ja)2007-12-25   2013-08-07   オリンパスメディカルシステムズ株式会社   送受信システム [KR101496896B1  ( ko ) ](https://www.google.com/patent/KR101496896B1/ko)*   2009-02-16   2015-02-27   삼성전자주식회사   대역 확장성을 지원하는 셀룰러 무선통신시스템에서 보호대역이 구성된 하향링크 신호의 송수신 방법 및 장치 [KR101298590B1  ( ko ) ](https://www.google.com/patent/KR101298590B1/ko)2009-12-21   2013-08-26   한국전자통신연구원   무선 통신 시스템에서 중계 장치 및 방법 [CN202026322U  ( zh ) ](https://www.google.com/patent/CN202026322U/zh)*   2011-04-29   2011-11-02   广东九联科技股份有限公司   一种宽带窄带合一的有线电视双向网络 [CN103209492B  ( zh ) ](https://www.google.com/patent/CN103209492B/zh)*   2011-09-15   2019-02-12   华为技术有限公司   一种无线资源管理方法和通信设备 [CN202975327U  ( zh ) ](https://www.google.com/patent/CN202975327U/zh)*   2012-12-18   2013-06-05   深圳市鼎耀科技有限公司   一种多频卫星信号转发设备 [WO2015002670A1  ( fr ) ](https://www.google.com/patent/WO2015002670A1/fr)*   2013-07-03   2015-01-08   Wireless Extenders, Inc.   Booster multi-amplificateur pour un système de communication sans fil [GB201410025D0  ( en ) ](https://www.google.com/patent/GB201410025D0/en)*   2014-06-05   2014-07-16   Ocado Ltd   Systems and methods for communication [KR101825417B1  ( ko ) ](https://www.google.com/patent/KR101825417B1/ko)*   2014-12-30   2018-02-06   주식회사 쏠리드   간섭제거 중계기 [CN104954062A  ( zh ) ](https://www.google.com/patent/CN104954062A/zh)*   2015-05-29   2015-09-30   西北工业大学   一种基于fpga的小卫星载ais信号采集系统 

2017  

2017-04-05   US   US15/479,557  [patent/US10356732B2/en](https://www.google.com/patent/US10356732B2/en)active   Active  

2017-04-05   CN   CN201780022064.3A  [patent/CN109328440A/zh](https://www.google.com/patent/CN109328440A/zh)active   Pending  

2017-04-05   WO   PCT/US2017/026069  [patent/WO2017176840A1/fr](https://www.google.com/patent/WO2017176840A1/fr)not_active   Ceased  

## Patent Citations (4)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [US20020045461A1  ( en ) ](https://www.google.com/patent/US20020045461A1/en)*   2000-10-18   2002-04-18   David Bongfeldt   Adaptive coverage area control in an on-frequency repeater [US20040156097A1  ( en ) ](https://www.google.com/patent/US20040156097A1/en)*   2003-02-06   2004-08-12   Spotwave Wireless Inc.   Intelligent gain control in an on-frequency repeater [US20100075704A1  ( en ) ](https://www.google.com/patent/US20100075704A1/en)*   2008-08-19   2010-03-25   Shared Spectrum Company   Method and System for Dynamic Spectrum Access Using Specialty Detectors and Improved Networking [US20130203403A1  ( en ) ](https://www.google.com/patent/US20130203403A1/en)*   2011-08-23   2013-08-08   Wilson Electronics, Inc.   Verifying and mitigating oscillation in amplifiers 

## Non-Patent Citations (1)

* Cited by examiner, † Cited by third party   Title   "[American National Standard for Compliance Testing of Transmitters Used in Licensed Radio Services](http://scholar.google.com/scholar?q="American+National+Standard+for+Compliance+Testing+of+Transmitters+Used+in+Licensed+Radio+Services")", C63.26-2015- IEEE /ANSI STANDARD FOR COMPLIANCE TESTING OF TRANSMITTERS USED I N LICENSED RADIO SERVICES, 15 January 2016 (2016-01-15), XP055431094, ISBN: 978-1-5044-0073-2, Retrieved from the Internet <URL:http://ieeexplore.ieee.org/document/7396001>   *  

## Cited By (2)

* Cited by examiner, † Cited by third party   Publication number   Priority date   Publication date   Assignee   Title  [US20210336652A1  ( en ) ](https://www.google.com/patent/US20210336652A1/en)*   2017-10-16   2021-10-28   Cellphone-Mate, Inc.   Signal boosters with compensation for cable loss [US11683067B2  ( en ) ](https://www.google.com/patent/US11683067B2/en)*   2017-10-16   2023-06-20   Cellphone-Mate, Inc.   Signal boosters with compensation for cable loss 

## Also Published As

Publication number   Publication date  [US10356732B2  ( en ) ](https://www.google.com/patent/US10356732B2/en)2019-07-16  [US20170288766A1  ( en ) ](https://www.google.com/patent/US20170288766A1/en)2017-10-05  [CN109328440A  ( zh ) ](https://www.google.com/patent/CN109328440A/zh)2019-02-12  

## Similar Documents

Publication   Publication Date   Title  [US10356732B2  ( en ) ](https://www.google.com/patent/US10356732B2/en)2019-07-16   Narrowband signal detection for network protection [US12063094B2  ( en ) ](https://www.google.com/patent/US12063094B2/en)2024-08-13   Desktop signal booster [US10148341B2  ( en ) ](https://www.google.com/patent/US10148341B2/en)2018-12-04   Independent band detection for network protection [US10873387B2  ( en ) ](https://www.google.com/patent/US10873387B2/en)2020-12-22   Signal booster with spectrally adjacent bands [US11012143B2  ( en ) ](https://www.google.com/patent/US11012143B2/en)2021-05-18   Desktop signal booster [US10630371B2  ( en ) ](https://www.google.com/patent/US10630371B2/en)2020-04-21   Signal booster with spectrally adjacent bands [US10805026B2  ( en ) ](https://www.google.com/patent/US10805026B2/en)2020-10-13   Narrowband signal detection [US10659142B1  ( en ) ](https://www.google.com/patent/US10659142B1/en)2020-05-19   Independent band detection for network protection [US20180139626A1  ( en ) ](https://www.google.com/patent/US20180139626A1/en)2018-05-17   Signal booster for boosting signals in contiguous bands [CA3052454C  ( fr ) ](https://www.google.com/patent/CA3052454C/fr)2024-01-02   Amplificateur de signal a bandes spectralement adjacentes [WO2018187498A1  ( fr ) ](https://www.google.com/patent/WO2018187498A1/fr)2018-10-11   Amplificateur de signaux à trajets de signaux actifs et passifs [WO2018144639A1  ( fr ) ](https://www.google.com/patent/WO2018144639A1/fr)2018-08-09   Réduction des oscillations dans un amplificateur de signal [HK1261833A1  ( en ) ](https://www.google.com/patent/HK1261833A1/en)2020-01-03   Narrowband signal detection for network protection [EP3577794A1  ( fr ) ](https://www.google.com/patent/EP3577794A1/fr)2019-12-11   Détection spécifique à la bande dans un amplificateur de signal 

## Legal Events

Date   Code   Title   Description   2018-10-06   NENP   Non-entry into the national phase  

**Ref country code**:  DE  

2018-12-05   121   Ep: the epo has been informed by wipo that ep was designated in this application  

**Ref document number**:  17779714  

**Country of ref document**:  EP  

**Kind code of ref document**:  A1  

2019-05-01   122   Ep: pct application non-entry in european phase  

**Ref document number**:  17779714  

**Country of ref document**:  EP  

**Kind code of ref document**:  A1  