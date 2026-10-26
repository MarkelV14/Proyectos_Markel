# 🔴 WISH Pokédex - Pokémon Kudeaketa Sistema / Sistema de Gestión Pokémon


---

# 🟢 WISH Pokédex - Pokémon Kudeaketa Sistema (EU)

**WISH Pokédex** **Python (Flask)** eta **SQLite** erabiliz garatutako web-aplikazio bat da. Erabiltzaileei beren Pokémon bilduma propioa (1. Belaunaldia) kudeatzeko, gehienez 6 kideko borroka-taldeak sortu eta administratzeko, beste entrenatzaile batzuekin lagun- eta jakinarazpen-sistema (*Changelog*) baten bidez elkarreragiteko eta estatistikak, eboluzio-kateak zein moten taulak aztertzeko laguntzaile adimendun bat (**ChatBot**) kontsultatzeko aukera ematen die.

## ✨ Ezaugarri Nagusiak

* **🔐 Autentifikazioa eta Erabiltzaile Rolak:**
  * Erregistroa eta saio-hasiera pasahitzen zifratzearekin (`SHA-256` + *salt*) eta saio iraunkorrekin.
  * Onarpen-fluxua: Kontu berriek administratzaile baten baliozkotzea behar dute aplikazioa erabili ahal izateko.
  * **Administrazio Panela:** Erabiltzaileak onartu, baztertu eta betiko ezabatzeko aukera, baita estatistika orokorrak ikusteko ere.
  * Profila editatzea (erabiltzaile-izena, posta elektronikoa eta biografia).

* **📖 Pokédex Kudeaketa eta Bilatzaile Aurreratua:**
  * Pokémon **Harrapatuen** eta **Harrapatzeko daudenen** jarraipena.
  * Bilatzaile dinamikoa iragazki konbinagarriekin: **Izena**, **Mota**, **Belaunaldia** eta **Eboluzio** gaitasuna.
  * Pokémon bakoitzaren fitxa tekniko xehatua (pisua, altuera, oinarrizko estatistikak, motak, ahuleziak, indarguneak eta eboluzio-katea).

* **⚔️ Taldeen Sortzailea eta Kudeatzailea (*Taldeak*):**
  * Borroka-talde pertsonalizatuak sortzea (gehienez 6 Pokémon, errepikapenik gabe).
  * Izenen autokonpletatua eta negozio-arauen baliozkotzea gordetzean.

* **🤖 ChatBot Laguntzailea:**
  * **Pokemon Hoberena:** Zure taldeko kiderik indartsuena automatikoki kalkulatzen du oinarrizko estatistikak batuz.
  * **Estatistikak:** PS, Erasoa, Defentsa, Defentsa Berezia eta Abiadura aurrerapen-barren bidez grafikoki bistaratzea.
  * **Ahulezi eta Indarguneak:** Borrokan moten arteko eraginkortasunaren kalkulua.
  * **Eboluzio Katea:** Pokémon baten etorkizuneko eboluzio guztien ibilbide errekurtsiboa.

* **👥 Komunitatea eta Jakinarazpenak (*Changelog*):**
  * Lagunak jarraitzeko sistema (*Lagunak*).
  * Jarduera global eta pertsonalaren erregistro automatikoa (harrapaketak, askatzeak, talde-aldaketak eta lagun berriak) erabiltzailearen araberako iragazkiekin.

## 🛠️ Erabilitako Teknologiak

* **Backend:** Python 3, Flask (arkitektura modularra *Blueprints* eta MVC patroiaren bidez).
* **Datu-basea:** SQLite3 (eskema erlazional propioarekin).
* **Kanpoko Datuak:** `pokebase` (PokéAPI-ren wrapper-a 1. Belaunaldiko 151 Pokémonen hasierako kargarako).
* **Frontend:** HTML5, CSS3, Bootstrap 5.1.3 eta Jinja2 txantiloiak (interfazea euskaraz).
* **Testing:** `pytest`, `pytest-cov` (kode-estaldura) eta `pytest-html` (txosten bisualak sortzea).

## 📁 Proiektuaren Egitura

