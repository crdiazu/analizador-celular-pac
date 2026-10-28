# Presentación Ejecutiva: Solución Integral de Cobertura Celular Indoor
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda (Centro Consistorial)  
**Atención:** **Álvaro O. Carreño Cerda** — Jefe Depto. de Informática (SECPLA)  
**Empresa Proponente:** **Tecnovoa Ltda.** (`www.tecnovoa.cl` — Pedro de Valdivia #273, Providencia)  
**Presentado por:** **Cristián Díaz** — KAM TI (`cristian@tecnovoa.cl` / `+569 4943 8288`)  
**Fecha:** Octubre 2026  
**Solución Principal:** **weBoost Office 200 LATAM (SKU 531047)** — `CLP$ 1.650.898 + IVA`  
**Web App del Proyecto en Vivo:** [https://crdiazu.github.io/analizador-celular-pac/](https://crdiazu.github.io/analizador-celular-pac/)  

---

## 🏢 1. Diagnóstico del Problema: ¿Por qué no hay señal en el Piso -1?

Muchos usuarios asumen que cuando no hay señal en un subterráneo, la culpa es de las compañías telefónicas (Entel, Movistar, Claro o WOM). **La evidencia oficial demuestra exactamente lo contrario:**

1. **Afuera en la calle y azotea, la cobertura es excelente (100% verificada ante SUBTEL):**
   * El Centro Consistorial está rodeado por **10 estaciones base celulares en un radio menor a 750 metros**.
   * La torre más cercana de Claro (`43_691`) está a solo **`271 metros`** por Club Hípico; WOM (`RM3519`) está a **`365 metros`** y Entel/Movistar (`UZM482`) a **`457 metros`**.
   * En la azotea técnica (`+8,25 m`) medimos niveles óptimos de señal: **`-68 a -74 dBm`** en 4G LTE y 5G con una alta pureza de señal (`SINR > 12 dB`).
2. **El origen físico del fallo es el apantallamiento estructural (Jaula de Faraday):**
   * El Departamento de Informática, Emergencia, Relaciones Públicas y Archivo operan en la cota **`-3,20 metros` bajo nivel de calle**.
   * Para que las microondas celulares lleguen a sus escritorios, deben atravesar **dos losas macizas de hormigón armado de 25 cm de espesor con doble malla de fierro**, además de vidrios Low-E y muros de contención.
   * Esto genera una **atenuación mayor a 35 dB**, hundiendo la señal por debajo de los **`-112 dBm`**.
   * **Consecuencia directa:** Cortes inmediatos de llamadas (*Call Drop*), llamadas que ni siquiera timbran, audio robótico ininteligible y drenaje acelerado de la batería de los celulares.

---

## 📡 2. La Solución Propuesta: weBoost Office 200 LATAM (SKU 531047)

Para resolver este aislamiento sin depender de que las telcos instalen costosas antenas micro-celdas, Tecnovoa implementa el sistema de amplificación celular profesional **weBoost Office 200 LATAM**, fabricado por **Wilson Electronics** (líder mundial en tecnología in-building con más de 20 años en el mercado):

```
       [Azotea Municipal: +8,25 m]
  📡 Antena Exterior Omni Plus (314422) 360°
                 │
                 │ Cable Wilson400 (baja pérdida) por Shaft GI 07/08
                 ▼
       [Sala Racks / Subterráneo]
  ⚡ Amplificador Office 200 LATAM (74 dB Ganancia / Pantalla LCD)
                 │
                 │ Cable Wilson400 por cielo falso
                 ▼
       [Pasillo Informática / Eje R: -3,20 m]
  📶 Antena Interior Domo de Perfil Bajo (314407)
     └──> Cobertura uniforme para Álvaro Carreño, Técnicos, Emergencia y RR.PP.
```

### ¿Por qué este modelo específico es el indicado para el Centro Consistorial?
* **100% Compatible con las 4 Compañías en Chile:** Opera nativamente en **Banda 5 (850 MHz)** para Movistar y Claro, **Banda 4 (AWS 1700/2100 MHz)** para WOM y Entel, y **Banda 2 (1900 MHz PCS)** para Entel, Movistar y Claro. Cubre voz en HD (VoLTE) y datos móviles 4G simultáneamente.
* **Ganancia Profesional de 74 dB y Potencia Downlink de +22 dBm:** Entrega hasta **`4.300 m²`** de cobertura en planta abierta, compensando con holgura los 35 dB de pérdida de las losas.
* **Tecnología Patentada XDR (*eXtended Dynamic Range*):** A diferencia de repetidores chinos o genéricos que se apagan cuando una torre cercana emite con mucha fuerza, el Office 200 ajusta su ganancia en microsegundos sin apagarse jamás.
* **Antena Exterior Omni Plus 360° (`314422`):** Dado que las torres de Entel, Movistar, Claro y WOM rodean al municipio en distintos ángulos (Poniente, Norte y Oriente), una antena direccional dejaría operadores fuera. La Omni Plus capta todos los operadores a la vez.

---

## ⚖️ 3. Comparativa: weBoost Office 200 vs. Otras Alternativas

| Criterio de Decisión | Solución weBoost Office 200 LATAM | Alternativa: "Wi-Fi Calling" (VoWi-Fi Municipal) | Alternativa: Repetidores Genéricos de Internet |
| :--- | :--- | :--- | :--- |
| **¿Quién puede usarlo?** | **Todos:** Cualquier funcionario, vecino o visita que entre al Piso -1 (Entel, Movistar, Claro o WOM). | Solo funcionarios que tengan la clave Wi-Fi municipal y celulares con VoWi-Fi configurado. | No garantizan soporte de bandas chilenas ni multi-operador. |
| **Impacto en la red LAN municipal** | **Cero impacto:** Es una red de RF autónoma. No usa ancho de banda, switches ni IPs municipales. | Consume ancho de banda del enlace de internet y satura los Access Points de Informática. | Nulo, pero genera interferencia radioeléctrica. |
| **Llamadas y SMS tradicionales** | **100% transparente:** Llamadas de voz normales, SMS de autenticación bancaria y claves token. | Muchas apps y bancos no envían SMS sobre Wi-Fi puro si no hay portadora celular. | Inestable. |
| **Cumplimiento SUBTEL** | **100% legal:** Homologado con corte anti-oscilación y auto-standby (Res. Ex. N° 737). | N/A | **Ilegal:** Genera ruido hacia las torres de las telcos y arriesga multas e incautación de SUBTEL. |
| **Costo Total** | **CLP\$ 1.650.898 + IVA (Pago único).** | Requiere renovar APs, licencias de controladora Wi-Fi y soporte permanente. | Barato inicialmente, pero falla en pocas semanas. |

---

## 🛠️ 4. Plan de Implementación No Invasivo

1. **Uso de Infraestructura Existente:** La bajada coaxial aprovecha el **Shaft vertical de corrientes débiles `GI 07/08` (Ejes N–P)**, por lo que **no se realizan perforaciones en losas ni roturas de hormigón**.
2. **Cero Impacto Estético:** En el subterráneo, el cableado corre oculto sobre el cielo americano desmontable (`h = 2,60 m`). La antena interior domo queda mimetizada a nivel de cielo falso.
3. **Puesta a Tierra y Protección Eléctrica:** El kit incluye protector de sobretensiones a gas conectado a la tierra del edificio, protegiendo los equipos ante tormentas.
4. **Tiempo de Ejecución:** Una vez adjudicado, la instalación y comisionamiento se realiza en **1 sola jornada de trabajo (1 día)**, sin interrumpir las labores de los funcionarios.

---

## 💼 5. Respaldo y Garantía Tecnovoa

* **3 Años de Garantía de Fábrica** en el amplificador Wilson weBoost.
* **Soporte Técnico Local Certificado:** Ingenieros de Tecnovoa disponibles para post-venta, calibración y mediciones de verificación post-instalación.
* **Respaldo en Terreno:** Medición previa con instrumental profesional (G-NetTrack y modelamiento 3D) que certifica el antes y el después de la señal en cada escritorio municipal.

---

*Tecnovoa Ltda. — Conectividad e Infraestructura de Telecomunicaciones*  
*Pedro de Valdivia #273, Providencia | www.tecnovoa.cl | cristian@tecnovoa.cl*
