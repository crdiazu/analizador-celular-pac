# Análisis Técnico de Cobertura y Calidad de Señal Celular en Infraestructuras Edificadas Mediante Dispositivos Móviles

# Análisis Técnico de Cobertura y Calidad de Señal Celular en Infraestructuras Edificadas Mediante Dispositivos Móviles

El diagnóstico y la caracterización radioeléctrica de redes móviles en el interior de edificaciones e infraestructuras complejas constituye un procedimiento crítico para la ingeniería de telecomunicaciones [cite: 1, 2]. La evaluación cualitativa basada en el indicador gráfico de barras en un teléfono inteligente resulta técnicamente insuficiente, dado que dicho icono representa una abstracción no estandarizada que varía según el fabricante y el operador, omitiendo parámetros esenciales como la interferencia co-canal, la densidad de potencia y la eficiencia espectral del canal [cite: 1, 3]. Para llevar a cabo una auditoría técnica rigurosa de la cobertura indoor utilizando dispositivos móviles comerciales (iOS y Android), es necesario acceder a las métricas de la capa física (PHY) del módem, emplear los códigos de servicio del sistema operativo y ejecutar un protocolo metódico de prueba en recorrido (*walk test*) [cite: 4, 5].

---

## Fundamentos Radioeléctricos y Métricas de Rendimiento en Redes 4G LTE y 5G NR

La calidad de la conexión inalámbrica en el interior de una infraestructura está gobernada por la relación entre la potencia recibida desde la estación base servidora, el nivel de ruido ambiental y la interferencia generada por sectores adyacentes [cite: 1, 2, 3]. El análisis requiere la descomposición de la señal en métricas específicas estandarizadas por el *3rd Generation Partnership Project* (3GPP) [cite: 2, 6].

### Métricas Primarias de Capa Física en LTE

En las redes 4G LTE, el módem del dispositivo móvil evalúa de manera continua la señal a través de cuatro parámetros cardinales:

**RSRP (Reference Signal Received Power)**: Mide la potencia media recibida de los símbolos que transportan señales de referencia específicas de la celda (*Cell-Specific Reference Signals*, CRS) distribuidas en el dominio de la frecuencia y el tiempo [cite: 1, 3]. Expresado en dBm, el RSRP representa la métrica pura de cobertura, siendo independiente del ancho de banda del canal [cite: 3].

**RSSI (Received Signal Strength Indicator)**: Cuantifica la potencia total recibida por el dispositivo dentro de todo el ancho de banda del canal [cite: 2]. Incluye la potencia de la celda servidora, la interferencia co-canal de celdas vecinas, las emisiones no esenciales y el ruido térmico del receptor [cite: 2].

**RSRQ (Reference Signal Received Quality)**: Indica la calidad de la señal de referencia considerando la cantidad total de energía presente en el canal [cite: 2, 3]. Su cálculo matemático viene dado por la expresión: RSRQ = \frac{N \times RSRP}{RSSI} donde N es el número de bloques de recursos (*Resource Blocks*, RB) asignados al ancho de banda de la portadora de acceso terrestre evolucionado (E-UTRA) [cite: 1, 2, 7]. Un valor degradado de RSRQ en presencia de un RSRP elevado es un indicador directo de fuerte interferencia o congestión en el canal [cite: 1, 2, 3].

**SINR (Signal to Interference plus Noise Ratio)**: Es la relación entre la potencia de la señal deseada y la suma de la potencia de interferencia procedente de otros sectores más el ruido térmico [cite: 2, 3, 8]: SINR = \frac{P_{\text{señal}}}{P_{\text{interferencia}} + P_{\text{ruido}}} El SINR es el predictor más directo de la tasa de transferencia de datos alcanzable (*throughput*), puesto que condiciona la asignación del esquema de modulación y codificación (*Modulation and Coding Scheme*, MCS) por parte del planificador (*scheduler*) de la red [cite: 3, 9].

### Métricas Específicas de 5G NR (Sub-6 GHz y mmWave)