```text
WISH_Pokedex/
├── app/
│   ├── __init__.py                 # Flask aplikazioaren hasieratzea eta Blueprint-en erregistroa
│   ├── controllers/                # Kontroladoreak (Ibilbideak eta negozio-logika)
│   │   ├── admin_controller.py
│   │   ├── auth_controller.py
│   │   ├── chatbot_controller.py
│   │   ├── friend_controller.py
│   │   ├── notifications_controller.py
│   │   ├── pokedex_controller.py
│   │   ├── team_controller.py
│   │   └── model/                  # Datu-sarbideko modeloak (SQL kontsultak)
│   │       ├── auth_model.py
│   │       ├── chatbot_model.py
│   │       ├── friend_model.py
│   │       ├── message_model.py
│   │       ├── pokedex_model.py
│   │       ├── team_model.py
│   │       └── user_model.py
│   ├── database/                   # SQLite datu-basearen kudeaketa
│   │   ├── connection.py
│   │   └── schema.sql              # Taulen eta gako arrotzen definizioa
│   ├── static/
│   │   └── style.css               # Estilo pertsonalizatuak
│   └── templates/                  # HTML bistak Jinja2 eta Bootstrap-ekin
│       ├── chatbot/                # ChatBot laguntzailearen azpitxantiloiak
│       └── ...
├── tests/                          # Proba unitarioen eta integrazio-proben bateria (96 test)
│   ├── conftest.py
│   ├── test_auth_controller.py
│   ├── test_changelog_controller.py
│   ├── test_chatbot_controller.py
│   ├── test_pokedex_controller.py
│   ├── test_pokemon_features.py
│   └── test_team_controller.py
├── config.py                       # Konfigurazio orokorreko aldagaiak
├── create_admin.py                 # Lehenetsitako administratzailea sortzeko script-a
├── populate_db.py                  # PokéAPI-tik 151 Pokémonak deskargatzeko script-a
├── fix_evolutions.py               # DBan eboluzio-kateak lotzeko script-a
├── fill_weaknesses.py              # Moten eraginkortasun-taula betetzeko script-a
├── pytest.ini                      # pytest-en konfigurazioa
├── requirements.txt                # Proiektuaren mendekotasunak
└── run.py                          # Zerbitzaria abiarazteko sarrera-puntua
```

## 🚀 Instalazioa eta Martxan Jartzea

Jarraitu urrats hauek proiektua zure ingurune lokalean konfiguratzeko eta exekutatzeko:

### 1. Biltegia klonatu eta ingurune birtuala sortu

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS-en
# venv\Scripts\activate   # Windows-en
```

### 2. Mendekotasunak instalatu

```bash
pip install -r requirements.txt
pip install pytest pytest-cov pytest-html
```

### 3. Datu-basea hasieratu eta bete

Lehenik eta behin, abiarazi aplikazioa une batez oinarrizko eskema (`database.db`) sortzeko, eta ondoren exekutatu konfigurazio script-ak ordena honetan:

```bash
# 1. Administratzaile kontua sortu (aurretik aplikazioa abiarazi bada taulak sortuta egongo dira)
python3 create_admin.py

# 2. PokéAPI-tik 151 Pokémonak deskargatu (minutu batzuk iraun dezake)
python3 populate_db.py

# 3. Pokémonen arteko eboluzio-erlazioak konfiguratu
python3 fix_evolutions.py

# 4. Moten, ahulezien eta indarguneen taula kargatu
python3 fill_weaknesses.py
```

> **Lehenetsitako Administratzaile Kredentzialak:**
> * **Erabiltzailea:** `admin`
> * **Pasahitza:** `admin123`

### 4. Garapen-zerbitzaria exekutatu

```bash
python3 run.py
```

Ireki zure web-nabigatzailea eta sartu helbide honetara: `http://127.0.0.1:5000`

## 🧪 Testen Exekuzioa (Testing)

Proiektu honek **96 proba automatizatuko** bateria osoa dauka aplikazioaren funtzionalitate kritikoak (Autentifikazioa, Pokédex, Pokémonak, Taldeak, ChatBot eta ChangeLog) eta egonkortasuna bermatzeko.

Test hauek exekutatzeko, kodearen estaldura (*coverage*) neurtzeko eta HTML formatuko txosten zehatza sortzeko, exekutatu hurrengo komandoa proiektuaren erroan:

```bash
pytest --cov=app --html=reporte_final_completo.html
```

Exekuzioa amaitzean, `reporte_final_completo.html` fitxategia sortuko da. Fitxategi hau nabigatzailean ireki dezakezu testen emaitzak eta euskarazko azalpenak ikusteko.

