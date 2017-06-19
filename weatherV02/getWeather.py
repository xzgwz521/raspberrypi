from urllib import request, parse
import json


class Weather:
    def __init__(self, location='hangzhou'):
        self.location = location

    def get_weather_now(self):
        try:
            req = request.Request('https://api.seniverse.com/v3/weather/now.'
                                  'json?key=u5l6zgrzcdcagkmz&location=' + self.location + '&language=zh-Hans&unit=c')
            response = request.urlopen(req).read().decode('UTF-8')
            json_now = json.loads(response)
            return json_now
        except:
            return None

    def get_weather_daily(self):
        try:
            req = request.Request('https://api.seniverse.com/v3/weather/daily.'
                                  'json?key=u5l6zgrzcdcagkmz&location=' + self.location +
                                  '&language=zh-Hans&unit=c&start=0&days=3')
            response = request.urlopen(req).read().decode('UTF-8')
            json_daily = json.loads(response)
            return json_daily
        except:
            return None


if __name__ == '__main__':
    weather = Weather('beijing')
    print(weather.location)
    print(weather.get_weather_now())
