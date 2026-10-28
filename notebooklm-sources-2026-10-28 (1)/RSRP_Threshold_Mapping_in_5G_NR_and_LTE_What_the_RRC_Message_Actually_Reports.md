# RSRP Threshold Mapping in 5G NR and LTE: What the RRC Message Actually Reports

RSRP Threshold Mapping in 5G NR and LTE: What the RRC Message Actually Reports - 5G NR - telecomHall Forum

[telecomHall Forum](https://www.telecomhall.net/)

# [RSRP Threshold Mapping in 5G NR and LTE: What the RRC Message Actually Reports](https://www.telecomhall.net/t/rsrp-threshold-mapping-in-5g-nr-and-lte-what-the-rrc-message-actually-reports/36657)

[5G NR](https://www.telecomhall.net/c/5g-nr/51)

[5g-nr](https://www.telecomhall.net/tag/5g-nr), [4g-lte](https://www.telecomhall.net/tag/4g-lte), [protocol-testing](https://www.telecomhall.net/tag/protocol-testing), [performance-kpi](https://www.telecomhall.net/tag/performance-kpi)

[hicelltek](https://www.telecomhall.net/u/hicelltek) May 28, 2026, 1:04pm 1

## The Mapping Problem

When you decode an RRC Measurement Report, RSRP values are not transmitted in dBm. The UE sends an integer range index, and the network (and your analysis tool) must convert it back to an actual power level.

The catch: **LTE and 5G NR use different mapping formulas.** If you apply the wrong offset, your handover analysis is off by 16 dB.

## The 3GPP Conversion Formulas

**LTE (TS 36.133, Section 9.1.4)**

**5G NR (TS 38.133, Section 10.1.6.1)**

The 16 dB offset difference between the two formulas comes from NR's extended measurement range, designed to handle mmWave propagation where signal levels drop well below LTE's minimum reporting threshold.

## Why This Matters for Handover Analysis

When a Measurement Report carries `threshold-RSRP = 30` , the actual trigger level depends on the RAT:

**LTE**: 30 - 141 = **-111 dBm**

**NR**: 30 - 157 = **-127 dBm**

If your post-processing tool applies the LTE formula to NR data (or vice versa), every threshold comparison in your handover analysis will be shifted by 16 dB. That is enough to completely misinterpret cell reselection behavior.

## Quick Field Example

You capture a MeasurementReport with these values:

|   |   |   |   |

| --- | --- | --- | --- |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

If you mix up the formulas, you might conclude a cell has adequate coverage when it is actually 16 dB below your threshold.

## Full Mapping Tables

For complete RSRP/RSRQ/SINR threshold mapping tables with both LTE and NR formulas verified against 3GPP specifications: 

[3GPP RSRP Threshold Mapping Reference](https://hicelltek.com/en/5g-nr-thresholds/) (interactive, all ranges)

For more RF diagnostic tools (ARFCN calculator, EARFCN lookup, NCI decoder): 

[HiCellTek Telecom Tools](https://hicelltek.com/en/outils/)

*Takwa Sebai | HiCellTek | Pro 4G/5G diagnostics on Android*

3 Likes

[Home](https://www.telecomhall.net/)

[Categories](https://www.telecomhall.net/categories)

[Guidelines](https://www.telecomhall.net/guidelines)

[Terms of Service](https://www.telecomhall.net/tos)

[Privacy Policy](https://www.telecomhall.net/privacy)

Powered by [Discourse](https://www.discourse.org/), best viewed with JavaScript enabled