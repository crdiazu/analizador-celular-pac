# Coax Loss Calculator - Cable Attenuation & Power - Turn2engineering

Coax Loss Calculator - Cable Attenuation & Power 

We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies.

Customize Reject All Accept All

Customize Consent Preferences 

We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.

The cookies that are categorized as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site.... Show more

Necessary Always Active

Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.

Cookie cookieyes-*

Duration 1 year

Description CookieYes sets this cookie for consent solution management.

Functional

Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.

No cookies to display.

Analytics [-]

Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.

Cookie *ga**

Duration 1 year 1 month 4 days

Description Google Analytics sets this cookie to store and count page views.

Cookie _ga

Duration 1 year 1 month 4 days

Description Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors.

Performance

Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.

No cookies to display.

Advertisement

Advertisement cookies are used to provide visitors with customized advertisements based on the pages you visited previously and to analyze the effectiveness of the ad campaigns.

No cookies to display.

Reject All Save My Preferences Accept All

Powered by 

[Skip to content](https://turn2engineering.com/calculators/coax-loss-calculator#content)  

[Turn2Engineering](https://turn2engineering.com/)

[Civil](https://turn2engineering.com/civil-engineering)

[Mechanical](https://turn2engineering.com/mechanical-engineering)

[Electrical](https://turn2engineering.com/electrical-engineering)  

[Home](https://turn2engineering.com/)

[Calculators](https://turn2engineering.com/calculators)

[Charts & Tables](https://turn2engineering.com/charts-and-tables)

[Equations](https://turn2engineering.com/equations)

[Civil Engineering](https://turn2engineering.com/civil-engineering)

[Mechanical Engineering](https://turn2engineering.com/mechanical-engineering)

[Electrical Engineering](https://turn2engineering.com/electrical-engineering)

[About](https://turn2engineering.com/about)

[Home](https://turn2engineering.com/)

[Calculators](https://turn2engineering.com/calculators/)

Coax Loss Calculator

# Coax Loss Calculator

Calculate coaxial cable attenuation, total feedline loss, power delivered, and efficiency from cable type, frequency, and run length.

Example values loaded Replace the example values before using the result for a real RF system.

Calculator is for informational purposes only. [Terms and Conditions](https://turn2engineering.com/terms-and-conditions)

Matched-line coax attenuation and power transfer

𝐿 t o t a l = 𝛼  ( 𝑓 )  ℓ 1 0 0 f t + 𝐿 a d d , 𝑃 o u t = 𝑃 i n  1 0 − 𝐿 t o t a l / 1 0

Preset cable attenuation is based on verified manufacturer equations or published attenuation tables and assumes a matched line under the stated source conditions.

1

## Enter the coax run

Choose the actual cable family, then enter the operating frequency and one-way physical cable length.

Power is optional for attenuation-only work. Use Custom Published Loss when you have an exact datasheet attenuation value for a cable not listed.

### Check the highlighted fields

Coax Cable *

Select a manufacturer-backed preset or enter your own published attenuation.

LMR-195

LMR-240

LMR-400

LMR-600

8240 / RG-58/U class — 52 Ω

MRG2132 / RG-213 — 50 Ω

1694A / RG-6/U — 75 Ω

Custom Published Loss

Operating Frequency *

Use the actual RF, IF, or highest frequency that must pass through the coax. 146

Hz

kHz

MHz

GHz

Attenuation rises with frequency. Preset cables are limited to the frequency range supported by the verified manufacturer equation or published table.

Cable Length *

Enter the one-way physical run, including jumpers, service loops, and routing slack. 100

ft

m

Loss in decibels scales directly with cable length for a uniform transmission line operated within its published range.

Input Power

Optional. Enter source power to calculate watts or milliwatts delivered to the load. 100

mW

W

kW

dBm

dBW

Power does not change the calculated attenuation. It is used only to convert dB loss into delivered and lost power.

Published Attenuation *

Enter the datasheet loss at the same operating frequency entered above.

dB/100 ft

dB/100 m

dB/ft

dB/m

Use the manufacturer's matched-line attenuation for your exact cable at the operating frequency. The calculator scales that published loss linearly with length.

Advanced Options

Additional Passive Loss

Optional combined insertion loss for connectors, adapters, lightning protectors, filters, switches, or other passive components. 0

dB

Enter only passive losses not already included in the cable attenuation. Use published insertion-loss data when available; amplifier gain belongs in a link-budget calculation.

System Impedance

Used only to flag nominal 50 Ω / 75 Ω cable mismatch; it does not add a guessed mismatch loss.

50 Ω RF system

75 Ω RF/video system

Displayed Precision

3 significant figures

2 significant figures

4 significant figures

2

## Result

Total feedline loss is shown first, followed by cable attenuation, efficiency, and power delivery checks.

Total Feedline Loss

1.53

dB

Times Microwave LMR-400 • 100 ft • 146 MHz

70.3% of input power remains after the entered total path loss.

### Result details

Coax-only loss 1.53 dB

Attenuation at frequency 1.53 dB/100 ft

Metric attenuation 5.02 dB/100 m

Power delivered 70.3%

Power at load 70.3 W

Power not delivered 29.7%

Power not delivered 29.7 W

Cable impedance 50 Ω nominal

Show calculation steps Review the cable model, conversions, attenuation scaling, and power transfer

Enter valid values to see the complete calculation.

Copy Result Share Print Reset

3

## Power Through the Feedline

The bar view shows the percentage of input power delivered to the load versus not delivered because of the entered passive path loss.

Delivered to load 70.3%

Not delivered due to entered loss 29.7%

Input power basis **100%**

4

## Method, Sources, and Assumptions

The active cable preset determines whether the calculator uses a manufacturer attenuation equation, calculator interpolation between published table points, or your own datasheet value.

Manufacturer-backed matched-line attenuation

Manufacturer equation Matched line Length-scaled dB loss

Uses the manufacturer form α = k₁√f + k₂f with f in MHz and α in dB/100 ft. Typical attenuation, matched line, +25 °C ambient.

**References**

[Times Microwave Systems — LMR Complete Guide (LMR-400 Standard)](https://timesmicrowave.com/wp-content/uploads/2024/04/lmr-complete-guide.pdf) — Manufacturer technical data, verified 2026-09-15

Cable attenuation is treated as matched-line insertion loss and is proportional to physical cable length in decibels.

The cable preset does not include connector, adapter, surge-protector, filter, switch, water-ingress, aging, bend, or installation losses unless entered as Additional Passive Loss.

The impedance check is advisory only; mismatch loss is not guessed from nominal impedance alone because the actual source/load impedances, line length, and complex load are required.

Manufacturer attenuation values are nominal/typical data under stated reference conditions; verify the exact cable part number and current datasheet for final engineering work.

## Calculation Summary

Calculator

Coax Loss Calculator

Page URL

https://turn2engineering.com/calculators/coax-loss-calculator

Calculated On

10/27/2026, 9:12:32 PM

Result

1.53 dB

Cable

Times Microwave LMR-400

Frequency

146 MHz

Cable Length

100 ft

Coax-only Loss

1.53 dB

Total Feedline Loss

1.53 dB

Power Delivered

70.3%

Power Not Delivered

29.7%

Input Power

100 W

Power at Load

70.3 W

Key Assumptions

Cable attenuation is treated as matched-line insertion loss and is proportional to physical cable length in decibels.; The cable preset does not include connector, adapter, surge-protector, filter, switch, water-ingress, aging, bend, or installation losses unless entered as Additional Passive Loss.; The impedance check is advisory only; mismatch loss is not guessed from nominal impedance alone because the actual source/load impedances, line length, and complex load are required.; Manufacturer attenuation values are nominal/typical data under stated reference conditions; verify the exact cable part number and current datasheet for final engineering work.

### Subscribe to Turn2Engineering.com!

Get updates on the latest posts and more from Turn2Engineering.com straight to your inbox.

Subscribe

We use your personal data for interest-based advertising, as outlined in our [Privacy Notice](https://www.mediavine.com/legal-and-privacy-center/). 

[What is this?](https://www.journeymv.com?utm_source=journey|&utm_medium=ad&utm_campaign=logo)

Total Feedline Loss

1.53

dB

On this page

[How to Read a Coax Loss Result](https://turn2engineering.com/calculators/coax-loss-calculator#article-overview)

[How to Use the Coax Loss Calculator](https://turn2engineering.com/calculators/coax-loss-calculator#article-how-to-use)

[Coax Loss Formula and Calculation Method](https://turn2engineering.com/calculators/coax-loss-calculator#article-method)

[Worked Coax Loss Example](https://turn2engineering.com/calculators/coax-loss-calculator#article-worked-example)

[How to Interpret Coax Loss in dB](https://turn2engineering.com/calculators/coax-loss-calculator#article-interpret-results)

[Why Coax Loss Increases With Frequency](https://turn2engineering.com/calculators/coax-loss-calculator#article-frequency-loss)

[Why Real Coax Loss Can Be Higher](https://turn2engineering.com/calculators/coax-loss-calculator#article-real-world-factors)

[How to Choose Lower-Loss Coax](https://turn2engineering.com/calculators/coax-loss-calculator#article-design-selection)

[Coax Loss Reference Values](https://turn2engineering.com/calculators/coax-loss-calculator#article-reference-values)

[Assumptions and Limits](https://turn2engineering.com/calculators/coax-loss-calculator#article-assumptions)

[Related RF Calculators](https://turn2engineering.com/calculators/coax-loss-calculator#article-related)

[Data Sources and Verification](https://turn2engineering.com/calculators/coax-loss-calculator#article-sources)

[Coax Loss Calculator FAQs](https://turn2engineering.com/calculators/coax-loss-calculator#article-faq)

Calculator guide

## How to Read a Coax Loss Result

The coax loss calculator above estimates matched-line attenuation for a selected coax cable at the operating frequency and one-way cable length you enter. Its primary result is total feedline loss in decibels. If you also enter source power, the calculator converts that loss into the power expected at the load; Advanced Options can add known passive component loss without hiding it inside the cable value.

Coax loss is not a fixed number for a cable name. It depends on frequency and physical run length, and manufacturer data for the exact cable construction is the best basis when accuracy matters. The calculator therefore uses manufacturer equations or published attenuation tables for its presets and keeps mismatch effects outside the matched-line loss model.

Minimum inputs

Cable type, operating frequency, and one-way cable length

Primary output

Total feedline loss in dB

Key scope

Matched-line cable attenuation plus any passive loss you explicitly add

### Low attenuation does not prove the RF system is matched

The calculator can flag a nominal 50 Ω versus 75 Ω mismatch, but it does not invent a mismatch-loss value. Actual mismatch behavior depends on the source, load, line impedance, electrical length, operating frequency, and complex impedances in the installed system.

## How to Use the Coax Loss Calculator

Use the shortest path that matches the information you actually know: select a listed cable when the exact preset applies, or choose Custom Published Loss when you have a datasheet attenuation value for another coax.

1.

### Choose the coax cable

Select the manufacturer-backed preset that matches the installed cable. The listed choices include Times Microwave LMR-195, LMR-240, LMR-400, and LMR-600 plus selected Belden RG-58/U-class, RG-213, and RG-6 products. Do not substitute a similar-looking family name when the exact construction or part number is different. 2.

### Enter operating frequency and one-way cable length

Frequency may be entered in Hz, kHz, MHz, or GHz, while cable length may be entered in feet or meters. Use the actual routed cable length, including service loops and jumpers that are part of the run, rather than the straight-line distance between equipment. 3.

### Add input power only when you want delivered power

Input power is optional. The calculator accepts mW, W, kW, dBm, and dBW. Leaving power blank still gives the dB loss and percentage delivered because those values depend on attenuation, not on the absolute starting power. 4.

### Use Advanced Options for known passive loss and impedance checking

Enter the combined insertion loss of connectors, adapters, lightning protectors, filters, switches, or other passive components only when you have a defensible value. The System Impedance control is advisory: it warns about a nominal cable/system mismatch but does not add guessed mismatch loss. 5.

### Use Custom Published Loss at the same frequency as the datasheet value

In custom mode, enter the manufacturer attenuation in dB/100 ft, dB/100 m, dB/ft, or dB/m at the operating frequency. The calculator scales that published attenuation by physical cable length; it does not create a new frequency curve from a single data point.

## Coax Loss Formula and Calculation Method

The calculator first determines attenuation at the selected frequency, scales that attenuation to the entered run length, adds any known passive loss, and then converts total dB loss into a power ratio.

### Scale published attenuation to cable length

𝐿 c a b l e = 𝛼  ( 𝑓 )  ℓ 1 0 0 f t

Plain language: cable loss equals the attenuation rate at the operating frequency multiplied by the cable length expressed in hundreds of feet. The same relationship applies when the attenuation rate is stated per 100 meters or another supported length basis.

### Add passive path losses separately

𝐿 t o t a l = 𝐿 c a b l e + 𝐿 a d d

Plain language: known connector or accessory insertion losses are added in dB. Keeping them separate makes it clear how much loss belongs to the coax itself.

### Convert dB loss to power delivered

𝜂 = 1 0 − 𝐿 t o t a l / 1 0 , 𝑃 o u t = 𝑃 i n  𝜂

Plain language: every positive loss in dB reduces the remaining power by a logarithmic ratio. A 3 dB loss leaves about one-half of the starting power, while a 10 dB loss leaves one-tenth.

### Manufacturer equation used by the LMR presets

𝛼  ( 𝑓 ) = 𝐾 1  √ 𝑓 + 𝐾 2  𝑓

For the Times Microwave LMR presets, frequency is in MHz and the selected coefficient set returns attenuation in dB/100 ft. The calculator uses the coefficients published for the exact LMR family rather than applying one generic frequency multiplier to every coax.

The Belden presets use published attenuation-table points instead and interpolate only inside the verified table range.

𝐿 c a b l e

Coax-only loss Matched-line attenuation caused by the selected coax over the entered physical run. dB calculated value

𝛼  ( 𝑓 )

Attenuation at frequency Manufacturer-backed loss rate evaluated or interpolated at the operating frequency. dB/100 ft derived from cable data

𝑓

Operating frequency RF or IF frequency passing through the coax. MHz in the LMR equation user input

ℓ

Cable length One-way physical length of coax included in the calculation. ft or m user input

𝐿 a d d

Additional passive loss Known insertion loss from passive components that is not already part of the cable attenuation. dB optional user input

𝐿 t o t a l

Total feedline loss Coax-only loss plus the additional passive loss entered in Advanced Options. dB primary output

𝜂

Power-delivery fraction Fraction of input power remaining after the entered total loss. ratio dimensionless

𝑃 i n , 𝑃 o u t

Input and output power Power before the modeled feedline loss and the power remaining at the load after that loss. W, mW, kW, dBm, or dBW input power is optional

## Worked Coax Loss Example

Use the same illustrative state loaded by the calculator: 100 ft of Times Microwave LMR-400 at 146 MHz, 100 W input power, and 0 dB of additional passive loss.

### Given values

Cable

LMR-400

Frequency

146 MHz

Cable length

100 ft

Input power

100 W

Additional passive loss

0 dB

Find

Total feedline loss and power at the load

### Calculate LMR-400 attenuation at 146 MHz

𝛼 = 0 . 1 2 3 5 1 2 9  √ 1 4 6 + 0 . 0 0 0 2 6 2 6  ( 1 4 6 ) ≈ 1 . 5 3 0 7 5 d B / 1 0 0 f t

### Scale the attenuation to 100 ft

𝐿 c a b l e = 1 . 5 3 0 7 5  ( 1 0 0 1 0 0 ) = 1 . 5 3 0 7 5 d B

### Convert loss to delivered power

𝜂 = 1 0 − 1 . 5 3 0 7 5 / 1 0 ≈ 0 . 7 0 2 9 5

𝑃 o u t = 1 0 0  ( 0 . 7 0 2 9 5 ) ≈ 7 0 . 3 0 W

### Result

Total feedline loss ≈ 1.531 dB

About 70.30% of the input power remains after the modeled loss, so a 100 W source delivers about 70.30 W to the load under the matched-line assumptions. About 29.70 W is not delivered to the load because of the modeled attenuation.

### Independent check

Reversing the power-ratio relationship gives 1 0  l o g 1 0  ( 1 0 0 / 7 0 . 2 9 5 ) ≈ 1 . 5 3 0 7 5 d B , reproducing the attenuation result from the power calculation.

The calculator's preloaded example uses the same cable, frequency, length, power, and zero additional loss and returns the same result before display rounding.

## How to Interpret Coax Loss in dB

A dB loss is logarithmic, so the most useful interpretation is often the percentage of power that remains. The table below converts several common loss values using 1 0 − 𝐿 / 1 0 .

Power remaining after a passive loss

|   |   |   |

| --- | --- | --- |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

### Loss affects transmit and receive paths

For a passive coax run, insertion loss reduces RF power passing through the line in either direction. On transmit that appears as less power reaching the antenna or load; on receive it appears as signal attenuation before the receiver input.

### Length is linear in dB

Holding cable type and frequency constant, doubling the physical cable length doubles the coax loss in dB. A 50 ft run therefore has half the dB attenuation of the same cable at 100 ft under the same matched-line conditions.

### There is no universal acceptable loss

Whether 1 dB, 2 dB, or 3 dB is acceptable depends on the complete RF system: available link margin, antenna gain, transmitter power, receiver sensitivity, noise requirements, installation length, cable cost, and mechanical constraints.

### How much coax loss is acceptable?

A useful way to judge the result is to translate dB into remaining power rather than apply an arbitrary good/bad label. At 1 dB, about 79.4% of the input power remains; at 2 dB, about 63.1%; at 3 dB, about 50.1%; and at 6 dB, only about 25.1% remains. The acceptable value is the loss your complete RF link can tolerate while still meeting the required performance margin.

### What to do next

If the calculated attenuation consumes too much of the available RF budget, compare a lower-loss cable, shorten the run, remove unnecessary passive components, or move active equipment closer to the antenna. Then carry the verified feedline loss into a complete [RF link budget calculation](https://turn2engineering.com/calculators/link-budget-calculator) rather than judging the cable in isolation.

## Why Coax Loss Increases With Frequency

Coax attenuation generally rises as frequency increases because both conductor-related loss and dielectric loss increase. The exact curve depends on cable construction, which is why manufacturer-specific equations or tables are preferable to one generic frequency multiplier.

### Skin effect raises conductor loss

As frequency rises, RF current becomes increasingly concentrated near the conductor surfaces. The effective conducting cross-sectional area becomes smaller and AC resistance rises. The square-root-of-frequency term in common coax attenuation equations reflects much of this conductor-loss behavior.

### Dielectric loss also grows with frequency

The insulating material between the inner and outer conductors dissipates some RF energy. Its contribution becomes more important at higher frequency, which is why a simple √ 𝑓 scaling alone does not accurately describe every cable across a wide frequency range.

### Why this matters in practice

A cable that is satisfactory for a short HF run can be a poor choice for a long UHF or microwave run. Use the actual operating frequency when comparing cable options, and use the [Skin Depth Calculator](https://turn2engineering.com/calculators/skin-depth-calculator) if you want to examine how conductor skin depth changes with frequency.

## Why Real Coax Loss Can Be Higher

The calculator models the selected cable from published matched-line data. An installed feedline can measure differently when connectors, accessories, mismatch, damage, environment, or aging add effects that are not part of the nominal cable attenuation.

### Connectors and passive accessories

Adapters, lightning protectors, filters, RF switches, and connectors can add insertion loss. Enter a known combined value in Additional Passive Loss when you have manufacturer or measured data, and avoid counting a loss twice if it is already included in an assembly specification.

### Impedance mismatch and SWR

Published attenuation normally describes a matched line. A mismatched load creates a reflected wave, so part of the RF energy travels through the lossy line again. The resulting system loss can therefore exceed the simple matched-line attenuation shown by the cable datasheet.

### A lossy line can make transmitter-end SWR look better

The reflected wave is attenuated on its trip back toward the source. As feedline loss increases, an SWR measurement made at the radio can appear less severe than the mismatch that actually exists at the antenna or load. That is one reason a good-looking transmitter-end SWR does not prove the feedline is low loss.

### Water ingress, corrosion, and damaged cable

Field damage can make an installed feedline perform worse than new-cable data. If measured insertion loss is materially higher than the calculator result, inspect weather seals, connectors, shield continuity, crushed sections, sharp bends, and any location where moisture could enter.

### Temperature and exact product construction

Manufacturer attenuation values are published for stated reference conditions and a specific construction. Cable family names should not be treated as universal electrical specifications across every manufacturer, jacket, dielectric, center-conductor, or flexible variant.

### Receive systems can be especially sensitive to feedline loss

Loss ahead of the receiver attenuates weak incoming signals before they reach the first active stage. This is why systems such as ADS-B, satellite reception, GNSS, SDR, and weak-signal VHF/UHF often benefit from minimizing coax loss or placing a low-noise amplifier close to the antenna when the system design supports it.

### How to verify an installed feedline

When the exact loss matters, compare the calculator with a current datasheet for the exact part number and, when practical, a calibrated insertion-loss measurement of the complete cable assembly at the operating frequency. That comparison helps separate ordinary published cable attenuation from installation-specific degradation.

## How to Choose Lower-Loss Coax

Choose coax by comparing loss at the actual operating frequency and installed length, then check the electrical and mechanical requirements that the attenuation number does not capture. There is no single cable that is automatically best for every RF system.

### Compare at the exact frequency

A small difference between cables at HF can become much larger at UHF or microwave frequencies. This is why the calculator evaluates attenuation at the entered frequency instead of assigning one loss number to each cable type.

### Compare the full installed length

The lower-loss choice becomes more valuable as the run gets longer because dB loss scales with physical length. Include jumpers and other coax sections that are actually in the RF path.

### Keep 50 Ω and 75 Ω systems distinct

A 75 Ω cable can have attractive matched-line attenuation and still be a mismatch in a nominal 50 Ω system. The calculator's impedance warning is a prompt to check the complete transmission-line design, not a statement that one impedance is universally better.

### Verify power, connectors, routing, and environment

Attenuation alone does not establish suitability. Before choosing a cable, verify the manufacturer's frequency range, average and peak power limits when relevant, compatible connector system, minimum bend radius, jacket/environmental rating, and installation constraints.

### Use the exact cable datasheet for final selection

The calculator's LMR presets use the manufacturer's published K-factor attenuation method. Its RG-family examples use specific Belden products rather than assuming every cable with the same RG family name has one universal attenuation curve. For example, Belden 8240 is an RG-58/U-class product with a nominal characteristic impedance of 52 Ω, not an exact 50.0 Ω specification.

## Coax Loss Reference Values

Reference data is most useful when it stays tied to a specific manufacturer and product. The values below illustrate why generic RG-family labels should not be treated as exact attenuation specifications.

Selected published attenuation points for Belden MRG2132

|   |   |

| --- | --- |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

Source: [Belden MRG2132 technical data](https://catalog.belden.com/techdata/EN/MRG2132_techdata.pdf). Belden identifies these as nominal attenuation values and notes that maximum attenuation may be higher. Use the current datasheet for the exact product being installed.

### Why the calculator blocks unsupported extrapolation

When a preset is based on published table points rather than a manufacturer equation, the calculator stays inside the verified frequency range. Extending a table beyond the source data could make a precise-looking result less trustworthy than leaving the frequency unsupported.

## Assumptions and Limits

This is a matched-line attenuation calculator and preliminary RF planning tool. It is deliberately transparent about what is calculated and what still requires system-specific data.

### Manufacturer data is the baseline

Preset attenuation is based on manufacturer equations or published table values for specific cable families or products. These are nominal or typical data under the source's stated conditions, not a measurement of your installed cable.

### Table presets do not extrapolate

For published-table cables, the calculator interpolates only between verified frequency points and blocks frequencies outside the supported table range instead of inventing an extrapolated value.

### Mismatch is not solved from nominal impedance

The System Impedance option provides a warning when the selected cable's nominal impedance differs from the selected system impedance. It does not calculate reflection coefficient, SWR, return loss, or additional mismatch-related feedline loss.

### Power rating is not verified

Entering transmitter power lets the calculator report power remaining after loss; it does not confirm that the cable, connectors, or accessories are rated for that power at the selected frequency or environmental condition.

### Final check before implementation

For a consequential RF installation, verify the exact cable part number, current manufacturer attenuation and power data, connector and accessory insertion loss, source/load impedance, measured or modeled mismatch, environmental exposure, routing and bend limits, and the complete system link budget. Use the calculator as one verified loss term inside that larger design check.

## Related RF Calculators

Coax loss is usually one term in a larger RF system calculation. These tools extend the result without repeating the same calculation.

[RF system calculator Link Budget Calculator Use the feedline loss from this page with transmitter power, antenna gain, propagation loss, receiver sensitivity, and other system terms to evaluate received power and link margin.](https://turn2engineering.com/calculators/link-budget-calculator)

[Antenna calculator Antenna Gain Calculator Calculate or convert antenna gain before combining gain and feedline loss in an RF power budget.](https://turn2engineering.com/calculators/antenna-gain-calculator)

[Electromagnetics calculator Skin Depth Calculator Explore how conductor skin depth decreases as frequency rises, one of the physical effects behind increasing high-frequency conductor loss.](https://turn2engineering.com/calculators/skin-depth-calculator)

## Data Sources and Verification

The calculator and guide use manufacturer data for cable-specific attenuation and independently derived dB-to-power relationships for interpretation. Exact product data takes precedence over generic cable-family assumptions.

[Times Microwave Systems — LMR Complete Guide](https://timesmicrowave.com/wp-content/uploads/2024/04/lmr-complete-guide.pdf) — supports the LMR attenuation coefficient method, cable-specific coefficient sets, frequency scope, and related product data.

[Times Microwave Systems — Coaxial Cable Attenuation and Power Calculator](https://timesmicrowave.com/calculator/) — provides the manufacturer's current calculator and a direct external check on LMR attenuation behavior.

[Belden MRG2132 Technical Data](https://catalog.belden.com/techdata/EN/MRG2132_techdata.pdf) — supports the RG-213 preset attenuation table through 2.4 GHz and the stated nominal-table scope.

[Belden 8240 Technical Data](https://catalog.belden.com/techdatam/8240.pdf) — supports the RG-58/U-class representative product data, including its nominal 52 Ω characteristic impedance.

[Belden 1694A Product Data](https://www.belden.com/products/cable/broadcast-cable/sdi-video-coax-cable/6g-sdi/1694a) — supports the 75 Ω RG-6-class reference product and its published frequency-dependent attenuation data.

The worked example was checked two ways: first from the published LMR-400 attenuation equation, then by reversing the resulting power ratio back to dB. The two calculations agree before display rounding.

## Coax Loss Calculator FAQs

These questions address common decisions that come up after calculating feedline attenuation.

How much coax loss is there per 100 feet?

There is no single loss value per 100 ft because attenuation depends on the exact cable and operating frequency. Use the manufacturer's attenuation value or equation for the specific product at the frequency of interest, then scale it to the actual run length.

Does coax loss affect reception as well as transmission?

Yes. Passive coax attenuation reduces RF signals traveling through the line in either direction. On receive, feedline loss occurs before the receiver input, so minimizing loss is especially important when working with weak signals.

Can I use RG-6 in a 50-ohm RF system?

RG-6 is commonly a nominal 75 Ω cable, while many radio systems are nominally 50 Ω. It may be usable in a deliberately designed system, but lower matched-line attenuation alone does not prove interchangeability. Check the complete impedance transformation, reflections, connectors, and equipment requirements before substituting it.

Why can SWR measured at the radio look better than SWR at the antenna?

A lossy feedline attenuates both the forward and reflected waves. The reflected wave is smaller by the time it returns to a meter at the transmitter, so the measured transmitter-end SWR can appear less severe than the actual mismatch at the load.

How can I measure actual coax cable loss?

For an installed assembly, use a calibrated RF measurement method appropriate to the frequency range, such as a vector network analyzer or other insertion-loss setup, and compare the measured result with the current datasheet value for the exact cable and connectors. The measurement should include the same adapters and accessories that are part of the real RF path.

Should I use the highest frequency for a wideband coax run?

For a conservative attenuation check across a band, evaluate the cable at the highest operating frequency because coax loss generally increases with frequency. If the system has multiple critical channels or the manufacturer data is irregular, check each relevant frequency rather than relying on one point. 

[What is this?](https://www.journeymv.com?utm_source=journey|&utm_medium=ad&utm_campaign=logo)

Recommended

[

Refrigeration Cycles Explained | Thermodynamics Guide

](https://urls.grow.me/https%3A%2F%2Fturn2engineering.com%2Fmechanical-engineering%2Fthermodynamics%2Frefrigeration-cycles%23growMeRecommId%3D2004d6e65fc363ecef1306bfe2eeee8c%26growSource%3Drecs%26growReferrer%3Dtrue)

[

Electrical Properties of Materials

](https://urls.grow.me/https%3A%2F%2Fturn2engineering.com%2Fmechanical-engineering%2Fmaterials-science%2Felectrical-properties%23growMeRecommId%3D2004d6e65fc363ecef1306bfe2eeee8c%26growSource%3Drecs%26growReferrer%3Dtrue)

[

Atomic Structure | Materials Science Guide

](https://urls.grow.me/https%3A%2F%2Fturn2engineering.com%2Fmechanical-engineering%2Fmaterials-science%2Fatomic-structure%23growMeRecommId%3D2004d6e65fc363ecef1306bfe2eeee8c%26growSource%3Drecs%26growReferrer%3Dtrue) 

[What is this?](https://www.journeymv.com?utm_source=journey|&utm_medium=ad&utm_campaign=logo)

[About](https://turn2engineering.com/about)

[About](https://turn2engineering.com/about)

[Privacy Policy](https://turn2engineering.com/privacy-policy)

[Privacy Policy](https://turn2engineering.com/privacy-policy)

[Terms and Conditions](https://turn2engineering.com/terms-and-conditions)

[Terms and Conditions](https://turn2engineering.com/terms-and-conditions)

Copyright © 2026 Turn2DigitalMedia LLC

Scroll to Top

Search suggestions

DO NOT SELL OR SHARE MY PERSONAL INFORMATION

[Welding Symbols Chart: AWS Symbols & Meanings Welding Symbols Chart: AWS Symbols & Meanings](https://urls.grow.me/https%3A%2F%2Fturn2engineering.com%2Fcharts-and-tables%2Fwelding-symbols-chart%23growMeRecommId%3D2004d6e65fc363ecef1306bfe2eeee8c%26growSource%3Drecs%26growReferrer%3Dtrue)  

[What is this?](https://www.journeymv.com?utm_source=journey&utm_medium=ad&utm_campaign=logo) 

[What is this?](https://www.journeymv.com?utm_source=journey|&utm_medium=ad&utm_campaign=logo)  