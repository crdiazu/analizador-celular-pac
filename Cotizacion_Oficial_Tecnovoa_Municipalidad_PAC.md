# Propuesta Técnica de Ingeniería: Solución Integral de Cobertura Celular Indoor y Red en Techumbre
**Documento en Evaluación Conjunta con Área Técnica e Ingeniería — Sin Valorizar**

| Datos del Integrador | Datos de la Institución |
| :--- | :--- |
| **Razón Social:** Tecnovoa Ltda. | **Razón Social:** Ilustre Municipalidad de Pedro Aguirre Cerda |
| **RUT:** 76.842.190-K | **RUT:** 69.254.800-4 |
| **Dirección:** Av. Pedro de Valdivia N° 273, Providencia, Santiago | **Dirección:** Av. Presidente Salvador Allende N° 2029, PAC |
| **Contacto Comercial:** Cristián Díaz — KAM TI (`cristian@tecnovoa.cl`) | **Atención:** **Álvaro O. Carreño Cerda** — Jefe Depto. Informática (SECPLA) |
| **Ingeniería de Terreno y Preventa:** Javier De la Fuente & Diego Pérez | **Fecha de Actualización:** 30 de Octubre de 2026 |

---

## 🎯 1. Alcance Técnico del Proyecto
Suministro, instalación, canalización y puesta en marcha de una solución de amplificación celular in-building multibanda (Entel, Movistar, Claro y WOM) para cubrir al 100% las dependencias del **Piso -1 (Zócalo Subterráneo: Video Wall, Seguridad Ciudadana, Despacho de Móviles, Servicios Especiales, Jefatura de Informática y Pasillo Trasero)** y la **Sala de Concejo Municipal / Óvalo del Alcalde (Piso 1)**.

*(Nota: Los requerimientos de red exterior para drones y telemetría en techumbre se gestionan de manera independiente en el documento complementario correspondiente).*

---

## 📡 2. Detalle de Equipamiento de Radiofrecuencia (Configuración 1 Ala vs. 2 Alas)

### Configuración por 1 Ala (1 Amplificador + 2 Antenas Domo Interiores)

| Ítem | SKU Wilson | Descripción Técnica del Componente | Cantidad |
| :---: | :---: | :--- | :---: |
| **1** | `531047` | **Kit Amplificador Celular weBoost Office 200 LATAM (50 Ω)**<br>• 1 Amplificador Office 200 LATAM (74 dB ganancia, +22 dBm Downlink, pantalla LCD, XDR)<br>• 1 Antena Exterior Omni Plus 360° (SKU 314422)<br>• 1 Antena Interior Domo de Perfil Bajo (SKU 314407)<br>• 1 Protector de Sobretensión de Rayos 50 Ω (SKU 859902)<br>• 1 Jumper Wilson400 0,60 m (SKU 952302)<br>• 1 Cable Wilson400 18,28 m (SKU 952360) para bajada desde poste de techumbre<br>• 1 Cable Wilson400 22,86 m (SKU 952375) para rama interior larga | 1 set |
| **2** | `859957` | **Splitter Pasivo de 2 Vías Wideband 50 Ω (698–2700 MHz, -3 dB)** | 1 un. |
| **3** | `314407` | **Segunda Antena Interior Domo de Perfil Bajo (50 Ω, N-Hembra)** | 1 un. |
| **4** | `952350` | **Cable Coaxial Adicional Wilson400 (15,24 m / 50 ft, N-Macho)** | 1 rollo |
| **5** | `952302` | **Jumper Coaxial Adicional Wilson400 (0,60 m / 2 ft, N-Macho)** | 1 un. |

---

### Configuración Maestra 2 Alas Completa (2 Amplificadores + 4 Antenas Domo Interiores)
*Cubre el 100% de las zonas identificadas en la visita técnica: **Video Wall, Seguridad Ciudadana, Despacho de Móviles y Servicios Especiales** (Sistema 1 Norte) + **Óvalo del Alcalde / Sala de Concejo en Piso 1, Oficina de Álvaro Carreño y Pasillo Trasero en Piso -1** (Sistema 2 Sur).*

| Ítem | SKU Wilson | Descripción Técnica del Componente | Cantidad Total |
| :---: | :---: | :--- | :---: |
| **1** | `531047` | **Kit Amplificador Celular weBoost Office 200 LATAM (50 Ω)** | **2 sets** |
| **2** | `859957` | **Splitter Pasivo de 2 Vías Wideband 50 Ω (698–2700 MHz, -3 dB)** | **2 un.** |
| **3** | `314407` | **Antena Interior Domo de Perfil Bajo Adicional (50 Ω, N-Hembra)** *(Total 4 domos sumando los 2 de los kits)* | **2 un.** |
| **4** | `952350` | **Cable Coaxial Adicional Wilson400 (15,24 m / 50 ft, N-Macho)** | **2 rollos** |
| **5** | `952302` | **Jumper Coaxial Adicional Wilson400 (0,60 m / 2 ft, N-Macho)** | **2 un.** |

---

## 🌐 3. Partidas de Obras Civiles y Montaje RF (En Dimensionamiento por Área Técnica)

| Partida | Descripción de Ingeniería e Instalación | Estado |
| :---: | :--- | :---: |
| **I-01** | **Montaje e Instalación RF In-Building:** Fijación de 2 antenas donantes en los postes metálicos existentes de `3,5 m` en techumbre, canalización vertical por shaft hacia racks de Piso -1 y Piso 1, montaje de 2 amplificadores weBoost Office 200 + Splitters y tendido por escalerilla/cielo falso hacia los 4 domos interiores. | En cubicación por Área Técnica |
