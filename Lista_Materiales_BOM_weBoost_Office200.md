# Lista de Materiales e Ingeniería (BOM): Solución Dual weBoost Office 200 LATAM
**Proyecto:** Optimización de Señal Celular Indoor (Pisos -1 y 1) y Red Outdoor en Techumbre  
**Cliente:** Ilustre Municipalidad de Pedro Aguirre Cerda (Centro Consistorial)  
**Integrador:** Tecnovoa Ltda. — KAM TI: Cristián Díaz (`cristian@tecnovoa.cl` / `+569 4943 8288`)  
**Ingeniería:** Javier De la Fuente & Diego Pérez Ibarra  
**Fabricante de Hardware:** **Wilson Electronics / weBoost (Línea Profesional 50 Ω)**  

---

## 📦 1. Componentes Incluidos por Cada Kit `weBoost Office 200 LATAM (SKU 531047)`

| Ítem | Componente Oficial Wilson | N° de Parte (SKU) | Cant. por Kit | Especificación y Rol en la Instalación |
| :---: | :--- | :---: | :---: | :--- |
| **1.1** | **Amplificador de Señal Office 200 LATAM** | `460047` | 1 | Unidad central de ganancia variable (74 dB máx., +22 dBm Downlink). Bandas: B5 (850), B4 (AWS 1700/2100), B2 (1900 PCS). Pantalla táctil LCD a color y tecnología patentada XDR (anti-saturación). |
| **1.2** | **Antena Exterior Omni Plus 360° (50 Ω)** | `314422` | 1 | Antena exterior omnidireccional con conector N-Hembra. Se monta en los postes existentes de `3,5 m` en la techumbre (extremos Norte y Sur). |
| **1.3** | **Antena Interior Domo de Perfil Bajo (50 Ω)** | `314407` | 1 | Antena omnidireccional para cielo falso (`h = 2,60 m`). |
| **1.4** | **Protector Contra Sobretensiones / Rayos** | `859902` | 1 | Protector de descarga de gas 50 Ω (N-Hembra a N-Hembra, DC-3 GHz). |
| **1.5** | **Jumper Coaxial Wilson400 (0,60 m)** | `952302` | 1 | Tramo de interconexión entre el Amplificador y el Protector de Relámpagos `859902`. |
| **1.6** | **Cable Coaxial Wilson400 Tramo Donante (18,28 m)** | `952360` | 1 | Bobina LMR-400 de 50 Ω con conectores N-Macho premontados. Conecta la antena en el poste de techumbre con el rack interior. |
| **1.7** | **Cable Coaxial Wilson400 Tramo Servidor Largo (22,86 m)** | `952375` | 1 | Bobina LMR-400 de 50 Ω con conectores N-Macho premontados. Cubre los tramos largos hacia Video Wall/Despacho (Norte) e Informática/Pasillo Trasero (Sur). |
| **1.8** | **Fuente de Alimentación AC/DC 220V** | `850021` | 1 | Transformador 12V / 3.0A (Consumo máximo: 20 W). |

---

## 🔀 2. Cuadro Consolidado de Equipamiento para Arquitectura Maestra (2 Alas / 4 Antenas Domo)

Para cubrir tanto el **Ala Norte/Poniente (Video Wall, Seguridad Ciudadana, Despacho de Móviles y Servicios Especiales)** como el **Ala Sur/Oriente (Óvalo del Alcalde en Piso 1, Oficina de Álvaro Carreño y Pasillo Trasero en Piso -1)**:

| Ítem | SKU Wilson | Componente | Cant. (1 Ala · 2 Domos) | Cant. (2 Alas · 4 Domos) | Función Técnica |
| :---: | :---: | :--- | :---: | :---: | :--- |
| **01** | `531047` | **Kit Base weBoost Office 200 LATAM (50 Ω)** | 1 Kit | **2 Kits** | Provee los 2 amplificadores, 2 antenas exteriores, 2 domos base, 2 cables de `18,28 m` y 2 cables de `22,86 m`. |
| **02** | `859957` | **Wideband 2-Way Splitter (698–2700 MHz, 50 Ω)** | 1 un. | **2 un.** | Divide la salida de cada amplificador en 2 ramas interiores (`-3,2 dB`). |
| **03** | `314407` | **Antena Interior Domo de Perfil Bajo Adicional (50 Ω)** | 1 un. | **2 un.** | Suma 2 domos adicionales a los 2 ya incluidos en los kits (Total = **4 Domos Interiores**). |
| **04** | `952350` | **Cable Coaxial Wilson400 de 50 ft / 15,24 m (N-Macho)** | 1 rollo | **2 rollos** | Alimenta la segunda salida de cada splitter (hacia Servicios Especiales y hacia el Óvalo del Alcalde). |
| **05** | `952302` | **Jumper Coaxial Wilson400 de 2 ft / 0,60 m (N-Macho)** | 1 un. | **2 un.** | Une el puerto Indoor de cada amplificador con la entrada `INPUT` de su Splitter `859957`. |

---

## 🌐 3. Requerimiento Complementario en Techumbre (Drones y Fluviómetro)

| Ítem | Especialidad | Descripción del Requerimiento | Cantidad |
| :---: | :--- | :--- | :---: |
| **R-01** | **Cableado Estructurado Exterior** | Habilitación de puntos de red Cat.6 para intemperie en techumbre (conectados a Rack SecPlan Piso 2 o Rack Seguridad Piso -1) para operación de drones y estación meteorológica. | **2 Puntos** |
| **R-02** | **Wi-Fi Outdoor** | Suministro e integración de Access Point **Cisco Meraki Outdoor** compatible con el portal Dashboard existente de la Municipalidad. | **1 Unidad** |
