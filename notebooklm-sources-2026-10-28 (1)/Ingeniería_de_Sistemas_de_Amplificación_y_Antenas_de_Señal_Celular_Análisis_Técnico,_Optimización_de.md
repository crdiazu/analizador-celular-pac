# Ingeniería de Sistemas de Amplificación y Antenas de Señal Celular: Análisis Técnico, Optimización de Líneas de Transmisión y Marco Regulatorio

# Ingeniería de Sistemas de Amplificación y Antenas de Señal Celular: Análisis Técnico, Optimización de Líneas de Transmisión y Marco Regulatorio

## Arquitectura General de Captación y Distribución Radiada

Los sistemas de mejora de cobertura celular, conocidos técnicamente como amplificadores bidireccionales (BDA, por sus siglas en inglés) o repetidores de señal celular, están diseñados para mitigar las pérdidas de propagación por trayectoria (*path loss*) y la atenuación estructural en entornos interiores [cite: 1]. La arquitectura fundamental de un sistema de amplificación consta de tres bloques funcionales interconectados: la antena donante orientada al exterior, la unidad activa de amplificación y procesamiento espectral, y la red de distribución interior conformada por antenas servidoras e infraestructura de cableado coaxial [cite: 1].

La función esencial de la antena donante es establecer un enlace de radiofrecuencia (RF) de alta calidad con la estación base (BTS) del operador móvil [cite: 1]. La selección de la antena donante depende directamente de la topología radioeléctrica del entorno. En escenarios donde se requiere captar la señal de una torre celular distante o aislar una portadora específica en entornos con severa interferencia cocanal, se emplean antenas directivas, tales como las configuraciones Yagi-Uda o las formaciones periódico-logarítmicas (LPDA) [cite: 1]. Estas antenas proporcionan una alta ganancia en el lóbulo principal y un elevado rechazo de relación frente-espalda (*front-to-back ratio*) [cite: 1]. Por el contrario, en entornos urbanos consolidados donde el dispositivo debe conmutar entre múltiples celdas o recibir señales de diferentes operadores orientados en distintas direcciones, se instalan antenas omnidireccionales de alineación vertical [cite: 1].

El acoplamiento y la estabilidad del sistema están supeditados al aislamiento electromagnético (I) entre la antena donante y las antenas servidoras interiores [cite: 1, 2]. Si la ganancia total del amplificador (G_{\text{amp}}) supera la pérdida por trayectoria en el espacio libre entre la antena exterior y la interior, el sistema entra en un bucle de realimentación positiva, provocando oscilación en RF [cite: 1, 2]. Esta oscilación no solo satura los amplificadores de potencia de la unidad local, sino que emite ruido que desensibiliza los receptores de la estación base del operador móvil, degradando el servicio para todos los usuarios de la celda [cite: 3]. Para garantizar la estabilidad del enlace sin activar los circuitos de atenuación por autoprotección, se requiere cumplir rigurosamente con la condición de aislamiento mínimo:

I_{\text{mín}} > G_{\text{amp}} + 15\text{ dB}

---

## Física de Líneas de Transmisión Coaxial y Coeficientes de Atenuación

La infraestructura física de interconexión entre las antenas y la unidad central de amplificación representa uno de los puntos más críticos en el presupuesto de enlace (*link budget*) [cite: 4]. La atenuación en una línea de transmisión coaxial aumenta de manera no lineal en función de la frecuencia de operación, impulsada por dos mecanismos físicos dominantes: la resistencia por efecto piel (*skin effect*) en los conductores interno y externo, y la tangente de pérdidas en el material dieléctrico [cite: 5, 6].

La tasa de atenuación total por unidad de longitud (\alpha) a una frecuencia dada (f en MHz) se modela cuantitativamente mediante la ecuación empírica de dos términos desarrollada por los fabricantes de líneas de transmisión [cite: 5, 7, 8]:

\alpha(f) = k_1 \sqrt{f} + k_2 f

