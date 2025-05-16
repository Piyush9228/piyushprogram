from flask import Flask, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def weather():
    location = "London"  #Select by on your choice
    API_KEY = "bc6f0e6520a08b4c95b0ae1753f65000"
    url = "http://api.weatherstack.com/current"

    response = requests.get(url, params={"access_key": API_KEY, "query": location})
    data = response.json()

    if "current" not in data:
        return f"<h1>Error: {data.get('error', 'Unknown error')}</h1>"

    html = f"""
    <html>
    <head><title>WeatherReport</title></head>
    <body>
        <h1>Weather in {location}</h1>
        <ul>
            <li><strong>Temperature:</strong> {data['current']['temperature']}°C</li>
            <li><strong>Description:</strong> {data['current']['weather_descriptions'][0]}</li>
            <li><strong>Humidity:</strong> {data['current']['humidity']}%</li>
            <li><strong>Pressure:</strong> {data['current']['pressure']} hPa</li>
            <li><strong>Wind Speed:</strong> {data['current']['wind_speed']} km/h</li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
