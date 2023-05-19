import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'y0_AgA {self.token}'
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': file_path, 'overwrite': "false"}
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()
        href = response_data[href]
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = open("")
    print(path_to_file)
    token = ''
    uploader = YaUploader(token=token)
    result = uploader.upload(path_to_file)
