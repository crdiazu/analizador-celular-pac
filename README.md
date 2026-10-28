# Analizador de Cobertura Celular Indoor — Proyecto Municipalidad de Pedro Aguirre Cerda

Repositorio técnico-comercial y aplicación web interactiva para el levantamiento, diagnóstico de cobertura móvil (4G LTE / 5G NR / 3G / 2G — Voz) y diseño de solución de amplificación indoor **Wilson Connectivity (`weBoost Office 200 LATAM SKU 531047`)** en el **Piso -1 (Zócalo / Subterráneo, cota `-3,20 m`)** del Centro Consistorial de la **Ilustre Municipalidad de Pedro Aguirre Cerda** (`Av. Presidente Salvador Allende N° 2029`).

- **Web App Interactiva y Diagrama de Mediciones (GitHub Pages):** https://crdiazu.github.io/analizador-celular-pac/
- **Geoportal Oficial SUBTEL Consultado (`appid=6c807cd119444c6fa3201d6b1a3ef5ed`):** https://licancabur.subtel.gob.cl/portal/apps/instant/portfolio/index.html?appid=6c807cd119444c6fa3201d6b1a3ef5ed
- **Integrador:** Tecnovoa (`www.tecnovoa.cl`) — KAM TI: Cristián Díaz (`cristian@tecnovoa.cl`)
- **Contraparte Cliente:** Álvaro O. Carreño Cerda — Jefe Departamento de Informática (`SECPLA`)
- **Operadores evaluados:** Entel, Movistar, Claro y WOM.

---

## Catastro Geoespacial Oficial SUBTEL (`licancabur.subtel.gob.cl`) en `Av. Presidente Salvador Allende N° 2029`

Consulta directa a las capas REST GIS de **SUBTEL** (*Coberturas Operadoras Móviles Junio 2026* y *Portal de Torres 2026*) para las coordenadas del Centro Consistorial (`lat = -33.4886, lon = -70.6655`):

1. **Cobertura Exterior 100% Verificada en las 4 Compañías:** Polígonos oficiales `3G / 4G LTE / 5G` activos sobre el edificio municipal para **Entel, Movistar, Claro y WOM** (`potencia ≥ -97 dBm`). Esto demuestra técnicamente que la falta de señal en el Piso `-1` (`-3,20 m`) se debe exclusivamente a la **atenuación estructural de las losas de hormigón armado subterráneas** (`> 30 dB`).
2. **Zona No Saturada (Ley de Antenas N° 20.599):** `ARC_TERRI_URB_SATURADA = 0` y mediciones de densidad de potencia entre `0,0055` y `0,033 µW/cm²` (*Ingeaudit Ltda.*).
3. **Estaciones Base Vecinas (`< 750 m`) y Calce 100% con `weBoost Office 200 LATAM (SKU 531047)`:**

| Distancia | Azimut | Operador(es) | Código SUBTEL | Dirección Exacta | Bandas Registradas | Calce con `Office 200 (531047)` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`163 m`** | `235° (SO)` | **Claro** | `43_691` (*Apolo-Teresa Vial*) | Av. Club Hípico N° 4676 | `2600 / 3500 MHz` | Macro 850/1900 + 4G/5G |
| **`253 m`** | `253° (OSO)` | **WOM** | `RM3519` | Teresa Vial fte. N° 2431 (Poste 118671) | `AWS 1700/2100 MHz` | **Banda 4 AWS (`1700/2100 MHz`)** |
| **`332 m`** | `14° (NNE)` | **WOM** | `RM4114` | Pasaje Nueva Seis N° 1951 | `AWS 1700/2100 MHz` | **Banda 4 AWS (`1700/2100 MHz`)** |
| **`346 m`** | `259° (O)` | **Entel + Movistar** | `UZM482 / GZM482` · `BALAK13` | Balakireff N° 4417 (*Parque André Jarlán*) | `850 / 1900 / 2600 / 3500 MHz` | **Banda 5 (`850`) + Banda 2 (`1900`)** |
| **`460 m`** | `110° (ESE)` | **Claro + Entel** | `13_851` · `GVM662` | Av. J.J. Prieto (Ruta 5) N° 4260 esq. Salesianos | `850 / 1900 / 2600 / 3500 MHz` | **Banda 5 (`850`) + Banda 2 (`1900`)** |
| **`495 m`** | `5° (N)` | **Entel + Claro** | `URS078 / GRS078 / EPCS3736` | Av. Club Hípico N° 3365 (Pob. Magallanes) | `1900 / 2600 / 3500 MHz` | **Banda 2 PCS (`1900 MHz`)** |
| **`553 m`** | `250° (OSO)` | **Claro** | `13_517` (*P.A.C.*) | Ángel Guarello esq. Félix Mendelssohn | `850 / 1900 / 2600 / 3500 MHz` | **Banda 5 (`850`) + Banda 2 (`1900`)** |
| **`573 m`** | `212° (SSO)` | **WOM** | `RM3502` | Av. Club Hípico N° 4811 | `AWS 1700/2100 MHz` | **Banda 4 AWS (`1700/2100 MHz`)** |
| **`684 m`** | `241° (OSO)` | **Entel + Movistar + Claro** | `MSA614` · `MRNC1` · `43_687` | Av. La Marina N° 2725 | `1900 / 2600 / 3500 MHz` | **Banda 2 PCS (`1900 MHz`)** |
| **`726 m`** | `160° (SSE)` | **Entel + Movistar + Claro** | `USA803` · `INA2U` · `13_938` | Av. José Joaquín Prieto N° 4850 | `850 / 1900 / 2600 / 3500 MHz` | **Banda 5 (`850`) + Banda 2 (`1900`)** |

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

- [`index.html`](./index.html): Aplicación web interactiva (GitHub Pages) con **5 vistas sincronizadas**:
  1. **`🌍 Mapa 3D Google Earth` (MapLibre GL + Satélite Esri World Imagery):** Vista satelital 3D inclinable/rotable de `Av. Presidente Salvador Allende N° 2029 esq. Av. Club Hípico`, con el **modelo 3D extruido del Centro Consistorial**, modo **Rayos-X Subterráneo `-1`** (recintos `P3`–`P8` coloreados en vivo según RSRP), las **10 Torres SUBTEL (`T1`–`T10`)** extruidas en 3D en sus coordenadas GPS exactas con haces de enlace hacia la azotea (`P1`), vuelo orbital 360° y exportador de malla 3D **`.OBJ`** para Blender/Scenario.
  2. **`Corte Esquemático D-D'`:** Diagrama vectorial interactivo de los niveles `-1`, `1`, `2` y `Azotea` con trazado del coaxial `Wilson400`.
  3. **`Plano Corte D-D' (JPG)`:** Pines interactivos sobre el plano original de cortes de *GMM Arquitectos*.
  4. **`Plano Planta Nivel 1 (JPG)`:** Pines interactivos sobre la planta arquitectónica original.
  5. **`📡 Radar Antenas SUBTEL (GIS)`:** Radar polar azimutal (`0°–360°`) de estaciones base en radio `< 750 m`.
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
