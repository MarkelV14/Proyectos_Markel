import requests
import urllib
import webbrowser
from socket import AF_INET, socket, SOCK_STREAM
import json
import helper

app_key = '7k5ubwz8k2ov7t3'
app_secret = 'redlwwzwic0i22h'
server_addr = "localhost"
server_port = 8070
redirect_uri = "http://" + server_addr + ":" + str(server_port)

class Dropbox:
    _access_token = ""
    _path = "/"
    _files = []
    _root = None
    _msg_listbox = None

    def __init__(self, root):
        self._root = root

    def local_server(self):
        # por el puerto 8090 esta escuchando el servidor que generamos
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((server_addr, server_port))
        server_socket.listen(1)
        print("\tLocal server listening on port " + str(server_port))

        # recibe la redireccio 302 del navegador
        client_connection, client_address = server_socket.accept()
        peticion = client_connection.recv(1024)
        print("\tRequest from the browser received at local server:")
        print (peticion)

        # buscar en solicitud el "auth_code"
        primera_linea =peticion.decode('UTF8').split('\n')[0]
        aux_auth_code = primera_linea.split(' ')[1]
        auth_code = aux_auth_code[7:].split('&')[0]
        print ("\tauth_code: " + auth_code)

        # devolver una respuesta al usuario
        http_response = "HTTP/1.1 200 OK\r\n\r\n" \
                        "<html>" \
                        "<head><title>Proba</title></head>" \
                        "<body>The authentication flow has completed. Close this window.</body>" \
                        "</html>"
        client_connection.sendall(http_response.encode('utf-8'))
        client_connection.close()
        server_socket.close()

        return auth_code

    def do_oauth(self):
        auth_url = (
                "https://www.dropbox.com/oauth2/authorize"
                "?client_id=" + app_key +
                "&redirect_uri=" + redirect_uri +
                "&response_type=code"
        )
        webbrowser.open(auth_url)

        auth_code = self.local_server()
        print("auth_code obtenido: " + auth_code)

        token_url = "https://api.dropbox.com/oauth2/token"
        data = {
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "client_id": app_key,
            "client_secret": app_secret
        }
        response = requests.post(token_url, data=data)
        response_json = response.json()
        print("Respuesta token: ", response_json)

        self._access_token = response_json["access_token"]
        print("access_token: " + self._access_token)


        self._root.destroy()

    def list_folder(self, msg_listbox):
        print("/list_folder")
        uri = 'https://api.dropboxapi.com/2/files/list_folder'

        # Dropbox-en APIrako erroaren (root) balidazioa
        folder_path = "" if self._path == "/" else self._path

        headers = {
            'Authorization': f'Bearer {self._access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            "path": folder_path,
            "recursive": False,
            "include_media_info": False,
            "include_deleted": False,
            "include_has_explicit_shared_members": False
        }

        response = requests.post(uri, headers=headers, json=data)

        if response.status_code == 200:
            contenido_json = response.json()
            self._files = helper.update_listbox2(msg_listbox, self._path, contenido_json)
        else:
            print(f"Errorea karpeta zerrendatzean: {response.text}")

    def transfer_file(self, file_path, file_data):
        print("/upload")
        uri = 'https://content.dropboxapi.com/2/files/upload'

        headers = {
            'Authorization': f'Bearer {self._access_token}',
            'Dropbox-API-Arg': json.dumps({
                "path": file_path,
                "mode": "add",
                "autorename": True,
                "mute": False,
                "strict_conflict": False
            }),
            'Content-Type': 'application/octet-stream'
        }

        response = requests.post(uri, headers=headers, data=file_data)

        if response.status_code == 200:
            print("Fitxategia ondo igo da.")
        else:
            print(f"Errorea fitxategia igotzean: {response.text}")

    def delete_file(self, file_path):
        print("/delete_file")
        uri = 'https://api.dropboxapi.com/2/files/delete_v2'

        headers = {
            'Authorization': f'Bearer {self._access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            "path": file_path
        }

        response = requests.post(uri, headers=headers, json=data)

        if response.status_code == 200:
            print("Fitxategia ondo ezabatu da.")
        else:
            print(f"Errorea fitxategia ezabatzean: {response.text}")

    def create_folder(self, path):
        print("/create_folder")
        uri = 'https://api.dropboxapi.com/2/files/create_folder_v2'

        headers = {
            'Authorization': f'Bearer {self._access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            "path": path,
            "autorename": False
        }

        response = requests.post(uri, headers=headers, json=data)

        if response.status_code == 200:
            print("Karpeta ondo sortu da.")
        else:
            print(f"Errorea karpeta sortzean: {response.text}")

    ## 8. Puntua, metodo extra
    def get_space_usage(self):
        """
        Funtzionalitate gehigarria: Kontuaren espazioa kontsultatu.
        """
        print("/get_space_usage")
        uri = 'https://api.dropboxapi.com/2/users/get_space_usage'

        headers = {
            'Authorization': f'Bearer {self._access_token}'
        }

        response = requests.post(uri, headers=headers)

        if response.status_code == 200:
            data = response.json()
            used_mb = data.get('used', 0) / (1024 * 1024)
            allocated_mb = data.get('allocation', {}).get('allocated', 0) / (1024 * 1024)
            print(f"--- KONTUAREN INFORMAZIOA ---")
            print(f"Erabilitako espazioa: {used_mb:.2f} MB")
            print(f"Guztirako espazioa: {allocated_mb:.2f} MB")
            print(f"-----------------------------")
            return used_mb, allocated_mb
        else:
            print(f"Errorea kontuaren informazioa eskuratzean: {response.text}")
            return None, None