La arquitectura de 5G NR sustituye las señales CRS continuas de LTE por bloques de señales de sincronización (*Synchronization Signal Blocks*, SSB) transmitidos mediante barrido de haces directivos (*beamforming*) [cite: 10]. En consecuencia, las métricas equivalentes en 5G NR adoptan el prefijo SS [cite: 10, 11]:

**SS-RSRP**: Potencia recibida de los elementos de recurso de la señal de sincronización secundaria del haz seleccionado [cite: 10, 11].

**SS-RSRQ**: Calidad de la señal de sincronización respecto a la energía total del haz [cite: 10, 11].

**SS-SINR**: Relación señal a interferencia más ruido medida sobre los bloques SSB del haz [cite: 1, 11].

En despliegues 5G de onda milimétrica (mmWave), los valores de SS-RSRP sufren atenuaciones severas y repentinas ante obstáculos físicos leves, como muros de tabiquería, cristales blindados o la presencia de personas, debido a las pérdidas por propagación en espacio libre y la baja difracción inherente a frecuencias superiores a 24 GHz [cite: 1]. Por el contrario, los despliegues en bandas Sub-6 GHz presentan una capacidad de penetración estructural más afín a la de LTE [cite: 1].

### Conversión Estándar 3GPP en Reportes de Medición

Cuando el terminal móvil transmite informes de medición (*RRC Measurement Reports*) a la red, los valores de RSRP no se codifican en dBm de forma directa, sino como enteros discretos [cite: 6]. Para la post-procesación de datos, la conversión a potencia real debe aplicar el desfase normativo adecuado según la tecnología [cite: 6]:

\text{RSRP}_{\text{LTE}} (\text{dBm}) = \text{Índice}_{\text{reportado}} - 141 \quad (\text{según 3GPP TS 36.133}) [cite: 6] \text{RSRP}_{\text{5G NR}} (\text{dBm}) = \text{Índice}_{\text{reportado}} - 157 \quad (\text{según 3GPP TS 38.133}) [cite: 6]

El desfase adicional de 16 dB en 5G NR responde a la necesidad de acomodar el rango dinámico extendido que requieren las frecuencias altas para medir señales recibidas extremadamente débiles [cite: 6].

|   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

---

## Interfaz de Diagnóstico en Sistemas Operativos Móviles

El acceso a las métricas de ingeniería en tiempo real varía en función del sistema operativo del dispositivo y del fabricante del procesador de señal [cite: 11, 12].

### Menú Field Test Mode en iOS (iPhone)

Los dispositivos Apple integran una aplicación oculta denominada *Field Test Mode* [cite: 11, 13]. Para inicializarla, se debe marcar la secuencia MMI `*3001#12345#*` en el marcador telefónico [cite: 4, 11, 13].

En versiones modernas del sistema (iOS 16 y posteriores), la interfaz expone submenús divididos por tecnología de acceso de radio (RAT) [cite: 4, 14]:

**Ruta para Redes LTE**: Navegar a la pestaña lateral \rightarrow **LTE** \rightarrow **Serving Cell Meas** [cite: 4, 14].

`rsrp0`: Potencia de la celda servidora principal en la antena 0 (expresada en dBm) [cite: 11, 13, 14].

`rsrp1`: Potencia medida en la antena secundaria de diversidad [cite: 13, 14].

`sinr`: Relación señal a ruido e interferencia en el canal descendente [cite: 13].

**Ruta para Redes 5G NR**: Navegar a **NR** o **NR NSA/SA** \rightarrow **5G NR Serving Cell Info / Meas** [cite: 4, 11].

`ss-RSRP`: Potencia del haz activo de la estación base 5G (gNodeB) [cite: 14].

`ss-RSRQ` y `ss-SINR`: Indicadores de pureza de la señal 5G [cite: 11].

**Identificadores de Red**:

`Physical Cell ID (PCI)`: Código de identificación de la celda física, indispensable para detectar conmutaciones inestables entre sectores (*handover ping-pong*) [cite: 4, 11].

`EARFCN` / `NR-ARFCN`: Número de canal de radiofrecuencia que identifica la banda espectral exacta en uso [cite: 4, 11].

