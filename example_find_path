import requests
import json
# Мой дом, посмотреть можно тут https://www.google.ru/maps/@60.0179656,30.23251,17.5z
lon_1 = 60.01774
lat_1 = 30.23169

# Политех
lon_2 = 60.00034
lat_2 = 30.36574

r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")

# Получим пути
routes = json.loads(r.content)
# Получим лучший путь
route_1 = routes.get("routes")[0]

# ответ
print(route_1)
# формат ответа:
"""
{
  'legs': 
    [
        {'steps': [], 'weight': 1509.9, 'distance': 14707.6, 'summary': '', 'duration': 1509.9}
    ], 
  'weight_name': 'routability', 
  'weight': 1509.9, 
  'distance': 14707.6, 
  'duration': 1509.9} # Нас интересует это - длительность поездки
"""
