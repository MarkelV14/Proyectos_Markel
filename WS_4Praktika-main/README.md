# 📂 eGela -> Dropbox Fitxategi Kudeatzailea / Gestor de Archivos eGela -> Dropbox

---

# 🟢 eGela -> Dropbox Fitxategi Kudeatzailea (EU)

**eGela -> Dropbox** **Python** eta **Tkinter** erabiliz garatutako mahaigaineko aplikazio grafiko bat da (*Web Sistemak* irakasgaiko 4. jarduera praktikoa). Aplikazio honen bidez, UPV/EHUko **eGela** plataforman autentifikatu, *Web Sistemak* irakasgaiko atal eta karpetetako PDF dokumentu guztiak automatikoki atera (*web scraping* bidez), eta zuzenean **Dropbox** kontu batera transferitu daitezke **OAuth 2.0** eta Dropbox-en API ofiziala erabiliz.

## ✨ Ezaugarri Nagusiak

* **🔐 Autentifikazioa eGelan (HTTP saio-kudeaketa):**
  * eGelako saio-hasieraren 4 HTTP eskaera/erantzunen fluxu osoa simulatzen du (`GET` eta `POST` bidez).
  * `MoodleSessionegela` saio-cookiea eta segurtasuneko `logintoken`-a automatikoki erauzten eta kudeatzen ditu.
* **🕷️ Web Scraping Aurreratua eGelan:**
  * *Web Sistemak* (*Sistemas Web*) irakasgaia automatikoki bilatzen du eta bere atal guztiak (`format_onetopic-tabs`) zeharkatzen ditu.
  * Baliabide zuzenak (`modtype_resource`) zein barneko karpetak (`modtype_folder`) aztertzen ditu, PDF fitxategi guztien izenak eta deskarga-estekak lortuz.
* **☁️ OAuth 2.0 Autentifikazioa Dropbox-en:**
  * Baimen-fluxua nabigatzailean irekitzen du eta aldi baterako **socket zerbitzari lokal bat** (`localhost:8070`) abiarazten du birbideratzea (`auth_code`) automatikoki jasotzeko eta `access_token`-agatik trukatzeko.
* **🔄 Fitxategien Transferentzia eta Kudeaketa (Dropbox API v2):**
  * **Fitxategiak Igo (`>>>`):** eGelan hautatutako PDF bat edo gehiago deskargatu eta uneko Dropbox direktoriora igotzen ditu aurrerapen-barra batekin.
  * **Nabigazio Interaktiboa:** Dropbox-eko karpetetan klik bikoitza eginez barrura sartzeko edo `..` hautatuz atzera egiteko aukera.
  * **Karpetak Sortu (*Create folder*):** Direktorio berriak sortzen ditu hodeian interfaze grafikotik bertatik.
  * **Fitxategiak Ezabatu (*Delete*):** Hautatutako elementuak Dropbox-etik ezabatzen ditu.
  * **Kontuaren Espazioa (*Espazioa*):** Funtzionalitate gehigarria; kontuan erabilitako eta guztirako espazioa (MB-tan) kalkulatzen eta barra grafiko baten bidez erakusten du (`/users/get_space_usage`).

## 🛠️ Erabilitako Teknologiak

* **Hizkuntza:** Python 3
* **Interfaze Grafikoa (GUI):** `tkinter` eta `tkinter.ttk`
* **HTTP Eskaerak eta Sarea:** `requests`, `urllib`, `socket` (OAuth callback zerbitzarirako)
* **Web Scraping / Parsing:** `BeautifulSoup4` (`bs4`) eta adierazpen erregularrak (`re`)
* **Kanpoko APIa:** Dropbox HTTP API v2

## 📁 Proiektuaren Egitura

```text
WS_4Praktika/
├── actividad_4.py     # Aplikazio nagusia: Tkinter interfazea eta gertaeren kontrola
├── eGela.py           # eGelako logina (4 urratsak) eta PDFen erauzketa (Web Scraping)
├── Dropbox.py         # OAuth 2.0 fluxua (socket zerbitzaria) eta Dropbox API v2 deiak
├── helper.py          # Funtzio laguntzaileak: leihoak zentratu, aurrerapen-barrak eta zerrendak
└── favicon.ico        # Aplikazioko leihoen ikonoa
```

## 🚀 Instalazioa eta Martxan Jartzea

### 1. Aurrebaldintzak eta mendekotasunak instalatu

Ziurtatu Python 3 instalatuta duzula (`tkinter` eta `socket` lehenetsita datoz) eta instalatu kanpoko liburutegiak:

```bash
pip install requests beautifulsoup4
```

### 2. Aplikazioa exekutatu

Exekutatu script nagusia proiektuaren direktoriotik:

```bash
python3 actividad_4.py
```

### 3. Erabilera Fluxua

1. **Login eGela:** Sartu zure UPV/EHUko LDAP erabiltzailea eta pasahitza lehenengo leihoan. Aplikazioak *Web Sistemak* ikastaroko PDF guztiak bilatuko ditu.
2. **Login Dropbox:** Sakatu *Login* botoia. Nabigatzailea irekiko da Dropbox-i baimena emateko. Baimena emandakoan, leihoa itxi dezakezu.
3. **Kudeaketa Leiho Nagusia:**
   * Ezkerreko zerrendan eGelako PDFak agertuko dira; eskuinekoan, zure Dropbox-eko edukia.
   * Hautatu nahi dituzun PDFak ezkerrean eta sakatu **`>>>`** botoia Dropbox-era pasatzeko.
   * Erabili eskuineko botoiak karpetak sortzeko (**Create folder**), fitxategiak ezabatzeko (**Delete**) edo biltegiratze-egoera ikusteko (**Espazioa**).

