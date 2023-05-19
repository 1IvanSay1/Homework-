import requests
def intelligence():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    names_of_characters = ['Hulk', 'Captain America', 'Thanos']
    responce = requests.get(url)
    heroes = responce.json()
    super_hero = {}
    for i in heroes:
        for name in names_of_characters:
            if name == i["name"]:
                super_hero_dict = dict.fromkeys([i["name"]], i["powerstats"]["intelligence"])
                super_hero.update(super_hero_dict)
    max_intelligence_super_hero = max(super_hero, key=super_hero.get)
    print(f'Самый умный супергерой {max_intelligence_super_hero}, его интеллект = {max(super_hero.values())}')         


if __name__ == '__main__':
    intelligence()
