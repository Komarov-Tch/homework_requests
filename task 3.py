import requests
from pprint import pprint
import datetime as dt


class StackOvewrflow:
    def tag_request(self, tag):
        date = f'{dt.date.today() - dt.timedelta(days=2)}'
        url = f'https://api.stackexchange.com/2.2/questions?fromdate={date}' \
              f'&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
        response = requests.get(url)
        result = [(i['title'], i['link']) for i in response.json()['items']]
        if response:
            pprint(result)
        else:
            print('Ошибка выполнения запроса: \n' + url + f'\nHttp статус: {response.status_code}, ({response.reason})')


if __name__ == '__main__':
    so = StackOvewrflow()
    so.tag_request('Python')