### Menús de Ingeniería y Herramientas en Android

El sistema operativo Android ofrece flexibilidad para la extracción automatizada de datos a través de APIs del sistema, aunque el acceso a los menús secretos marcados varía según la marca [cite: 11, 12].

**Menú Estándar Android**: Marcando `*#*#4636#*#*` se ingresa a "Información del Teléfono", donde se despliega la intensidad de señal en dBm y el identificador de celda [cite: 11, 15]. En versiones de Android 12 o superiores, este menú puede estar bloqueado por políticas del fabricante [cite: 12].

**Modos de Servicio Propietarios por Fabricante**:

**Samsung (One UI)**: Mediante el código `*#0011#` se accede al *Service Mode*, que proporciona una lectura precisa y no filtrada de RSRP, RSRQ, RSSNR, banda operativa, ancho de banda y canal EARFCN/ARFCN [cite: 4, 12].

**Motorola**: Acceso mediante `*#*#2486#*#*` (*Engineering Mode*) [cite: 15, 16, 17].

**Xiaomi / POCO / Redmi**: Menú CIT mediante `*#*#6484#*#*` o `*#*#64663#*#*` [cite: 12, 17].

**OPPO / Realme / OnePlus**: `*#899#` para activar el *EngineerMode* [cite: 12, 17].

**Aplicaciones Especializadas para Registros Continuos**: Para la realización de levantamientos de cobertura en Android, resulta eficiente recurrir a herramientas como **G-NetTrack Pro** o **Network Cell Info Lite**, las cuales automatizan la recolección de métricas, generan registros georreferenciados y permiten superponer mapas temáticos sobre planos arquitectónicos [cite: 4, 11, 18].

|   |   |   |   |

| --- | --- | --- | --- |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

|   |   |   |   |

---

## Metodología Operativa para la Auditoría e Inspección Indoor

La ejecución de un estudio de cobertura dentro de un inmueble exige una sistemática rigurosa que garantice la validez de los datos recopilados [cite: 2, 19].

### Fase 1: Calibración y Carga de Planos Arquitectónicos

Previo al trabajo de campo, se debe digitalizar la cartografía del edificio para posibilitar el rastreo dentro del espacio [cite: 19]:

Exportar los planos de cada planta a archivos de imagen en formato PNG o JPG, orientándolos exactamente hacia el Norte geográfico [cite: 19].

Generar el archivo de georreferenciación pasiva `index.txt` en la carpeta de registros de la aplicación de medición (por ejemplo, `G-NetTrack_Pro_Logs/floorplan`) [cite: 19].

El archivo `index.txt` debe contener una estructura delimitada por tabulaciones donde se especifiquen las esquinas geográficas de la imagen:

`planta1.png [tab] longitud_oeste [tab] latitud_sur [tab] longitud_este [tab] latitud_norte` [cite: 19]

Este procedimiento asigna coordenadas espaciales ficticias o reales al plano, permitiendo que el software interpole las lecturas radioeléctricas a lo largo del inmueble sin requerir señal GPS [cite: 5, 19].

### Fase 2: Recorrido Metódico e Interpolación de Puntos

Debido a que las estructuras de hormigón, forjados y cerramientos metálicos bloquean las señales GNSS/GPS en el interior de los edificios, la trayectoria de medición se reconstruye mediante interpolación manual [cite: 5, 19, 20]:

**Modo Indoor Manual**: Con el plano cargado en la aplicación, el operador se posiciona en un punto de origen conocido (por ejemplo, la puerta de acceso) y marca la opción `Set Point` [cite: 5, 19].

**Caminata a Paso Uniforme**: El técnico camina a una velocidad constante siguiendo una trayectoria recta [cite: 19]. Al alcanzar un hito geográfico (esquinas, columnas, intersecciones de pasillos), se vuelve a presionar `Set Point` [cite: 5, 19]. El sistema distribuye automáticamente las muestras recopiladas segundo a segundo de forma proporcional a lo largo del segmento trazado [cite: 5, 19].