En esta formulación, el coeficiente k_1 representa las pérdidas óhmicas proporcionales a la raíz cuadrada de la frecuencia derivadas del efecto piel en los conductores metálicos [cite: 5]. El coeficiente k_2 cuantifica las pérdidas dieléctricas que escalan de forma lineal con la frecuencia [cite: 5]. A frecuencias de banda baja (700 MHz – 900 MHz), las pérdidas por conductor (k_1 \sqrt{f}) predominan en la ecuación [cite: 5]. Sin embargo, al migrar hacia bandas de frecuencia de telefonía móvil de mayor espectro (AWS 1700/2100 MHz, 2.6 GHz e incrementos en Sub-6 GHz 5G a 3.5 GHz), las pérdidas dieléctricas (k_2 f) aceleran la degradación de la potencia transmitida [cite: 5].

La composición del material dieléctrico determina el factor de velocidad (VF) y la eficiencia de la línea [cite: 5]. Las líneas coaxiales tradicionales con dieléctrico de polietileno sólido (PE), como el cable RG-58, exhiben un VF \approx 0.66 y una elevada tangente de pérdidas, volviéndolas inviables para trayectos superiores a unos pocos metros en frecuencias celulares [cite: 5, 6, 9]. Las familias modernas de bajo nivel de pérdida (como las series LMR-240, LMR-400 y LMR-600) incorporan dieléctricos de espuma de polietileno inyectada con gas inerte, alcanzando un VF de entre 0.84 y 0.88 [cite: 5]. El gas atrapado en celdas cerradas se comporta de manera similar al aire en el espacio libre, reduciendo sustancialmente el valor del coeficiente k_2 [cite: 5].

Para poner en perspectiva las pérdidas de potencia en decibelios (dB) respecto a la energía que se entrega efectivamente a la antena, se aplican las reglas fundamentales de atenuación logarítmica: una pérdida de 3 dB reduce la potencia útil al 50.1%, una pérdida de 6 dB transmite solo el 25.1% de la energía original, y una atenuación de 10 dB disipa el 90% de la señal en forma de calor a lo largo de la línea [cite: 5, 7, 9].

|   |   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

El análisis de la tabla de atenuación revela una implicación crítica para los despliegues de tecnología móvil: mientras que un cable de grado intermedio como el LMR-240 resulta técnicamente aceptable para tramos cortos de hasta 10 metros en bandas bajas de 850 MHz (acumulando una pérdida tolerable de ~2.5 dB), ese mismo tramo en una frecuencia de banda media-alta como 2.4 GHz o 3.5 GHz absorberá más de 4.2 dB de la señal [cite: 5, 9]. En instalaciones comerciales de mediana y larga distancia (superiores a 15 metros), el uso de cables de menor atenuación como LMR-400 o líneas rígidamente blindadas tipo Heliax de 1/2 pulgada resulta imprescindible para evitar la anulación de la ganancia neta provista por el amplificador [cite: 6, 9].

---

## Dinámica de Impedancia (50 \Omega vs. 75 \Omega) y Conectórica RF

El estándar de la industria de telecomunicaciones móviles está fijado rigurosamente en una impedancia característica (Z_0) de 50\ \Omega [cite: 5, 7, 10, 11]. Esta cifra representa un compromiso físico óptimo entre la capacidad de manejo de potencia pico (obtenida idealmente a 30\ \Omega) y la mínima atenuación por voltaje en líneas coaxiales con dieléctrico de aire (obtenida idealmente a 77\ \Omega). Por otro lado, la industria de televisión por cable (CATV) y video residencial utiliza de manera generalizada el estándar de 75\ \Omega respaldado por cables económicos tipo RG-6 y conectores F [cite: 5, 10, 12, 13].

Cuando se interconecta una unidad amplificadora de 50\ \Omega con una línea de transmisión o antena de 75\ \Omega mediante adaptadores pasivos, se induce una discontinuidad de impedancia en la interfaz [cite: 10, 13]. Esta condición genera una onda estacionaria debido a la reflexión parcial de la energía incidente [cite: 9]. El coeficiente de reflexión de voltaje (\Gamma) asociado a la interfaz entre 50\ \Omega y 75\ \Omega se calcula de la siguiente manera:

