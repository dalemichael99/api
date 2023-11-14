from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

locations = {
    'Lake District National Park': (54.4609, -3.0886),
    'Corfe Castle': (50.6395, -2.0566),
    'The Cotswolds': (51.8330, -1.8433),
    'Cambridge': (52.2053, 0.1218),
    'Bristol': (51.4545, -2.5879),
    'Oxford': (51.7520, -1.2577),
    'Norwich': (52.6309, 1.2974),
    'Stonehenge': (51.1789, -1.8262),
    'Watergate Bay': (50.4429, -5.0553),
    'Birmingham': (52.4862, -1.8904)
}

def generate_fake_weather(location):
    latitude, longitude = locations.get(location, (0, 0))
    temperature = round(random.uniform(15, 30), 2)
    humidity = round(random.uniform(40, 80), 2)
    wind_speed = round(random.uniform(0, 10), 2)
    description_options = ['Sunny', 'Cloudy', 'Rainy', 'Stormy']
    description = random.choice(description_options)

    weather_data = {
        'location': location,
        'latitude': latitude,
        'longitude': longitude,
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'description': description
    }

    return weather_data

@app.route('/')
def index():
    return render_template('index.html', locations=locations.keys())

@app.route('/api/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')

    if location:
        weather_data = generate_fake_weather(location)
        return jsonify(weather_data), 200
    else:
        return jsonify({'error': 'Please provide a location parameter'}), 400

if __name__ == '__main__':
    app.run(debug=True)
