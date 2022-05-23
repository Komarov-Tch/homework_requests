import requests


def the_smartest(adress='https://superheroapi.com/api/2619421814940190/search/',
                 heroes=['Hulk', 'Captain America', 'Thanos'],
                 stat='intelligence'):
    for hero_name in heroes:
        result = []
        response = requests.get(adress + hero_name)
        result = [(hero_name, character['powerstats'][stat])
                  for character in response.json()['results']
                  if character['name'] == hero_name]

    return max(result, key=lambda x: int(x[1]))


if __name__ == '__main__':
    print(the_smartest())
