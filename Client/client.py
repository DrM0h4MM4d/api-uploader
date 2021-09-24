import requests
from time import sleep
from os.path import getsize
import os

class ClientRequests:
    def __init__(self):
        self.url = '127.0.0.1' # Change it on real projects
        self.port = 8000 # Remove it on real projects
        self.full_url = '127.0.0.1:8000/api/v1/' 
        self.methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] # Default method is GET
        self.api_key = []

    def connection_status(self, url_parameter):
        if url_parameter:
            url = self.full_url + url_parameter
            req = requests.get(url)
            return req.status_code
        return requests.get(self.full_url).status_code

    def connect(self, method: str, url_parameter: str, data: dict):
        if method:
            if method.upper == 'POST':
                conn = requests.post(self.full_url, params=url_parameter, data=data)
                print(f"Connection is available with : {conn.status_code} status code.")
                sleep(5)
                print(f"The data recieved is :\n{conn.json()}")
            elif method.upper == 'PUT':
                conn = requests.put(self.full_url, params=url_parameter, data=data)
                print(f"Connection is available with : {conn.status_code} status code.")
                sleep(5)
                print(f"The data recieved is :\n{conn.json()}")
            elif method.upper == 'PATCH':
                conn = requests.patch(self.full_url, params=url_parameter, data=data)
                print(f"Connection is available with : {conn.status_code} status code.")
                sleep(5)
                print(f"The data recieved is :\n{conn.json()}")
            elif method.uppper == 'DELETE':
                conn = requests.delete(self.full_url, params=url_parameter, data=data)
                print(f"Connection is available with : {conn.status_code} status code.")
                sleep(5)
                print(f"The data recieved is :\n{conn.json()}")
            else:
                conn = requests.get(self.full_url, params=url_parameter, data=data)
                print(f"Connection is available with : {conn.status_code} status code.")
                sleep(5)
                print(f"The data recieved is :\n{conn.json()}")
            return 1
        return 0

    def get_all_files(self):
        all = requests.get(self.full_url + 'upload/files/')
        print(all.json())

    def download(self, fileId):
        api_key = self.api_key[0]
        url = self.full_url + f'upload/file/{fileId}/'
        downloadable_file = requests.get(url, headers={'authorize': api_key})
        name = downloadable_file['file_code']
        dl = downloadable_file['file']
        with requests.get(self.url + str(self.port), params=dl, stream=True) as cf:
            cf.raise_for_status()
            with open(f'downloads/{name}', 'wb') as f:
                for chunk in cf.iter_content(chunk_size=8192):
                    f.seek(0, os.SEEK_END)
                    print(f"{len(cf.content) / f.tell() * 100} Downloading...")
                    f.write(chunk)
            f.close()
            return 1
        return 0

    def upload(self, title, file_path):
        conn = requests.post(self.full_url, params='upload/file/', 
                                            data={'title':title,'file': file_path})
        if conn.status_code == 200:
            print("Uploaded Successfully")
            
    def upload_update(self, title, file_path, pk):
        conn = requests.put(self.full_url, params=f'upload/file/{pk}', 
                                            data={'title':title,'file': file_path})
        if conn.status_code == 200:
            print("Uploaded Successfully")

    def register(self, username, password, password2, phone_number, region, job, why_using):
        conn = requests.post(self.full_url, params='accounts/register/', data={
            'username': username,
            'password': password,
            'password2': password2,
            'phone_number': phone_number,
            'region': region,
            'job': job,
            'why_using': why_using,  
        })
        if conn.status_code == 200:
            print("Registration Completed.")

    def authentication(self, username, password):
        conn = requests.post(self.full_url, params='token/', 
                                    data={'username': username, 'password': password})
        if conn.status_code == 200:
            print('Authentication Success.')
            return 1
        return 0

    def admin_perms(self, perm):
        if perm == "files":
            x = input('1)Delete\n2)Update\n3)RetrieveList\n\nEnter??')
            if x == 1:
                uid = int(input('Enter pk ??'))
                if uid is not None:
                    res = requests.delete(self.full_url + f'upload/file/{uid}')
                    if res.status_code == 200:
                        print("Success.")
            elif x == 2:
                uid = int(input('Enter pk ??'))
                title = input('Enter title >>')
                file_path = input('Enter path of file >>')
                if os.path.exists(file_path):
                    self.upload_update(title, file_path, uid)
                else:
                    print("Wrong path.")
            elif x == 3:
                self.get_all_files()
        else:
            print("wrong input!")



clirequest = ClientRequests()