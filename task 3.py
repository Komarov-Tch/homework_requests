import requests
from pprint import pprint
import datetime as dt
import time


class StackOvewrflow:
    def tag_request(self, tag):
        date = f'{dt.date.today() - dt.timedelta(days=2)}'
        result = []
        for i in range(1, 1000):
            result_temp = []
            url = f'https://api.stackexchange.com/2.3/questions?page={i}&pagesize=100&fromdate={date}' \
                  f'&order=desc&sort=creation&tagged={tag}&site=stackoverflow'
            response = requests.get(url)
            if response:
                result_temp = [i['link'] for i in response.json()['items']]
                result.extend(result_temp)
            else:
                print(f'Http статус: {response.status_code}, ({response.reason})')
                break
            time.sleep(1)
        print(len(result))
        print(i)
        pprint(result)


if __name__ == '__main__':
    so = StackOvewrflow()
    so.tag_request('Python')
