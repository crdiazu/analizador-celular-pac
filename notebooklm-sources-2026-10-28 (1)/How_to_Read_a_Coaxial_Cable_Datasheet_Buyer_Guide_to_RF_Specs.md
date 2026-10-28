# How to Read a Coaxial Cable Datasheet: Buyer Guide to RF Specs

How to Read a Coaxial Cable Datasheet: Buyer Guide to RF Specs

[WHP Wire Harness Production](https://wireharnessproduction.com/)

[Services](https://wireharnessproduction.com/custom-cable-assembly)

[Wire Harness & Cable Assembly](https://wireharnessproduction.com/custom-cable-assembly) [Custom Wire Harness Assembly](https://wireharnessproduction.com/custom-wire-harness-assembly) [Wire Harness vs Cable Assembly](https://wireharnessproduction.com/wire-harness-cable-assembly) [Molex Connector Assemblies](https://wireharnessproduction.com/custom-cable-assembly/molex) [Waterproof IP67 / IP68](https://wireharnessproduction.com/custom-cable-assembly/waterproof) [Battery & Power Cables](https://wireharnessproduction.com/custom-cable-assembly/battery-cable) [Overmolded Cables](https://wireharnessproduction.com/custom-cable-assembly/overmolded) [Rapid Prototyping](https://wireharnessproduction.com/custom-cable-assembly/prototype) [View all services](https://wireharnessproduction.com/custom-cable-assembly)

[Industries](https://wireharnessproduction.com/industries)

[Automotive & EV](https://wireharnessproduction.com/industries/automotive) [Medical Devices](https://wireharnessproduction.com/industries/medical) [Robotics & Automation](https://wireharnessproduction.com/industries/robotics) [EV Charging](https://wireharnessproduction.com/industries/ev-charging-harness) [Solar & Energy](https://wireharnessproduction.com/industries/solar) [View all industries](https://wireharnessproduction.com/industries)

[Capabilities](https://wireharnessproduction.com/capabilities)

[Manufacturing Capabilities](https://wireharnessproduction.com/capabilities) [Engineering & DFM](https://wireharnessproduction.com/capabilities#engineering) [Quality & Certifications](https://wireharnessproduction.com/capabilities#certifications) [Equipment & Testing](https://wireharnessproduction.com/capabilities#equipment)

[Company](https://wireharnessproduction.com/about)

[About Us](https://wireharnessproduction.com/about) [Our Facilities](https://wireharnessproduction.com/factories) [Case Studies](https://wireharnessproduction.com/case-studies) [FAQ](https://wireharnessproduction.com/faq)

[Resources](https://wireharnessproduction.com/resources)

[Blog & Guides](https://wireharnessproduction.com/blog) [Engineering Tools](https://wireharnessproduction.com/tools) [Comparisons](https://wireharnessproduction.com/comparisons/wire-harness-vs-cable-assembly) [Technical Resources](https://wireharnessproduction.com/resources)

[Contact](https://wireharnessproduction.com/contact)

[English](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet)

[English](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet) [Español (México)](https://wireharnessproduction.com/mx)

[Start Program Review](https://wireharnessproduction.com/#program-review)

[Home](https://wireharnessproduction.com/)/ [Blog](https://wireharnessproduction.com/blog)/ How to Read a Coaxial Cable Datasheet: Buyer Guide to RF Specs

Technical Guide

# How to Read a Coaxial Cable Datasheet: Buyer Guide to RF Specs

Learn how OEM buyers read a coaxial cable datasheet correctly, including impedance, attenuation, velocity factor, shielding, bend radius, and RFQ details.

By [Hommer Zhao](https://wireharnessproduction.com/author/hommer-zhao) April 25, 2026 19 min read Copy link

Table of Contents

[1. Why a Coax Datasheet Changes Cost and Risk](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#why-datasheets-matter)

[2. The Core Datasheet Fields Buyers Must Read First](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#core-fields)

[3. How to Read Loss, Frequency, and Velocity Factor Together](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#loss-and-frequency)

[4. The Mechanical Lines That Break Assemblies in Production](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#mechanical-fields)

[5. Fast Comparison Table for Common Datasheet Lines](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#comparison-table)

[6. Choosing Low-Loss Coax by Run Length and Frequency](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#run-length-frequency)

[7. What to Send with an RFQ or Drawing Package](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#rfq-checklist)

[Frequently Asked Questions](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#faq)

[↑ Back to top](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet#top)

Consider a hypothetical sourcing team that approves a coax cable because the OD fits the enclosure and the price looks good. During qualification, the RF path fails its insertion-loss budget, the bend at the bulkhead is too tight for the dielectric, and the connector originally quoted does not match the actual braid and center-conductor construction. That is how a simple cable line item turns into scrap, resampling, and program delay. Reading a coaxial cable datasheet correctly is not an engineering formality. It is a purchasing control step for signal integrity, manufacturability, and field reliability.

2

common impedance options: 50 ohm and 75 ohm. [Times Microwave](https://timesmicrowave.com/wp-content/uploads/2024/04/lmr-complete-guide.pdf)

3 dB

of loss leaves roughly half the signal power. [Anritsu](https://dl.cdn-anritsu.com/en-us/test-measurement/ohs/10450-00028P/User_Guide/3-Adv-Cable_Antenna.04.02.html)

*Custom coaxial cable assemblies depend on more than connector type. The cable datasheet determines impedance, loss, shielding behavior, bend limits, and which termination process is actually manufacturable.*

This guide is for OEM buyers, procurement managers, NPI teams, and engineers who need to evaluate coaxial cable part numbers before they release samples or POs. It explains what each important datasheet line means, which values materially affect the commercial decision, and how to turn a cable datasheet into a manufacturable RFQ. If you also need broader assembly context, our [coaxial cable assembly guide](https://wireharnessproduction.com/blog/coaxial-cable-assembly-guide) covers the system-level custom-versus-standard choice, and our [BNC connector guide](https://wireharnessproduction.com/blog/bnc-connector-types-guide) shows how connector family and impedance must stay aligned with the selected cable.

## 1. Why a Coax Datasheet Changes Cost and Risk

A coax datasheet is where the supplier tells you what the cable really is, not what the sales description implies. Two cables can both be advertised as "50 ohm low-loss coax" and still behave very differently once you compare attenuation at your operating band, center-conductor material, dielectric type, braid coverage, jacket compound, and minimum bend radius. For sourcing, those differences control three expensive outcomes: whether the assembly passes electrical test, whether the connector family can be terminated repeatably, and whether the cable survives installation and service.

That is why experienced buyers do not evaluate coax by impedance alone. Controlled impedance matters, but so do attenuation curves, shield construction, conductor type, and mechanical stack-up. The difference is well explained by the basics of [coaxial cable construction](https://en.wikipedia.org/wiki/Coaxial_cable) and [characteristic impedance](https://en.wikipedia.org/wiki/Characteristic_impedance): the geometry is what creates the RF behavior, and small construction changes show up later as mismatch, loss, or assembly difficulty.

For B2B programs, the datasheet also sets commercial expectations. A cable with lower attenuation may cost more per meter but reduce amplifier load, avoid redesign, or preserve margin in a long run. A tougher jacket may raise unit cost slightly but prevent field failures in [robotics](https://wireharnessproduction.com/industries/robotics), telecom, or outdoor routing. A datasheet is therefore not only a technical document. It is a cost-and-risk document that should be read before the RFQ goes out, not after first article fails.

## 2. The Core Datasheet Fields Buyers Must Read First

If time is limited, read these lines first: impedance, capacitance, attenuation, velocity factor, maximum frequency, shield construction, outer diameter, and minimum bend radius. Those eight items usually tell you whether the cable belongs in the short list.

**Impedance** is usually the first gate. Most RF communications, instrumentation, antennas, and wireless systems are 50 ohm. Most broadcast, CCTV, and video distribution systems are 75 ohm. If the equipment side, connector family, and test expectation are built around one impedance family, a mismatch is a sourcing error even if the cable "physically fits."

**Capacitance** is often ignored by non-specialists, but it matters when the circuit is sensitive to loading, timing, or high-frequency roll-off. Lower capacitance per meter is usually favorable in longer runs and higher-frequency work, but it must be read together with impedance and dielectric design. Do not compare capacitance in isolation.

**Shield construction** tells you more than whether the cable is "shielded." A single braid, foil plus braid, or dual-braid structure changes coverage, flex behavior, weight, and termination difficulty. For EMI-sensitive programs, buyers should cross-check the datasheet against our [EMI shielding guide](https://wireharnessproduction.com/blog/emi-shielding-wire-harness-guide) and confirm whether the assembly needs simple continuity, controlled transfer impedance, or stronger shielding effectiveness under motion.

**Outer diameter** and **center-conductor construction** are the lines that connect the cable datasheet to the connector datasheet. They determine strip dimensions, contact style, ferrule size, and whether the approved termination process can be repeated at scale. That is why a datasheet review should happen together with connector review, especially for [custom coaxial cable assemblies](https://wireharnessproduction.com/custom-cable-assembly/coaxial) and [micro-coaxial cable assemblies](https://wireharnessproduction.com/custom-cable-assembly/micro-coaxial-cable-assembly) where tolerances are tighter and termination windows are smaller.

## 3. How to Read Loss, Frequency, and Velocity Factor Together

Attenuation is the line item that most directly affects whether the cable can support your run length and frequency plan. Datasheets usually list attenuation as dB per 100 ft, dB per 100 m, or dB per km at several frequency points. Buyers should never read only one number out of context. Loss increases with frequency, so the relevant question is not "What is the attenuation?" but "What is the attenuation at my actual operating band and installed length?"

Here is the practical rule: convert the datasheet number to your real length, then compare it to the total allowable loss budget of the system. If the cable alone consumes most of the budget, the program will have little tolerance left for connectors, adapters, aging, or field variation. That is how an apparently acceptable sample becomes a marginal production release. If your team needs a broader supplier-evaluation lens, our [RF cable assembly manufacturer guide](https://wireharnessproduction.com/blog/rf-cable-assembly-manufacturers) outlines the RF test questions that should sit next to the cable review.

**Velocity factor** is another line that buyers often skim past. It expresses how fast the signal propagates through the cable relative to the speed of light. In many standard industrial RF jobs it mainly affects delay calculations. In phase-sensitive, timing-sensitive, or matched-length assemblies, it becomes critical because electrical length matters as much as physical length. If the system includes array timing, delay matching, or calibrated RF paths, make sure the datasheet value and tolerance are explicitly linked to the drawing and test plan.

**Maximum frequency** should also be read carefully. It is not a promise that all performance parameters remain ideal all the way to that number. It is usually a boundary for intended operation, and the acceptance criteria still depend on VSWR, insertion loss, shielding, and application margin. The underlying logic is the same one described in [voltage standing wave ratio](https://en.wikipedia.org/wiki/Voltage_standing_wave_ratio) behavior: a cable can be electrically usable at a given band and still be commercially poor if the assembly margin is too thin.

## 4. The Mechanical Lines That Break Assemblies in Production

Electrical buyers sometimes focus so hard on impedance and loss that they miss the mechanical fields that decide whether the cable can be installed, routed, and terminated without damage. The most important of these are minimum bend radius, jacket material, operating temperature, conductor type, and weight or stiffness.

**Minimum bend radius** must be read as an installation rule, not a suggestion. If the cable is routed tighter than the datasheet allows, the center conductor can migrate, the dielectric can deform, the shield can wrinkle, and the impedance profile can change. Even if the cable still passes continuity, the RF path may not behave the same way. Static routing and repeated movement can require different bend limits; use the actual cable datasheet rather than a generic diameter multiplier. Where movement or repeated service loops exist, align the routing review with our [strain-relief guide](https://wireharnessproduction.com/blog/wire-harness-strain-relief-guide) before approving the release package.

**Jacket material** matters because coaxial cable is not used only indoors in clean racks. PVC, PE, FEP, PTFE, and LSZH-style constructions bring different tradeoffs in flexibility, temperature range, smoke behavior, chemical resistance, and surface durability. A cable that works electrically may still be the wrong commercial choice if it hardens in the field, cracks during maintenance, or fails the environmental exposure profile of the product.

**Conductor type** also changes the buying decision. Solid conductors may hold geometry differently than stranded versions, while copper-clad steel differs from bare copper in both electrical and mechanical behavior. If the assembly will flex repeatedly, route near hinges, or live in portable equipment, the conductor line cannot be treated as a footnote. It affects both product life and connector-process stability.

## 5. Fast Comparison Table for Common Datasheet Lines

Table

Swipe to see the full table →

|   |   |   |   |   |

| --- | --- | --- | --- | --- |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

The table above is the practical shortlist most buyers should work through before approving a coax cable part number. It is especially useful during alternate approval, cost-down review, and design-transfer work when the temptation is to compare only headline price, OD, and impedance.

## 6. Choosing Low-Loss Coax by Run Length and Frequency

Reading the attenuation line is one skill; turning it into a cable choice is another. The practical selection rule is simple: **total cable loss = the datasheet's dB-per-100-ft value, scaled to your real length, checked at your real operating frequency, against your loss budget**. Because attenuation rises with frequency and length, the same cable can be a fine jumper and a bad backbone. Deciding by run length and frequency — not by habit or headline price — is what keeps a marginal cable out of a production release.

The table below identifies cable families to compare. RG family labels do not establish a universal attenuation value; obtain the selected part's loss data at the required frequency. The LMR-400 entry is tied to the manufacturer reference.

Attenuation Review by Coax Family (dB per 100 ft)

Swipe to see the full table →

|   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

LMR-400's nominal 900 MHz attenuation is from the Times Microwave LMR guide at +25°C. Check the exact cable variant and current datasheet before release.

**Worked example.** For an assumed 50 ft run at 900 MHz with a 5 dB cable-loss budget, the LMR-400 guide value of 3.9 dB/100 ft gives 1.95 dB of cable loss, leaving 3.05 dB for other losses and margin. This is an illustrative calculation, not a measured assembly result. Source: [Times Microwave LMR guide](https://timesmicrowave.com/wp-content/uploads/2024/04/lmr-complete-guide.pdf).

Use these rules of thumb, then confirm with the real numbers:

**Short jumpers (a few feet), any band:** a thin general-purpose cable may suit the application, but loss, flexibility, outer diameter, and connector fit still need checking.

**Mid-length runs or higher bands:** step up to a lower-loss family — RG-6 for 75 Ω, LMR-240/LMR-400 for 50 Ω — before the cable eats the whole budget.

**Long runs at GHz frequencies:** evaluate a lower-loss coax construction; otherwise move the active electronics closer, shorten the path, or accept a higher grade of cable.

**Always leave margin.** Each connector pair and adapter adds loss, and cables age. If the cable alone consumes most of the budget, the assembly has no tolerance left, which is how a passing first article becomes a marginal production part.

This selection step sits directly on top of Section 3: read the attenuation line correctly, then scale it to length and check it at frequency. For the broader supplier-side test questions that go with a low-loss RF build, see our [RF cable assembly manufacturer guide](https://wireharnessproduction.com/blog/rf-cable-assembly-manufacturers).

## 7. What to Send with an RFQ or Drawing Package

A strong RFQ prevents the classic "quoted the right connector on the wrong cable" cycle. When requesting a custom coax assembly, send the exact cable part number or the full cable construction target, connector family on each end, operating frequency range, target assembly length, routing constraints, environment, quantity split, target lead time, and compliance target. If the cable will route through a bulkhead, hinge, or high-vibration area, include that mechanical context up front.

Buyers should also ask what they will receive back beyond unit price. A strong supplier response should include cable-to-connector compatibility review, any strip-dimension or ferrule risks, expected electrical test scope, and a clear note on whether the requested routing violates the cable bend rule. For new-product introduction, that feedback is often more valuable than the first quoted price because it prevents the wrong sample set from ever being built.

Checklist

Send This with the RFQ

Drawing, BOM, or cable datasheet with the exact part number

Connector type on each end and whether the interface is 50 ohm or 75 ohm

Operating frequency range, target insertion-loss limit, or other RF acceptance criteria

Assembly length, routing path, bend constraint, and whether the cable is static or dynamic

Environment: temperature range, outdoor exposure, vibration, chemicals, or washdown if applicable

Quantity split for prototype, pilot, and production, plus the target lead time

Compliance target such as RoHS, REACH, UL style expectation, or customer-specific approval scope

### Cta

**Title:** Need a Coaxial Cable Assembly Quote Based on the Real Datasheet, Not Guesswork?

Send the drawing, BOM, quantity, environment, target lead time, compliance target, and the exact cable or connector datasheets you want used through our [contact page](https://wireharnessproduction.com/contact). We will review impedance fit, attenuation risk, bend-radius constraints, and connector compatibility, then return a manufacturable quote with test-scope recommendations and any missing-spec flags before release.

**Primarybutton:** Request a Quote

**Secondarybutton:** Contact Engineering

Badges

Coax cable-to-connector compatibility review

Routing and bend-radius risk check before sampling

Prototype and production test planning support

**Rfqtitle:** Send This Next

Rfqitems

Drawing, BOM, and the target cable or approved alternate datasheet

Quantity by prototype, pilot, and production stage

Application environment, routing limits, and operating frequency band

Target lead time and compliance target

Any specific acceptance criteria for VSWR, insertion loss, shielding, or continuity

**Deliverablestitle:** What You Get Back

Deliverablesitems

Manufacturability review of cable, connector, and routing assumptions

Quoted cost and lead time with any datasheet mismatch called out

Recommended electrical and workmanship test scope for the program stage

Clear list of missing inputs blocking a production-ready release

## Frequently Asked Questions

### How do I choose low-loss coax for a long run?

Scale the selected cable's datasheet attenuation to the installed length and compare it with the system loss budget at the operating frequency. Leave margin for connectors, adapters, and expected variation; do not choose from the cable family name alone.

### How much attenuation does a coax cable have per 100 ft?

Attenuation depends on the specific cable construction and frequency. As a manufacturer-specific reference, standard LMR-400 is listed at 3.9 dB/100 ft at 900 MHz and +25°C in the [Times Microwave LMR guide](https://timesmicrowave.com/wp-content/uploads/2024/04/lmr-complete-guide.pdf). Confirm the chosen part's data before release.

### What is the most important number on a coaxial cable datasheet?

There is no single universal number, but for most B2B buyers the first three checks are impedance, attenuation at the real operating frequency, and minimum bend radius. Those three values usually determine whether the cable fits the interface, meets the loss budget, and can survive the mechanical routing in production.

### Can two 50 ohm coax cables still behave very differently in the same assembly?

Yes. Two 50 ohm cables can differ in attenuation, velocity factor, shield construction, dielectric material, outer diameter, and conductor type. That is why a same-impedance substitute can still break connector compatibility, change loss by several dB over the installed length, or force a different bend rule.

### How should buyers read attenuation correctly?

Read the loss at the actual operating frequency, convert it to the installed cable length, and compare it to the total path budget. If the datasheet gives dB per 100 ft and your run is 20 ft, use one fifth of the listed value. Then add connector and adapter losses before judging whether the margin is acceptable.

### Why does bend radius matter if the cable still passes continuity?

Because continuity does not prove that the coax geometry stayed intact. Bending tighter than the specified minimum radius can deform the dielectric, disturb shield shape, and change the impedance profile. The cable may still conduct electricity but perform worse in return loss, insertion loss, or long-term reliability.

### What should I send a supplier for a custom RF cable quote?

Send the drawing, BOM, target quantity, application environment, target lead time, compliance target, and the exact cable and connector datasheets if you already selected them. A capable supplier should return a manufacturability review, quote assumptions, and a recommended test scope rather than price alone.

### When should velocity factor become a commercial concern?

Velocity factor becomes commercially important when the assembly is phase-sensitive, delay-sensitive, or length-matched. In those programs, a cable choice can change timing behavior even when the physical length and impedance remain the same, so the datasheet value needs to be tied directly to the drawing and acceptance plan.

### Have a harness or cable-assembly program?

Send a drawing, BOM or photos — our engineers return a free DFM review, MOQ and lead time within 24 hours on business days.

[Send Drawing / BOM for DFM Review](https://wireharnessproduction.com/#program-review)

## Related Resources

[Technical Guide

### Coaxial Cable Bend Radius and Routing Guidelines

](https://wireharnessproduction.com/blog/coaxial-cable-bend-radius-routing-guidelines)

June 16, 2026

A practical OEM guide to coaxial cable bend radius, no-bend zones, clamp spacing, routing drawings, RF test evidence, and supplier release checks.

[Read article](https://wireharnessproduction.com/blog/coaxial-cable-bend-radius-routing-guidelines)

[Technical Guide

### Coaxial Cable Impedance: 50 Ohm vs 75 Ohm Explained

](https://wireharnessproduction.com/blog/coaxial-cable-impedance-50-ohm-vs-75-ohm)

May 26, 2026

A practical buyer guide to 50 ohm vs 75 ohm coaxial cable impedance, connector matching, RF loss, video use cases, and factory test evidence.

[Read article](https://wireharnessproduction.com/blog/coaxial-cable-impedance-50-ohm-vs-75-ohm)

[Technical Guide

### Coaxial Cable Wiring Diagram Guide for OEM Cable Assemblies

](https://wireharnessproduction.com/blog/coaxial-cable-wiring-diagram-guide)

May 19, 2026

Learn how to read and specify a coaxial cable wiring diagram for RF, video, sensor, and instrumentation cable assemblies without losing impedance, shield.

[Read article](https://wireharnessproduction.com/blog/coaxial-cable-wiring-diagram-guide)

WHP Wire Harness

Production

Engineered interconnect systems for complex OEM manufacturing programs across China and the Philippines.   

Capabilities

[DFM & Engineering Review](https://wireharnessproduction.com/capabilities) [Manufacturing](https://wireharnessproduction.com/capabilities) [Quality & Testing](https://wireharnessproduction.com/capabilities) [Cable Assembly](https://wireharnessproduction.com/custom-cable-assembly)

Industries

[Automotive & EV](https://wireharnessproduction.com/industries/automotive) [Medical](https://wireharnessproduction.com/industries/medical) [Industrial Automation](https://wireharnessproduction.com/industries/industrial-automation) [Robotics](https://wireharnessproduction.com/industries/robotics)

Company

[About](https://wireharnessproduction.com/about) [Facilities](https://wireharnessproduction.com/factories) [Blog](https://wireharnessproduction.com/blog) [Contact](https://wireharnessproduction.com/contact)

© 2026 WellPCB Tech Co., Ltd. All rights reserved. [Privacy](https://wireharnessproduction.com/privacy)

· [Terms](https://wireharnessproduction.com/terms)

· [Español (México)](https://wireharnessproduction.com/mx)

· Cookie Settings

· ISO 9001 · IATF 16949

We use cookies for analytics and advertising measurement (Google Analytics and Google Ads). Essential cookies are always on. You can accept or reject the optional ones — see our [Privacy Policy](https://wireharnessproduction.com/privacy).

Reject Accept