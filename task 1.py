import requests


def the_smartest(adress='https://superheroapi.com/api/2619421814940190/search/',
                 heroes=['Hulk', 'Captain America', 'Thanos']):
    result = []
    for hero_name in heroes:
        response = requests.get(adress + hero_name)
        result.append((hero_name, response.json()['results'][0]['powerstats']['intelligence']))
    return max(result, key=lambda x: int(x[1]))


if __name__ == '__main__':
    print(the_smartest())
