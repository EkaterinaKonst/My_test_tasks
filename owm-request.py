import requests
from datetime import datetime

APPID = '103a8f53e1ac39dd1b9393bd3c10e3ac'
URL_BASE = "http://api.openweathermap.org/data/2.5/"
OUT_OF_VIEW = ['current,minutely,hourly,alerts']

def sort_key(e):
    return e[1]

def weather_onecall(lat: float = 55.75, lon: float = 37.61,
                    appid: str = APPID,
                    exclude = OUT_OF_VIEW,
                    units='metric')-> dict:
    """https://openweathermap.org/api/one-call-api"""
    ans = requests.get(URL_BASE + "onecall", params=locals()).json()
    temp1=[]
    temp2=[]
    for i in ans['daily']:
        k=i['feels_like']['night'] - i['temp']['night']
        temp1.append([i['dt'],k])
        my_temp = sorted(temp1, key=sort_key, reverse=True)
        my_date = my_temp[0][0]
        my_date = datetime.utcfromtimestamp(int(my_date)).strftime('%Y-%m-%d')
        n=i['sunset'] - i['sunrise']
        temp2.append([i['dt'],n])
        my_time= sorted(temp2, key=sort_key, reverse=True)
        my_timedate1 = datetime.utcfromtimestamp(int(my_time[0][0])).strftime('%Y-%m-%d')
        my_timedate2 = datetime.utcfromtimestamp(int(my_time[0][1])).strftime('%H:%M:%S')


    print(f'День с минимальной разницей фактической и ощущаемой температурой ночью это {my_date} с температурой {round(my_temp[0][1],2)}')
    print(f'Максимальная продолжительность светового дня {my_timedate2} в день {my_timedate1}')



if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location:").strip()
        if location:
            pprint(weather_onecall())
        else:
            break