# Analizador de Cobertura Celular Indoor — Proyecto Municipalidad de Pedro Aguirre Cerda

Repositorio técnico-comercial y aplicación web interactiva para el levantamiento, diagnóstico de cobertura móvil (4G LTE / 5G NR / 3G / 2G — Voz) y diseño de solución de amplificación indoor **Wilson Connectivity (`weBoost Office 200 LATAM SKU 531047`)** en el **Piso -1 (Zócalo / Subterráneo, cota `-3,20 m`)** del Centro Consistorial de la **Ilustre Municipalidad de Pedro Aguirre Cerda** (`Av. Presidente Salvador Allende N° 2029`).

- **Web App Interactiva y Diagrama de Mediciones (GitHub Pages):** https://crdiazu.github.io/analizador-celular-pac/
- **Integrador:** Tecnovoa (`www.tecnovoa.cl`) — KAM TI: Cristián Díaz (`cristian@tecnovoa.cl`)
- **Contraparte Cliente:** Álvaro O. Carreño Cerda — Jefe Departamento de Informática (`SECPLA`)
- **Operadores evaluados:** Entel, Movistar, Claro y WOM.

---

## Especificaciones de la Solución Cotizada (`weBoost Office 200 LATAM · SKU 531047 / 530047`)

Según la ficha oficial [`531047-530047_office200_ss_LATAM_102721b (1).pdf`](./531047-530047_office200_ss_LATAM_102721b%20(1).pdf):

- **Bandas de Operación LATAM:**
  - **Banda 5 (`850 MHz`):** DL `+18.0 dBm` / UL `+24.1 dBm` (Movistar, Claro)
  - **Banda 4 (`1700/2100 MHz AWS`):** DL `+19.6 dBm` / UL `+25.0 dBm` (**WOM**, Entel, Claro)
  - **Banda 25/2 (`1900 MHz PCS`):** DL `+22.0 dBm` / UL `+24.5 dBm` (Entel, Movistar, Claro)
- **Ganancia Máxima:** **`74 dB`** (Cumple norma técnica SUBTEL `< 100 dB`, con tecnología **XDR** anti-sobrecarga y pantalla táctil LCD a color).
- **Impedancia y Conectores:** **`50 Ohm`** profesional con conectores **N-Hembra** (`VSWR < 1.2:1`).
- **Componentes incluidos en el Kit `531047`:**
  1. Amplificador **weBoost Office 200** (`531047`).
  2. Antena Exterior **Omni Plus (`314422`)** — Captación omnidireccional 360° para las 4 compañías en Azotea (`Eje P–Q`).
  3. Antena Interior **Domo de Perfil Bajo (`314407`)** — Para cielo falso del Nivel -1 (`Eje R`).
  4. **Protector Contra Sobretensiones de Relámpago (`859902`)** + Jumper `Wilson400` de `0,60 m` (`952302`).
  5. **2 Rollos de Cable Coaxial `Wilson400` (LMR-400) de Baja Pérdida:**
     - `18,28 m` (`952360`) — Tramo Donante desde Azotea por Shaft `GI 07/08`.
     - `22,86 m` (`952375`) — Tramo Servidor hacia Antena Domo en Nivel -1.

---

## Estructura del Repositorio

- [`index.html`](./index.html): Aplicación web interactiva (GitHub Pages) con diagrama del `Corte D-D'`, visor sobre planos reales, simulador de 5 configuraciones **Wilson Connectivity** (`weBoost Office 200`, `WilsonPro 1300R`, `WilsonPro 4300R`, `Zinwave Hybrid DAS`), calculadora de *Link Budget* (`Wilson400 50 Ω`) y verificación de aislamiento SUBTEL ($I_{\text{mín}} > G + 15\text{ dB} = 89\text{ dB}$).
- [`Procedimiento_Medicion_Cobertura_Subterraneo.md`](./Procedimiento_Medicion_Cobertura_Subterraneo.md): Procedimiento completo de terreno (Comercial + Prevencionista de Riesgos), ingeniería de detalle del kit `531047`, normativa SUBTEL y plantilla de registro.
- [`plantilla_mediciones_pac.csv`](./plantilla_mediciones_pac.csv): Matriz pre-cargada con los **9 puntos estructurales (`P0` a `P8`) × 4 compañías** lista para Excel/Sheets o importación directa en la web app.
- [`531047-530047_office200_ss_LATAM_102721b (1).pdf`](./531047-530047_office200_ss_LATAM_102721b%20(1).pdf): Datasheet oficial en español del kit **weBoost Office 200 LATAM (`531047 / 530047`)**.
- **Planos Arquitectónicos (GMM Arquitectos):**
  - [`Elevation-Sections-001.jpg`](./Elevation-Sections-001.jpg): Cortes `A-A'` a `E-E'` (incluye el **Corte D-D'** donde se identifican las oficinas del Nivel -1: *Jefe Informática*, *2 Técnicos Informática*, *Jefatura Emergencia*, *Relaciones Públicas* y *Archivo e Inventario*).
  - [`First_Floor_Plan-001.jpg`](./First_Floor_Plan-001.jpg): Planta Nivel 1 (ubicación de `Racks y Central Servidores` y shafts verticales `GI 07` y `GI 08` en el **Eje P–Q**).
  - [`Second_Floor_Plan-001.jpg`](./Second_Floor_Plan-001.jpg): Planta Nivel 2.
- **Documentación Técnica RF, Wilson Connectivity y Normativa SUBTEL:**
  - [`G-NetTrack_Pro_manual.pdf`](./G-NetTrack_Pro_manual.pdf): Manual oficial de G-NetTrack Pro.
  - [`notebooklm-sources-2026-10-28 (1)/`](./notebooklm-sources-2026-10-28%20(1)/): Compendio completo de 73 documentos sobre ingeniería de amplificadores BDA, cables coaxiales (`LMR-400 / Wilson400`), impedancia `50 Ω vs 75 Ω`, arquitectura **Wilson Connectivity** (`weBoost`, `WilsonPro`, `Zinwave`), **Norma Técnica SUBTEL de Repetidores** y **Resolución Exenta 737**.