## 👥 Egileak

**ISAD (Software Ingeniaritza eta Datuen Analisia)** irakasgairako garatutako proiektua:

* **Iker Díez** - Saioa Hasi, Erregistroa, Erabiltzaile Kudeaketa eta Kontuak Kudeatu.
* **Hodei Castro** - Pokémon Taldeak Sortu, Editatu eta Gorde.
* **Andoni Ortiz de Zarate** - Pokédex Bilatzailea eta Informazioa Erakutsi.
* **Markel Valle** - ChatBot Modulua (Pokemon Hoberena, Estatistikak, Ahulezi/Indarguneak eta Eboluzio Katea).
* **Asier Fernández** - Jakinarazpenen Sistema eta Iragazkiak (Changelog).

---
---

# 🔴 WISH Pokédex - Sistema de Gestión Pokémon (ES)

**WISH Pokédex** es una aplicación web desarrollada en **Python (Flask)** y **SQLite** que permite a los usuarios gestionar su propia colección de Pokémon (1ª Generación), crear y administrar equipos de combate de hasta 6 integrantes, interactuar con otros entrenadores mediante un sistema de amigos y notificaciones (*Changelog*), y consultar un asistente inteligente (**ChatBot**) para analizar estadísticas, cadenas evolutivas y tablas de tipos.

## ✨ Características Principales

* **🔐 Autenticación y Roles de Usuario:**
  * Registro e inicio de sesión con encriptación de contraseñas (`SHA-256` + *salt*) y sesiones persistentes.
  * Flujo de aprobación: Las cuentas nuevas requieren validación por parte de un administrador antes de poder operar.
  * **Panel de Administración:** Aprobación, rechazo y eliminación definitiva de usuarios, además de visualización de métricas globales.
  * Edición de perfil (nombre de usuario, correo electrónico y biografía).

* **📖 Gestión de Pokédex y Buscador Avanzado:**
  * Seguimiento de Pokémon **Capturados** (*Harrapatuak*) y **Pendientes** (*Harrapatzeko*).
  * Buscador dinámico con filtros combinables por **Nombre**, **Tipo** (*Mota*), **Generación** (*Belaunaldia*) y capacidad de **Evolución**.
  * Ficha técnica detallada por Pokémon (peso, altura, estadísticas base, tipos, debilidades, fortalezas y línea evolutiva).

* **⚔️ Creador y Gestor de Equipos (*Taldeak*):**
  * Creación de equipos de combate personalizados (máximo 6 Pokémon sin duplicados).
  * Autocompletado de nombres y validación de reglas de negocio al guardar.

* **🤖 ChatBot Asistente:**
  * **Mejor Pokémon (*Pokemon Hoberena*):** Calcula automáticamente el integrante más fuerte de tu equipo sumando sus estadísticas base.
  * **Estadísticas (*Estatistikak*):** Visualización gráfica mediante barras de progreso de PS, Ataque, Defensa, Defensa Especial y Velocidad.
  * **Debilidades y Fortalezas (*Ahulezi eta Indarguneak*):** Cálculo de efectividad de tipos en combate.
  * **Cadena Evolutiva (*Eboluzio Katea*):** Recorrido recursivo de todas las evoluciones futuras de un Pokémon.

* **👥 Comunidad y Notificaciones (*Changelog*):**
  * Sistema de seguimiento de amigos (*Lagunak*).
  * Registro automático de actividad global y personal (capturas, liberaciones, cambios en equipos y nuevos amigos) con filtros por usuario.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask (arquitectura modular mediante *Blueprints* y patrón MVC).
* **Base de Datos:** SQLite3 (con esquema relacional propio).
* **Datos Externos:** `pokebase` (wrapper de PokéAPI para la carga inicial de los 151 Pokémon de la 1ª Generación).
* **Frontend:** HTML5, CSS3, Bootstrap 5.1.3 y plantillas Jinja2 (interfaz en euskera).
* **Testing:** `pytest`, `pytest-cov` (cobertura de código) y `pytest-html` (generación de reportes visuales).

## 📁 Estructura del Proyecto

