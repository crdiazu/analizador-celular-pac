# Coaxial Cable Attenuation & Power Loss Calculator - TelecomCalculators

Coaxial Cable Attenuation & Power Loss Calculator | TelecomCalculators

[Telecom Calculators](https://telecomcalculators.com/) [Home](https://telecomcalculators.com/) [Calculators](https://telecomcalculators.com/#categories) [Reference](https://telecomcalculators.com/reference/) [About](https://telecomcalculators.com/about/) [Contact](https://telecomcalculators.com/contact/)

[Home](https://telecomcalculators.com/) / [Calculators](https://telecomcalculators.com/#categories) / [RF Transmission Lines](https://telecomcalculators.com/calculators/rf-transmission-lines/) / Coax Cable Attenuation

# Coaxial Cable Attenuation & Power Loss Calculator

Calculate RF coaxial cable attenuation (dB/100m, dB/100ft) and transmitted power loss across frequency and run length. Features RG-58, LMR-400, Heliax presets.

Select Coaxial Cable Type Empirical k 1 / k 2 Presets

LMR-400 (Gas-Injected Foam PE, 50 Ω)

RG-58 C/U (Solid PE, 50 Ω)

RG-8X / Mini-8 (Foam PE, 50 Ω)

RG-213 / RG-8U (Solid PE, 50 Ω)

LMR-195 (Gas-Injected Foam PE, 50 Ω)

LMR-240 (Gas-Injected Foam PE, 50 Ω)

LMR-600 (Gas-Injected Foam PE, 50 Ω)

1/2" Corrugated Heliax (Cellular Foam, 50 Ω)

7/8" Corrugated Heliax (Cellular Foam, 50 Ω)

RG-6 / U (Foam PE, 75 Ω CATV / Sat)

± Custom Cable (Specify k1, k2, VF, Z0)

Resistive k 1 (√f) 0.122

Dielectric k 2 (f) 0.0003

Velocity Factor (VF) 0.85

Impedance (Z 0, Ω) 50

Operating Carrier Frequency (f) RF / Microwave Band 2400

MHz

GHz

kHz

Quick Bands: 144 MHz (2m VHF) 433 MHz (UHF) 900 MHz (Cellular) 2.4 GHz (Wi-Fi) 5.8 GHz (UNII-3)

Feeder Physical Run Length (L) End-to-End Distance 30

Meters (m)

Feet (ft)

Common Runs: 5 m (Patch) 15 m (Rooftop) 30 m (Tower) 50 ft 100 ft

Transmitter Input Power (P in) Source Wattage to Feeder 50

Watts (W)

dBm

Kilowatts (kW)

Transmitter Levels: 5 W (Handheld) 50 W (Base Stn) 100 W (PA) 43 dBm (20 W) 1 kW (Broadcast)

Please enter positive numerical values for frequency, cable length, and input power.

Total Cable Run Attenuation

2.01 dB

62.96% Power Pass-Through Efficiency

Feeder Rating

●

Low Loss / High Eff.

Delivered Load Power (P out)

31.48 W

44.98 dBm (63.0%)

Heat Dissipated Power (P loss)

18.52 W

37.04% dissipated as thermal heat

Attenuation Rate (Metric)

6.70 dB

dB per 100 meters

Attenuation Rate (Imperial)

2.04 dB

dB per 100 feet

Nominal Velocity Factor (VF)

0.85 c

Phase Velocity: 254.8 km/ms

Characteristic Line Impedance

50 Ω

Gas-Injected Foam PE

Δ Two-Term Empirical Attenuation Breakdown

α(f) = k 1

· √f + k 2

· f = 0.122· √(2400.0) + 0.00030· (2400.0) = 5.98 + 0.72 = 6.70 dB/100m (2.04 dB/100ft)

Total Loss (30.0m) = 6.70 × (30.00 / 100) = 2.01 dB

P out = 50.00 W × 10^(-2.01 / 10) = 31.48 W (63.0%) | Thermal Heat = 18.52 W (37.0%)

## The Electromagnetics of Coaxial Line Losses: Conductor Skin Depth, Dielectrics & Power Derating

An in-depth technical treatise on electromagnetic wave propagation inside coaxial waveguides, the physics separating skin resistance from dielectric loss, and thermal dissipation thresholds in high-power transmitters.

### 1. The Physics of Attenuation in Coaxial Waveguides

A coaxial cable is a transverse electromagnetic (TEM) transmission line consisting of two concentric cylindrical conductors separated by a continuous dielectric insulating medium. As a high-frequency RF voltage wave propagates along the axis $z$, its total attenuation constant $\alpha$ (expressed in Nepers/meter or converted to decibels/meter via $1\text{ Np} \approx 8.686\text{ dB}$) is the algebraic sum of two independent physical dissipation mechanisms:

Total Complex Waveguide Attenuation Constant

α = α c + α d

α c = Conductor resistive attenuation due to finite skin depth (Nepers/m)

α d = Dielectric dissipation loss due to alternating electric polarization (Nepers/m)

In the transmission line lumped-element equivalent model ($R, L, G, C$ per unit length), the attenuation constant under low-loss conditions ($R \ll \omega L$ and $G \ll \omega C$) is governed by: $$\alpha \approx \frac{R}{2 Z_0} + \frac{G Z_0}{2}$$ where $Z_0 = \sqrt{L/C}$ is the characteristic line impedance. Notice that the first term ($R / 2Z_0$) accounts for the series conductor resistance, while the second term ($G Z_0 / 2$) accounts for the shunt dielectric conductance.

### 2. The Two-Term Empirical Attenuation Formula: α(f) = k 1 √f + k 2 f

Because pure analytical formulas require microscopic knowledge of conductor surface roughness, braid weave optical coverage, and microscopic dielectric inclusions, RF cable manufacturers characterize line loss using the classic two-term empirical formula:

Empirical Dual-Mechanism Attenuation Formula

α(f) = k 1 × √(f MHz) + k 2 × f MHz [dB / 100 meters or dB / 100 feet]

The physical origin of each term reveals why transmission lines behave differently across spectrum bands:

**The √f Term (k 1 × √f — Conductor Skin Losses):** At alternating radio frequencies, the magnetic flux inside the metal forces electrical current to concentrate in a thin outer boundary known as the *skin depth*: $$\delta = \sqrt{\frac{\rho}{\pi f \mu_0 \mu_r}}$$ Because effective cross-sectional conducting area shrinks proportionally to $\delta \propto 1/\sqrt{f}$, high-frequency AC resistance increases in direct proportion to $\sqrt{f}$. At HF and lower VHF frequencies (below $150\text{ MHz}$), the $k_1 \sqrt{f}$ term accounts for more than $90%$ of all cable loss.

**The Linear f Term (k 2 × f — Dielectric Dissipation):** The insulating dielectric substrate between inner and outer conductors has an alternating electric displacement field running through it. The dielectric loss factor is governed by its loss tangent $\tan\delta = \epsilon'' / \epsilon'$. The shunt dielectric conductance per unit length is: $$G = \omega C \tan\delta = 2\pi f C \tan\delta$$ Because each cycle of the RF sine wave forces polar molecules to re-orient and dissipate kinetic heat, dielectric loss scales linearly with frequency $f$. As frequencies push above $1\text{ GHz}$ (Wi-Fi, 5G, and satellite Ku-band), the linear $k_2 f$ term grows rapidly, eventually rivaling or exceeding conductor skin losses in solid polyethylene cables.

⚠ The Solid PE vs. Gas-Injected Foam Trap at Microwave Frequencies

Legacy cables like **RG-58 C/U** and **RG-213** utilize solid polyethylene ($PE$) dielectrics with a velocity factor of $VF \approx 0.66$ and a relatively high loss factor ($k_2 \approx 0.0016$). At $2.4\text{ GHz}$, RG-58 attenuates an astonishing $112\text{ dB / 100m}$ — meaning a $30\text{ meter}$ antenna run loses $33.6\text{ dB}$ (leaving less than $0.05%$ of transmitter power!). In stark contrast, modern low-loss cables like **LMR-400** replace solid PE with closed-cell gas-injected foam PE ($VF = 0.85$, $k_2 = 0.0003$). The injected inert gas behaves almost identically to free-space air, reducing $2.4\text{ GHz}$ attenuation to only $22.3\text{ dB / 100m}$ ($6.7\text{ dB}$ over $30\text{ m}$).

### 3. Coaxial Geometry Optimization: The 50 Ω vs. 75 Ω Paradigm

For a coaxial geometry with inner conductor outer radius $a$ and outer conductor inner radius $b$, the characteristic impedance is: $$Z_0 = \frac{138}{\sqrt{\epsilon_r}} \log_{10}\left(\frac{b}{a}\right) = \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{b}{a}\right)$$ Analytical optimization demonstrates three conflicting physical maxima for air-dielectric lines:

**Minimum Attenuation ($b/a \approx 3.59$ → $Z_0 \approx 76.7\ \Omega$):** By differentiating total conductor resistance with respect to the radius ratio $b/a$, minimum RF skin loss occurs when $b/a = 3.59$. This is the mathematical reason why video broadcast, cable television (CATV), and master antenna satellite systems standardized on **75 Ω** coaxial lines (such as RG-6/U), where minimizing microvolt signal attenuation across kilometer-long residential trunk drops is paramount.

**Maximum Voltage Breakdown ($b/a \approx 2.72$ → $Z_0 \approx 60\ \Omega$):** The peak radial electric field at the inner conductor surface is $E_{\text{max}} = V / [a \ln(b/a)]$. Maximizing dielectric breakdown voltage occurs at $b/a = e \approx 2.718$, yielding $Z_0 \approx 60\ \Omega$.

**Maximum Continuous Power Handling ($b/a \approx 1.65$ → $Z_0 \approx 30\ \Omega$):** Maximizing the transfer of raw RF power before thermal core destruction occurs at approximately $30\ \Omega$.

The standard **50 Ω** line represents the historical IEEE and military compromise: it sits squarely between the peak power handling of $30\ \Omega$ and the minimum attenuation of $77\ \Omega$, while matching quarter-wave ground-plane monopole radiation resistances ($36.8\ \Omega$) and folded dipole transformations exceptionally well.

### 4. Thermal Power Dissipation & High-Power Derating Factors

All power lost in a transmission line ($P_{\text{loss}} = P_{\text{in}} - P_{\text{out}}$) is converted into internal thermal heat. In high-power commercial transmitters ($100\text{ W}$ to $50\text{ kW}$), feeder heat generation creates serious engineering failure modes:

**Core Melt and Dielectric Migration:** Excessive inner conductor temperatures cause solid or cellular polyethylene to soften. Under gravitational pull or mechanical bending radii, the center conductor slowly migrates off-center toward the outer shield, altering $Z_0$, creating severe local impedance lumps, and eventually forming an electrical dead short.

**Ambient Temperature Derating:** Cable manufacturer power ratings are universally specified at an ambient room temperature of $+20^\circ\text{C}$ ($68^\circ\text{F}$) under sea-level convection. In outdoor rooftop deployments where ambient solar loading elevates feeder jacket temperatures to $+50^\circ\text{C}$ or $+60^\circ\text{C}$, maximum allowable transmitter power must be derated by $30%$ to $50%$ to prevent catastrophic jacket thermal runaway.

**VSWR Multiplier Penalties:** When an antenna load is mismatched (e.g., VSWR $> 2.0:1$), the standing wave creates voltage maximums ($V_{\text{max}} = V_{\text{inc}}(1 + |\Gamma|)$) and current maximums ($I_{\text{max}} = I_{\text{inc}}(1 + |\Gamma|)$). Local dielectric heating increases by $(1 + |\Gamma|)^2$ at voltage antinodes, while localized $I^2 R$ conductor heating spikes dramatically at current antinodes, creating intense localized hot spots along the feeder run.

## Standard Coaxial Cable Attenuation Reference Table

Industry benchmark attenuation ratings (dB/100m) across VHF, UHF, cellular, and microwave bands.

|   |   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

## Related RF Transmission Line & Power Calculators

Complementary tools for wave propagation, impedance mismatch, velocity delay, and link budgeting.

Mismatch & Reflections

### VSWR & Return Loss Calculator

Convert bi-directionally between VSWR, Return Loss (dB), Reflection Coefficient (|Γ|), and Reflected Power percentage.

VSWR = (1 + |Γ|) / (1 - |Γ|)

[Open Calculator →](https://telecomcalculators.com/calculators/rf-transmission-lines/vswr-return-loss/)

Power Transfer

### Impedance Mismatch Loss Calculator

Quantify net power delivery attenuation to mismatched antenna loads and master reflection vs. mismatch loss distinctions.

Loss mismatch = -10 log 10(1 - |Γ|²)

[Open Calculator →](https://telecomcalculators.com/calculators/rf-transmission-lines/mismatch-loss/)

Phase Velocity & Delay

### Velocity Factor & Cable Delay

Determine electrical line length, dielectric propagation delay in nanoseconds, and phase shifting across coaxial stubs.

v p = c × VF • t delay = L / v p

[Open Calculator →](https://telecomcalculators.com/calculators/rf-transmission-lines/velocity-factor/)

RF Link Planning

### RF Power Budget Calculator

Calculate end-to-end transmission link margins, cascaded stage gains, feeder insertion losses, and terminal receiver sensitivity.

P rx = P tx + G tx - Losses + G rx

[Open Calculator →](https://telecomcalculators.com/calculators/power-rf/rf-power-budget/)

TelecomCalculators

[Sitemap](https://telecomcalculators.com/sitemap/) [FAQ](https://telecomcalculators.com/faq/) [Privacy Policy](https://telecomcalculators.com/privacy/) [Terms of Service](https://telecomcalculators.com/terms/)

Disclaimer: Calculations provided on this site are designed for professional engineering estimation, link planning, and academic analysis. While formulas strictly follow ITU-R, 3GPP, and IEEE published specifications, real-world deployments require site surveys and certified equipment manufacturer verification.

© 2026 TelecomCalculators. All rights reserved. Contact: [contact@telecomcalculators.com](mailto:contact@telecomcalculators.com)

Carrier-grade, client-side precision.