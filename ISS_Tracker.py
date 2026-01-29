import requests
import json
from datetime import datetime

# URL for the ISS API that provides the current location of the International Space Station
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

# Save as JSON

# Creates a unique filename so that each run does not overwrite the previous
filename = f"iss_location_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(filename, 'w') as f:
    json.dump(data, f, indent=2)

# Pulls latitude and longtitude from API 
lat = data["iss_position"]["latitude"]
lon = data["iss_position"]["longitude"]

# Prints the longtitude, latitude, file name and Success message
print(f"The International Space Statitons coordinates are: Latitude {lat}, Longitude {lon}")
print(f"Data saved to {filename}")
print("Script ran successfully")
