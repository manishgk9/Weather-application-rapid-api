from django.shortcuts import render
import requests
from django.http import HttpResponse
def getWeather(city):
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    querystring = {'city':city}
    headers = {
    "X-RapidAPI-Key": "7470583c7amshd107513ad8c74d3p188d3bjsnbe8a4fdf1a01",
    "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"}
    response = requests.get(url, headers=headers, params=querystring)
    city=(response.json())
    return city
            

def home(request):
    data={'Shanghai':getWeather('Shanghai'),'Kolkata':getWeather('Kolkata'),'Jaunpur':getWeather('Jaunpur'),'Chennai':getWeather('Chennai'),'Noida':getWeather('Noida')}
    data1={'Lucknow':getWeather('Lucknow')}
    if request.method=='POST':
        search=request.POST.get('city')
        if search != None:
           data={search:getWeather(search)} 
           return render(request,'home.html',{'data':data})
        else:
            return HttpResponse("<h2>Please Search some valide places!")    
            
    return render(request,'home.html',{'data':data,'data1':data1})

def About(request):
    return render(request,'about_app.html')

