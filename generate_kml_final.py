import math
import zipfile
import os

# COORDENADA EXACTA DE LA AZOTEA DEL EDIFICIO CONSISTORIAL PAC
# Calculada rigurosamente a partir del polígono de Google Earth entregado por el usuario ("muni edificio .kmz")
lat_azotea = -33.488334
lon_azotea = -70.664339

# Polígono oficial dibujado por el usuario en Google Earth Pro
poly_coords_str = (
    "-70.66353404277331,-33.48803916758069,0 "
    "-70.6641097644153,-33.48783495764584,0 "
    "-70.66477368378537,-33.48877364797999,0 "
    "-70.66397789684351,-33.48897126989567,0 "
    "-70.66353404277331,-33.48803916758069,0"
)

def make_circle(radius_m, num_pts=72):
    coords = []
    for i in range(num_pts + 1):
        angle = (2 * math.pi * i) / num_pts
        dx = radius_m * math.sin(angle)
        dy = radius_m * math.cos(angle)
        dlat = dy / 111139.0
        dlon = dx / (111139.0 * math.cos(math.radians(lat_azotea)))
        coords.append(f"{lon_azotea + dlon:.6f},{lat_azotea + dlat:.6f},0")
    return " ".join(coords)

towers = [
  ("T1", "Claro — 43_691 (Apolo Teresa Vial)", -33.489442, -70.666942, 18, "Claro", "styleLineClaro", "Torre 9 m autosoportada", "2600 / 3500 MHz (4G/5G) + B2/B5 macro"),
  ("T2", "WOM — RM3519 (Teresa Vial fte. 2431)", -33.489261, -70.668114, 20, "WOM", "styleLineWOM", "Poste 12 m", "AWS 1700/2100 MHz (Banda 4 nativa)"),
  ("T3", "WOM — RM4114 (Nueva Seis 1951)", -33.485697, -70.664664, 20, "WOM", "styleLineWOM", "Poste 12 m", "AWS 1700/2100 MHz (Banda 4 nativa)"),
  ("T4", "Entel + Movistar — UZM482 / BALAK13 (Parque Jarlan)", -33.489167, -70.669167, 22, "Shared", "styleLineShared", "Monoposte 12 m", "850 (B5) / 1900 (B2) / 2600 / 3500 MHz"),
  ("T5", "Claro + Entel — 13_851 / GVM662 (Ruta 5 esq. Salesianos)", -33.490000, -70.660833, 35, "Shared", "styleLineShared", "Monoposte 30 m", "850 (B5) / 1900 (B2) / 2600 / 3500 MHz"),
  ("T6", "Entel + Claro — URS078 (Club Hipico 3365)", -33.484167, -70.665000, 22, "Entel", "styleLineEntel", "Monoposte 12 m", "1900 (B2 PCS) / 2600 / 3500 MHz"),
  ("T7", "Claro — 13_517 (Angel Guarello esq. Mendelssohn)", -33.490278, -70.671111, 40, "Claro", "styleLineClaro", "Monoposte 36 m", "850 (B5) / 1900 (B2) / 2600 / 3500 MHz"),
  ("T8", "WOM — RM3502 (Club Hipico 4811)", -33.492969, -70.668775, 22, "WOM", "styleLineWOM", "Monoposte 12 m", "AWS 1700/2100 MHz (Banda 4)"),
  ("T9", "Movistar + Entel + Claro — MSA614 (La Marina 2725)", -33.491544, -70.671981, 32, "Shared", "styleLineShared", "Monoposte 28 m", "1900 (B2 PCS) / 2600 / 3500 MHz"),
  ("T10", "Movistar + Entel + Claro — USA803 (J.J. Prieto 4850)", -33.494722, -70.662778, 35, "Shared", "styleLineShared", "Torre 30 m", "850 (B5) / 1900 (B2) / 2600 / 3500 MHz")
]

