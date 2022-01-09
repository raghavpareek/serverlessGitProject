import json
import urllib3 
import os
from datetime import datetime
def helloWorld(event, context):
     return {
         'statusCode' : 200,
         'body' : json.dumps("Hello Bewgle")
     }
  
def getDetailsByCity(event, context):
     http = urllib3.PoolManager()
     #creating output variable
     out_var={}
     #api_key from openWeatherMap Website
     user_api = "1c2f943d8f485d7b125a9b9aae08324b"
     #print(user_api)
     location = event["queryStringParameters"]["city"]

     complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
     r = http.request('GET', complete_api_link)
    
     #api_link = requests.get(complete_api_link)
     #api_data = api_link.json()
     
     api_data = json.loads(r.data.decode('utf-8'))

     #print(api_data)
     #print(api_data)
     if api_data['cod'] =='404':
        #print("Invalid City: {}, Please check your City name".format(location))
        return{
            'statusCode':404,
            'body':json.dumps({"error":"Invalid City: {}, Please check your City name".format(location)})
        }
    
     else:
        #storing required data into the variables.
        temp_city = ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


        # print("Weather stats for - {} ||{}".format(location.upper(),date_time))
        # print("Current temperature is: {:.2f} deg C".format(temp_city))
        # print("Current Weather desc: ",weather_desc)
        # print("Current humidity: ",hmdt, '%')
        # print("Current Wind Speed: ",wind_spd, 'kpmh')
        out_var = {
            "Weather Stats for ":"{} ||{}".format(location.upper(),date_time),
            "Current_temperature" :"{:.2f} deg C".format(temp_city),
            "Current Weather Description ":weather_desc,
            "Current Humidity ":hmdt
        }
    
     return {
        'statusCode': 200,
        'body': json.dumps(out_var)
    }