\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{75 - 50}{75 + 50} = \frac{25}{125} = 0.2

A partir de este coeficiente, se deriva la Relación de Onda Estacionaria de Voltaje (VSWR):

\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{1 + 0.2}{1 - 0.2} = \frac{1.2}{0.8} = 1.5:1

Una relación VSWR de 1.5:1 genera una pérdida por desadaptación de impedancia (*mismatch loss*) calculada explícitamente como:

L_{\text{desadaptación}} = -10 \log_{10}(1 - |\Gamma|^2) = -10 \log_{10}(1 - 0.04) \approx 0.177\text{ dB}

Aunque una pérdida directa de ~0.18 dB por desadaptación individual representa un valor acotado, la presencia de múltiples interfaces desadaptadas (antena exterior, entradas del amplificador, divisores de potencia y antenas interiores) desencadena reflexiones múltiples. En la práctica, el acoplamiento directo entre un sistema de amplificación celular de 50\ \Omega e infraestructura de 75\ \Omega introduce degradaciones que oscilan habitualmente entre 0.5 dB y 1.0 dB por punto de transición, lo que equivale a una disipación no deseada superior al 11% de la potencia del sistema [cite: 9]. Además del impacto en la potencia transmitida, la onda reflejada retorna hacia las etapas finales del amplificador de potencia (PA) o del amplificador de bajo ruido (LNA), incrementando la figura de ruido general, induciendo distorsión por intermodulación y provocando la activación errónea de las rutinas automáticas de reducción de ganancia del equipo [cite: 1, 2].

La selección de la conectórica mecánica debe responder estrictamente a la impedancia de diseño y a la banda de frecuencia de operación. El conector Tipo N es el estándar profesional en 50\ \Omega, caracterizado por un mecanismo de acoplamiento roscado estanco, una excelente respuesta en frecuencias de DC a 11 GHz y la capacidad de acomodar cables gruesos como LMR-400 o Heliax sin introducir discontinuidades severas [cite: 10, 11, 13]. El conector SMA opera igualmente en 50\ \Omega en un formato subminiatura de alta precisión, orientado primordialmente a jumpers internos y puertos de prueba en equipos compactos. En contraste, el conector Tipo F es una interfaz de bajo costo de 75\ \Omega orientada a aplicaciones de video que utiliza el propio conductor central del cable RG-6 como pin de contacto, por lo que su uso debe evitarse en sistemas celulares profesionales de 50\ \Omega [cite: 10, 12, 13].

---

## Mecanismos de Control de Ganancia, Aislamiento y Mitigación de Ruido

Los repetidores celulares modernos incorporan arquitecturas de procesamiento en tiempo real diseñadas para proteger la integridad de la red radioeléctrica del operador [cite: 1, 2, 14]. El funcionamiento incontrolado de un amplificador analógico convencional puede saturar el canal de subida (*uplink*), degradando el umbral de sensibilidad de recepción de la estación base (BTS) y provocando la caída de llamadas en la celda [cite: 1, 3].

Para prevenir estas interferencias, los equipos homologados incorporan circuitos de Control Automático de Ganancia (AGC) y módulos de autoprotección [cite: 1, 2, 14]. El módulo AGC monitorea continuamente los niveles de potencia recibidos y transmitidos en los enlaces ascendente y descendente [cite: 1]. Si la señal proveniente de la BTS se eleva drásticamente por la activación de una celda cercana o si la señal del enlace ascendente se aproxima al punto de saturación, el AGC ajusta dinámicamente la ganancia del repetidor para evitar la emisión de productos de intermodulación fuera de banda, manteniendo las emisiones espurias por debajo de los límites normativos internacionales (típicamente -19\text{ dBm} en los puertos de RF) [cite: 1, 2].

