# Guía Operativa de Terreno: Detección y Mapeo de Zonas Sin Señal (Dead Zones) con G-NetTrack en Android
**Documento Técnico de Ejecución — Walk Test & Auditoría RF Indoor**  
**Proyecto:** Solución de Cobertura Celular Wilson Connectivity (`weBoost Office 200 LATAM SKU 531047`)  
**Preparado por:** Cristián Díaz — KAM TI Tecnovoa Ltda. (`cristian@tecnovoa.cl` / `+569 4943 8288`)  
**Plataforma Web de Soporte:** [https://crdiazu.github.io/analizador-celular-pac/](https://crdiazu.github.io/analizador-celular-pac/)  
**Fecha de Aplicación:** Octubre 2026 / Actualizado para pruebas de terreno  

---

## 🎯 Objetivo de la Misión de Terreno: "Caza de Zonas Muertas"
El objetivo principal de esta medición **no es registrar señal bonita en la calle**, sino **identificar, geolocalizar y cuantificar exactamente dónde se corta la señal, dónde caen las llamadas y qué zonas del edificio quedan aisladas comunicacionalmente**.

Con este registro técnico se fundamenta la necesidad técnica y económica de instalar el amplificador celular **weBoost Office 200 LATAM**, demostrando ante la jefatura del cliente:
1. Que **afuera y en azotea hay excelente señal** (las torres de Entel, Movistar, Claro y WOM funcionan al 100 %).
2. Que **dentro del edificio y subterráneo hay un apagón de radiofrecuencia (atenuación > 30 dB)** por losas y hormigón.
3. El **punto exacto donde colocar la antena donante exterior (en azotea)** y la **antena servidora domo interior (en subterráneo)**.

---

## 📱 1. Configuración Previa del Teléfono Android (Antes de Salir)
*Basado en los hallazgos del log previo de prueba (`Movistar_2026.10.19_15.51.11.txt`), para evitar pérdida de datos, cold-starts y saltos de muestreo.*

### A. Desactivar Optimización de Batería (¡Paso Crítico!)
En Android, el sistema congela apps en segundo plano para ahorrar energía, provocando baches de 15 a 20 segundos sin datos:
1. Ve a **Ajustes > Aplicaciones > G-NetTrack (o G-NetTrack Pro)**.
2. Pulsa en **Batería** (o Uso de batería).
3. Selecciona **"Sin restricciones"** (o "No optimizar" / "Permitir actividad en segundo plano").
4. Desactiva temporalmente el "Modo de ahorro de batería" general de Android.

### B. Ajustes Internos en la App G-NetTrack
Abre G-NetTrack y entra a **Settings (Ajustes)**:
1. **Log Interval (Intervalo de Registro):**
   - Configúralo en **`1 segundo`** (para registrar con alta resolución cada paso del recorrido).
2. **Min Distance (Distancia Mínima):**
   - Configúralo en **`0 metros`** (o 1 m) para que registre incluso si estás detenido en una oficina o rincón midiendo señal estática.
3. **Log Format / Parámetros extendidos:**
   - Asegúrate de tener activada la casilla para registrar **Serving Cell**, **PCI**, **Cell ID**, **TAC/LAC**, **RSRP**, **RSRQ** y **SINR / SNR**.
4. **Auto Start GPS:** Activo.
5. **Keep Screen On (Mantener pantalla encendida):** **ACTIVADO** (evita que el SO entre en deep-sleep al caminar).

### C. Bloqueo de GPS Previo (Evitar el Cold-Start de 2 Minutos)
- Al llegar a las inmediaciones del edificio, **abre G-NetTrack en la calle a cielo abierto**.
- Espera entre **60 y 90 segundos** hasta que las coordenadas no muestren `--` y el icono de GPS se ponga en color verde (precisión `< 5 metros`).
- **No inicies la grabación indoor hasta que el GPS esté enganchado**.

---

## 🏢 2. ¿Cómo Medir Indoor / Subterráneo si el GPS se Pierde?
En recintos cerrados y subterráneos (Nivel -1), **la señal satelital GPS se bloquea completamente** por las losas de hormigón. Si dependes solo del GPS automático, todos los puntos interiores quedarán con `--` o pegados en la puerta de entrada.

### La Solución: Uso de Marcadores Manuales (`Filemark` / Eventos)
G-NetTrack cuenta con un botón en pantalla llamado **"Filemark"** (o menú `Filemark / Marker`).
Cada vez que llegues a un punto clave del edificio:
1. Detén tu marcha en el punto exacto.
2. Presiona **Filemark** y escribe el identificador de la zona (ej. `P4_HALL_S1`, `P5_TI`, `P6_ALVARO`, `P8_ARCHIVO`).
3. Permanece en el punto **30 segundos inmóvil** sosteniendo el teléfono en la mano (sin tapar las antenas traseras del móvil).
4. El log de G-NetTrack grabará una línea con el campo `Filemark` etiquetado, permitiendo cruzar de inmediato la fila del TXT con el plano arquitectónico.

---

## 🗺️ 3. Ruta Estratégica de "Caza de Zonas Muertas"
*Recorrido sugerido paso a paso para documentar el contraste de señal (desde la fuente exterior hasta el fondo del apagón):*

```
[EXTERIOR / AZOTEA]           [PLANTA ACCESO]               [SUBTERRÁNEO NIVEL -1]
     P1 (Azotea)  ────────►   P0 (Calle / Fachada) ───►     P4 (Hall Subterráneo)
    RSRP: -70 dBm              RSRP: -76 dBm                 RSRP: -98 dBm
     Señal Donante              Transición exterior           Inicio zona sombría
                                                                    │
                                                                    ▼
                                                            P5 (Técnicos TI)
                                                             RSRP: -108 dBm
                                                             Borde de desconexión
                                                                    │
                                                                    ▼
                                                            P6 (Oficina Álvaro Carreño)
                                                             RSRP: -114 dBm
                                                             🔴 ZONA MUERTA / DROP CALL
                                                                    │
                                                                    ▼
                                                            P8 (Archivo Municipal)
                                                             RSRP: -120 dBm / Sin Servicio
                                                             🔴 APAGÓN TOTAL
```

### Detalle de Puntos a Recorrer:

| Punto | Recinto / Ubicación | Qué esperas encontrar | Acción en G-NetTrack |
| :---: | :--- | :--- | :--- |
| **P0** | **Acceso Principal Exterior** (Calle) | 5G / 4G con RSRP de -70 a -80 dBm. Señal limpia de torre directa. | Enganchar GPS en verde. Marcar `P0_ACCESO_EXT`. |
| **P1** | **Azotea / Cubierta Técnica** (Punto Donante) | RSRP excelente (-65 a -75 dBm), SINR > 10 dB. Es el punto donde irá la antena exterior. | Marcar `P1_AZOTEA_DONANTE`. Tomar foto panorámica 360°. |
| **P2** | **Sala de Racks / Servidores** (Nivel 1) | Señal media atenuada por muros perimetrales (-85 a -95 dBm). | Marcar `P2_RACKS_N1`. Verificar espacio para amplificador. |
| **P3** | **Patio Inglés Hundido** (Zócalo Exterior) | Primera caída por sombra del edificio (-90 a -100 dBm). | Marcar `P3_PATIO_INGLES`. |
| **P4** | **Hall Subterráneo / Núcleo Escalera** (Nivel -1) | Transición crítica: el teléfono intenta saltar de 5G a 4G Band 2/5 (-98 a -104 dBm). | Marcar `P4_HALL_S1`. Observar si parpadea el icono de red. |
| **P5** | **Oficina Técnicos de Informática / Bodega** | **Inicio de Zona Crítica:** RSRP < -105 dBm. La voz se robotiza. | Marcar `P5_TI_TECNICOS`. Hacer llamada de prueba de 30 s. |
| **P6** | **Oficina Jefe Informática (Álvaro Carreño)** | **ZONA MUERTA CLAVE:** RSRP < -110 dBm, SINR < 0 dB. Llamadas se caen o no entran. | Marcar `P6_OF_ALVARO`. Marcar llamada: si se corta, anotar "DROP CALL". |
| **P7** | **Oficinas Relaciones Públicas** | Zona con sombra profunda hacia el ala oriente (-108 a -116 dBm). | Marcar `P7_RRPP`. Probar envío de WhatsApp de audio. |
| **P8** | **Archivo Municipal / Fondo Enterrado** | **APAGÓN COMPLETO:** RSRP < -120 dBm o "Solo Llamadas de Emergencia / Sin Servicio". | Marcar `P8_ARCHIVO_FONDO`. Esperar 45 s y registrar pérdida de portadora. |

---

## 📊 4. Semáforo Técnico de Calidad de Señal (Umbrales 3GPP y Subtel)
Utiliza esta escala oficial para clasificar instantáneamente el estado de cada recinto durante la caminata:

| Estado Semáforo | RSRP (Potencia Señal) | SINR (Relación Señal/Ruido) | Experiencia Real de Usuario (QoE) | Acción Requerida |
| :---: | :---: | :---: | :--- | :--- |
| 🟢 **Excelente** | `> -80 dBm` | `> 12 dB` | 5G / 4G+ óptimo. Llamadas VoLTE cristalinas, navegación inmediata. | Señal típica en Azotea (Punto Donante). |
| 🟡 **Aceptable** | `-81 a -95 dBm` | `5 a 12 dB` | 4G estable. Llamadas conectan sin dificultad, datos aceptables. | Señal en pasillos de Nivel 1. |
| 🟠 **Límite / Degradado** | `-96 a -105 dBm` | `0 a 5 dB` | Conexión inestable. Salto continuo entre 5G/4G/3G, audio entrecortado. | Requiere amplificación para evitar cortes. |
| 🔴 **ZONA MUERTA (Dead Zone)** | ` < -105 dBm` *(o < -110 dBm)* | `< 0 dB` *(ruido domina)* | **FALLO TOTAL:** Llamadas no entran (suena ocupado/apagado), llamadas activas se caen (*Call Drop*), batería del celular se drena rápido. | **Zona target para Antena Domo Interior Wilson.** |
| ❌ **Sin Servicio** | `≤ -120 dBm` o *No Signal* | N/A | Pantalla muestra "Solo Emergencias" o "Sin Servicio". Cero conectividad. | **Aislamiento total de seguridad.** |

---

## 📞 5. Prueba Activa de Llamada (Voice Stress Test)
No te fíes únicamente de las "barritas" del celular en reposo (Modo Idle). En reposo el teléfono muestra un nivel teórico; al presionar "Llamar", el módem debe transmitir hacia la torre (Uplink), y si está bajo tierra, la torre no lo escucha.

### Protocolo de 45 Segundos en Zonas Críticas (P5, P6, P7, P8):
1. Ubícate en la oficina de Álvaro Carreño (P6) o en Técnicos TI (P5).
2. Marca a un número conocido o teléfono de respaldo.
3. Cronometra:
   - **Tiempo de establecimiento:** ¿Tarda más de 5 a 8 segundos en dar tono? (Indica degradación a 3G/CSFB lento).
   - **Estabilidad de llamada:** Habla de forma continua durante 30 a 45 segundos mientras caminas dentro de la oficina.
   - **Resultado:**
     - Si la voz se escucha entrecortada o metálica: **MOS 2 (Mala)**.
     - Si la llamada se corta sola antes de los 30 segundos: **CALL DROP (Falla Crítica)**.
     - Si dice "Red no disponible" o "Llamada finalizada" sin timbrar: **BLOQUEO TOTAL**.
4. Anota el resultado en la planilla de terreno o en la Web App.

---

## 📋 6. Checklist Rápido de Terreno para el Día de la Prueba

### Antes de Entrar al Edificio:
- [ ] Batería del teléfono al 100 % + Power Bank en bolsillo.
- [ ] Optimización de batería desactivada en Android para G-NetTrack.
- [ ] G-NetTrack abierto con GPS enganchado a cielo abierto (verde, fix < 5 m).
- [ ] Presionar **Start Log** en G-NetTrack en la vereda exterior (P0).
- [ ] Abrir en navegador móvil la plataforma del proyecto:  
      `https://crdiazu.github.io/analizador-celular-pac/`

### Durante el Recorrido Interior:
- [ ] En cada cambio de piso o recinto crítico, presionar botón **Filemark** y nombrar el punto.
- [ ] Esperar 30 segundos estático en cada punto de medición.
- [ ] En P5 (Técnicos) y P6 (Álvaro Carreño), hacer la llamada de prueba activa de 45 segundos.
- [ ] Tomar fotografía del cielo falso y ductos en el pasillo de Informática (donde bajará el cable coaxial Wilson400).
- [ ] Validar con huincha o visualmente la trayectoria del cable desde la azotea (Shaft GI 07/08).

### Al Finalizar la Medición:
- [ ] Presionar **Stop Log** en G-NetTrack.
- [ ] Exportar archivo `.txt` y `.kml` desde la app (se guardan en la carpeta `/G-NetTrack/Logs/` de la memoria del teléfono).
- [ ] Enviar el archivo TXT por WhatsApp o correo para cruzarlo con el visualizador web de Tecnovoa.

---

## 💼 7. Discurso Técnico para el Cliente (Álvaro Carreño / SECPLA)
Cuando Álvaro Carreño te acompañe y vea las mediciones en pantalla, resume la situación con estos 3 puntos clave:

> *"Álvaro, fíjate en el registro: afuera en la calle y en la azotea las 4 compañías (Entel, Movistar, Claro y WOM) llegan con niveles óptimos de -72 dBm en 4G y 5G.*  
> *Sin embargo, al bajar a este subterráneo (cota -3,20 m), las dos losas de hormigón armado de 25 cm absorben más de 35 dB de potencia. La señal cae por debajo de los -110 dBm, entrando en la 'Zona Muerta' donde las llamadas se cortan o ni siquiera conectan.*  
> *El kit **weBoost Office 200 de Wilson Connectivity** que te cotizamos resuelve exactamente esto: capta la señal pura en azotea con una antena omnidireccional 360°, la baja por cable Wilson400 de ultra baja pérdida a través del shaft técnico, y la reinyecta aquí en el subterráneo con una antena domo, devolviendo cobertura plena a todas las oficinas de tu equipo sin alterar la red municipal."*

---

*Tecnovoa Ltda. — Soluciones Profesionales de Conectividad Celular y Telecomunicaciones.*  
*Pedro de Valdivia #273, Providencia, Santiago | www.tecnovoa.cl*
