# Ficha de Especificaciones Técnicas: Sistema de Amplificación Celular In-Building
**Documento Técnico para Evaluación de Ingeniería — SECPLA / Depto. de Informática**  
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda  
**Unidad Requirente:** Departamento de Informática (SECPLA) — Álvaro Carreño Cerda  
**Integrador:** Tecnovoa Ltda. (`www.tecnovoa.cl`)  

---

## 📌 1. Nombre del Proyecto
```text
Suministro e Instalación de Sistema Dual de Amplificación de Señal Celular Multibanda In-Building para Piso -1 y Sala de Concejo Municipal (Piso 1)
```

## 📝 2. Descripción Técnica del Requerimiento
```text
Suministro e integración de sistema profesional de amplificación celular multibanda para interiores (in-building BDA), destinado a resolver el aislamiento radioeléctrico en las dependencias operativas del Piso -1 (Seguridad Ciudadana, Video Wall, Despacho de Móviles, Servicios Especiales, Informática y Pasillo Trasero) y en la Sala de Concejo Municipal (Óvalo Piso 1) del Centro Consistorial de la Municipalidad de Pedro Aguirre Cerda. El sistema opera de manera autónoma en 50 Ohms, amplificando simultáneamente voz (VoLTE/3G) y datos 4G de los operadores Entel, Movistar, Claro y WOM, en cumplimiento con la normativa técnica de SUBTEL.
```

## ⚙️ 3. Especificaciones Técnicas del Equipamiento (`weBoost Office 200 LATAM SKU 531047`)

1. **Bandas de Frecuencia Homologadas para Chile (Multi-Operador):**
   * **Banda 5 (850 MHz)** — Operadores Movistar y Claro.
   * **Banda 4 (AWS 1700/2100 MHz)** — Operadores WOM y Entel.
   * **Banda 2 / 25 (1900 MHz PCS)** — Operadores Entel, Movistar y Claro.
2. **Potencia, Ganancia e Impedancia:**
   * Ganancia máxima de cada amplificador: **74 dB**.
   * Potencia de salida Downlink: **Hasta +22 dBm**.
   * Impedancia característica del sistema: **50 Ohms** con conectores profesionales tipo **N-Hembra**.
3. **Control Automático y Protección:**
   * Sistema de Control Automático de Ganancia (AGC) y tecnología de rango dinámico extendido (**XDR**) para evitar apagados por saturación ante torres celulares cercanas.
   * Sistema de corte automático anti-oscilación en cumplimiento de la normativa SUBTEL (Resolución Exenta N° 737).
   * Pantalla táctil LCD a color para diagnóstico y monitoreo en tiempo real de cada banda.
4. **Configuración de Antenas y Distribución Coaxial (Solución Completa 2 Alas):**
   * **2 Amplificadores weBoost Office 200 LATAM (`SKU 531047`)**.
   * **2 Antenas Exteriores Omnidireccionales 360° (`SKU 314422`)** montadas en los postes existentes de `3,5 m` en ambos extremos de la techumbre.
   * **2 Protectores contra descargas atmosféricas (`SKU 859902`)** de 50 Ω.
   * **2 Splitters Pasivos de 2 Vías Wideband (`SKU 859957`, 698–2700 MHz, 50 Ω)**.
   * **4 Antenas Interiores Tipo Domo de Perfil Bajo (`SKU 314407`, 50 Ω)** para montaje en cielo falso.
   * **Cableado Coaxial `Wilson400` de Ultra Baja Pérdida (50 Ω):**
     * 2 tramos de `18,28 m` (`SKU 952360`) para bajadas desde techumbre.
     * 2 tramos de `22,86 m` (`SKU 952375`) para ramas principales interiores.
     * 2 tramos de `15,24 m` (`SKU 952350`) para ramas secundarias interiores.
     * 4 jumpers de `0,60 m` (`SKU 952302`) para interconexión de protectores y splitters.
