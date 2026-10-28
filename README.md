# Analizador de Cobertura Celular Indoor — Proyecto Municipalidad de Pedro Aguirre Cerda

Repositorio técnico-comercial para el levantamiento, diagnóstico de cobertura móvil (4G LTE / 5G NR / 3G / 2G — Voz) y diseño de solución de amplificación indoor (**Wilson Connectivity**) en el **Piso -1 (Zócalo / Subterráneo)** del Centro Consistorial de la **Ilustre Municipalidad de Pedro Aguirre Cerda** (`Av. Presidente Salvador Allende N° 2029`).

- **Integrador:** Tecnovoa (`www.tecnovoa.cl`) — KAM TI: Cristián Díaz (`cristian@tecnovoa.cl`)
- **Contraparte Cliente:** Álvaro O. Carreño Cerda — Jefe Departamento de Informática (`SECPLA`)
- **Operadores evaluados:** Entel, Movistar, Claro y WOM.

---

## Estructura del Repositorio

- [`Procedimiento_Medicion_Cobertura_Subterraneo.md`](./Procedimiento_Medicion_Cobertura_Subterraneo.md): Procedimiento completo de terreno (Comercial + Prevencionista de Riesgos), hallazgos del análisis de planos arquitectónicos, protocolo de seguridad y plantilla de registro.
- [`plantilla_mediciones_pac.csv`](./plantilla_mediciones_pac.csv): Matriz pre-cargada con los **9 puntos estructurales (`P0` a `P8`) × 4 compañías** lista para abrir en Excel/Sheets en terreno o importar en la futura app de análisis.
- **Planos Arquitectónicos (GMM Arquitectos):**
  - [`Elevation-Sections-001.jpg`](./Elevation-Sections-001.jpg): Cortes `A-A'` a `E-E'` (incluye el **Corte D-D'** donde se identifican las oficinas del Nivel -1: *Jefe Informática*, *2 Técnicos Informática*, *Jefatura Emergencia*, *Relaciones Públicas* y *Archivo e Inventario*).
  - [`First_Floor_Plan-001.jpg`](./First_Floor_Plan-001.jpg): Planta Nivel 1 (incluye ubicación de `Racks y Central Servidores` y shafts verticales `GI 07` y `GI 08` en el **Eje P–Q**).
  - [`Second_Floor_Plan-001.jpg`](./Second_Floor_Plan-001.jpg): Planta Nivel 2 (proyección vertical de shafts y núcleo de escalera hacia cubierta/azotea).
- **Documentación y Manuales de Referencia RF:**
  - [`G-NetTrack_Pro_manual.pdf`](./G-NetTrack_Pro_manual.pdf): Manual oficial de G-NetTrack Pro para levantamiento indoor (`Floorplan`) y registro de métricas.
  - [`notebooklm-sources-2026-10-28/`](./notebooklm-sources-2026-10-28/): Compendio técnico sobre métricas 3GPP (`RSRP`, `RSRQ`, `SINR`, `RSSI`), códigos MMI/Field Test Mode en Android e iOS y umbrales de señal.

---

## Resumen de Puntos de Medición (`P0` a `P8`)

| Punto | Nivel / Cota | Ejes en Plano | Recinto / Ubicación | Rol en el Estudio |
| :--- | :--- | :--- | :--- | :--- |
| **P0** | Nivel 1 (`+0,45 m`) | Ejes A–D / 6–8 | Acceso Principal (Av. Salvador Allende) | Referencia a nivel de calle |
| **P1** | Azotea (`+8,25 m`) | Ejes N–Q / 12–14 | Cubierta sobre Escalera / Shaft `GI 07-08` | **Punto Donante Antena Exterior Wilson** |
| **P2** | Nivel 1 (`+0,45 m`) | Ejes P–Q / 14–15 | Sala Racks y Central Servidores (`GI 07-08`) | Paso vertical de coaxial |
| **P3** | Nivel -1 (`-3,20 m`) | Ejes L–N / Patio | Patio Inglés Hundido (pie de escalera) | Medición de difracción exterior hacia zócalo |
| **P4** | Nivel -1 (`-3,20 m`) | Ejes P–Q (Corte D-D') | Hall Subterráneo / Salida Ascensor y Escalera | Transición al Nivel -1 |
| **P5** | Nivel -1 (`-3,20 m`) | Ejes Q–R (Corte D-D') | Oficina 2 Técnicos Informática y Bodega | **Zona Crítica 1 (Usuarios TI)** |
| **P6** | Nivel -1 (`-3,20 m`) | Ejes R–S (Corte D-D') | Oficina Jefe Informática y Jefatura Emergencia | **Zona Crítica 2 (Álvaro Carreño + Emergencia)** |
| **P7** | Nivel -1 (`-3,20 m`) | Ejes S–T (Corte D-D') | Oficinas Relaciones Públicas (Jefatura + 2 Prof.) | **Zona Crítica 3 (Usuarios RR.PP.)** |
| **P8** | Nivel -1 (`-3,20 m`) | Ejes K–P (Corte D-D') | Archivo Municipal e Inventario | Fondo confinado bajo losa |
