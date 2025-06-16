from flask import Flask,render_template,request
import requests
import json
app = Flask(__name__)

def get_cities_data():
    cities = ['Hyderabad', 'Mumbai', 'Kolkata', 'Bengaluru']
    city_data = []

    for city in cities:
        URL = f"http://api.weatherapi.com/v1/current.json?key=16408770f955407d8c2182733251106&q={city}"
        response = requests.get(URL)
        data = json.loads(response.text)

        city_data.append({
            'name': city,
            'temp': data["current"]["temp_c"],
            'humidity': data["current"]["humidity"],
            'wind': data["current"]["wind_kph"]
        })

    return city_data


def get_city_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=16408770f955407d8c2182733251106&q={city}"
    response = requests.get(url)
    data = json.loads(response.text)
    return {
        "city": data["location"]["name"],
        "temp": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"]
    }
@app.route('/')
def home():
    cities = ["Hyderabad", "Mumbai", "Kolkata", "Bengaluru"]
    return render_template('index.html',
                           temp="-",
                           humidity="-",
                           wind="-",
                           city="-",
                           avg_temp="-",
                           min_temp="-",
                           max_temp="-",
                           avg_humidity="-",
                           chance="-",
                           dewpoint_c="-",
                           wind_kph="-",
                           wind_degree="-",
                           wind_dir="-",
                           cities=get_cities_data())  # if using 4 city data

@app.route('/weather' , methods=['POST'])
def weather():
    city= request.form['city']
    URL=f"http://api.weatherapi.com/v1/forecast.json?key=16408770f955407d8c2182733251106&q={city}"
    response = requests.get(URL)
    data=json.loads(response.text)
    if 'error' in data:
        error_message = data['error']['message']
        cities = ["Hyderabad", "Mumbai", "Kolkata", "Bengaluru"]
        city_data = [get_city_weather(c) for c in cities]
        return render_template('index.html',
                               temp="-",
                               humidity="-",
                               wind="-",
                               city=city,
                               avg_temp="-",
                               min_temp="-",
                               max_temp="-",
                               avg_humidity="-",
                               chance="-",
                               dewpoint_c="-",
                               wind_kph="-",
                               wind_degree="-",
                               wind_dir="-",
                               error=error_message,
                               cities=city_data)
    T=data["current"]["temp_c"]
    H=data["current"]["humidity"]
    W=data["current"]["wind_kph"]
    current = data["current"]
    dewpoint_c = current["dewpoint_c"]
    wind_kph = current["wind_kph"]
    wind_degree = current["wind_degree"]
    wind_dir = current["wind_dir"]
    average = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    max_temp = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
    avg_humidity = data["forecast"]["forecastday"][0]["day"]["avghumidity"]
    chance = data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]

    cities = ["Hyderabad", "Mumbai", "Kolkata", "Bengaluru"]
    city_data = [get_city_weather(c) for c in cities]

    return render_template('index.html',temp=T,
                           humidity=H,
                           wind=W,
                           city=city,
                           avg_temp=average,
                           min_temp=min_temp,
                           max_temp=max_temp,
                           avg_humidity=avg_humidity,
                           chance=chance,
                           dewpoint_c=dewpoint_c,
                           wind_kph=wind_kph,
                           wind_degree=wind_degree,
                           wind_dir=wind_dir,
                           cities=city_data)

if __name__ == '__main__':
    app.run(debug=True)
