# -*- coding: UTF-8 -*-
from tkinter import messagebox
import requests
import urllib
from urllib.parse import unquote
from bs4 import BeautifulSoup
import time
import helper
import re

class eGela:
    _login = 0
    _cookie = ""
    _curso = ""
    _refs = []
    _root = None

    def __init__(self, root):
        self._root = root

    def check_credentials(self, username, password, event=None):
        popup, progress_var, progress_bar = helper.progress("check_credentials", "Logging into eGela...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()

        print("##### 1. PETICION #####")
        metodo = 'GET'
        uri_1 = "https://egela.ehu.eus/login/index.php"

        resp_1 = requests.get(uri_1, allow_redirects=False)
        print("\n" + "=" * 50)
        print("1. ESKAERA")
        print("GET", uri_1)

        print("\n1. ERANTZUNA")
        print(resp_1.status_code, resp_1.reason)
        set_cookie_1 = resp_1.headers.get('Set-Cookie', '')
        location_1 = resp_1.headers.get('Location', 'Ez dago')
        print("Set-Cookie:", set_cookie_1)
        print("Location:", location_1)

        cookie_balioa = re.search(r'(MoodleSessionegela=[^;]+)', set_cookie_1).group(1)
        soup = BeautifulSoup(resp_1.text, 'html.parser')
        logintoken_balioa = soup.find('input',{'name':'logintoken'})['value']



        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 25
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)




        print("\n##### 2. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################


        login_form = soup.find('form')
        uri_2 = login_form['action']
        data_2 = {
            'username': username,
            'password': password,
            'logintoken': logintoken_balioa
        }
        headers_2 = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie_balioa,
        }
        response_2 = requests.post(uri_2, data=data_2, headers=headers_2, allow_redirects=False)
        print("\n" + "=" * 50)
        print("2. ESKAERA")
        print("POST", uri_2)
        print(data_2)
        print("\n2. ERANTZUNA")
        print(response_2.status_code, response_2.reason)

        set_cookie_2 = response_2.headers.get('Set-Cookie', '')
        location_2 = response_2.headers.get('Location', 'Ez dago')
        match_cookie_2 = re.search(r'(MoodleSessionegela=[^;]+)', set_cookie_2)
        if match_cookie_2:
            cookie_balioa = match_cookie_2.group(1)




        progress = 50
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)

        print("\n##### 3. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        uri_3 = location_2
        headers_3 = {
            'Cookie': cookie_balioa
        }

        response_3 = requests.get(uri_3, headers=headers_3, allow_redirects=False)
        print("\n" + "=" * 50)
        print("3. ESKAERA")
        print("GET", uri_3)

        print("\n3. ERANTZUNA")
        print(response_3.status_code, response_3.reason)

        set_cookie_3 = response_3.headers.get('Set-Cookie', '')
        location_3 = response_3.headers.get('Location', 'Ez dago')
        print("Set-Cookie:", set_cookie_3)
        print("Location:", location_3)

        progress = 75
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)

        print("\n##### 4. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        uri_4 = location_3

        headers_4 = {
            'Cookie': cookie_balioa
        }

        response_4 = requests.get(uri_4, headers=headers_4, allow_redirects=False)
        print("\n" + "=" * 50)
        print("4. ESKAERA")
        print("GET", uri_4)

        print("\n4. ERANTZUNA")
        print(response_4.status_code, response_4.reason)

        set_cookie_4 = response_4.headers.get('Set-Cookie', '')
        location_4 = response_4.headers.get('Location', 'Ez dago')
        print("Set-Cookie:", set_cookie_4)
        print("Location:", location_4)

        html_4 = response_4.text

        soup_4 = BeautifulSoup(html_4, 'html.parser')
        curso= soup_4.find('a', string=re.compile("Web Sistemak", re.IGNORECASE))
        if curso:
            print("Login correcto y curso encontrado")
            self._login=1
            self._cookie= cookie_balioa
            self._curso = curso['href']
        else:
            print("Login incorrecto")
        progress = 100
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)
        popup.destroy()


        if self._login==1:
            #############################################
            # ACTUALIZAR VARIABLES
            #############################################
            self._root.destroy()
        else:
            messagebox.showinfo("Alert Message", "Login incorrect!")

    def get_pdf_refs(self):
        popup, progress_var, progress_bar = helper.progress("get_pdf_refs", "Downloading PDF list...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()

        print("\n##### 4. PETICION (Página principal de la asignatura en eGela) #####")
        headers = {'Cookie': self._cookie}
        response = requests.get(self._curso, headers=headers)
        html_ikastaroa = response.text
        soup = BeautifulSoup(html_ikastaroa, "html.parser")

        atalak = []
        nabigazio_fitxak = soup.find("ul", class_=re.compile("format_onetopic-tabs"))
        if nabigazio_fitxak:
            for li in nabigazio_fitxak.find_all("li", class_="nav-item"):
                esteka = li.find("a", href=True)
                if not esteka:
                    continue
                urla = esteka["href"].split("#")[0]
                if not urla or not urla.startswith("https://egela.ehu.eus/course/view.php"):
                    continue
                atalak.append(urla)
                
        if not atalak:
            atalak.append(self._curso)
            
        print(f"  [INFO] Se han encontrado {len(atalak)} secciones para revisar.")
        
        deskargatutako_urlak = set()
        lista_de_pdfs_encontrados = []
        
        progress_per_section = 100.0 / len(atalak)

        for i, urla in enumerate(atalak):
            print(f"  [►] Revisando sección {i+1}/{len(atalak)}...")
            if urla == self._curso:
                e = response
                s = soup
            else:
                e = requests.get(urla, headers=headers)
                s = BeautifulSoup(e.text, "html.parser")

            # Buscar recursos
            recursos = s.find_all("li", class_=re.compile("modtype_resource"))
            for li in recursos:
                esteka = li.find("a", href=True)
                if not esteka: continue
                baliabide_url = esteka["href"].split("&")[0]
                if baliabide_url in deskargatutako_urlak: continue
                deskargatutako_urlak.add(baliabide_url)

                try:
                    e_bal = requests.get(baliabide_url, headers=headers, allow_redirects=False, timeout=10)
                    azken_url = e_bal.headers.get("Location", "")
                    
                    if azken_url and ".pdf" in azken_url.lower():
                        fitxategi_izena = unquote(azken_url.split("/")[-1].split("?")[0])
                        lista_de_pdfs_encontrados.append({'pdf_name': fitxategi_izena, 'pdf_link': azken_url})
                        print(f"    [PDF] Encontrado: {fitxategi_izena}")
                    elif e_bal.status_code == 200:
                        soup_bal = BeautifulSoup(e_bal.text, "html.parser")
                        for est_bal in soup_bal.find_all("a", href=True):
                            href = est_bal["href"]
                            if "pluginfile" in href and ".pdf" in href.lower():
                                fitxategi_izena = unquote(href.split("/")[-1].split("?")[0])
                                lista_de_pdfs_encontrados.append({'pdf_name': fitxategi_izena, 'pdf_link': href})
                                print(f"    [PDF] Encontrado: {fitxategi_izena}")
                                break
                    time.sleep(0.1) # Pausa suave
                except Exception as ex:
                    print(f"    [!] Error revisando recurso: {ex}")

            # Buscar carpetas
            carpetas = s.find_all("li", class_=re.compile("modtype_folder"))
            for li in carpetas:
                esteka = li.find("a", href=True)
                if not esteka: continue
                karpeta_url = esteka["href"]
                if karpeta_url in deskargatutako_urlak: continue
                deskargatutako_urlak.add(karpeta_url)
                
                try:
                    e_karpeta = requests.get(karpeta_url, headers=headers, timeout=10)
                    soup_karpeta = BeautifulSoup(e_karpeta.text, "html.parser")
                    for est_karp in soup_karpeta.find_all("a", href=True):
                        href = est_karp["href"]
                        if "pluginfile" in href and ".pdf" in href.lower():
                            if href not in deskargatutako_urlak:
                                deskargatutako_urlak.add(href)
                                fitxategi_izena = unquote(href.split("/")[-1].split("?")[0])
                                lista_de_pdfs_encontrados.append({'pdf_name': fitxategi_izena, 'pdf_link': href})
                                print(f"    [PDF] Encontrado en carpeta: {fitxategi_izena}")
                    time.sleep(0.1)
                except Exception as ex:
                    print(f"    [!] Error en carpeta: {ex}")
            
            # Actualizar progreso tras cada sección
            progress += progress_per_section
            progress_var.set(min(progress, 100))
            progress_bar.update()

        for pdf in lista_de_pdfs_encontrados:
            if pdf not in self._refs:
                self._refs.append(pdf)

        popup.destroy()
        return self._refs

    def get_pdf(self, selection):

        print("\t##### descargando  PDF... #####")

        pdf_info = self._refs[selection]
        pdf_name = pdf_info['pdf_name']
        pdf_link = pdf_info['pdf_link']

        headers = {'Cookie': self._cookie}
        response = requests.get(pdf_link, headers=headers)
        
        pdf_content = response.content

        return pdf_name, pdf_content