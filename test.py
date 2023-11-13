
import math
from geopy.geocoders import Nominatim


def calculate_dew_point_alternative(temp, humid):
    dew_point = 243.04 * (math.log(humid/100.0) + ((17.625 * temp)/(243.04 + temp))) / (17.625 - math.log(humid/100.0) - ((17.625 * temp)/(243.04 + temp)))
    return dew_point

# Given values
temperature = 65
humidity = 100  # Assuming 100% humidity

# Calculate dew point using the alternative function
dew_point_result = calculate_dew_point_alternative(temperature, humidity)

# Print the result
print(f"The dew point is approximately {dew_point_result:.2f}.")



def getAltitudeFromGeopy(latitude, longitude):
    geolocator = Nominatim(user_agent="altitude_finder")
    location = geolocator.reverse((latitude, longitude), language="en")

    if location and "altitude" in location.raw:
        altitude = location.raw["altitude"]
        return altitude
    else:
        return None


latitude = 37.7749  # Replace with your desired latitude
longitude = -122.4194  # Replace with your desired longitude

altitude = getAltitudeFromGeopy(32.7795842121212,-96.8648941818182,)
print(altitude)