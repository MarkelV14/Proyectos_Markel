# 💻 Markelen Proiektuak / Proyectos de Markel


---

# 🟢 Markelen Proiektuak - Portfolio Akademikoa (EU)

Ongi etorri nire GitHub biltegira! Biltegi honetan Informatika Ingeniaritzako graduan zehar garatutako zenbait proiektu nagusi biltzen dira, **Web Garapena**, **Web Sistemak eta APIen Integrazioa** zein **Datuen Meatzaritza eta Ikasketa Automatikoa (Machine Learning)** arloak jorratuz.

## 📂 Biltegiko Proiektuak

| Proiektua | Irakasgaia / Arloa | Teknologia Nagusiak | Esteka |
| :--- | :--- | :--- | :--- |
| 🔴 **WISH Pokédex** | Software Ingeniaritza (ISAD) | Python, Flask, SQLite, Bootstrap, Pytest | [`./WISH_Pokedex-main`](./WISH_Pokedex-main) |
| 📂 **eGela -> Dropbox** | Web Sistemak (WS) | Python, Tkinter, Requests, BeautifulSoup4, OAuth 2.0 | [`./WS_4Praktika-main`](./WS_4Praktika-main) |
| 🧠 **Tweet Sentiment Analysis** | Datuen Meatzaritza / ML | Java, Weka API, NLP | [`./WekaProiektu-main`](./WekaProiektu-main) |

---

### 1. 🔴 WISH Pokédex (`WISH_Pokedex-main`)
1. Belaunaldiko Pokémon bilduma osoa kudeatzeko web-aplikazioa, **Flask** eta **SQLite** bidez garatua (MVC arkitektura).
* **Ezaugarriak:** Erabiltzaileen erregistroa eta administratzaileen onarpen-fluxua, 6 Pokémoneko borroka-taldeen sortzailea, bilatzaile aurreratua, lagun-sistema eta jarduera-erregistroa (*Changelog*).
* **Nabarmendua:** Laguntzaile adimenduna (**ChatBot**) taldeko Pokémon hoberena kalkulatzeko, estatistikak ikusteko, moten ahuleziak/indarguneak aztertzeko eta eboluzio-kateak bistaratzeko. **96 proba automatizatu** (`pytest`) biltzen ditu.

### 2. 📂 eGela -> Dropbox Fitxategi Kudeatzailea (`WS_4Praktika-main`)
UPV/EHUko **eGela** plataforma eta **Dropbox** hodeiko biltegiratzea konektatzen dituen mahaigaineko aplikazio grafikoa (**Tkinter**).
* **Ezaugarriak:** HTTP saioen kudeaketa manuala eGelan (4 urratseko logina eta cookie-ak), *Web Scraping* (`BeautifulSoup4`) ikastaroko atal eta karpetetako PDF guztiak erauzteko, eta **OAuth 2.0** baimen-fluxua socket zerbitzari lokal baten bidez.
* **Nabarmendua:** Fitxategiak zuzenean eGelatik Dropbox-era transferitzeko, karpetetan nabigatzeko/sortzeko/ezabatzeko eta kontuaren espazio erabilgarria (`Espazioa`) kontsultatzeko aukera.

### 3. 🧠 Tweet Sentiment Analysis - Weka (`WekaProiektu-main`)
Txioetako (*tweets*) sentimenduen analisia eta sailkapen automatikoa (**Testuen Meatzaritza / NLP**) **Java** eta **Weka** liburutegia erabiliz.
* **Ezaugarriak:** Testu-datuen aurreprozesamendua eta garbiketa (`CSVPreprocessor.java`), ARFF formatura bihurtzea, atributuen erauzketa (`StringToWordVector`) eta sailkapen-ereduen entrenamendua zein ebaluazioa (`TweetSentiment.java`).
* **Nabarmendua:** Entrenamendu (`train`), garapen (`dev`) eta proba itsuko (`test_blind`) datu-multzoekin lan egiten du, iragarpenak eta ebaluazio-txosten automatikoak sortuz (`Iragarpenak/` eta `reporte_final.txt`).

---

## 🛠️ Teknologia Multzoa (Tech Stack)

* **Programazio Lengoaiak:** Python 3, Java, SQL, HTML5, CSS3
* **Framework-ak eta Liburutegiak:** Flask, Bootstrap 5, Tkinter, Weka API, BeautifulSoup4, Requests, Pokébase
* **Datu-baseak eta Formatuak:** SQLite3, CSV, ARFF, JSON
* **Kalitatea eta Tresnak:** Pytest (`pytest-cov`, `pytest-html`), Git, OAuth 2.0, REST APIak

## 🚀 Erabilera

Proiektu bakoitzak bere konfigurazio- eta exekuzio-argibide propioak ditu. Sartu dagokion karpetan xehetasun gehiago ikusteko:

