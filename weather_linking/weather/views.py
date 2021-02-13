from django.shortcuts import render
from .models import today_weather_db,weather_data_db
import requests

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=37.566535&lon=126.977969&exclude=minutely,hourly,alerts&appid=43fcd06479e874bea4eb2b675ab6b465'
    
    
    if request.method == "POST":
        pass

    r = requests.get(url).json()
    current = r["current"]
    daily_list = r["daily"]

    today_weather = {
        "temp": round((current["temp"] - 271.94), 2),
        "main": current["weather"][0]["main"],
        "description" : current["weather"][0]["description"],
        "icon": current["weather"][0]["icon"]
    }

    weather_data = []
    for index, daily in enumerate(daily_list):
        daily_weather = {
            "day": index,
            "main": daily["weather"][0]["main"],
            "description" : daily["weather"][0]["description"],
            "icon": daily["weather"][0]["icon"]
        }
        weather_data.append(daily_weather)
    del weather_data[0]
    context = {
        'weather_data' : weather_data, 
        'today_weather' : today_weather    
    }

    return render(request, 'weather/weather.html', context)



def save_weather(request):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=37.566535&lon=126.977969&exclude=minutely,hourly,alerts&appid=43fcd06479e874bea4eb2b675ab6b465'
    
    
    if request.method == "POST":
        pass

    r = requests.get(url).json()
    current = r["current"]
    daily_list = r["daily"]

    today_weather = {
        "temp": round((current["temp"] - 271.94), 2),
        "main": current["weather"][0]["main"],
        "description" : current["weather"][0]["description"],
        "icon": current["weather"][0]["icon"]
    }

    today_weather_db(
        real=True,
        main=today_weather["main"], 
        description=today_weather["description"]
    ).save()

    ## 예측 값을 저장 7개죠
    weather_data = []

    for index, daily in enumerate(daily_list):
        daily_weather = {
            "day": index,
            "main": daily["weather"][0]["main"],
            "description" : daily["weather"][0]["description"],
            "icon": daily["weather"][0]["icon"]
        }
        weather_data.append(daily_weather)

    del weather_data[0]
    
    for idx, data in enumerate(weather_data):
        weather_data_db(
            day= weather_data[idx]["day"],
            main = weather_data[idx]["main"],
            description = weather_data[idx]["description"]
        ).save()


    return render(request, 'weather/save_success.html')


def view_weather(request):
    saved_weather = today_weather_db.objects.all()
    print(saved_weather)

    return render(request, 'weather/save_success.html')