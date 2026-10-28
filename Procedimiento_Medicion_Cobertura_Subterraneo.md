# Procedimiento y Plantilla de Terreno: Estudio de Cobertura Celular Indoor (Piso -1)
**Proyecto:** Optimización de Señal Móvil (Voz / 4 Operadores) — Solución Wilson Connectivity  
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda (Edificio Consistorial)  
**Integrador:** Tecnovoa (`cristian@tecnovoa.cl`) — KAM TI: Cristián Díaz + Prevencionista de Riesgos  

---

## 0. Hallazgos del Análisis de Planos Arquitectónicos (Pre-Visita)

A partir de los planos [Elevation-Sections-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/Elevation-Sections-001.jpg), [First_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/First_Floor_Plan-001.jpg) y [Second_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/Second_Floor_Plan-001.jpg), se identificó la geometría exacta del problema reportado por **Álvaro Carreño (Jefe Depto. Informática)**:

1. **Ubicación exacta de los usuarios en Piso -1 (Cota -3,20 m, altura libre 2,60 m):**
   En el **Corte D-D'** se observa que el propio **Departamento de Informática** y otras unidades municipales operan en el zócalo subterráneo (Nivel -1), distribuidos en módulos estructurales de **6,0 m entre ejes**:
   - **Ejes T–S (12 m):** *2 Profesionales Relaciones Públicas* y *Jefatura Relaciones Públicas*.
   - **Ejes S–R (6 m):** *Jefatura Emergencia* y ***Jefe Informática (oficina de Álvaro Carreño)***.
   - **Ejes R–Q (6 m):** *Bodega* y ***2 Técnicos Informática***.
   - **Ejes Q–P (6 m):** **Hall Subterráneo / Núcleo de Escalera y Ascensor** (acceso principal al Nivel -1).
   - **Ejes P–O (6 m):** *Encargado Archivo Municipal e Inventario* y *Bodega de Inventario*.
   - **Ejes O–K (~23 m):** *Archivo Municipal* (bajo losa maciza del patio central).
   - **Ejes A–N (Corte B-B' y C-C'):** *Estacionamientos subterráneos* (con rampa vehicular de acceso por el extremo oriente, Ejes U–W por calle Manuela Errázuriz).

2. **Causa física de la sombra radioeléctrica:**
   - Las oficinas del Nivel -1 están hundidas a **-3,20 m** respecto al nivel de acera (`N +-0,00`), confinadas por muros perimetrales de contención de hormigón armado, losas gruesas de hormigón y un **patio inglés hundido** (con escalera exterior en Ejes L–N) cuyos ventanales utilizan cristales con control solar (*Low-E*), los cuales atenúan entre 15 y 30 dB la señal celular exterior.

3. **Ruta óptima para cableado coaxial y antena donante (Eje P–Q):**
   - En [First_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/First_Floor_Plan-001.jpg) (Nivel 1, Ala Sur - DIDECO, **Eje P–Q**), exactamente encima del núcleo de Informática, se encuentra la sala **`RACKS Y CENTRAL SERVIDORES`** junto a los shafts verticales de corrientes débiles **`GI 07` y `GI 08`** (y en el Ala Norte, Registro Civil, **`GI 03` y `GI 04`**).
   - En el **Corte B-B'**, la caja de escalera en **Ejes N–P / P–Q** sube directamente hasta la **cubierta/azotea** (cota +8,25 m / caseta superior), lo que ofrece una vertical limpia para bajar desde la **antena donante exterior (Wilson Yagi/LPDA)** en azotea hasta el amplificador Wilson en el Nivel -1 (o en la Sala de Racks Nivel 1).

4. **Consideración crítica de bandas en Chile para el equipo Wilson ($1.650.898 + IVA):**
   - Para garantizar llamadas de voz en las 4 compañías (**Entel, Movistar, Claro y WOM**) para **>10 usuarios**, en terreno debemos verificar qué bandas dominan en el exterior/azotea:
     - **B2 (1900 MHz):** Entel, Movistar, Claro (Voz 2G/3G/4G VoLTE).
     - **B4 / B66 (AWS 1700/2100 MHz):** **WOM** (Voz 3G/4G VoLTE principal), Entel, Claro.
     - **B5 (850 MHz):** Movistar y Claro (3G/4G).
     - **B28 (700 MHz APT):** Entel, Movistar, Claro (*Atención:* los repetidores Wilson estándar FCC de EE.UU. traen B12/B13 de 700 MHz y **no amplifican B28**; por tanto, el amplificador trabajará sobre **B2 (1900), B4 (AWS) y B5 (850)**, por lo que hay que medir la potencia de esas 3 bandas en la azotea).

