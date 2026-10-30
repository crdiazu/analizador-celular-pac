# Procedimiento y Plantilla de Terreno: Estudio de Cobertura Celular Indoor (Piso -1)
**Proyecto:** Optimización de Señal Móvil (Voz / 4 Operadores) — Solución **Wilson Connectivity (`weBoost Office 200 LATAM SKU 531047`)**  
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda (Edificio Consistorial)  
**Integrador:** Tecnovoa (`cristian@tecnovoa.cl`) — KAM TI: Cristián Díaz + Prevencionista de Riesgos  
**Web App Interactiva (GitHub Pages):** https://crdiazu.github.io/analizador-celular-pac/

---

## 0. Hallazgos del Análisis de Planos + Ingeniería del Kit Cotizado (`weBoost Office 200 SKU 531047`)

Cruzando los planos arquitectónicos ([Elevation-Sections-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/Elevation-Sections-001.jpg), [First_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/First_Floor_Plan-001.jpg), [Second_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/Second_Floor_Plan-001.jpg)) con la ficha oficial [531047-530047_office200_ss_LATAM_102721b (1).pdf](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/531047-530047_office200_ss_LATAM_102721b%20(1).pdf) y la documentación técnica de **Wilson Connectivity / SUBTEL**:

### 1. Geometría exacta del Nivel -1 (Cota `-3,20 m`, altura libre `2,60 m`)
En el **Corte D-D'** se verifica que el **Departamento de Informática** y otras unidades municipales trabajan en el zócalo subterráneo (módulos estructurales de **6,0 m entre ejes**):
- **Ejes T–S (`12 m`):** *2 Profesionales Relaciones Públicas* y *Jefatura Relaciones Públicas*.
- **Ejes S–R (`6 m`):** *Jefatura Emergencia* y ***Jefe Informática (oficina de Álvaro Carreño)***.
- **Ejes R–Q (`6 m`):** *Bodega* y ***2 Técnicos Informática***.
- **Ejes Q–P (`6 m`):** **Hall Subterráneo / Núcleo de Escalera y Ascensor** (acceso principal al Nivel -1).
- **Ejes P–O (`6 m`):** *Encargado Archivo Municipal e Inventario* y *Bodega de Inventario*.
- **Ejes O–K (`~23 m`):** *Archivo Municipal* (bajo losa maciza del patio central).
- **Ejes A–N (`Corte B-B'` y `C-C'`):** *Estacionamientos subterráneos* (acceso por rampa en Ejes U–W desde calle Manuela Errázuriz).

### 2. Especificaciones Exactas del Equipo Cotizado: `weBoost Office 200 LATAM (SKU 531047 / 530047)`
A diferencia de las versiones norteamericanas estándar, la ficha técnica [531047-530047_office200_ss_LATAM_102721b (1).pdf](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/531047-530047_office200_ss_LATAM_102721b%20(1).pdf) confirma que el modelo **SKU `531047` (`50 Ohm`)** es la **versión LATAM**, optimizada para las bandas de voz y 4G de **Entel, Movistar, Claro y WOM** en Chile:

| Parámetro Técnico | Especificación Oficial `weBoost Office 200 LATAM (531047)` | Ventaja en Municipalidad de PAC |
| :--- | :--- | :--- |
| **Frecuencias / Bandas** | • **Banda 5 (`850 MHz`)** — Movistar / Claro<br>• **Banda 4 (`1700/2100 MHz AWS`)** — **WOM** / Entel / Claro<br>• **Banda 25/2 (`1900 MHz PCS`)** — Entel / Movistar / Claro | Cubre las 4 telcos simultáneamente en voz (3G/2G y 4G VoLTE) y datos 4G. |
| **Ganancia Máxima** | **`74 dB`** (Superior a los 65–70 dB de kits domésticos; cumple norma SUBTEL `< 100 dB`) | Compensa de sobra los ~35 dB de pérdida estructural hacia el Piso -1. |
| **Potencia Máxima (UL / DL)** | • **Uplink (a torre):** `24.1 dBm` (B5) · `25.0 dBm` (B4) · `24.5 dBm` (B2)<br>• **Downlink (indoor):** `18.0 dBm` (B5) · `19.6 dBm` (B4) · **`22.0 dBm` (B2)** | Sus `+22 dBm` en Downlink entregan hasta **4.300 m²** teóricos de cobertura en planta abierta. |
| **Impedancia y Conectores** | **`50 Ohm`** con conectores profesionales **N-Hembra** (`VSWR < 1.2:1`) | Evita las pérdidas por reflexión (`VSWR 1.5:1`) típicas de sistemas de 75 Ohm con conector F. |
| **Control Dinámico y Pantalla** | **Pantalla táctil LCD a color** + Tecnología **XDR (*eXtended Dynamic Range*)** | Nunca se apaga por saturación; permite apagar/encender bandas y calibrar antena en pantalla. |
| **Antena Exterior Incluida** | **Antena Omni Plus (`314422`)** — Omnidireccional 360° (50 Ohm) | **Crucial para las 4 compañías:** capta torres en 360° sin sacrificar un operador por apuntar a otro. |
| **Antena Interior Incluida** | **Antena Domo de Perfil Bajo (`314407`)** (50 Ohm) | Diseñada para montaje discreto en el cielo falso (`h = 2,60 m`) del pasillo de Informática. |
| **Protección Eléctrica** | **Protector Contra Sobretensiones de Relámpago (`859902`)** + Jumper `0,60 m` (`952302`) | Protege el amplificador y la Sala de Racks ante descargas atmosféricas en la azotea. |
| **Cables Coaxiales Incluidos** | **Cable `Wilson400` (LMR-400) de ultra baja pérdida:**<br>• 1 rollo de **`18,28 m`** (`952360`)<br>• 1 rollo de **`22,86 m`** (`952375`)<br>• 1 jumper de **`0,60 m`** (`952302`) | **Total `41,74 m` incluidos en caja:** alcanza desde la Azotea (`+8,25 m`) hasta el Piso -1 (`-3,20 m`) por el Shaft `GI 07/08` sin comprar cable extra. |

