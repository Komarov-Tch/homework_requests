import requests
import os
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_header()
        params = {'path': 'netology/myfile.txt', 'overwrite': 'true'}
        resp = requests.get(files_url, headers=headers, params=params)
        if resp:
            href = resp.json().get('href', '')
            response = requests.put(href, data=open(file_path, 'rb'))
            if response.status_code == 201:
                return 'Успех, файл загружен'
            else:
                return 'Ошибка загрузки файла:'
        else:
            return 'Ошибка выполнения запроса: \n' + files_url + f'\nHttp статус: {resp.status_code}, ({resp.reason})'


if __name__ == '__main__':
    adress_file = os.path.join(os.getcwd(), 'uplod_file')
    file_name = 'netology.txt'
    path_to_file = os.path.join(adress_file, file_name)
    token = 'AQAEA7qj0raoAADLW_vnoQBqMUVSomYC9clYjfw'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
