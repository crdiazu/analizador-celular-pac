# Acta de Visita Técnica — Centro Consistorial Municipalidad de Pedro Aguirre Cerda
**Fecha visita:** 29-10-2026 · **Elaborada a partir de:** transcripción automática de audio (calidad baja, ver advertencia)  
**Tecnovoa:** Cristián Díaz (KAM TI) + acompañante  
**Municipalidad (según audio):** Álvaro Carreño (Informática), Javier (Seguridad Pública / cámaras y radioenlaces), encargado de Riesgo y Desastres / Seguridad Ciudadana (estación meteorológica y drones), mención a un "Álvaro Castro" como jefe de unidad.

> [!WARNING]
> La transcripción tiene muchos errores de reconocimiento de voz. Los puntos marcados con **(?)** son interpretaciones y hay que confirmarlos con el cliente antes de usarlos en una propuesta: nombres, cifras y ubicaciones.

---

## 1. Requerimientos detectados (4 oportunidades + 1 por confirmar)

### R1 — Telefonía móvil en Nivel -1 (requerimiento original) ✅ confirmado
- En **todo el Nivel -1** (Informática, Seguridad Pública y el pasillo completo) la voz celular falla: **no se escucha, se corta y hay que salir para hablar**.
- **Internet en los PC funciona bien** (red cableada). El problema es solo la cobertura móvil.
- Usuario de prueba con **iPhone**: G-NetTrack no corre en iOS. El log Android del 29-10 (`movistar_2026.10.29_09.08.42.txt`) **quedó vacío**, así que no hay medición registrada de esta visita.
- El cliente sugiere que el **ala opuesta** del edificio es estructuralmente igual: posible ampliación de alcance.
- Solución ya cotizada: weBoost Office 200 (Opción A). Ahora el alcance real parece ser **todo el pasillo de Seguridad Pública**, así que hay que evaluar la Opción B (splitter + domos adicionales).

### R2 — Conectividad estable para la estación meteorológica en azotea 🔴 urgente para el cliente
- La estación funciona hoy con **un chip 4G** (primero prepago, luego plan). Se queda **sin datos o sin señal** y deja de reportar. **En el último temporal se cayó a mitad del evento.**
- El equipo tiene **WiFi, 4G y otra interfaz**, CPU interna, alimentación solar más red eléctrica (energía asegurada) y **8 baterías recargables de respaldo que hay que revisar**.
- Guarda los datos localmente y los reenvía al reconectarse, pero **el alcalde necesita datos en tiempo real** para informar.
- **Uso operativo (Plan Comunal de Riesgo y Desastres):** umbrales de acción por precipitación acumulada: **~5 → preparar sacos, ~10 → despliegue, ~25 mm → operación total (?)**. El último evento registró **53 mm**, y la comuna soporta 25–28 mm. Antes se informaba con datos de Quinta Normal o Pudahuel, que no reflejan la comuna.
- **Objetivo futuro:** oficializar la estación como **punto de referencia ante la Dirección Meteorológica de Chile**.
- **Mantenimiento detectado:** el **pluviómetro de balancín ("cucharita") se tapa con tierra** y marca datos falsos. Necesita limpieza periódica.
- **Propuesta conversada en terreno:** usar **WiFi como enlace principal** con antenas outdoor mini-direccionales (2–3) y dejar **el chip 4G como respaldo**.

### R3 — Centro de operación de drones / "helipuerto" en azotea (ala frontis) 🟡 proyecto en definición
- Seguridad Pública convertirá un ala de la azotea en **pista y centro de manejo de drones**, con un puesto de mando o comando de incidentes.
- **Flota:** tienen **4 drones** y van a activar más, todos similares **(?)**. Hoy operan **1 a la vez** para no saturar.
- **Hoy:** la transmisión va por un **canal privado de YouTube** usando el **hotspot del celular** de un funcionario. El vínculo dron–joystick también depende de esa conexión.
- **Necesidad:** **~4 puntos de red estables (1 por dron)** y cobertura **inalámbrica** para que el operador se mueva por la azotea con 2–3 drones simultáneos.
- Hay **enchufe disponible** para cargar baterías.
- Todavía **no está definida la ubicación física** del centro operativo.

### R4 — Ampliación de cámaras y radioenlaces de Seguridad Pública 🟢 oportunidad mayor
- **57 cámaras hoy, pasarán a 127 (+80)** y los postes subirán a **18 m**.
- Hay radioenlaces en la azotea hacia el repetidor de la **Casa de la Cultura (~3 km (?))**, que reparte hacia las cámaras. Otro enlace cubre el sector norte. La cámara más lejana está a ~300 m del límite comunal (la comuna tiene ~10 km²).
- Necesitan **aumentar la capacidad de los repetidores** para las nuevas cámaras.
- En la azotea también están las antenas de la **radio de patrullas**.

### R5 — Calidad de audio en la central telefónica ⚪ por confirmar
- En la central, las llamadas se escuchan "como acelerado" o entrecortado. **Parece un problema distinto de la cobertura celular**, quizás de la central o VoIP (jitter o códec). Hay que confirmar marca y tipo de central.

### Oferta adicional mencionada por Tecnovoa
- **Pantallas interactivas Huawei** (HarmonyOS, con módulo OPS para Windows o Android), en **venta o arriendo**, para salas de dirección y reuniones.

---

## 2. Datos del edificio aportados en la visita
- Las dos alas son **estructuralmente iguales**. En el ala opuesta hay **3 pisos no habitados** y está la Dirección de Alimentación **(?)**.
- **Nivel -1:** Informática (Álvaro Carreño, al inicio del pasillo) y luego **toda la Dirección de Seguridad Pública**. Hay una zona de estacionamientos.
- La **alcaldía** está en los pisos superiores **(?)**.

---

## 3. Próximos pasos propuestos
| # | Acción | Responsable |
| :-- | :-- | :-- |
| 1 | Repetir la medición con un **Android** (confirmando que el contador de muestras sube) en todo el pasillo del Nivel -1 | Tecnovoa |
| 2 | Pedir **marca/modelo de la estación meteorológica** y de su plataforma (interfaces WiFi/4G y protocolo de envío) | Riesgo y Desastres |
| 3 | Proponer un **enlace WiFi outdoor en azotea** que sirva a la estación (principal) y a los drones (4 puntos), con 4G de respaldo | Tecnovoa |
| 4 | Pedir **planos o ubicación del futuro centro de drones** y el modelo de los drones y del control remoto | Seguridad Pública |
| 5 | Pedir **inventario de radioenlaces** (marca, banda, capacidad) y bases técnicas de las +80 cámaras | Javier |
| 6 | Ajustar la cotización de telefonía al **alcance real del Nivel -1** (Opción B o más domos) | Tecnovoa |
| 7 | Consultar **marca y tipo de la central telefónica** (problema de audio) | Informática |
| 8 | Enviar la ficha de **pantallas interactivas Huawei** (venta/arriendo) | Tecnovoa |
