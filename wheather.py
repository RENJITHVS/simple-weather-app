import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=c492a30aa01c930bd50806b088306700"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = int(json_data['main']['pressure'])
    humidity = int(json_data['main']['humidity'])
    wind =  json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 19800))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "pressure: " + str(pressure) + "\n" + "humidity: " + str(humidity) + "\n" + "windspeed :" + str(wind) + "\n" + "sunrise: " + str(sunrise) + "\n" + "sunset: " + str(sunset)

    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("wheather app")

f= ("Monotype Corsiva", 15 , "bold")
t= ("Monotype Corsiva", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1= tk.Label(canvas,font = t)
label1.pack()

label2 = tk.Label(canvas,font = f)
label2.pack()

canvas.mainloop()