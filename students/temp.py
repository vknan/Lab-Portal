import requests

def get_user_location_and_temperature(request):
    # Get the user's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Make a request to the IP geolocation API
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()

    if data['status'] == 'success':
        # Retrieve the location details
        city = data['city']
        region = data['regionName']
        country = data['country']

        # Get the weather information using the location
        api_key = 'fad5fe7ea033e16e5c283b0c9184b152'
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}')
        weather_data = weather_response.json()
        print(weather_data)
        if weather_data['cod'] == 200:
            # Retrieve the temperature
            temperature = weather_data['main']['temp']
            temperature_celsius = temperature - 273.15  # Convert temperature to Celsius

            return city, region, country, temperature_celsius
        else:
            return None
    else:
        return None