```bash
# Biltegia klonatu
git clone https://github.com/<zure-erabiltzailea>/Proyectos_Markel.git
cd Proyectos_Markel
```

## 👤 Egilea

* **Markel Valle** - *Informatika Ingeniaritza (UPV/EHU)*

---
---

# 🔴 Proyectos de Markel - Portfolio Académico (ES)

¡Bienvenido a mi repositorio de GitHub! Este espacio reúne varios proyectos principales desarrollados durante el Grado en Ingeniería Informática, abarcando áreas como el **Desarrollo Web Full-Stack**, **Sistemas Web e Integración de APIs** y **Minería de Datos / Machine Learning**.

## 📂 Proyectos Incluidos

| Proyecto | Asignatura / Área | Tecnologías Principales | Directorio |
| :--- | :--- | :--- | :--- |
| 🔴 **WISH Pokédex** | Ingeniería del Software (ISAD) | Python, Flask, SQLite, Bootstrap, Pytest | [`./WISH_Pokedex-main`](./WISH_Pokedex-main) |
| 📂 **eGela -> Dropbox** | Sistemas Web (WS) | Python, Tkinter, Requests, BeautifulSoup4, OAuth 2.0 | [`./WS_4Praktika-main`](./WS_4Praktika-main) |
| 🧠 **Tweet Sentiment Analysis** | Minería de Datos / ML | Java, Weka API, NLP | [`./WekaProiektu-main`](./WekaProiektu-main) |

---

### 1. 🔴 WISH Pokédex (`WISH_Pokedex-main`)
Aplicación web completa desarrollada con **Flask** y **SQLite** (bajo patrón MVC y *Blueprints*) para gestionar colecciones Pokémon de la 1ª Generación.
* **Características:** Autenticación con encriptación y aprobación de cuentas por administrador, creador y gestor de equipos de combate (hasta 6 Pokémon), buscador dinámico multifiltro, sistema de amigos y registro de actividad (*Changelog*).
* **Destacado:** Incluye un módulo **ChatBot** interactivo (mejor Pokémon del equipo, visualización de estadísticas, efectividad de tipos y cadenas evolutivas) y una suite de **96 tests automatizados** con `pytest`.

### 2. 📂 Gestor de Archivos eGela -> Dropbox (`WS_4Praktika-main`)
Aplicación de escritorio con interfaz gráfica (**Tkinter**) que automatiza la extracción de apuntes desde la plataforma **eGela** (UPV/EHU) hacia la nube de **Dropbox**.
* **Características:** Simulación completa del flujo de login HTTP en 4 peticiones sobre Moodle/eGela, *Web Scraping* con `BeautifulSoup4` en pestañas y carpetas de la asignatura, y flujo de autorización **OAuth 2.0** mediante un servidor socket TCP local.
* **Destacado:** Permite transferir múltiples PDFs directamente a la nube, navegar entre directorios, crear/eliminar carpetas y visualizar gráficamente el uso de almacenamiento de la cuenta (`Espazioa`) consumiendo la API v2 de Dropbox.

### 3. 🧠 Tweet Sentiment Analysis - Weka (`WekaProiektu-main`)
Sistema de análisis de sentimientos y clasificación automática de textos sobre *tweets* desarrollado en **Java** utilizando la API de **Weka**.
* **Características:** Preprocesamiento y limpieza de archivos CSV crudos (`CSVPreprocessor.java`), vectorización de texto y selección de atributos, entrenamiento de modelos predictivos y evaluación de métricas (`TweetSentiment.java`).
* **Destacado:** Procesa conjuntos de entrenamiento (`train`), validación (`dev`) y pruebas ciegas (`test_blind`), generando automáticamente los archivos de predicciones y el informe estadístico de rendimiento (`Iragarpenak/` y `reporte_final.txt`).

---

## 🛠️ Tecnologías y Herramientas (Tech Stack)

* **Lenguajes:** Python 3, Java, SQL, HTML5, CSS3
* **Frameworks y Librerías:** Flask, Bootstrap 5, Tkinter, Weka API, BeautifulSoup4, Requests, Pokébase
* **Bases de Datos y Datos:** SQLite3, CSV, ARFF, JSON
* **Calidad y Protocolos:** Pytest (`pytest-cov`, `pytest-html`), Git, OAuth 2.0, APIs REST

## 🚀 Cómo explorar el repositorio

Cada subdirectorio cuenta con su propio archivo `README.md` detallado con los pasos de instalación y puesta en marcha. Para clonar el repositorio completo:

```bash
# Clonar el repositorio
git clone https://github.com/<tu-usuario>/Proyectos_Markel.git
cd Proyectos_Markel
```

## 👤 Autor

* **Markel Valle** - *Ingeniería Informática (UPV/EHU)*