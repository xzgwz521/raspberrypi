from urllib import request, parse
import json

LOCATION = 'hangzhou'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等


def fetch_weather_now():
    try:
        req = request.Request('https://api.seniverse.com/v3/weather/now.'
                              'json?key=u5l6zgrzcdcagkmz&location=hangzhou&language=zh-Hans&unit=c')
        response = request.urlopen(req).read().decode('UTF-8')
        json_now = json.loads(response)
        return json_now
    except:
        return None


def fetch_weather_daily():
    try:
        req = request.Request('https://api.seniverse.com/v3/weather/daily.'
                              'json?key=u5l6zgrzcdcagkmz&location=hangzhou&language=zh-Hans&unit=c&start=0&days=3')
        response = request.urlopen(req).read().decode('UTF-8')
        json_daily = json.loads(response)
        return json_daily
    except:
        return None


if __name__ == '__main__':
    jsonRes = fetch_weather_now()
    weather_now = jsonRes['results'][0]
    print(weather_now)
    city = weather_now['location']['name']
    temp_now = weather_now['now']['temperature']
    weather = weather_now['now']['text']
    last_update = weather_now['last_update']

    print(city, temp_now, weather, last_update)
