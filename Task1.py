import json
import wikipedia
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


class CountriesWiki:

    def __init__(self, file_name):
        self.counter = 0
        self.file_name = file_name
        self.file = open(self.file_name, encoding='utf8')
        self.json_data = json.load(self.file)
        self.country_name = ''
        self.url = ''

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.json_data):
            self.file.close()
            raise StopIteration

        self.country_name = self.json_data[self.counter]['translations']['rus']['common']
        try:
            wikipedia.set_lang('ru')
            self.url = wikipedia.page(self.json_data[self.counter]['translations']['rus']['common']).url
        except wikipedia.WikipediaException:
            wikipedia.set_lang('en')
            self.url = wikipedia.page(self.json_data[self.counter]['name']['official']).url

        self.counter += 1
        return f'{self.country_name} - {self.url}'


my_iter = CountriesWiki('countries.json')
with open('result.txt', 'w', encoding='utf8') as file:
    for i in my_iter:
        file.write(f'{i} \n')
        print(f'{i}')
