import forecastio
from geopy.geocoders import Nominatim

def get_current_weather(address):
  location = Nominatim.geocode(address) 
  api_key = " "
  forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude). currently()
  return f"It is currently {forecast.cummary} and {forecast.temperatur} degrees in {location.address}"
  else:
  return"Location not found"
  
print(get_current_weather("New York, NY"))
