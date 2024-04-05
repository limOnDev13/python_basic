import requests
from requests import Response
import json


def get_pilots_x_wing() -> None:
    """
    Функция выводит на экран и сохраняет в файл информацию о всех пилотах легендарного истребителя x-wing
    :return: None
    :raise KeyError: If the response body does not contain valid json.
    """
    ship_info: Response = requests.get('https://swapi.dev/api/starships/12')
    if ship_info.status_code == 200:
        data: dict = json.loads(ship_info.text)

        # По ключу 'pilots' лежат ссылки на пилотов. В словаре data заменим эти ссылки на json по этим ссылкам
        for index, pilot_url in enumerate(data['pilots']):
            data['pilots'][index] = json.loads(requests.get(pilot_url).text)

        print(json.dumps(data, indent=4))

        with open('pilots.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:
        raise KeyError(f'pilots_info.status_code = {ship_info.status_code}')


if __name__ == '__main__':
    get_pilots_x_wing()
