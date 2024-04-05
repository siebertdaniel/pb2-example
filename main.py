# Imports hier

# Lädt die prod.env Datei
load_dotenv("./prod.env")
API_KEY = os.getenv("API_KEY")

# Beispiel URL
URL = "http://api.openweathermap.org/data/2.5/weather?q=hamburg&appid=5c8ac9c5fca2b7b5313bb7be4059e04a&units=metric" 

# X und Y Coordinaten für Texte
location_x  = 70
location_y  = 25

sunrise_x = 60
sunrise_y = 240

sunset_x = 240
sunset_y = 240

temp_min_x = 60
temp_min_y = 430

temp_max_x = 240
temp_max_y = 430

description_x = 60
description_y = 530

# Start coding here