---

## 1. Preparación antes de salir (Oficina Tecnovoa)

- [ ] Confirmar cita con **Álvaro Carreño** (`alvarocarreno@pedroaguirrecerda.cl`, `+569 9442 7478`) e informar que asistes con tu **Prevencionista de Riesgos**.
- [ ] Solicitar autorización previa para subir a la **azotea/cubierta por escalera Eje N–P** e ingresar a la **Sala de Racks (Nivel 1, Eje P–Q)** y **oficinas Nivel -1**.
- [ ] Preparar **4 SIM activas con minutos de voz** (Entel, Movistar, Claro, WOM) y teléfonos con batería al 100 % + Power Bank.
- [ ] Configurar herramienta de medición en el teléfono:
  - **Android:** App **G-NetTrack Pro** (con [First_Floor_Plan-001.jpg](file:///c:/Users/Cristian/Obsidian/Cristian/CDU/PROYECTOS/Analizador%20de%20celular/First_Floor_Plan-001.jpg) cargado en modo *Floorplan* si se desea traza indoor) o menú de ingeniería: Samsung `*#0011#`, Android genérico `*#*#4636#*#*`, Xiaomi `*#*#6484#*#*`, Motorola `*#*#2486#*#*`.
  - **iPhone:** *Field Test Mode* marcando `*3001#12345#*` (revisar `LTE -> Serving Cell Meas -> rsrp0, rsrq, sinr, band`).
- [ ] Llevar kit de terreno: huincha láser (o cinta métrica) para medir distancia de coaxial desde azotea a Nivel -1, linterna, EPP completo y este documento impreso o en tablet.

---

## 2. Protocolo de Seguridad en Terreno (Lidera Prevencionista)

- [ ] **Registro y Charla Inicial:** Anunciarse en recepción (Acceso Principal por Av. Presidente Salvador Allende 2029, Ejes A–D), coordinar con el encargado de seguridad/prevención municipal y elaborar **AST (Análisis Seguro de Trabajo)**.
- [ ] **EPP obligatorio para inspección técnica:** Casco con barbiquejo (especialmente al revisar shafts, cielo falso y azotea), calzado de seguridad dieléctrico, chaleco reflectante (para zona de estacionamientos y rampa Ejes U–W) y linterna.
- [ ] **Inspección de Azotea / Cubierta (Eje N–P):**
  - Verificar altura de barandas/parapetos perimetrales (en planos se observa baranda en terraza transitable). No acercarse a menos de 2 m del borde sin protección contra caídas.
  - Identificar riesgos eléctricos o de tropiezo con equipos de clima (UMA/VRV en cubierta).
- [ ] **Inspección de Nivel -1 (Cota -3,20 m) y Salas Técnicas:**
  - Identificar vías de evacuación verticales: **Escalera Eje N–P**, **Escalera Exterior Patio Inglés (Ejes L–N)** y **Escalera Dirección de Tránsito (Ejes B–C)**.
  - **Protocolo en zona sin cobertura:** Mantenerse siempre en dupla (Comercial + Prevencionista) y avisar a Informática la hora de subida a cubierta y bajada a estacionamientos/archivo.
  - Al abrir shafts de corrientes débiles (`GI 07`, `GI 08`) o revisar sobre cielo americano (altura 2,60 m), usar escalera certificada y verificar ausencia de cables energizados expuestos.

---

## 3. Reconocimiento Técnico-Comercial para Instalación Wilson

- [ ] **Azotea (Punto Donante - Eje P–Q):** Buscar el punto con mejor vista hacia las antenas de las 4 telcos y medir distancia hasta el shaft `GI 07` / `GI 08` (ideal < 15–20 m de cable coaxial LMR-400 / Wilson400 para no perder más de 3–4 dB).
- [ ] **Paso vertical (Shafts Eje P–Q):** Verificar con Álvaro Carreño si existe ducto disponible o escalerilla portacables desde la azotea pasando por `Racks y Central Servidores` (Nivel 1, Eje P–Q) hasta el cielo del pasillo de Informática en Nivel -1.
- [ ] **Ubicación del Amplificador Wilson y Antena(s) Indoor (Nivel -1):**
  - Verificar enchufe 220V con respaldo UPS (idealmente en rack de Informática o Bodega Eje Q–R).
  - Evaluar el material de las divisiones entre las oficinas de Nivel -1 (Ejes O a T: ¿tabique liviano/vidrio o muro de hormigón?).
  - **Regla de diseño indoor:**
    - Si son tabiques livianos/vidrio, **1 antena panel o domo** en el eje Q–R o R–S puede cubrir los ~30 m lineales de Informática + Emergencia + RR.PP.
    - Si son muros gruesos de hormigón o si quieren cubrir también **Archivo (Ejes K–O)**, considerar un **splitter de 2 o 3 vías** con antenas domo distribuidas en Eje S (RR.PP./Emergencia), Eje R (Informática) y Eje O (Inventario/Archivo).
  - Verificar **aislamiento vertical/horizontal** entre la antena donante (azotea, cota +8,25 m) y las antenas indoor (cota -3,20 m): hay **>11 metros de diferencia vertical más 2 losas de hormigón armado**, lo que da un aislamiento excelente (>70 dB) y evita oscilación/feedback en el amplificador Wilson.

---

## 4. Procedimiento de Medición en Cada Punto (4 Compañías)

En cada uno de los puntos `P0` a `P8` definidos en la plantilla:
1. Posicionarse y **esperar 30 a 45 segundos** sin mover el equipo (para estabilizar el filtrado de capa 3 del módem y evitar *body loss* pegando el teléfono al cuerpo).
2. Anotar por cada operador (**Entel, Movistar, Claro, WOM**):
   - **Tecnología:** 4G LTE / 4G+ / 3G / 2G / 5G NR / Sin Servicio.
   - **Banda y Canal:** Ej. B2 (1900), B4/B66 (AWS), B5 (850), B28 (700) + PCI.
   - **Métricas RF:** `RSRP` (dBm), `RSRQ` (dB) y `SINR` (dB).
3. **Prueba activa de Voz (QoE — foco principal del cliente):**
   - Realizar una llamada de prueba de **30 a 45 segundos** y calificar en escala MOS subjetiva (1 a 5):
     - `5` = Voz nítida, conecta rápido (<3 s), sin cortes.
     - `4` = Buena, leve compresión pero conversación fluida.
     - `3` = Entrecortada / robótica, cuesta entender.
     - `2` = Se corta la voz, demora mucho en conectar o cae a 2G/3G inestable.
     - `1` = No conecta llamada / Se cae la llamada (*Call Drop*) / Sin Servicio.

### Escala de Referencia Rápida (3GPP LTE / 5G Sub-6)

| Clasificación | RSRP (Potencia) | RSRQ (Calidad) | SINR (Interferencia) | Comportamiento esperado en Voz (VoLTE) |
| :--- | :--- | :--- | :--- | :--- |
| **Excelente** | `>= -80 dBm` | `>= -10 dB` | `>= 20 dB` | Llamada HD instantánea, máxima estabilidad |
| **Buena** | `-80 a -90 dBm` | `-10 a -15 dB` | `13 a 20 dB` | Llamada estable y clara (objetivo post-instalación Wilson) |
| **Regular** | `-90 a -100 dBm` | `-15 a -20 dB` | `0 a 13 dB` | Voz aceptable, posibles microcortes al caminar |
| **Débil (Crítica)** | `-100 a -110 dBm` | `< -20 dB` | `< 0 dB` | Voz robótica, caída a 3G/2G, alto riesgo de corte |
| **Sin Cobertura** | `< -110 dBm` | `N/A` | `< -5 dB` | Llamadas fallidas, teléfono buscando red |

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
| **Objetivo del Cliente** | Mejorar calidad de llamadas de voz en **Piso -1** para **>10 usuarios** con teléfonos municipales (evaluación / prueba de solución Wilson Connectivity `$1.650.898 + IVA`). |
| **Modelos de Teléfonos de Prueba** | |

---

## B. Matriz de Mediciones por Punto Estructural (Pre-Mapeada según Planos)

> **Estructura para exportar a CSV (futura App):**  
> `punto,nivel,eje_plano,recinto,compania,tecnologia,banda_mhz,pci,rsrp_dbm,rsrq_db,sinr_db,llamada_conecta,calidad_voz_1a5,call_drop,observaciones`

| Punto | Nivel / Cota | Ejes en Plano | Recinto / Ubicación Exacta | Operador | Tec. (4G/3G) | Banda (B2/B4/B5/B28) | RSRP (dBm) | RSRQ (dB) | SINR (dB) | ¿Conecta Llamada? (S/N) | Calidad Voz (1–5) | ¿Se cayó? (S/N) | Obs. / Captura |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Entel | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Movistar | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | Claro | | | | | | | | | |
| **P0** | Nivel 1 (`+0,45 m`) | **Ejes A–D / 6–8** | **Acceso Principal** (Av. Salvador Allende, referencia calle) | WOM | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Exterior Wilson)* | Entel | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Exterior Wilson)* | Movistar | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Exterior Wilson)* | Claro | | | | | | | | | |
| **P1** | Azotea (`+8,25 m`) | **Ejes N–Q / 12–14** | **Cubierta sobre Escalera / Shaft GI 07-08** *(Punto Donante Antena Exterior Wilson)* | WOM | | | | | | | | | |
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