**Modo Auto-Indoor para Zonas Ciegas**: En infraestructuras complejas como sótanos o túneles de servicio, se configura un umbral de imprecisión GPS (*Accuracy threshold*) [cite: 5, 19]. Al perderse el enganche satelital al ingresar a la zona ciega, la aplicación almacena las lecturas en un buffer temporal y completa el trazado rectilíneo de los datos en el momento en que se recupera la fijación satelital al salir al exterior [cite: 5, 19, 20].

### Fase 3: Mediciones Estáticas y Caracterización Multi-Operador

Las pruebas de recorrido deben complementarse con muestras estáticas en puntos críticos (salas de reuniones, despachos ejecutivos, áreas de producción) [cite: 11]:

**Estabilización del Módem**: Es imperativo mantener el terminal inmóvil durante al menos 30 segundos en cada punto estático para permitir que el receptor del teléfono estabilice los promedios de RSRP/SINR y finalice los procesos de reconfiguración RRC [cite: 4].

**Evaluación de Redes Competidoras**: Cuando se analiza la cobertura de múltiples operadores con un solo terminal, la conmutación se realiza forzando la selección de red (`Ajustes` \rightarrow `Redes Móviles` \rightarrow `Búsqueda Manual`) [cite: 4]. Este escaneo pasivo toma entre 30 y 60 segundos por red para registrar la intensidad RSRP de las celdas encontradas [cite: 4].

### Fase 4: Pruebas de Tráfico Activo y Evaluación de QoE

La medición de parámetros pasivos (RSRP/SINR) debe validarse mediante pruebas activas que reflejen la calidad de experiencia percibida por el usuario (*Quality of Experience*, QoE) [cite: 5, 21]:

Ejecutar ciclos automatizados de transferencia de datos que incluyan latencia (tiempos de respuesta Ping ICMP), velocidad de descarga descendente (Downlink mediante peticiones HTTP/FTP multihilo) y velocidad de subida ascendente (Uplink) [cite: 5, 21].

Evaluar la degradación del rendimiento de datos en zonas donde el SINR sea inferior a +6 dB [cite: 3]. En tales condiciones, el planificador del nodo fuerza el uso de modulación QPSK, colapsando la tasa de transferencia efectiva aun cuando el nivel de RSRP sea aceptable debido a la cercanía de un transmisor lejano [cite: 3].

---

## Matriz Diagnóstica de Anomalías Radioeléctricas en Edificaciones

El diagnóstico de problemas de conectividad indoor requiere correlacionar las lecturas simultáneas de RSRP, RSRQ y SINR para identificar la causa física del fallo [cite: 1, 2, 3].

|   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

Las anomalías asociadas a la contaminación de pilotos son frecuentes en las plantas altas de los edificios [cite: 9]. Al ascender en una estructura, la atenuación producida por construcciones circundantes disminuye, lo que permite al dispositivo móvil entrar en visión directa (*Line-of-Sight*, LOS) con múltiples torres celulares distantes [cite: 9]. Aunque esto se traduce en un nivel de potencia RSRP elevado, la recepción simultánea de múltiples señales desfasadas destruye la relación SINR, provocando la caída drástica del ancho de banda y el fallo en las conexiones de voz y datos [cite: 1, 3, 9]. En estos casos, la instalación de un amplificador bidireccional simple (BDA) resulta contraproducente, dado que amplificará la interferencia existente; la intervención requiere forzar la selección de bandas de mayor frecuencia que no penetren desde el exterior o desplegar miniceldas indoor dedicadas (*Small Cells*) [cite: 2, 3].

---

## Discrepancias Técnicas Entre Teléfonos Móviles y Equipos de Medición Profesional

Si bien los teléfonos inteligentes permiten realizar diagnósticos preliminares y levantamientos de cobertura accesibles, existen diferencias metodológicas y de hardware sustanciales entre un smartphone comercial y un escáner de radiofrecuencia profesional (*Drive Test / Walk Test Scanner*) [cite: 3, 4].

El módem de un teléfono comercial está optimizado para la eficiencia energética y la experiencia del usuario, no para la metrología de precisión [cite: 4]. Esto introduce tres sesgos sistemáticos durante la recolección de datos indoor:

**Efecto de Absorción Corporal (*****Body Loss*****)**: Al sujetar el teléfono para inspeccionar la pantalla, el cuerpo del operador actúa como un elemento atenuador que absorbe entre 3 dB y 10 dB de la señal entrante en función de la frecuencia [cite: 9]. Los escáneres profesionales utilizan antenas omnidireccionales calibradas montadas en mástiles o arneses para aislar el patrón de radiación del impacto de la proximidad humana.

**Filtrado Temporal y Suavizado de Datos**: Para evitar conmutaciones innecesarias de celda, el firmware del smartphone aplica algoritmos de promediado (*Layer 3 filtering*) sobre las lecturas de capa física [cite: 4]. Esto provoca un desfase temporal en la representación de los datos; el valor mostrado en la pantalla del teléfono refleja la condición de la red de varios segundos atrás, enmascarando caídas nulas de señal (*fading*) de corta duración.

**Limitación del Conjunto de Celdas Monitoreadas**: Un teléfono móvil solo decodifica activamente la información del canal de control de la celda servidora a la que está conectado y de un número limitado de celdas vecinas reportadas en la lista de transmisión (*Neighbor List*) [cite: 4]. Por el contrario, un escáner de RF dedicado procesa simultáneamente todo el espectro de radiofrecuencia, decodificando las señales de sincronización (PSS/SSS) de cualquier emisor presente, incluso si su nivel de potencia se encuentra por debajo del umbral de sensibilidad del módem de un smartphone.

|   |   |   |

| --- | --- | --- |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

---

## Conclusiones y Recomendaciones de Ingeniería

El análisis de señales celulares en infraestructuras mediante teléfonos inteligentes constituye una metodología ágil y de bajo costo para diagnosticar las causas raíz de una conectividad deficiente [cite: 4, 5]. Para maximizar la eficacia de estas auditorías y guiar la implementación de soluciones de cobertura indoor, se deben aplicar las siguientes consideraciones:

**Priorización del SINR sobre el RSRP**: Las decisiones de diseño no deben tomarse evaluando únicamente la potencia de recepción (RSRP) [cite: 3]. Un entorno con RSRP alto pero SINR negativo es incapaz de sostener tasas de transferencia funcionales debido a la degradación de los esquemas de modulación [cite: 1, 3].

**Mitigación de Interferencia Externa**: Cuando el problema diagnosticado en plantas altas corresponda a contaminación de pilotos por visión directa con múltiples estaciones bases exteriores, se debe evitar el uso de amplificadores de señal genéricos [cite: 2, 3]. La intervención adecuada exige coordinar con los operadores móviles la reorientación de los sectores externos (*tilt* eléctrico/mecánico) o implementar soluciones indoor dedicadas (*Small Cells* o DAS pasivo/activo) [cite: 2, 3].

**Exportación y Documentación Georreferenciada**: Es fundamental documentar las auditorías indoor generando trazas georreferenciadas en formato KML o CSV mediante aplicaciones de registro [cite: 5, 20, 21]. Estos datos permiten respaldar la solicitud de mejoras de infraestructura ante las empresas operadoras de telefonía móvil o proyectar con precisión la ubicación de los puntos de emisión de un sistema de distribución de antenas [cite: 2, 18].

---