kml_parts = [
f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>🎯 Antena Donante y Enlaces SUBTEL — Centro Consistorial PAC</name>
    <open>1</open>
    <description><![CDATA[
      <h2>Tecnovoa Ltda. — Centro Consistorial I. Municipalidad de Pedro Aguirre Cerda</h2>
      <p><b>Centro Donante Exacto:</b> Azotea Técnica sobre Shaft GI 07/08 (+8,25 m)<br/>
      <b>Coordenadas de la Antena:</b> {lat_azotea:.6f}, {lon_azotea:.6f}<br/>
      <b>Dirección:</b> Av. Presidente Salvador Allende N° 2029 (esq. Club Hípico y Manuela Errázuriz)<br/>
      <b>Solución de Ingeniería:</b> weBoost Office 200 LATAM (SKU 531047)<br/>
      <b>Contraparte Municipal:</b> Álvaro O. Carreño Cerda — Jefe Depto. Informática (SECPLA)<br/>
      <b>KAM TI Tecnovoa:</b> Cristián Díaz (cristian@tecnovoa.cl / +569 4943 8288)</p>
    ]]></description>

    <LookAt>
      <longitude>{lon_azotea:.6f}</longitude>
      <latitude>{lat_azotea:.6f}</latitude>
      <altitude>0</altitude>
      <heading>325</heading>
      <tilt>52</tilt>
      <range>780</range>
      <altitudeMode>clampToGround</altitudeMode>
    </LookAt>

    <!-- ============================================== -->
    <!-- ESTILOS VISUALES DE ALTO IMPACTO EN GOOGLE EARTH -->
    <!-- ============================================== -->
    <Style id="styleAntenaCentro">
      <IconStyle>
        <scale>2.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/target.png</href>
        </Icon>
        <color>ff00ff00</color>
      </IconStyle>
      <LabelStyle>
        <color>ff00ff00</color>
        <scale>1.25</scale>
      </LabelStyle>
    </Style>

    <!-- Estilo Polígono del Edificio (Borde Azul Tecnovoa + Relleno Translúcido) -->
    <Style id="stylePoligonoMuni">
      <LineStyle>
        <color>ffa05f14</color>
        <width>3.5</width>
      </LineStyle>
      <PolyStyle>
        <color>40a05f14</color>
      </PolyStyle>
    </Style>

    <Style id="stylePinEdificio">
      <IconStyle>
        <scale>1.4</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
        </Icon>
        <color>ff145fa0</color>
      </IconStyle>
      <LabelStyle>
        <color>ffffffff</color>
        <scale>1.1</scale>
      </LabelStyle>
    </Style>

    <Style id="stylePinPuntoCritico">
      <IconStyle>
        <scale>1.4</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/paddle/red-diamond.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <color>ff0000ff</color>
        <scale>1.05</scale>
      </LabelStyle>
    </Style>

    <!-- Estilos de Torres -->
    <Style id="stylePinClaro">
      <IconStyle><scale>1.35</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/red-circle.png</href></Icon></IconStyle>
      <LabelStyle><color>ff0000ff</color><scale>0.95</scale></LabelStyle>
    </Style>

    <Style id="stylePinWOM">
      <IconStyle><scale>1.35</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/purple-circle.png</href></Icon></IconStyle>
      <LabelStyle><color>ffff00ff</color><scale>0.95</scale></LabelStyle>
    </Style>

    <Style id="stylePinEntel">
      <IconStyle><scale>1.35</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/blu-circle.png</href></Icon></IconStyle>
      <LabelStyle><color>ffffaa00</color><scale>0.95</scale></LabelStyle>
    </Style>

    <Style id="stylePinShared">
      <IconStyle><scale>1.45</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href></Icon></IconStyle>
      <LabelStyle><color>ff00d7ff</color><scale>1.0</scale></LabelStyle>
    </Style>

    <!-- Líneas de Enlace Radiales (Gruesas, Nítidas y Coloreadas por Operador) -->
    <Style id="styleLineClaro">
      <LineStyle><color>ff0000ff</color><width>4.5</width></LineStyle>
    </Style>
    <Style id="styleLineWOM">
      <LineStyle><color>ffff00ff</color><width>4.5</width></LineStyle>
    </Style>
    <Style id="styleLineEntel">
      <LineStyle><color>ffffaa00</color><width>4.5</width></LineStyle>
    </Style>
    <Style id="styleLineShared">
      <LineStyle><color>ff00d7ff</color><width>4.5</width></LineStyle>
    </Style>

    <!-- Anillos de Radar -->
    <Style id="styleRadarRing">
      <LineStyle><color>8800ffff</color><width>2.5</width></LineStyle>
    </Style>

    <!-- FOLDER 1: CENTRO DE ENLACE SOBRE EL EDIFICIO MUNICIPAL -->
    <Folder>
      <name>🏢 Edificio Municipal PAC &amp; Antena Donante en Azotea</name>
      <open>1</open>
      
      <!-- Polígono del Edificio (Entregado por el usuario en muni edificio .kmz) -->
      <Placemark>
        <name>Huella Edificio Consistorial PAC</name>
        <styleUrl>#stylePoligonoMuni</styleUrl>
        <description><![CDATA[
          <b>Perímetro del Edificio Consistorial PAC:</b> Av. Salvador Allende N° 2029<br/>
          Georreferenciado directamente desde <i>muni edificio .kmz</i>.
        ]]></description>
        <Polygon>
          <tessellate>1</tessellate>
          <altitudeMode>clampToGround</altitudeMode>
          <outerBoundaryIs>
            <LinearRing>
              <coordinates>{poly_coords_str}</coordinates>
            </LinearRing>
          </outerBoundaryIs>
        </Polygon>
      </Placemark>

      <!-- Punto Donante en Azotea -->
      <Placemark>
        <name>🎯 ANTENA DONANTE: Omni Plus 360° (Azotea Municipalidad PAC)</name>
        <styleUrl>#styleAntenaCentro</styleUrl>
        <description><![CDATA[
          <h2>🎯 Antena Exterior Omni Plus (314422) — weBoost Office 200</h2>
          <p><b>Ubicación Exacta:</b> Azotea del Centro Consistorial PAC (+8,25 m), sobre el Shaft técnico GI 07/08.<br/>
          <b>Coordenadas:</b> {lat_azotea:.6f}, {lon_azotea:.6f}<br/>
          <b>Función:</b> Punto central de enlace. Desde este punto exacto del techo se capta en 360° la señal directa de las 10 radiobases circundantes.<br/>
          <b>Bajada Coaxial:</b> Rollo de 18,28 m Wilson400 baja directamente por el shaft vertical hacia el subterráneo (cota -3,20 m).</p>
        ]]></description>
        <Point>
          <altitudeMode>relativeToGround</altitudeMode>
          <extrude>1</extrude>
          <coordinates>{lon_azotea:.6f},{lat_azotea:.6f},20</coordinates>
        </Point>
      </Placemark>

      <Placemark>
        <name>Acceso Principal (Av. Salvador Allende N° 2029)</name>
        <styleUrl>#stylePinEdificio</styleUrl>
        <description><![CDATA[
          <b>Acceso Peatonal:</b> Av. Presidente Salvador Allende N° 2029 esq. Manuela Errázuriz.
        ]]></description>
        <Point>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>-70.664376,-33.488872,0</coordinates>
        </Point>
      </Placemark>

      <Placemark>
        <name>🔴 P6: Oficina Álvaro Carreño — Informática (ZONA MUERTA SUBTERRÁNEA)</name>
        <styleUrl>#stylePinPuntoCritico</styleUrl>
        <description><![CDATA[
          <b>Nivel -1 (Cota -3,20 m):</b> RSRP -114 dBm | SINR &lt; 0 dB.<br/>
          <b>Falla Actual:</b> CALL DROP (Llamadas cortadas / No entran llamadas bajo las dos losas de hormigón armado).<br/>
          <b>Solución:</b> Antena Domo Interior (314407) en cielo falso alimentada por el amplificador Office 200.
        ]]></description>
        <Point>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>-70.664280,-33.488420,0</coordinates>
        </Point>
      </Placemark>

      <Placemark>
        <name>🔴 P8: Archivo Municipal (APAGÓN TOTAL DE SEÑAL)</name>
        <styleUrl>#stylePinPuntoCritico</styleUrl>
        <description><![CDATA[
          <b>Nivel -1 Fondo Enterrado:</b> RSRP &lt; -120 dBm / Sin Servicio (Solo llamadas de emergencia).
        ]]></description>
        <Point>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>-70.663950,-33.488120,0</coordinates>
        </Point>
      </Placemark>
    </Folder>

    <!-- FOLDER 2: LÍNEAS RADIALES QUE NACEN EN EL TECHO DE LA MUNICIPALIDAD -->
    <Folder>
      <name>📐 Líneas de Enlace que Nacen en la Azotea Municipal ➔ Torres</name>
      <open>1</open>
'''
]

for tid, tname, tlat, tlon, th, top, tstyle, tsop, tbands in towers:
    dlat = (tlat - lat_azotea) * 111139
    dlon = (tlon - lon_azotea) * 111139 * math.cos(math.radians(lat_azotea))
    dist = math.hypot(dlat, dlon)
    az = (math.degrees(math.atan2(dlon, dlat)) + 360) % 360
    card = 'N' if az < 22.5 or az >= 337.5 else ('NE' if az < 67.5 else ('E' if az < 112.5 else ('SE' if az < 157.5 else ('S' if az < 202.5 else ('SO' if az < 247.5 else ('O' if az < 292.5 else 'NO'))))))

    kml_parts.append(f'''      <Placemark>
        <name>Enlace Azotea ➔ {tid}: {top} ({dist:.0f} m / {az:.0f}° {card})</name>
        <styleUrl>#{tstyle}</styleUrl>
        <description><![CDATA[
          <b>Origen (Centro Donante):</b> Azotea Edificio Municipal PAC ({lat_azotea:.6f}, {lon_azotea:.6f})<br/>
          <b>Estación Base Celular:</b> {tname}<br/>
          <b>Distancia en Línea Recta:</b> <b>{dist:.0f} metros</b><br/>
          <b>Acimut:</b> <b>{az:.0f}° ({card})</b><br/>
          <b>Bandas Frecuencia:</b> {tbands}
        ]]></description>
        <LineString>
          <tessellate>1</tessellate>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>
            {lon_azotea:.6f},{lat_azotea:.6f},0
            {tlon:.6f},{tlat:.6f},0
          </coordinates>
        </LineString>
      </Placemark>''')

kml_parts.append('''    </Folder>

    <!-- FOLDER 3: ANILLOS DE COBERTURA 360° CENTRADOS EN LA AZOTEA MUNICIPAL -->
    <Folder>
      <name>🌐 Anillos Radiales de Alcance (Centrados en la Azotea)</name>
      <open>1</open>

      <Placemark>
        <name>Anillo 300 m (Radio Inmediato: Claro T1 y WOM T3)</name>
        <styleUrl>#styleRadarRing</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>''' + make_circle(300) + '''</coordinates>
        </LineString>
      </Placemark>

      <Placemark>
        <name>Anillo 500 m (Radio Medio: WOM T2, Claro/Entel T5, Entel/Mvs T4, Entel T6)</name>
        <styleUrl>#styleRadarRing</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>''' + make_circle(500) + '''</coordinates>
        </LineString>
      </Placemark>

      <Placemark>
        <name>Anillo 750 m (Alcance Completo SUBTEL)</name>
        <styleUrl>#styleRadarRing</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <altitudeMode>clampToGround</altitudeMode>
          <coordinates>''' + make_circle(750) + '''</coordinates>
        </LineString>
      </Placemark>
    </Folder>

    <!-- FOLDER 4: LAS 10 ESTACIONES BASE SUBTEL -->
    <Folder>
      <name>📡 Las 10 Estaciones Base Celulares SUBTEL (&lt; 750 m)</name>
      <open>1</open>
''')

for tid, tname, tlat, tlon, th, top, tstyle, tsop, tbands in towers:
    pin_style = 'stylePinClaro' if top == 'Claro' else ('stylePinWOM' if top == 'WOM' else ('stylePinEntel' if top == 'Entel' else 'stylePinShared'))
    dlat = (tlat - lat_azotea) * 111139
    dlon = (tlon - lon_azotea) * 111139 * math.cos(math.radians(lat_azotea))
    dist = math.hypot(dlat, dlon)
    az = (math.degrees(math.atan2(dlon, dlat)) + 360) % 360

    kml_parts.append(f'''      <Placemark>
        <name>{tid}: {tname}</name>
        <styleUrl>#{pin_style}</styleUrl>
        <description><![CDATA[
          <b>Estación:</b> {tname}<br/>
          <b>Operador:</b> {top}<br/>
          <b>Distancia al Techo Municipal:</b> {dist:.0f} m (Acimut {az:.0f}°)<br/>
          <b>Soporte / Altura:</b> {tsop}<br/>
          <b>Bandas Frecuencia:</b> {tbands}<br/>
          <b>Compatibilidad weBoost Office 200:</b> ✅ Compatible Bandas B2 (1900), B4 (AWS), B5 (850)
        ]]></description>
        <Point>
          <altitudeMode>relativeToGround</altitudeMode>
          <extrude>1</extrude>
          <coordinates>{tlon:.6f},{tlat:.6f},{th}</coordinates>
        </Point>
      </Placemark>''')

kml_parts.append('''    </Folder>

  </Document>
</kml>''')

full_kml = "\n".join(kml_parts)

# 1. Guardar KML
with open("Antenas_SUBTEL_PAC_Consistorial.kml", "w", encoding="utf-8") as f:
    f.write(full_kml)

# 2. Guardar KMZ (comprimido oficial para Google Earth)
with zipfile.ZipFile("Antenas_SUBTEL_PAC_Consistorial.kmz", "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("doc.kml", full_kml.encode("utf-8"))

print("DONE! Both Antenas_SUBTEL_PAC_Consistorial.kml and .kmz generated perfectly!")
