import ssl
from urllib import request, parse
import json
import sys


KEY = 'u5l6zgrzcdcagkmz'  # API key
UID = "U288E2A758"  # 用户ID

LOCATION = 'hangzhou'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API_NOW = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
API_DAILY = 'https://api.seniverse.com/v3/weather/daily.json'
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言
START = 0
DAYS = 3


gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


def get_location():
    """get location from user input
    default beijing
    """
    argvs = sys.argv
    location = argvs[1] if len(argvs) >= 2 else LOCATION
    return location


def fetch_weather_now(location):
    params = parse.urlencode({
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    })
    try:
        req = request.Request('{api}?{params}'.format(api=API_NOW, params=params))
        response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
        json_now = json.loads(response)
        return json_now
    except:
        return None


def fetch_weather_daily(location):
    params = parse.urlencode({
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT,
        'start': START,
        'days': DAYS
    })
    try:
        req = request.Request('{api}?{params}'.format(api=API_DAILY, params=params))
        response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
        json_daily = json.loads(response)
        return json_daily
    except:
        return None


if __name__ == '__main__':
    location = get_location()
    jsonRes = fetch_weather_now(location)
    weather_now = jsonRes['results'][0]
    print(weather_now)
    city = weather_now['location']['name']
    temp_now = weather_now['now']['temperature']
    weather = weather_now['now']['text']
    last_update = weather_now['last_update']

    print(city, temp_now, weather, last_update)