| Operador | Banda Donante en Azotea (P1) | RSRP en Azotea (P1) | RSRP Promedio en Nivel -1 (P5–P7) | ¿Conecta Voz hoy en Informática (P5–P6)? | Atenuación Azotea -> Nivel -1 (dB) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Entel** | | | | | |
| **Movistar** | | | | | |
| **Claro** | | | | | |
| **WOM** | | | | | |

---

## D. Levantamiento de Ingeniería para Instalación (Wilson Connectivity)

| Parámetro de Instalación | Medición / Observación en Terreno |
| :--- | :--- |
| **Cantidad exacta de usuarios en Piso -1** | Confirmado >10 por correo; desglosar cuántos en Informática, Emergencia, RR.PP. y Archivo: ________ |
| **Operador(es) de los teléfonos municipales** | ¿Tienen convenio con una telco específica o usan las 4?: ______________________ |
| **Punto de fijación Antena Donante (Azotea Eje P–Q)** | ¿Mástil existente, baranda o soporte en caseta de escalera?: ______________________ |
| **Metros lineales de coaxial (Azotea P1 -> Shaft GI 07/08 -> Nivel -1)** | Tramo vertical (~12 m) + tramos horizontales: ______ m totales |
| **Disponibilidad de ducto en Shaft `GI 07` / `GI 08` (Eje P–Q)** | ¿Pasa cable coaxial LMR-400 + conector N (~15 mm) o requiere canalización?: ______________________ |
| **Ubicación del Amplificador Wilson y toma 220V** | ______________________ |
| **Cantidad y tipo de Antenas Indoor requeridas** | [ ] 1 Antena Domo/Panel (pasillo Eje R) · [ ] 2 Antenas con Splitter (Eje R + Eje S/O) · [ ] 3 Antenas |
| **Material de tabiques entre oficinas Nivel -1 (Ejes O a T)** | [ ] Tabique volcanita/vidrio · [ ] Albañilería · [ ] Hormigón armado |
| **Observaciones del Prevencionista (Permisos, trabajo en altura, horarios)** | ______________________ |

---

## E. Firmas de Conformidad de Visita Técnica

**Por Tecnovoa (Comercial):** ___________________________  
**Por Tecnovoa (Prevencionista):** ___________________________  
**Por Municipalidad de PAC (Informática):** ___________________________

## E. Firmas de Conformidad de Visita Técnica

**Por Tecnovoa (Comercial):** ___________________________  
**Por Tecnovoa (Prevencionista):** ___________________________  
**Por Municipalidad de PAC (Informática):** ___________________________