RSRP, RSRQ, SINR Explained: Mobile Signal Metrics Guide - Simology, [https://simology.io/blog/coverage-metrics-decoded-rsrp-rsrq-sinr-plain-english](https://simology.io/blog/coverage-metrics-decoded-rsrp-rsrq-sinr-plain-english)

Understanding RSRQ: What It Means for Indoor Signal Quality - MobileCorp, [https://www.mobilecorp.com.au/learning-hub/rsrq](https://www.mobilecorp.com.au/learning-hub/rsrq)

Understanding Signal Metrics - SignalTester, [https://signaltester.co.uk/understanding-signal-metrics/](https://signaltester.co.uk/understanding-signal-metrics/)

Mobile Signal Tester – iPhone and Android - SignalTester, [https://signaltester.co.uk/mobile-signal-tester/](https://signaltester.co.uk/mobile-signal-tester/)

G-NetTrack Manual - Gyokov Solutions, [http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

RSRP Threshold Mapping in 5G NR and LTE: What the RRC Message Actually Reports, [https://www.telecomhall.net/t/rsrp-threshold-mapping-in-5g-nr-and-lte-what-the-rrc-message-actually-reports/36657](https://www.telecomhall.net/t/rsrp-threshold-mapping-in-5g-nr-and-lte-what-the-rrc-message-actually-reports/36657)

Understanding LTE Signal Strength Values - Digi International, [https://www.digi.com/support/knowledge-base/understanding-lte-signal-strength-values](https://www.digi.com/support/knowledge-base/understanding-lte-signal-strength-values)

Signal strength measure RSRP, RSRQ and SINR Reference for LTE & 5G Cheat Sheet, [https://poynting.tech/articles/antenna-faq/signal-strength-measure-rsrp-rsrq-and-sinr-reference-for-lte-cheat-sheet/](https://poynting.tech/articles/antenna-faq/signal-strength-measure-rsrp-rsrq-and-sinr-reference-for-lte-cheat-sheet/)

LTE Signal Strength and Quality | Download Scientific Diagram - ResearchGate, [https://www.researchgate.net/figure/LTE-Signal-Strength-and-Quality_tbl1_369044913](https://www.researchgate.net/figure/LTE-Signal-Strength-and-Quality_tbl1_369044913)

Understanding RSSI, RSRP, and RSRQ - Welcome To The 5Gstore Blog, [https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/](https://5gstore.com/blog/2021/04/08/understanding-rssi-rsrp-and-rsrq/)

Cell site testing in my area with ultra capacity - Facebook, [https://www.facebook.com/groups/1391099124480057/posts/3173363002920318/](https://www.facebook.com/groups/1391099124480057/posts/3173363002920318/)

Android Secret Codes List (Samsung, Pixel, OnePlus, Vivo & More) | Beebom Gadgets, [https://gadgets.beebom.com/guides/android-secret-codes-list](https://gadgets.beebom.com/guides/android-secret-codes-list)

Amplifier la 4G iPhone — Field Test Mode : code & mesures rapides | AmplificateurLCD.fr, [https://www.amplificateurlcd.fr/tips-tricks/field-test-mode/](https://www.amplificateurlcd.fr/tips-tricks/field-test-mode/)

Cell Tower Locations: How to Find 4G LTE and 5G Towers - Dgtl Infra, [https://dgtlinfra.com/cell-tower-locations-4g-lte-5g-towers/](https://dgtlinfra.com/cell-tower-locations-4g-lte-5g-towers/)

How to Use MMI and USSD Codes for Android - wikiHow, [https://www.wikihow.com/Android-Secret-Codes](https://www.wikihow.com/Android-Secret-Codes)

Android Secret Service Codes List | PDF | Smartphone - Scribd, [https://www.scribd.com/document/904423673/Android-Service-Code](https://www.scribd.com/document/904423673/Android-Service-Code)

Full List of MMI Codes for Android Devices (including Samsung) - Dr.Fone, [https://drfone.wondershare.com/imei-check/list-of-mmi-codes.html](https://drfone.wondershare.com/imei-check/list-of-mmi-codes.html)

G-NetTrack Pro manual - Gyokov Solutions, [https://gyokovsolutions.com/manual-g-nettrack/](https://gyokovsolutions.com/manual-g-nettrack/)

G-NetTrack Pro Manual - Gyokov Solutions, [https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

G-NetTrack Pro User Manual | PDF | Roaming - Scribd, [https://www.scribd.com/document/468503834/G-NetTrack-Pro-manual](https://www.scribd.com/document/468503834/G-NetTrack-Pro-manual)

G-NetTrack Pro User Manual | PDF | Computer File - Scribd, [https://www.scribd.com/document/250661321/G-NetTrack-Pro-Manual](https://www.scribd.com/document/250661321/G-NetTrack-Pro-Manual)