Un segundo mecanismo de control esencial es la función de Modo de Espera Automático (*Automatic Standby*) [cite: 2]. Cuando no hay dispositivos móviles activos transmitiendo en la zona cubierta por la antena servidora interior, el amplificador reduce automáticamente el piso de ruido inyectado hacia la estación base [cite: 2]. Las normativas técnicas actuales exigen que, tras un periodo máximo de 5 minutos sin tráfico de usuario activo, el equipo reduzca la potencia de ruido en el *uplink* a un nivel inferior o igual a -70\text{ dBm/MHz} expresado en Potencia Isotrópica Radiada Equivalente (p.i.r.e. / EIRP), salvaguardando la capacidad de la red pública [cite: 2].

---

## Marco Regulatorio Internacional y Homologación Técnica

Debido a que los amplificadores celulares transmiten en frecuencias bajo concesión estatal, la importación, distribución e instalación de estos dispositivos están sujetas a la fiscalización de las autoridades nacionales de telecomunicaciones [cite: 3, 15, 16]. La instalación de amplificadores no homologados o desprovistos de circuitos de autoprotección genera severas interferencias en el espectro público, lo que constituye una infracción legal sujeta a decomiso de infraestructura y sanciones administrativas o penales [cite: 3, 15].

En Estados Unidos, la Comisión Federal de Comunicaciones (FCC) establece los requisitos mediante la norma **FCC Part 20.21** (*Consumer Signal Booster Standards*), exigiendo mecanismos de apagado automático ante oscilaciones y control de potencia de *uplink* [cite: 1, 17]. En América Latina, los marcos regulatorios han evolucionado para exigir un control técnico equivalente sobre las emisiones radioeléctricas y la seguridad poblacional frente a campos electromagnéticos [cite: 3, 15, 18].

En Chile, la Subsecretaría de Telecomunicaciones (SUBTEL) establece mediante su propuesta de norma técnica para repetidores que los equipos deben limitar su potencia máxima según la clase 3GPP Power Class 3, mantener la intermodulación por debajo de -19\text{ dBm} e integrar la función *Automatic Standby* para reducir el ruido en *uplink* a un máximo de -70\text{ dBm/MHz} [cite: 2]. Asimismo, el régimen general de homologación de equipos de alcance reducido bajo la **Resolución Exenta 737** (que modifica la Res. 1985) exige un proceso de autodeclaración técnica acompañado por la colocación obligatoria de un código QR impreso en el empaque del producto (de dimensiones mínimas de 1\text{ cm} \times 1\text{ cm}, nivel de corrección de errores del 30% y sin marcos), el cual debe redirigir a una página web en idioma español que contenga el informe de ensayos y los datos del representante legal en el país [cite: 15, 16, 19].

En México, el Instituto Federal de Telecomunicaciones (IFT), a través de su Unidad de Cumplimiento, fiscaliza el uso del espectro radioeléctrico conforme a la Ley Federal de Telecomunicaciones y Radiodifusión (LFTR) [cite: 3]. El uso de amplificadores celulares ilegales o no homologados que afecten las redes de los concesionarios da lugar a procedimientos sancionatorios estipulados en los artículos 297, 298 y 299 de la LFTR, los cuales contemplan el aseguramiento cautelar de los equipos, el decomiso definitivo y multas económicas de consideración [cite: 3].

En Colombia, la Agencia Nacional del Espectro (ANE) regula los límites de exposición a campos electromagnéticos mediante la **Resolución 773 de 2023** [cite: 18]. Esta norma obliga a los operadores e instaladores de estaciones y repetidores a realizar una *Evaluación Simplificada* para verificar las distancias de seguridad y evitar que las radiaciones no ionizantes superen las restricciones normativas en zonas de acceso público [cite: 18]. Por su parte, en Argentina, el Ente Nacional de Comunicaciones (ENACOM) exige el cumplimiento de la **Resolución 3690/04 (CNC)**, requiriendo que los titulares de instalaciones radioeléctricas demuestren formalmente que los niveles de emisión generados no afectan a la población en el entorno circundante [cite: 20].

