from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'e833365165d487bf05b4ea823c4bea26'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return render_template('weather.html', weather=weather_data)
        else:
            error_message = data['message']
            return render_template('error.html', error=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