### 3. Presupuesto de Enlace (*Link Budget*) y Regla de Aislamiento SUBTEL
1. **Atenuación del Cable `Wilson400` ($\alpha(f) = k_1\sqrt{f} + k_2 f$, factor de velocidad $VF = 0.85$):**
   - Tramo Donante (`18,28 m`, SKU `952360`): pierde solo **`~2,3 dB`** en `850 MHz (B5)` y **`~3,4 dB`** en `1900/2100 MHz (B2/B4)`.
   - Tramo Servidor (`22,86 m`, SKU `952375`): pierde solo **`~2,9 dB`** en `850 MHz (B5)` y **`~4,3 dB`** en `1900/2100 MHz (B2/B4)`.
   - **Ganancia Neta del Sistema:** $74\text{ dB} - (3,4\text{ dB} + 4,3\text{ dB}) \approx \mathbf{+66,3\text{ dB}}$ efectivos.
2. **Condición de Aislamiento Electromagnético Anti-Oscilación ($I_{\text{mín}} > G_{\text{amp}} + 15\text{ dB}$):**
   - Para operar el `Office 200` a su ganancia máxima de `74 dB` sin activar recorte por bucle de realimentación (*feedback*), se requiere un aislamiento entre la Antena Omni Plus (`314422`) y la Antena Domo (`314407`) de:
     $$I_{\text{mín}} > 74\text{ dB} + 15\text{ dB} = \mathbf{89\text{ dB}}$$
   - En el Edificio Consistorial, entre la Azotea (`+8,25 m`) y el techo del Nivel -1 (`-0,60 m`) hay **`~9 a 11 metros` de separación vertical más 2 losas macizas de hormigón armado** (~25–30 dB por losa + ~55 dB por espacio libre), logrando un **aislamiento real estimado $> 105\text{ dB}$** (cumple holgadamente).

### 4. Matriz de Escalabilidad (Alternativas del Portafolio Wilson Connectivity)
Si en la visita el cliente solicita ampliar el alcance (por ejemplo, cubrir también Auditorio, Archivo completo y Estacionamientos), tienes estas opciones respaldadas en la documentación:

| Nivel / Solución | Modelo / SKU | Cobertura / Puertos | Cuándo ofrecerlo a la Municipalidad |
| :--- | :--- | :--- | :--- |
| **Opción 1 (Base 1 Domo)** | **weBoost Office 200 LATAM (`531047`)** — 1 Antena Domo (`314407`) | Hasta `4.300 m²` (1 puerto indoor, `+22 dBm` DL, `74 dB` ganancia) | Si los tabiques entre Informática (`Ejes Q–S`) y RR.PP. (`Ejes S–T`) son livianos/vidrio. |
| **Opción 2 (Expansión Pasiva)** | **weBoost Office 200 (`531047`) + Splitter 2/3 Vías 50 Ω + Antenas Domo extra** | 2 o 3 zonas dedicadas en Piso -1 (pierde `3,2 dB` en splitter de 2 vías) | Si hay muros de hormigón entre **Informática (`Eje R`)**, **RR.PP. (`Eje S`)** y **Archivo (`Eje O`)**. |
| **Opción 3 (Rack + Gestión Cloud)** | **WilsonPro Enterprise 1300R (`460149`)** (Chasis Rack 19" + **WilsonPro Cloud**) | Hasta `3.700 m²` · Monitoreo remoto Ethernet RJ-45 / LTE | Si Álvaro Carreño quiere montar el equipo en su **Rack de 19" (`Sala Racks Eje P–Q`)** y recibir alertas por correo/SMS en *WilsonPro Cloud*. |
| **Opción 4 (Multi-Torre / 4 Zonas)** | **WilsonPro Enterprise 4300R (`460153`)** (4 Amplificadores + **MTT 3 Donantes**) | Hasta `9.200 m²` · **4 salidas indoor** independientes + **3 antenas exteriores LPDA** | Si quieren cubrir **todo el subterráneo** (Informática + RR.PP. + Archivo + Auditorio + Estacionamientos) sin pérdidas por splitters. |
| **Opción 5 (Campus / 5G Banda n78)** | **Wilson Hybrid DAS / Zinwave 8000** (RF sobre Fibra Óptica `150 MHz – 5 GHz`) | Hasta 64 unidades remotas por fibra · Incluye **5G 3.5 GHz** y radios VHF/UHF | Proyecto mayor de modernización de todo el Centro Consistorial sin pérdidas coaxiales. |

### 5. Cumplimiento Normativo SUBTEL Chile
De acuerdo con la **Norma Técnica SUBTEL para Repetidores** y la **Resolución Exenta N° 737**:
- **Control Automático de Ganancia (AGC / XDR) y Anti-Oscilación:** Incorporado nativamente en el `Office 200` (tecnología patentada **XDR**).
- **Ganancia máxima `< 100 dB` y Figura de Ruido `≤ 7 dB`:** El `Office 200` opera con `74 dB` máx. y figura de ruido `< 5 dB`.
- **Intermodulación `≤ -19 dBm` y Automatic Standby (`≤ -70 dBm/MHz EIRP` en Uplink):** Garantiza cero interferencia hacia las radiobases públicas de Entel, Movistar, Claro y WOM.

### 6. Catastro Geoespacial Oficial SUBTEL (`licancabur.subtel.gob.cl`) en el Entorno del Centro Consistorial
Consulta directa a los servicios REST GIS de la **Subsecretaría de Telecomunicaciones (SUBTEL)** ([Portal de Mapas de Cobertura Digital `appid=6c807cd119444c6fa3201d6b1a3ef5ed`](https://licancabur.subtel.gob.cl/portal/apps/instant/portfolio/index.html?appid=6c807cd119444c6fa3201d6b1a3ef5ed) y *Portal de Torres 2026*) para las coordenadas exactas del edificio municipal (`Av. Presidente Salvador Allende N° 2029, esq. Av. Club Hípico`, `lat = -33.4886, lon = -70.6655`):

1. **Verificación de Cobertura Exterior Declarada ante SUBTEL:**
   - **Entel:** Cubierto en **3G (`900/1900 MHz`, `≥ -97 dBm`)**, **4G LTE** y **5G (`3500 MHz`)**.
   - **Movistar:** Cubierto en **3G (`850 MHz`, polígono `MVS_3G850_Centro ≥ -97 dBm`)**, **4G LTE** y **5G**.
   - **Claro:** Cubierto en **2G (`850 MHz`)**, **3G (`1900/2100 MHz`, `≥ -97 dBm`)**, **4G LTE (`Subtel LTE_ALL 2026`)** y **5G (`3500 MHz`)**.
   - **WOM:** Cubierto en **3G (`AWS 1700/2100 MHz`, `≥ -97 dBm`)**, **4G LTE (`AWS / 700 MHz`)** y **5G (`2100 / 3500 MHz`)**.
   - **Estado Ley de Antenas N° 20.599:** `ARC_TERRI_URB_SATURADA = 0` y `ARC_INFRA_SATURADA = 0` (**Zona NO saturada**; mediciones de densidad de potencia certificadas por *Ingeaudit Ltda.* entre `0,0055` y `0,033 µW/cm²`, muy bajo el límite legal).
   - **Conclusión Comercial para Álvaro Carreño:** Esto demuestra con datos oficiales de SUBTEL que **las 4 compañías tienen excelente cobertura exterior en el predio municipal**; la pérdida de llamadas en el Piso `-1` (`-3,20 m`) se debe exclusivamente al **apantallamiento estructural de las losas y muros de hormigón armado bajo cota cero** (Hipótesis #1 de Tecnovoa).

2. **Estaciones Base (Torres Celulares) Registradas en SUBTEL en un Radio de `< 750 m`:**

| Distancia | Azimut desde Azotea (`+8,25 m`) | Operador(es) | Código Estación SUBTEL | Dirección Exacta (Comuna) | Soporte / Altura | Tecnologías y Bandas Registradas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`163 m`** | **`235° (SO)`** | **Claro** | `43_691` (*Apolo - Teresa Vial*) | Av. Club Hípico N° 4676 (PAC) | Torre Autosoportada `9 m` | `4G LTE / 5G` (`2600 / 3500 MHz`) |
| **`253 m`** | **`253° (OSO)`** | **WOM** | `RM3519` | Calle Teresa Vial fte. N° 2431, Poste 118671 (PAC) | Poste `12 m` | `3G / 4G LTE` (**`AWS 1700/2100 MHz` — Banda 4**) |
| **`332 m`** | **`14° (NNE)`** | **WOM** | `RM4114` | Pasaje Nueva Seis N° 1951 (PAC) | Poste `12 m` | `3G / 4G LTE` (**`AWS 1700/2100 MHz` — Banda 4**) |
| **`346 m`** | **`259° (O)`** | **Entel + Movistar** | `UZM482 / GZM482` (Entel) · `BALAK13` (Movistar) | Balakireff N° 4417 — *Parque André Jarlán* (PAC) | Monoposte `12 m` | `3G / 4G / 5G` (**`850 / 1900 / 2600 / 3500 MHz` — B5/B2**) |
| **`460 m`** | **`110° (ESE)`** | **Claro + Entel** | `13_851` (Claro) · `GVM662` (Entel) | Av. J.J. Prieto (Ruta 5) N° 4260 esq. Salesianos (San Miguel) | Monoposte `30 m` | `2G / 3G / 4G / 5G` (**`850 / 1900 / 2600 / 3500 MHz` — B5/B2**) |
| **`495 m`** | **`5° (N)`** | **Entel + Claro** | `URS078 / GRS078 / EPCS3736` | Av. Club Hípico N° 3365, Pob. Magallanes (PAC) | Monoposte `12 m` | `2G / 3G / 4G / 5G` (**`1900 / 2600 / 3500 MHz` — Banda 2**) |
| **`553 m`** | **`250° (OSO)`** | **Claro** | `13_517` (*P.A.C.*) | Ángel Guarello esq. Félix Mendelssohn (PAC) | Monoposte `36 m` | `2G / 3G / 4G / 5G` (**`850 / 1900 / 2600 / 3500 MHz` — B5/B2**) |
| **`573 m`** | **`212° (SSO)`** | **WOM** | `RM3502` | Av. Club Hípico N° 4811 (PAC) | Monoposte `12 m` | `3G / 4G / 5G` (**`AWS 1700/2100 MHz` — Banda 4**) |
| **`684 m`** | **`241° (OSO)`** | **Entel + Movistar + Claro** | `MSA614` (Entel) · `MRNC1` (Movistar) · `43_687` (Claro) | Av. La Marina N° 2725 (PAC) | Monoposte `25–30 m` | `2G / 3G / 4G / 5G` (**`1900 / 2600 / 3500 MHz` — Banda 2**) |
| **`726 m`** | **`160° (SSE)`** | **Entel + Movistar + Claro** | `USA803` (Entel) · `INA2U` (Movistar) · `13_938` (Claro) | Av. José Joaquín Prieto N° 4850 (San Miguel) | Torre `30 m` | `2G / 3G / 4G / 5G` (**`850 / 1900 / 2600 / 3500 MHz` — B5/B2**) |

3. **Conclusión de Ingeniería RF a partir del Catastro SUBTEL:**
   - **Por qué la Antena Exterior `Omni Plus (314422)` (`360°`) del kit `weBoost Office 200 (531047)` es ideal:** Las estaciones base rodean el Centro Consistorial en **3 sectores acimutales opuestos**: **Oeste/Suroeste (`235°–259°`, a `163–346 m`)**, **Norte (`5°–14°`, a `332–495 m`)** y **Este/Sureste hacia Ruta 5 (`110°–160°`, a `460–726 m`)**. Una sola antena direccional apuntando a un sector dejaría fuera a las operadoras ubicadas en los otros cuadrantes; la **Omni Plus `314422`** capta los `360°` simultáneamente.
   - **Calce 100 % de Frecuencias con el `weBoost Office 200 LATAM (SKU 531047)`:**
     - **`Banda 5 (850 MHz)`** del `Office 200` amplifica directamente la voz/3G/4G de **Movistar** (`MVS_3G850_Centro`) y **Claro** (`13_517` / `13_851` en `850 MHz`).
     - **`Banda 4 (1700/2100 MHz AWS)`** del `Office 200` amplifica directamente **WOM** (`RM3519` a `253 m` y `RM4114` a `332 m`, que operan íntegramente en `AWS`).
     - **`Banda 25/2 (1900 MHz PCS)`** del `Office 200` amplifica directamente **Entel** (`UZM482` a `346 m` y `URS078` a `495 m` en `1900 MHz`), **Movistar** (`1900 MHz`) y **Claro** (`1900 MHz`).
   - **Mitigación del Efecto Cercano-Lejano (*Near-Far*):** Como Claro (`163 m`) y WOM (`253 m`) están muy cerca del edificio, la función **XDR (eXtended Dynamic Range)** del `weBoost Office 200` evita que el amplificador se apague por sobrecarga. Si se requiriera ajuste independiente por acimut, el escalamiento natural es el **`WilsonPro Enterprise 4300R`** con **3 antenas direccionales LPDA (Multi-Tower Targeting)** apuntando a `259° O` (Parque Jarlán/Teresa Vial), `5° N` (Club Hípico 3365) y `110° ESE` (Ruta 5 esq. Salesianos).

---

## 1. Preparación antes de salir (Oficina Tecnovoa)

- [ ] Confirmar cita con **Álvaro Carreño** (`alvarocarreno@pedroaguirrecerda.cl`, `+569 9442 7478`) e informar que asistes con tu **Prevencionista de Riesgos**.
- [ ] Solicitar autorización previa para subir a la **azotea/cubierta por escalera Eje N–P** e ingresar a la **Sala de Racks (Nivel 1, Eje P–Q)** y **oficinas Nivel -1**.
- [ ] Preparar **4 SIM activas con minutos de voz** (Entel, Movistar, Claro, WOM) y teléfonos con batería al 100 % + Power Bank.
- [ ] Configurar herramienta de medición en el teléfono:
  - **Android:** App **G-NetTrack Pro** o menú de ingeniería: Samsung `*#0011#`, Android genérico `*#*#4636#*#*`, Xiaomi `*#*#6484#*#*`, Motorola `*#*#2486#*#*`.
  - **iPhone:** *Field Test Mode* marcando `*3001#12345#*` (`LTE -> Serving Cell Meas -> rsrp0, rsrq, sinr, band`).
- [ ] Llevar kit de terreno: huincha láser (para validar que el tramo Azotea → Amplificador sea `< 18,28 m` y el tramo Amplificador → Antena Domo sea `< 22,86 m`), linterna, EPP completo y tablet/celular con https://crdiazu.github.io/analizador-celular-pac/ abierto.

---

## 2. Protocolo de Seguridad en Terreno (Lidera Prevencionista)

- [ ] **Registro y Charla Inicial:** Anunciarse en recepción (Acceso Principal por Av. Presidente Salvador Allende 2029, Ejes A–D), coordinar con el encargado de seguridad/prevención municipal y elaborar **AST (Análisis Seguro de Trabajo)**.
- [ ] **EPP obligatorio para inspección técnica:** Casco con barbiquejo (especialmente al revisar shafts, cielo falso y azotea), calzado de seguridad dieléctrico, chaleco reflectante (para zona de estacionamientos y rampa Ejes U–W) y linterna.
- [ ] **Inspección de Azotea / Cubierta (Eje N–P):**
  - Verificar altura de barandas/parapetos perimetrales y punto para fijar el mástil de la **Antena Omni Plus (`314422`)** y la puesta a tierra del **Protector de Relámpagos (`859902`)**. No acercarse a menos de 2 m del borde sin protección contra caídas.
- [ ] **Inspección de Nivel -1 (Cota `-3,20 m`) y Salas Técnicas:**
  - Identificar vías de evacuación verticales: **Escalera Eje N–P**, **Escalera Exterior Patio Inglés (Ejes L–N)** y **Escalera Dirección de Tránsito (Ejes B–C)**.
  - **Protocolo en zona sin cobertura:** Mantenerse siempre en dupla (Comercial + Prevencionista) y avisar a Informática la hora de subida a cubierta y bajada a estacionamientos/archivo.
  - Al abrir shafts de corrientes débiles (`GI 07`, `GI 08`) o revisar sobre cielo americano (`h = 2,60 m`), usar escalera certificada y verificar ausencia de cables energizados expuestos.

---

## 3. Reconocimiento Técnico-Comercial para Instalación `weBoost Office 200 (531047)`

- [ ] **Azotea (Punto Donante `P1` - Eje P–Q):**
  - Verificar despeje 360° para la **Antena Omni Plus (`314422`)** incluida en el kit `531047`.
  - Medir en `P1` que las bandas **B2 (`1900 MHz`), B4 (`AWS 1700/2100 MHz`) y B5 (`850 MHz`)** tengan buena relación señal/ruido (`SINR > 5 dB` y `RSRP > -90 dBm`), evitando contaminación de pilotos.
- [ ] **Validación de Largo de los Cables `Wilson400` Incluidos en el Kit:**
  - **Cable 1 (`952360` = `18,28 m`):** Medir desde el mástil en Azotea (`P1`), pasando por el protector de sobretensión (`859902` + jumper `0,60 m` `952302`) y bajando por el Shaft `GI 07/08` hasta la ubicación del amplificador `Office 200` (en `Sala Racks Nivel 1` o en `Bodega TI Nivel -1`).
  - **Cable 2 (`952375` = `22,86 m`):** Medir desde la salida del amplificador `Office 200` hasta el punto central del cielo falso en el Nivel -1 (**Eje R**, entre `2 Técnicos Informática` y `Jefe Informática / Emergencia`) donde irá la **Antena Domo de Perfil Bajo (`314407`)**.
- [ ] **Evaluación de Tabiques y Necesidad de Splitter Adicional:**
  - Revisar material de los tabiques entre **RR.PP. (`Ejes S–T`)**, **Informática/Emergencia (`Ejes Q–S`)** e **Inventario/Archivo (`Ejes K–P`)** y anotar si basta con la **Antena Domo `314407`** incluida o si conviene agregar un **Splitter 50 Ω de 2 vías + 1 Antena Domo adicional**.

---

## 4. Procedimiento de Medición en Cada Punto (4 Compañías)

En cada uno de los puntos `P0` a `P8` definidos en la plantilla:
1. Posicionarse y **esperar 30 a 45 segundos** sin mover el equipo (para estabilizar el filtrado de capa 3 del módem y evitar *body loss* manteniendo el teléfono separado del cuerpo).
2. Anotar por cada operador (**Entel, Movistar, Claro, WOM**):
   - **Tecnología:** 4G LTE / 4G+ / 3G / 2G / 5G NR / Sin Servicio.
   - **Banda y Canal:** Ej. `B2 (1900)`, `B4 (AWS)`, `B5 (850)`, `B28 (700)` + `PCI`.
   - **Métricas RF:** `RSRP` (dBm), `RSRQ` (dB) y `SINR` (dB).
3. **Prueba activa de Voz (QoE — foco principal del cliente):**
   - Realizar una llamada de prueba de **30 a 45 segundos** y calificar en escala MOS subjetiva (`1` a `5`):
     - `5` = Voz nítida, conecta rápido (`<3 s`), sin cortes.
     - `4` = Buena, leve compresión pero conversación fluida.
     - `3` = Entrecortada / robótica, cuesta entender.
     - `2` = Se corta la voz, demora mucho en conectar o cae a 2G/3G inestable.
     - `1` = No conecta llamada / Se cae la llamada (*Call Drop*) / Sin Servicio.

---

# 5. Plantilla de Registro en Terreno

## A. Ficha General de la Visita

| Campo | Detalle |
| :--- | :--- |
| **Fecha y Hora de Inicio / Término** | |
| **Cliente / Recinto** | Ilustre Municipalidad de Pedro Aguirre Cerda (Centro Consistorial) |
| **Dirección** | Av. Presidente Salvador Allende N° 2029 (esq. Manuela Errázuriz y Vassari), PAC |
| **Contraparte Cliente** | **Álvaro O. Carreño Cerda** — Jefe Depto. de Informática (SECPLA) · `+569 9442 7478` · `22 396 5042 / 5043 / 5044` · `alvarocarreno@pedroaguirrecerda.cl` |
| **Equipo Tecnovoa** | **Comercial:** Cristián Díaz (`cristian@tecnovoa.cl`, `+569 4943 8288`) · **Prevencionista:** ______________________ |
| **Solución Principal Evaluada** | **weBoost Office 200 LATAM (`SKU 531047`, 50 Ω)** — `74 dB` ganancia, bandas `B5 (850) / B4 (AWS) / B2 (1900)`, Antena Omni Plus `314422` + Antena Domo `314407` + `41,74 m` cable `Wilson400`. |
| **Modelos de Teléfonos de Prueba** | |

---

## B. Matriz de Mediciones por Punto Estructural (Pre-Mapeada según Planos)

> **Estructura CSV compatible con la Web App:**  
> `punto,nivel,eje_plano,recinto,compania,tecnologia,banda_mhz,pci,rsrp_dbm,rsrq_db,sinr_db,llamada_conecta,calidad_voz_1a5,call_drop,observaciones`

| Punto | Nivel / Cota | Ejes en Plano | Recinto / Ubicación Exacta | Operador | Tec. (4G/3G) | Banda (B2/B4/B5/B28) | RSRP (dBm) | RSRQ (dB) | SINR (dB) | ¿Conecta Llamada? (S/N) | Calidad Voz (1–5) | ¿Se cayó? (S/N) | Obs. / Captura |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Entel | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Movistar | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Claro | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | WOM | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Omni Plus `314422`)* | Entel | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Omni Plus `314422`)* | Movistar | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Omni Plus `314422`)* | Claro | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Omni Plus `314422`)* | WOM | | | | | | | | | |
| **P2** | Nivel 1 (`+0,45 m`) | **Ejes P–Q / 14–15** | **Sala Racks y Central Servidores** (junto a `GI 07` y `GI 08`) | Entel | | | | | | | | | |
| **P2** | Nivel 1 (`+0,45 m`) | **Ejes P–Q / 14–15** | **Sala Racks y Central Servidores** (junto a `GI 07` y `GI 08`) | Movistar | | | | | | | | | |
| **P2** | Nivel 1 (`+0,45 m`) | **Ejes P–Q / 14–15** | **Sala Racks y Central Servidores** (junto a `GI 07` y `GI 08`) | Claro | | | | | | | | | |
| **P2** | Nivel 1 (`+0,45 m`) | **Ejes P–Q / 14–15** | **Sala Racks y Central Servidores** (junto a `GI 07` y `GI 08`) | WOM | | | | | | | | | |
| **P3** | Nivel -1 (`-3,20 m`) | **Ejes L–N / Patio** | **Patio Inglés Hundido** (pie de escalera exterior hacia zócalo) | Entel | | | | | | | | | |
| **P3** | Nivel -1 (`-3,20 m`) | **Ejes L–N / Patio** | **Patio Inglés Hundido** (pie de escalera exterior hacia zócalo) | Movistar | | | | | | | | | |
| **P3** | Nivel -1 (`-3,20 m`) | **Ejes L–N / Patio** | **Patio Inglés Hundido** (pie de escalera exterior hacia zócalo) | Claro | | | | | | | | | |
| **P3** | Nivel -1 (`-3,20 m`) | **Ejes L–N / Patio** | **Patio Inglés Hundido** (pie de escalera exterior hacia zócalo) | WOM | | | | | | | | | |
| **P4** | Nivel -1 (`-3,20 m`) | **Ejes P–Q (Corte D-D')** | **Hall Subterráneo / Salida Ascensor y Escalera** | Entel | | | | | | | | | |
| **P4** | Nivel -1 (`-3,20 m`) | **Ejes P–Q (Corte D-D')** | **Hall Subterráneo / Salida Ascensor y Escalera** | Movistar | | | | | | | | | |
| **P4** | Nivel -1 (`-3,20 m`) | **Ejes P–Q (Corte D-D')** | **Hall Subterráneo / Salida Ascensor y Escalera** | Claro | | | | | | | | | |
| **P4** | Nivel -1 (`-3,20 m`) | **Ejes P–Q (Corte D-D')** | **Hall Subterráneo / Salida Ascensor y Escalera** | WOM | | | | | | | | | |
| **P5** | Nivel -1 (`-3,20 m`) | **Ejes Q–R (Corte D-D')** | **Oficina 2 Técnicos Informática y Bodega** *(Zona Crítica 1)* | Entel | | | | | | | | | |
| **P5** | Nivel -1 (`-3,20 m`) | **Ejes Q–R (Corte D-D')** | **Oficina 2 Técnicos Informática y Bodega** *(Zona Crítica 1)* | Movistar | | | | | | | | | |
| **P5** | Nivel -1 (`-3,20 m`) | **Ejes Q–R (Corte D-D')** | **Oficina 2 Técnicos Informática y Bodega** *(Zona Crítica 1)* | Claro | | | | | | | | | |
| **P5** | Nivel -1 (`-3,20 m`) | **Ejes Q–R (Corte D-D')** | **Oficina 2 Técnicos Informática y Bodega** *(Zona Crítica 1)* | WOM | | | | | | | | | |
| **P6** | Nivel -1 (`-3,20 m`) | **Ejes R–S (Corte D-D')** | **Oficina Jefe Informática (Álvaro Carreño) y Jefatura Emergencia** *(Zona Crítica 2)* | Entel | | | | | | | | | |
| **P6** | Nivel -1 (`-3,20 m`) | **Ejes R–S (Corte D-D')** | **Oficina Jefe Informática (Álvaro Carreño) y Jefatura Emergencia** *(Zona Crítica 2)* | Movistar | | | | | | | | | |
| **P6** | Nivel -1 (`-3,20 m`) | **Ejes R–S (Corte D-D')** | **Oficina Jefe Informática (Álvaro Carreño) y Jefatura Emergencia** *(Zona Crítica 2)* | Claro | | | | | | | | | |
| **P6** | Nivel -1 (`-3,20 m`) | **Ejes R–S (Corte D-D')** | **Oficina Jefe Informática (Álvaro Carreño) y Jefatura Emergencia** *(Zona Crítica 2)* | WOM | | | | | | | | | |
| **P7** | Nivel -1 (`-3,20 m`) | **Ejes S–T (Corte D-D')** | **Oficinas Relaciones Públicas (Jefatura + 2 Profesionales)** *(Zona Crítica 3)* | Entel | | | | | | | | | |
| **P7** | Nivel -1 (`-3,20 m`) | **Ejes S–T (Corte D-D')** | **Oficinas Relaciones Públicas (Jefatura + 2 Profesionales)** *(Zona Crítica 3)* | Movistar | | | | | | | | | |
| **P7** | Nivel -1 (`-3,20 m`) | **Ejes S–T (Corte D-D')** | **Oficinas Relaciones Públicas (Jefatura + 2 Profesionales)** *(Zona Crítica 3)* | Claro | | | | | | | | | |
| **P7** | Nivel -1 (`-3,20 m`) | **Ejes S–T (Corte D-D')** | **Oficinas Relaciones Públicas (Jefatura + 2 Profesionales)** *(Zona Crítica 3)* | WOM | | | | | | | | | |
| **P8** | Nivel -1 (`-3,20 m`) | **Ejes K–P (Corte D-D')** | **Archivo Municipal e Inventario** (fondo enterrado) | Entel | | | | | | | | | |
| **P8** | Nivel -1 (`-3,20 m`) | **Ejes K–P (Corte D-D')** | **Archivo Municipal e Inventario** (fondo enterrado) | Movistar | | | | | | | | | |
| **P8** | Nivel -1 (`-3,20 m`) | **Ejes K–P (Corte D-D')** | **Archivo Municipal e Inventario** (fondo enterrado) | Claro | | | | | | | | | |
| **P8** | Nivel -1 (`-3,20 m`) | **Ejes K–P (Corte D-D')** | **Archivo Municipal e Inventario** (fondo enterrado) | WOM | | | | | | | | | |

---

## C. Resumen Ejecutivo por Operador (en Nivel -1: Puntos P4 a P8)

| Operador | Banda Compatible `Office 200` (B2/B4/B5) | RSRP en Azotea (P1) | RSRP Promedio en Nivel -1 (P5–P6) | ¿Conecta Voz hoy en Informática (P5–P6)? | RSRP Proyectado con `weBoost Office 200` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Entel** | B2 (`1900`) / B4 (`AWS`) | | | | |
| **Movistar** | B5 (`850`) / B2 (`1900`) | | | | |
| **Claro** | B5 (`850`) / B2 (`1900`) / B4 (`AWS`) | | | | |
| **WOM** | B4 (`AWS 1700/2100`) | | | | |

---

## D. Levantamiento de Ingeniería para Instalación (`weBoost Office 200 SKU 531047`)

| Parámetro de Instalación | Medición / Observación en Terreno |
| :--- | :--- |
| **Cantidad exacta de usuarios en Piso -1** | Confirmado >10 por correo; desglosar cuántos en Informática, Emergencia, RR.PP. y Archivo: ________ |
| **Operador(es) de los teléfonos municipales** | ¿Tienen convenio con una telco específica o usan las 4?: ______________________ |
| **Punto de fijación Antena Omni Plus `314422` (Azotea Eje P–Q)** | ¿Mástil existente, baranda o soporte en caseta de escalera?: ______________________ |
| **Tierra física para Protector de Relámpagos `859902`** | ¿Existe barra de tierra débil/eléctrica en azotea o en Shaft `GI 07/08`?: ______________________ |
| **Tramo 1 Coaxial (Azotea `P1` → Amplificador)** | Medido: ______ m *(¿Alcanza con el rollo incluido `952360` de `18,28 m`?: [ ] Sí · [ ] No)* |
| **Tramo 2 Coaxial (Amplificador → Antena Domo `314407`)** | Medido: ______ m *(¿Alcanza con el rollo incluido `952375` de `22,86 m`?: [ ] Sí · [ ] No)* |
| **Disponibilidad de ducto en Shaft `GI 07` / `GI 08` (Eje P–Q)** | ¿Pasa cable `Wilson400` + conector N-Macho (~16 mm) o requiere crimpear en sitio?: ______________________ |
| **Ubicación del Chasis `Office 200` (`36,2 × 27,3 × 5,7 cm`) y 220V (`20 W`)** | [ ] Sala Racks Nivel 1 (`Eje P–Q`) · [ ] Bodega/Oficina TI Nivel -1 (`Eje Q–R`) |
| **Configuración de Antenas Indoor recomendada** | [ ] Kit base 1 Antena Domo `314407` (`Eje R`) · [ ] Agregar Splitter 50 Ω 2 vías + 2ª Antena Domo (`Eje S / Eje O`) |
| **Observaciones del Prevencionista (Permisos, trabajo en altura, horarios)** | ______________________ |

---

## E. Firmas de Conformidad de Visita Técnica

**Por Tecnovoa (Comercial):** ___________________________  
**Por Tecnovoa (Prevencionista):** ___________________________  
**Por Municipalidad de PAC (Informática):** ___________________________
