import csv
from requests_html import HTMLSession

filename = 'world_cities.csv'
H = HTMLSession()



def get_weather():
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            try:
                url = f'https://www.google.com/search?q=weather+{row[1]}'
                r = H.get(url, headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'} )

                temp = r.html.find('span#wob_tm', first=True).text
                unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
                description = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

                print(f'{row[0]}, {row[1]}, {temp} {unit}, {description}\n')
            except Exception as e:
                pass
    
get_weather()