---

# 🔴 Gestor de Archivos eGela -> Dropbox (ES)

**eGela -> Dropbox** es una aplicación de escritorio con interfaz gráfica desarrollada en **Python** con **Tkinter** (correspondiente a la Actividad 4 de la asignatura *Sistemas Web*). La herramienta permite autenticarse en la plataforma **eGela** de la UPV/EHU, extraer automáticamente todos los documentos PDF de la asignatura *Web Sistemak / Sistemas Web* mediante técnicas de *web scraping*, y transferirlos directamente a una cuenta de **Dropbox** haciendo uso de **OAuth 2.0** y la API oficial de Dropbox.

## ✨ Características Principales

* **🔐 Autenticación en eGela (Gestión de sesiones HTTP):**
  * Implementa el flujo completo de inicio de sesión en Moodle/eGela a través de 4 peticiones HTTP secuenciales (`GET` y `POST` controlando redirecciones `302`).
  * Extracción y gestión manual de la cookie de sesión (`MoodleSessionegela`) y del token CSRF (`logintoken`).
* **🕷️ Web Scraping Avanzado en eGela:**
  * Localiza automáticamente el curso *Web Sistemak* y recorre todas sus pestañas/secciones (`format_onetopic-tabs`).
  * Analiza tanto recursos directos (`modtype_resource`) como carpetas (`modtype_folder`), recopilando los nombres y enlaces de descarga de todos los archivos PDF.
* **☁️ Autenticación OAuth 2.0 en Dropbox:**
  * Abre el navegador web para autorizar la aplicación y levanta un **servidor socket TCP local** (`localhost:8070`) que captura automáticamente la redirección con el `auth_code` para intercambiarlo por el `access_token`.
* **🔄 Transferencia y Gestión de Archivos (Dropbox API v2):**
  * **Subida de Archivos (`>>>`):** Descarga los PDFs seleccionados de eGela en memoria y los sube al directorio actual de Dropbox mostrando una barra de progreso en tiempo real.
  * **Navegación Interactiva:** Permite explorar directorios en Dropbox haciendo doble clic sobre las carpetas o regresar al directorio padre mediante el elemento `..`.
  * **Creación de Carpetas (*Create folder*):** Crea nuevos directorios en Dropbox desde una ventana emergente.
  * **Eliminación de Archivos (*Delete*):** Borra múltiples archivos o carpetas seleccionados en Dropbox.
  * **Uso de Espacio (*Espazioa*):** Funcionalidad adicional que consulta el endpoint `/users/get_space_usage` y muestra en una ventana emergente el espacio utilizado y total de la cuenta (en MB) junto con un indicador porcentual.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Interfaz Gráfica (GUI):** `tkinter` y `tkinter.ttk`
* **Peticiones HTTP y Red:** `requests`, `urllib`, `socket` (para el servidor local de callback OAuth)
* **Web Scraping / Parsing:** `BeautifulSoup4` (`bs4`) y expresiones regulares (`re`)
* **API Externa:** Dropbox HTTP API v2

## 📁 Estructura del Proyecto

```text
WS_4Praktika/
├── actividad_4.py     # Script principal: Interfaz Tkinter y lógica de eventos
├── eGela.py           # Clase eGela: Login en 4 pasos y scraping de archivos PDF
├── Dropbox.py         # Clase Dropbox: Flujo OAuth 2.0 con sockets y llamadas a la API v2
├── helper.py          # Funciones auxiliares: centrado de ventanas, barras de progreso y actualización de UI
└── favicon.ico        # Icono de las ventanas de la aplicación
```

## 🚀 Instalación y Puesta en Marcha

### 1. Pre-requisitos e instalación de dependencias

Asegúrate de tener instalado Python 3 (los módulos `tkinter` y `socket` vienen incluidos en la librería estándar) e instala las dependencias externas:

```bash
pip install requests beautifulsoup4
```

### 2. Ejecutar la aplicación

Lanza el script principal desde la terminal en la carpeta raíz del proyecto:

```bash
python3 actividad_4.py
```

### 3. Flujo de Uso

1. **Login eGela:** Introduce tus credenciales de la UPV/EHU en la primera ventana emergente. Tras autenticarte, una barra de progreso mostrará el escaneo de secciones y PDFs de la asignatura.
2. **Login Dropbox:** Haz clic en el botón *Login*. Se abrirá tu navegador predeterminado para autorizar el acceso a Dropbox. Una vez completado, podrás cerrar la pestaña del navegador.
3. **Ventana Principal de Gestión:**
   * En el panel izquierdo verás los PDFs extraídos de eGela; en el panel derecho, los archivos y carpetas de tu Dropbox.
   * Selecciona uno o varios PDFs a la izquierda y pulsa **`>>>`** para transferirlos a la carpeta actual de Dropbox.
   * Utiliza los botones de la derecha para eliminar elementos (**Delete**), crear nuevas carpetas (**Create folder**) o consultar el almacenamiento disponible (**Espazioa**).