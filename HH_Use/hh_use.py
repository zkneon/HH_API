from tqdm import tqdm
import requests
from pprint import pprint
from time import sleep
import json

'''
fetch("https://api.hh.ru/vacancies", );
'''

class HH_Use:
    def __init__(self, s_text: str = 'Python'):
        self.params = {
            "found": 10,
            "hidden_on_page": 0,
            "text": s_text,
            "page": 0,
            "pages": 1,
            "per_page": 20,
            "area": ['1']
        }
        self.headers = {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "accept-language": "ru,en-US;q=0.9,en;q=0.8",
                        "cache-control": "max-age=0",
                        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "none",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1"
                      }
        self.url = 'https://api.hh.ru/vacancies/'
        self.v_id = []
        self.data = {}
        self.last_vacancy = 2

    def get_data(self):
        resp = requests.get(self.url, params=self.params)
        if resp.ok:
            pprint('Response get')
            return resp.json()
        else:
            print(Exception)

    def separ(self):
        data = self.get_data()
        self.data = data
        self.get_vacancy_id()

    def length_data(self):
        pprint(len(self.data))

    def get_vacancy_id(self):
        items = self.data['items']
        for i in range(self.last_vacancy):
            self.v_id.append(int(items[i]['id']))
        pprint(self.v_id)

    def get_vacancy_by_id(self):
        # pprint(self.v_id)
        ret_list = {}
        for vac in self.v_id:
            pprint(vac)
            resp = requests.get(f'{self.url}{vac}')
            data = resp.json()
            pprint(f'{data["name"]}:{data["alternate_url"]}')
            ret_list[vac] = [data["name"], data["alternate_url"]]

            sleep(1)
        return ret_list


def main():

    hh_o = HH_Use('Python')
    hh_o.separ()
    hh_o.get_vacancy_by_id()


if __name__ == '__main__':
    main()
