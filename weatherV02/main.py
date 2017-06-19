# -*- coding: utf-8 -*-
import pygame
import time
from datetime import datetime
from sys import exit
from pygame.locals import *
import getWeather


Yellow = (255,255,0)
Red = (255,0,0)
LightBlue = (190,190,255)
Green = (0,255,0)
Black = (0,0,0)
White = (255,255,255)

pygame.init()

width = 1024
height = 600
Fullscreen = False
screen = pygame.display.set_mode((width, height), 0, 32)


def show_background():
    pygame.draw.rect(screen, White, (0, 0, width, height), 10)
    pygame.draw.line(screen, White, (0, height/2), (width, height/2), 6)
    pygame.draw.line(screen, White, (width/2, 0), (width/2, height/2), 6)
    pygame.draw.line(screen, White, (width/3, height/2), (width/3, height), 2)
    pygame.draw.line(screen, White, (width/3*2, height/2), (width/3*2, height), 2)


def show_str(my_string, x0, y0, size):
    font = pygame.font.Font("msyh.ttf", size)
    text_surface = font.render(my_string, True, White)
    screen.blit(text_surface, (x0, y0))
    return


def show_img(img_path, x0, y0):
    background = pygame.image.load(img_path)
    background.convert_alpha()
    screen.blit(background, (x0, y0))
    return


loop = 0
updatetime = ""
while True:
    screen.fill(pygame.Color(0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((width, height), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((width, height), 0, 32)

    # 显示背景线框
    show_background()

    # 显示时间地点
    mylocaltime = time.localtime()
    mydate = time.strftime("%Y-%m-%d", mylocaltime)
    mytime = time.strftime("%H:%M:%S", mylocaltime)
    myweek = time.strftime("%A", mylocaltime)
    show_str(mytime, width/32*1.5, height/32*2, size=100)
    show_str(mydate, width/32*2, height/32*11, size=30)
    show_str(myweek, width/32*9, height/32*11, size=30)

    # 获取天气信息
    if (datetime.now().minute == 0 and datetime.now().second == 0)or loop == 0:
        json_now = getWeather.fetch_weather_now()
        json_daily = getWeather.fetch_weather_daily()

        weather_now = json_now['results'][0]
        weather_daily = json_daily['results'][0]
        updatetime = time.strftime("%H:%M:%S", mylocaltime)

    # 显示天气
    # 显示实时天气
    city = weather_now['location']['name']
    temp = weather_now['now']['temperature']
    weather = weather_now['now']['text']
    show_img('img-180/' + weather_now['now']['code'] + ".png", width/32*21, height/32*0.5)
    show_str(city, width/32*17, height/32*11, size=50)
    show_str(temp + '℃', width/32*20.5, height/32*9, size=100)
    show_str(weather, width/32*28, height/32*11, size=50)

    # 显示今天天气概况
    day0 = weather_daily['daily'][0]['date']
    weather_day_0 = weather_daily['daily'][0]['text_day']
    weather_night_0 = weather_daily['daily'][0]['text_night']
    temp_high_0 = weather_daily['daily'][0]['high']
    temp_low_0 = weather_daily['daily'][0]['low']

    show_str('今日天气', width/33*3, height/33*17, size=40)
    show_str('白天  ' + weather_day_0, width/33*1, height/33*21, size=30)
    show_str('温度  ' + temp_high_0 + '℃', width/33*1, height/33*23, size=30)
    show_img('img-60/' + weather_daily['daily'][0]['code_day'] + ".png", width/33*7, height/33*21.5)
    show_str('夜晚  ' + weather_night_0, width/33*1, height/33*26, size=30)
    show_str('温度  ' + temp_low_0 + '℃', width/33*1, height/33*28, size=30)
    show_img('img-60/' + weather_daily['daily'][0]['code_night'] + ".png", width / 33 * 7, height / 33 * 26.5)

    # 显示明天天气概况
    day1 = weather_daily['daily'][1]['date']
    weather_day_1 = weather_daily['daily'][1]['text_day']
    weather_night_1 = weather_daily['daily'][1]['text_night']
    temp_high_1 = weather_daily['daily'][1]['high']
    temp_low_1 = weather_daily['daily'][1]['low']

    show_str('明日天气', width/33*14, height/33*17, size=40)
    show_str('白天  ' + weather_day_1, width/33*12, height/33*21, size=30)
    show_str('温度  ' + temp_high_1 + '℃', width/33*12, height/33*23, size=30)
    show_img('img-60/' + weather_daily['daily'][1]['code_day'] + ".png", width / 33 * 18, height / 33 * 21.5)
    show_str('夜晚  ' + weather_night_1 + '℃', width/33*12, height/33*26, size=30)
    show_str('温度  ' + temp_low_1, width/33*12, height/33*28, size=30)
    show_img('img-60/' + weather_daily['daily'][1]['code_night'] + ".png", width / 33 * 18, height / 33 * 26.5)

    # 显示后天天气概况
    day2 = weather_daily['daily'][2]['date']
    weather_day_2 = weather_daily['daily'][2]['text_day']
    weather_night_2 = weather_daily['daily'][2]['text_night']
    temp_high_2 = weather_daily['daily'][2]['high']
    temp_low_2 = weather_daily['daily'][2]['low']

    show_str('后日天气', width/33*25, height/33*17, size=40)
    show_str('白天  ' + weather_day_2, width/33*23, height/33*21, size=30)
    show_str('温度  ' + temp_high_2 + '℃', width/33*23, height/33*23, size=30)
    show_img('img-60/' + weather_daily['daily'][2]['code_day'] + ".png", width/33*29, height/33*21.5)
    show_str('夜晚  ' + weather_night_2, width/33*23, height/33*26, size=30)
    show_str('温度  ' + temp_low_2 + '℃', width/33*23, height/33*28, size=30)
    show_img('img-60/' + weather_daily['daily'][2]['code_night'] + ".png", width/33*29, height/33*26.5)

    show_str('Last update: ' + updatetime, width/33*26, height/33*31, 15)

    pygame.display.update()
    time.sleep(0.1)
    loop += 1
    if datetime.now().hour == 0:
        loop = 0
