# Imports hier
import os
from dotenv import load_dotenv

# Lädt die prod.env Datei
load_dotenv("prod.env")
API_KEY = os.getenv("API_KEY")

# Beispiel URL
URL = "http://api.openweathermap.org/data/2.5/weather?q=hamburg&appid=5c8ac9c5fca2b7b5313bb7be4059e04a&units=metric" 

# X und Y Coordinaten für Texte
location_x_y = (120, 25)

sunrise_x_y = (75, 242)

sunset_x_y = (250, 242)

temp_min_x_y = (65, 432)

temp_max_x_y = (245, 432)

description_x_y = (65, 530)

# Start coding here