|   |   |   |   |   |

| --- | --- | --- | --- | --- |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

|   |   |   |   |   |

---

## Conclusiones e Implicaciones de Ingeniería de Despliegue

La ingeniería de proyectos de amplificación celular exige priorizar el equilibrio térmico y electromagnético en el presupuesto de enlace sobre la simple amplificación bruta de la señal. La selección de la línea de transmisión coaxial constituye el factor determinante en la eficiencia global de la instalación. En frecuencias de telefonía móvil pertenecientes a las bandas AWS, 2.6 GHz y Sub-6 GHz 5G, la atenuación Dieléctrica domina las pérdidas de la línea, haciendo inaceptable el uso de cables coaxiales tradicionales con dieléctrico de polietileno sólido. Para trayectos comerciales o residenciales superiores a 15 metros, la especificación técnica debe inclinarse hacia líneas de ultra baja pérdida basadas en espuma inyectada por gas, como el LMR-400 o cables corrugados tipo Heliax de 1/2 pulgada, evitando que la atenuación del cable anule la ganancia provista por la unidad central.

Asimismo, la preservación de una impedancia homogénea de 50\ \Omega a lo largo de toda la cadena radioeléctrica es indispensable para garantizar el rendimiento del sistema y evitar fallas en los amplificadores. La introducción de componentes pasivos de 75\ \Omega o conectores F genera desadaptaciones que inducen relaciones de onda estacionaria (VSWR) superiores a 1.5:1. Las reflexiones de potencia asociadas degradan la figura de ruido del receptor, disipan energía en forma de calor y alteran el funcionamiento del Control Automático de Ganancia (AGC). Por tanto, la conectórica debe estandarizarse en interfaces profesionales roscadas tipo N para tendidos principales e interfaces SMA para interconexiones de precisión.

Desde el punto de vista operativo y legal, la viabilidad de una instalación depende del cumplimiento estricto de las normativas de espectro radioeléctrico dictadas por los organismos reguladores nacionales. Los sistemas de amplificación deben incorporar rutinas de control en tiempo real capaces de limitar los productos de intermodulación y desactivar la transmisión en la banda de subida (*uplink*) mediante el modo de espera automático (*Automatic Standby*) cuando no existan usuarios activos. El despliegue de equipos homologados garantiza que la mejora de la cobertura celular interior se ejecute de manera transparente, protegiendo la infraestructura de las estaciones base circundantes y asegurando la estabilidad a largo plazo del servicio.

---

