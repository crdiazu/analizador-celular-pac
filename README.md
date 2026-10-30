# Optimización de Cobertura Celular Indoor y Conectividad Outdoor — Municipalidad de Pedro Aguirre Cerda

Repositorio de ingeniería de radiofrecuencia y aplicación web interactiva para el diagnóstico de cobertura móvil (4G LTE / VoLTE / 3G — Voz) y diseño de la solución **Wilson Connectivity (`2× weBoost Office 200 LATAM SKU 531047` + `4 Antenas Domo Interiores`)** en el **Piso -1 (Zócalo Subterráneo)** y **Piso 1 (Óvalo del Alcalde / Sala de Concejo Municipal)** del Centro Consistorial de la **Ilustre Municipalidad de Pedro Aguirre Cerda** (`Av. Presidente Salvador Allende N° 2029`).

- **Presentación Ejecutiva de Ingeniería:** [https://crdiazu.github.io/analizador-celular-pac/presentacion.html](https://crdiazu.github.io/analizador-celular-pac/presentacion.html)
- **Plataforma Web Interactiva 3D:** [https://crdiazu.github.io/analizador-celular-pac/](https://crdiazu.github.io/analizador-celular-pac/)
- **Integrador TI:** **Tecnovoa Ltda.** (`www.tecnovoa.cl`) — Av. Pedro de Valdivia N° 273, Providencia, Santiago.
- **Equipo de Proyecto Tecnovoa:** Cristián Díaz (KAM TI | `cristian@tecnovoa.cl` | +569 4943 8288), Javier De la Fuente y Diego Pérez (Ingeniería).
- **Contraparte Técnica Municipal:** Álvaro O. Carreño Cerda — Jefe Departamento de Informática (`SECPLA`).
- **Operadores Soportados:** Entel, Movistar, Claro y WOM.

---

## 1. Diagnóstico en Terreno (Visita Técnica 29 de Octubre de 2026)

El Centro Consistorial de Pedro Aguirre Cerda cuenta con **100% de cobertura exterior declarada en 3G, 4G y 5G** en las 4 compañías de telefonía móvil según el Geoportal Oficial de la **SUBTEL** (`licancabur.subtel.gob.cl`).

Sin embargo, tras el levantamiento técnico en sitio se identificaron las siguientes zonas críticas con **sombra de radiofrecuencia severa** (niveles RSRP inferiores a `-110 dBm` por atenuación de losas de hormigón armado):

1. **Planta Tipo "U" en Piso -1 (`cota -3,20 m`):**
   - **Sector Norte (Zona 3):** Video Wall, Dirección de Seguridad Ciudadana y Despacho de Móviles.
   - **Sector Poniente (Zona 2):** Servicios Especiales (bajo acceso principal).
   - **Sector Sur-Oriente (Zona 1):** Oficina Jefe de Informática (Álvaro Carreño), Técnicos TI y Pasillo Trasero.
2. **Piso 1 — Óvalo del Alcalde / Sala de Concejo Municipal:**
   - Volumen central ovalado donde se requiere garantizar continuidad de voz y datos móviles durante sesiones municipales.

---

## 2. Arquitectura Maestra Propuesta: `2× weBoost Office 200 LATAM (SKU 531047)` + `4 Antenas Domo`

Aprovechando que el edificio cuenta en ambos extremos de la techumbre con **postes metálicos existentes de `3,5 metros`** y salas de racks en los pisos `-1`, `1` y `2`, se diseña una arquitectura simétrica de **2 sistemas amplificadores independientes de `50 Ohm`**:

### 🔴 Sistema 1 — Hub Norte / Poniente (Rack Seguridad Piso -1)
- **Antena Donante #1 (`Omni Plus 314422`):** Montada en poste de `3,5 m` de la Techumbre Norte con protector de sobretensión (`859902`) y bajada coaxial de `18,28 m` (`952360`) hasta el **Rack de Seguridad (-1)**.
- **Amplificador `Office 200 #1` + Splitter 2 Vías (`859957`):**
  - **Domo 1A (`314407` en Piso -1 Norte):** Con el rollo incluido de `22,86 m` (`952375`) cubre **Video Wall, Seguridad Ciudadana y Despacho de Móviles**.
  - **Domo 1B (`314407` en Piso -1 Poniente):** Con un rollo adicional de `15,24 m` (`952350`) cubre **Servicios Especiales (Ala Poniente)**.

### 🟢 Sistema 2 — Hub Sur / Oriente (Rack Piso 1 & Piso -1)
- **Antena Donante #2 (`Omni Plus 314422`):** Montada en poste de `3,5 m` de la Techumbre Sur con bajada coaxial de `18,28 m` (`952360`) hasta el núcleo sur junto al puente del Óvalo.
- **Amplificador `Office 200 #2` + Splitter 2 Vías (`859957`):**
  - **Domo 2A (`314407` en Piso 1):** Con un rollo adicional de `15,24 m` (`952350`) cruza la pasarela peatonal para iluminar el **Óvalo del Alcalde / Sala de Concejo Municipal**.
  - **Domo 2B (`314407` en Piso -1 Sur-Oriente):** Con el rollo incluido de `22,86 m` (`952375`) baja al Piso -1 para cubrir la **Oficina de Álvaro Carreño (Informática)** y el **Pasillo Trasero**.

---

## 3. Cuadro Consolidado de Equipamiento (BOM Técnico)

| Ítem | SKU Wilson | Descripción Técnica | Cant. (1 Ala) | Cant. (Solución 2 Alas) |
| :---: | :---: | :--- | :---: | :---: |
| **01** | `531047` | **Kit Amplificador weBoost Office 200 LATAM (50 Ω)** (Incluye Amplificador 74 dB, 1 Antena Omni Plus `314422`, 1 Antena Domo `314407`, Protector `859902`, Jumper `0,60 m`, Cable `18,28 m` y Cable `22,86 m`) | 1 Kit | **2 Kits** |
| **02** | `859957` | **Splitter Pasivo de 2 Vías Wideband (698–2700 MHz, 50 Ω, -3 dB)** | 1 un. | **2 un.** |
| **03** | `314407` | **Antena Interior Domo de Perfil Bajo Adicional (50 Ω, N-Hembra)** | 1 un. | **2 un.** |
| **04** | `952350` | **Cable Coaxial Baja Pérdida Wilson400 de 50 ft / 15,24 m (N-Macho)** | 1 rollo | **2 rollos** |
| **05** | `952302` | **Jumper Coaxial Wilson400 de 2 ft / 0,60 m (N-Macho)** | 1 un. | **2 un.** |

---

## 4. Contacto de Ingeniería y Preventa

**Tecnovoa Tecnología & Servicios Ltda.**  
- **KAM TI:** Cristián Díaz (`cristian@tecnovoa.cl` | +569 4943 8288)  
- **Dirección:** Av. Pedro de Valdivia N° 273, Providencia, Santiago  
- **Web:** [www.tecnovoa.cl](https://www.tecnovoa.cl/)
