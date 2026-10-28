# Optimización de Cobertura Celular Indoor — Municipalidad de Pedro Aguirre Cerda

Repositorio técnico-comercial y aplicación web de ingeniería para el levantamiento de terreno, diagnóstico de cobertura móvil (4G LTE / 5G / 3G — Voz) y dimensionamiento de la solución BDA **Wilson Connectivity (`weBoost Office 200 LATAM SKU 531047`)** en el **Piso -1 (cota `-3,20 m`)** del Centro Consistorial de la **Ilustre Municipalidad de Pedro Aguirre Cerda** (`Av. Presidente Salvador Allende N° 2029`).

- **Plataforma Web Interactiva (GitHub Pages):** https://crdiazu.github.io/analizador-celular-pac/
- **Integrador TI:** **Tecnovoa Ltda.** (`www.tecnovoa.cl`) — Pedro de Valdivia #273, Providencia, Santiago.
- **Responsable Comercial / Preventa:** Cristián Díaz, KAM TI (+569 4943 8288 | `cristian@tecnovoa.cl`).
- **Contraparte Técnica:** Álvaro O. Carreño Cerda — Jefe Departamento de Informática (`SECPLA`), Municipalidad de Pedro Aguirre Cerda.
- **Operadores Evaluados:** Entel, Movistar, Claro y WOM.

---

## 1. Alcance y Diagnóstico del Problema

El Centro Consistorial de Pedro Aguirre Cerda (obra de *GMM Arquitectos*) cuenta con **100% de cobertura exterior declarada en 3G, 4G y 5G** en las 4 compañías de telefonía móvil según el Geoportal Oficial de la **SUBTEL** (`licancabur.subtel.gob.cl`).

Sin embargo, las dependencias ubicadas en el **Subterráneo Nivel -1 (`cota -3,20 m`)** presentan una condición de **sombra de radiofrecuencia severa** con niveles RSRP inferiores a `-110 dBm` (sin servicio / corte inmediato de llamadas), producto de:
1. **Dos losas macizas de hormigón armado** entre el nivel de calle y el subterráneo (atenuación acumulada superior a `32 dB`).
2. Muros perimetrales de contención enterrados y ventanales con perfilería metálica y cristales térmicos Low-E en el patio inglés.
3. Dependencias afectadas:
   - **Oficina Jefe de Informática (Álvaro Carreño)** y **Jefatura de Emergencia** (`Ejes R-S · Punto P6`).
   - **Oficina 2 Técnicos de Informática y Bodega TI** (`Ejes Q-R · Punto P5`).
   - **Relaciones Públicas** (`Ejes S-T · Punto P7`).
   - **Archivo Municipal e Inventario** (`Ejes K-P · Punto P8`).
   - **Hall Subterráneo y Salida de Ascensores** (`Ejes P-Q · Punto P4`).

---

## 2. Solución Cotizada: `weBoost Office 200 LATAM (SKU 531047)`

- **Precio Referencial:** **CLP$ 1.650.898 + IVA** (Entrega desde 48 horas post orden de compra).
- **Ganancia del Sistema:** **`74 dB`** con tecnología patentada **XDR (eXtended Dynamic Range)** que previene auto-oscilaciones y sobrecargas de señal.
- **Impedancia Profesional:** **`50 Ohm`** con conectores N-Hembra y cables coaxiales de ultra baja pérdida **`Wilson400`**.
- **Bandas Homologadas SUBTEL Chile:**
  - Banda 5 (`850 MHz`) — Movistar y Claro.
  - Banda 4 AWS (`1700/2100 MHz`) — WOM y Entel.
  - Banda 25/2 PCS (`1900 MHz`) — Entel, Movistar y Claro.
- **Topología de Instalación:**
  1. **Antena Donante Exterior (`Omni Plus 314422`):** Montada en mástil sobre la azotea (`+8,25 m`) en el Eje P-Q, recibiendo en 360° las torres celulares circundantes de las 4 compañías.
  2. **Protector de Relámpago (`859902`):** Aterrizado a la malla de tierra física de la caseta de azotea.
  3. **Bajada Vertical Coaxial `Wilson400` (18,28 m):** A través del **Shaft de Corrientes Débiles `GI 07/08`** pasando junto a la Sala de Racks del Nivel 1.
  4. **Amplificador `Office 200`:** Montado en rack o sobre cielo falso en el Nivel -1.
  5. **Antena Servidora Interior (`Domo 314407`):** Embutida en cielo falso en el pasillo de Informática (`Eje R`), irradiando en 360° hacia Informática, Emergencia y RR.PP.

---

## 3. Características de la Aplicación Web Tecnovoa (`index.html`)

La plataforma web interactiva cuenta con las siguientes secciones:

1. **Plano 3D Interactivo del Edificio (Three.js):**
   - Modelado arquitectónico tridimensional volumétrico a escala basado en los planos de *GMM Arquitectos*.
   - **Modo Rayos-X:** Oculta los niveles 1 y 2 para inspeccionar el interior del Subterráneo Nivel -1, las oficinas de Informática y la cúpula de radiación RF.
   - **Modo Edificio Completo y Vista Explotada:** Separa los niveles verticalmente para entender la bajada coaxial.
   - Esferas 3D interactivas para los puntos de medición `P0` a `P8`, coloreadas dinámicamente según RSRP.
   - Botón simulador **`Amplificador Wilson: ON/OFF`** que demuestra la recuperación de señal desde `-111 dBm` (Rojo) hasta `-78 dBm` (Verde).
2. **Galería Fotográfica de Terreno (20 Fotografías de Alta Resolución):**
   - Registro visual exhaustivo del edificio clasificado por zonas: Patio Central Cívico, Patio Hundido hacia Nivel -1, Escaleras de Hormigón, Volumen Oval de Sala de Concejo en Acero Corten, Acceso Principal y Galerías.
   - Visor modal con ficha técnica de impacto en propagación RF para cada foto.
3. **Radar y Catastro de Antenas SUBTEL (GIS):**
   - Gráfico polar de las 10 radiobases más cercanas en un radio menor a 750 m (`T1` a `T10`), detallando azimut, distancia, operadoras (Entel, Movistar, Claro, WOM), códigos de estación y calce de bandas.
4. **Visor de Planos Arquitectónicos 2D:**
   - Visualización directa de los planos originales de arquitectura (`Elevation-Sections-001.jpg`, `First_Floor_Plan-001.jpg`, `Second_Floor_Plan-001.jpg`).
5. **Calculadora de Presupuesto de Enlace (Link Budget 50 Ω):**
   - Cálculo en tiempo real de pérdidas por tramo de cable `Wilson400` por frecuencia (850, 1900, 2100 MHz) y verificación de aislamiento anti-oscilación exigido por SUBTEL ($I_{\text{mín}} > G + 15\text{ dB} = 89\text{ dB}$).
6. **Exportación e Importación CSV:**
   - Permite descargar la matriz completa de mediciones para trabajo de campo y reimportarla para actualizar el modelo.

---

## 4. Estructura de Archivos del Proyecto

```text
├── index.html                                   # Aplicación web interactiva Tecnovoa (Three.js + Radar + Galería)
├── README.md                                    # Documento técnico principal
├── Procedimiento_Medicion_Cobertura_Subterraneo.md # Protocolo de visita comercial y prevención de riesgos
├── mediciones_pac_terreno1.csv                  # Matriz de mediciones de campo (P0 a P8 x 4 compañías)
├── 531047-530047_office200_ss_LATAM_102721b (1).pdf # Ficha técnica oficial weBoost Office 200 LATAM
├── Elevation-Sections-001.jpg                   # Plano original de cortes D-D' y E-E' (GMM Arquitectos)
├── First_Floor_Plan-001.jpg                     # Plano original Planta Nivel 1
├── Second_Floor_Plan-001.jpg                    # Plano original Planta Nivel 2
├── assets/
│   ├── logo-tecnovoa.png                        # Logo corporativo Tecnovoa
│   ├── favicon-tecnovoa.png                     # Favicon Tecnovoa
│   └── fotos/                                   # 20 fotos del Centro Consistorial clasificadas
│       ├── 01-patio-central-nucleo-escalera.png
│       ├── 02-patio-hundido-volumen-corten.png
│       ├── 03-escalera-interior-hacia-nivel-1.png
│       ├── ...
│       └── 20-patio-hundido-fachada-nivel-1.png
```

---

## 5. Contacto Comercial e Ingeniería

**Tecnovoa Tecnología & Servicios**  
- **KAM TI:** Cristián Díaz  
- **Teléfono / WhatsApp:** +569 4943 8288  
- **Email:** [cristian@tecnovoa.cl](mailto:cristian@tecnovoa.cl)  
- **Dirección:** Pedro de Valdivia #273, Providencia, Santiago  
- **Web:** [www.tecnovoa.cl](https://www.tecnovoa.cl/)

---

## 5. Contacto Comercial e Ingeniería

**Tecnovoa Tecnología & Servicios**  
- **KAM TI:** Cristián Díaz  
- **Teléfono / WhatsApp:** +569 4943 8288  
- **Email:** [cristian@tecnovoa.cl](mailto:cristian@tecnovoa.cl)  
- **Dirección:** Pedro de Valdivia #273, Providencia, Santiago  
- **Web:** [www.tecnovoa.cl](https://www.tecnovoa.cl/)