US20180323860A1 - Signal booster system with automatic gain control - Google Patents, [https://patents.google.com/patent/US20180323860A1/en](https://patents.google.com/patent/US20180323860A1/en)

FIJA NORMA TÉCNICA PARA LA INSTALACIÓN Y USO DE AMPLIFICADORES O REPETIDORES QUE SE - SUBTEL, [https://www.subtel.gob.cl/wp-content/uploads/2026/03/Propuesta_de_Norma_Tecnica_instalacion_y_el_uso_de_amplificadores_o_repetidores.pdf](https://www.subtel.gob.cl/wp-content/uploads/2026/03/Propuesta_de_Norma_Tecnica_instalacion_y_el_uso_de_amplificadores_o_repetidores.pdf)

el IFT, [https://www.ift.org.mx/sites/default/files/industria/notificacionesdiarias/unidad-de-cumplimiento/2021/01/dipticouc-impresion.pdf](https://www.ift.org.mx/sites/default/files/industria/notificacionesdiarias/unidad-de-cumplimiento/2021/01/dipticouc-impresion.pdf)

How to Read a Coaxial Cable Datasheet: Buyer Guide to RF Specs, [https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet](https://wireharnessproduction.com/blog/how-to-read-a-coaxial-cable-datasheet)

Coaxial Cable Attenuation & Power Loss Calculator - TelecomCalculators, [https://telecomcalculators.com/calculators/rf-transmission-lines/coax-cable-attenuation/](https://telecomcalculators.com/calculators/rf-transmission-lines/coax-cable-attenuation/)

Coaxial Cable Loss Calculator - everything RF, [https://www.everythingrf.com/rf-calculators/coaxial-cable-loss-calculator](https://www.everythingrf.com/rf-calculators/coaxial-cable-loss-calculator)

Coax Loss Calculator - Cable Attenuation & Power - Turn2engineering, [https://turn2engineering.com/calculators/coax-loss-calculator](https://turn2engineering.com/calculators/coax-loss-calculator)

Coax Cable Loss Calculator — dB for LMR-400, RG-58, RG-213 - rftools.io, [https://rftools.io/calculators/rf/coax-loss/](https://rftools.io/calculators/rf/coax-loss/)

User Guide: Com-Power Cable Loss & Attenuation Calculator, [https://www.com-power.com/tech-notes/user-guide--com-power-cable-loss---attenuation-calculator](https://www.com-power.com/tech-notes/user-guide--com-power-cable-loss---attenuation-calculator)

Connectors from old booster to new : r/CellBoosters - Reddit, [https://www.reddit.com/r/CellBoosters/comments/1lld2v5/connectors_from_old_booster_to_new/](https://www.reddit.com/r/CellBoosters/comments/1lld2v5/connectors_from_old_booster_to_new/)

SureCall 50-ohm Lightning Protector – SC-LP - Northstar, [https://shop.northstardist.com/product/surecall-50-ohm-lightning-protector/](https://shop.northstardist.com/product/surecall-50-ohm-lightning-protector/)

The Complete Guide to Coaxial Cable Types and Their ... - AIChipLink, [https://aichiplink.com/blog/complete-guide-to-coaxial-cable-types-and-applications_1651](https://aichiplink.com/blog/complete-guide-to-coaxial-cable-types-and-applications_1651)

Top Signal N-Female to F-Male Connector | TS451027, [https://powerfulsignal.com/top-signal-n-female-to-f-male-connector-ts451027/](https://powerfulsignal.com/top-signal-n-female-to-f-male-connector-ts451027/)

Cómo Mejorar la Señal Celular en Subterráneos, Bodegas y Faenas Mineras en Chile, [https://smarthold.cl/blogs/noticias/como-mejorar-la-senal-celular-en-subterraneos-bodegas-y-faenas-mineras-en-chile](https://smarthold.cl/blogs/noticias/como-mejorar-la-senal-celular-en-subterraneos-bodegas-y-faenas-mineras-en-chile)

Resolución 737 SUBTEL: guía completa 2026 para equipos de alcance reducido en Chile, [https://certificacion-telecom.cl/blog/resolucion-737-subtel-guia-completa-2026/](https://certificacion-telecom.cl/blog/resolucion-737-subtel-guia-completa-2026/)

Equipos de Alcance Reducido - Subsecretaría de Telecomunicaciones de Chile, [https://www.subtel.gob.cl/equipos-de-alcance-reducido/](https://www.subtel.gob.cl/equipos-de-alcance-reducido/)

WO2017176840A1 - Détection de signal de bande étroite pour une, [https://www.google.com/patents/WO2017176840A1?cl=fr](https://www.google.com/patents/WO2017176840A1?cl=fr)

Antenas y Bienestar - Agencia Nacional del Espectro, [https://www.ane.gov.co/SitePages/Antenas-Salud/faq.aspx](https://www.ane.gov.co/SitePages/Antenas-Salud/faq.aspx)

Ley Chile - Resolución 737 Exenta (22-may-2025) M. de Transportes y Telecomunicaciones, [https://www.bcn.cl/leychile/navegar?idNorma=1213556](https://www.bcn.cl/leychile/navegar?idNorma=1213556)

Antenas - Normativa - Enacom, [https://www.enacom.gob.ar/antenas_p120/normativas](https://www.enacom.gob.ar/antenas_p120/normativas)