# Presentación Ejecutiva: Solución Integral de Cobertura Celular Indoor y Red en Techumbre
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda (Centro Consistorial)  
**Atención:** **Álvaro O. Carreño Cerda** — Jefe Depto. de Informática (SECPLA)  
**Empresa Proponente:** **Tecnovoa Ltda.** (`www.tecnovoa.cl` — Pedro de Valdivia #273, Providencia)  
**Equipo de Proyecto:** Cristián Díaz (KAM TI), Javier De la Fuente y Diego Pérez (Ingeniería)  
**Fecha:** Octubre 2026  
**Presentación Web Interactiva:** [https://crdiazu.github.io/analizador-celular-pac/presentacion.html](https://crdiazu.github.io/analizador-celular-pac/presentacion.html)  

---

## 🏢 1. Diagnóstico en Terreno: ¿Por qué se requiere una Arquitectura Dual?

Durante la visita técnica realizada el **29 de octubre de 2026** junto a Álvaro Carreño, se verificaron en terreno las condiciones arquitectónicas y operativas del Centro Consistorial:

1. **Planta Subterránea Tipo "U" (Piso -1) y Sala de Concejo (Piso 1):**
   * El nivel `-1` presenta una distribución perimetral en forma de "U" alrededor del patio central y casino, superando los `85 metros` de recorrido longitudinal, además de divisiones de hormigón armado que atenúan la señal celular en más de `35 dB`.
   * Las áreas críticas a iluminar comprenden:
     * **Ala Norte (Piso -1):** Video Wall, Seguridad Ciudadana y Despacho de Móviles.
     * **Ala Poniente (Piso -1):** Servicios Especiales.
     * **Ala Sur-Oriente (Piso -1):** Oficina de Álvaro Carreño (Jefatura de Informática), Técnicos TI y Pasillo Trasero.
     * **Volumen Central (Piso 1):** Sala de Concejo Municipal / Óvalo del Alcalde.
2. **Infraestructura Existente Favorable:**
   * En ambos extremos de la techumbre (Norte y Sur) existen **postes metálicos de `3,5 metros` de altura** listos para soportar las antenas donantes omnidireccionales.
   * Existen salas de racks de comunicaciones en **Piso -1 (Dirección de Seguridad)**, **Piso 1 (Recepciones Comunitarias)** y **Piso 2 (SecPlan)**.

---

## 📡 2. Solución de Ingeniería: 2 Sistemas `weBoost Office 200 LATAM` + 4 Antenas Domo

Para garantizar una señal potente y uniforme sin pérdidas excesivas en cable coaxial, se diseña una configuración simétrica con **2 amplificadores `weBoost Office 200 LATAM (SKU 531047, 50 Ω)`**, cada uno alimentando **2 antenas interiores tipo Domo (`314407`)** a través de un **Splitter Pasivo de 2 Vías (`859957`)**:

```text
SISTEMA 1 (HUB NORTE - RACK SEGURIDAD PISO -1)
  📡 Antena Omni Plus #1 (Poste 3,5 m Techumbre Norte)
       │  Cable Wilson400 18,28 m (952360) + Protector Rayos (859902)
       ▼
  ⚡ Amplificador weBoost Office 200 #1 (74 dB) ──► Splitter 2 Vías (859957)
       ├──► [Cable 22,86 m incluido] ──► 🔵 Domo 1A (Piso -1): Video Wall, Seguridad Ciudadana y Despacho Móviles
       └──► [Cable 15,24 m extra]    ──► 🔵 Domo 1B (Piso -1): Servicios Especiales (Ala Poniente)

SISTEMA 2 (HUB SUR - RACK PISO 1 / SHAFT SUR)
  📡 Antena Omni Plus #2 (Poste 3,5 m Techumbre Sur)
       │  Cable Wilson400 18,28 m (952360) + Protector Rayos (859902)
       ▼
  ⚡ Amplificador weBoost Office 200 #2 (74 dB) ──► Splitter 2 Vías (859957)
       ├──► [Cable 15,24 m extra]    ──► 🟢 Domo 2A (Piso 1):  Óvalo del Alcalde / Sala de Concejo Municipal
       └──► [Cable 22,86 m incluido] ──► 🟢 Domo 2B (Piso -1): Oficina Álvaro Carreño (TI) y Pasillo Trasero
```

---

## 🚁 3. Conectividad en Techumbre: Helipuerto de Drones y Estación Meteorológica

Como requerimiento complementario levantado en la visita técnica, Tecnovoa contempla:
1. **2 Puntos de Red Cat.6 Exterior** en el sector de techumbre, canalizados desde el Rack SecPlan (Piso 2) o Rack Seguridad (Piso -1).
2. **1 Access Point Cisco Meraki Outdoor**, integrable al portal de administración (Dashboard) de la Municipalidad, para proveer conectividad Wi-Fi de alta estabilidad a la operación de drones de Seguridad Comunal y a la estación meteorológica en azotea.

---

*Tecnovoa Ltda. — Conectividad e Infraestructura de Telecomunicaciones*  
*Av. Pedro de Valdivia N° 273, Providencia | www.tecnovoa.cl | cristian@tecnovoa.cl*