```text
WISH_Pokedex/
├── app/
│   ├── __init__.py                 # Inicialización de la app Flask y registro de Blueprints
│   ├── controllers/                # Controladores (Rutas y lógica de negocio)
│   │   ├── admin_controller.py
│   │   ├── auth_controller.py
│   │   ├── chatbot_controller.py
│   │   ├── friend_controller.py
│   │   ├── notifications_controller.py
│   │   ├── pokedex_controller.py
│   │   ├── team_controller.py
│   │   └── model/                  # Modelos de acceso a datos (Consultas SQL)
│   │       ├── auth_model.py
│   │       ├── chatbot_model.py
│   │       ├── friend_model.py
│   │       ├── message_model.py
│   │       ├── pokedex_model.py
│   │       ├── team_model.py
│   │       └── user_model.py
│   ├── database/                   # Gestión de la base de datos SQLite
│   │   ├── connection.py
│   │   └── schema.sql              # Definición de tablas y claves foráneas
│   ├── static/
│   │   └── style.css               # Estilos personalizados
│   └── templates/                  # Vistas HTML con Jinja2 y Bootstrap
│       ├── chatbot/                # Subplantillas del asistente ChatBot
│       └── ...
├── tests/                          # Batería de pruebas unitarias y de integración (96 tests)
│   ├── conftest.py
│   ├── test_auth_controller.py
│   ├── test_changelog_controller.py
│   ├── test_chatbot_controller.py
│   ├── test_pokedex_controller.py
│   ├── test_pokemon_features.py
│   └── test_team_controller.py
├── config.py                       # Variables de configuración global
├── create_admin.py                 # Script para crear el usuario administrador por defecto
├── populate_db.py                  # Script para descargar los 151 Pokémon desde PokéAPI
├── fix_evolutions.py               # Script para enlazar las cadenas evolutivas en la BD
├── fill_weaknesses.py              # Script para poblar la tabla de efectividad de tipos
├── pytest.ini                      # Configuración de pytest
├── requirements.txt                # Dependencias del proyecto
└── run.py                          # Punto de entrada para ejecutar el servidor
```

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio y crear el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
pip install pytest pytest-cov pytest-html
```

### 3. Inicializar y poblar la Base de Datos

Primero, inicia brevemente la aplicación para que se genere el esquema base (`database.db`), y luego ejecuta los scripts de configuración en el siguiente orden:

```bash
# 1. Crear la cuenta de administrador (Crea las tablas si se ha iniciado la app antes)
python3 create_admin.py

# 2. Descargar los 151 Pokémon desde PokéAPI (puede tardar unos minutos)
python3 populate_db.py

# 3. Configurar las relaciones de evolución entre los Pokémon
python3 fix_evolutions.py

# 4. Cargar la tabla de tipos, debilidades y fortalezas
python3 fill_weaknesses.py
```

> **Credenciales de Administrador por defecto:**
> * **Usuario:** `admin`
> * **Contraseña:** `admin123`

### 4. Ejecutar el servidor de desarrollo

```bash
python3 run.py
```

Abre tu navegador web y accede a: `http://127.0.0.1:5000`

## 🧪 Ejecución de Pruebas (Testing)

El proyecto cuenta con una suite completa de **96 pruebas automatizadas** que validan todos los casos de uso (inicio de sesión, registro, gestión de perfil, creación/edición de equipos, filtros de la Pokédex, ChatBot y notificaciones).

Para ejecutar los tests, medir la cobertura de código (*coverage*) y generar el informe interactivo en HTML, ejecuta el siguiente comando en la raíz del proyecto:

```bash
pytest --cov=app --html=reporte_final_completo.html
```

Una vez finalizada la ejecución, podrás abrir el archivo `reporte_final_completo.html` en cualquier navegador para inspeccionar el desglose detallado de cada prueba y su descripción en euskera.

## 👥 Autores

Proyecto desarrollado para la asignatura **ISAD (Ingeniería del Software y Análisis de Datos)**:

* **Iker Díez** - Autenticación, Registro, Gestión de Usuarios y Cuentas.
* **Hodei Castro** - Creación, Edición y Gestión de Equipos Pokémon.
* **Andoni Ortiz de Zarate** - Buscador de Pokédex y Visualización de Detalles.
* **Markel Valle** - Módulo ChatBot (Mejor Pokémon, Estadísticas, Tipos y Evoluciones).
* **Asier Fernández** - Sistema de Notificaciones y Filtrado (Changelog).