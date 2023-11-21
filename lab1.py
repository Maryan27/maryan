import math
import requests

url = "https://www.python.org"
response = requests.get(url)
print(response.text)

holiday = "New Year"
print(holiday)
is_adult = False
is_teen = True
Result= is_adult and is_teen
is_calm = True
is_windy = True
Result2= is_calm or is_windy
print(Result2)

x=0.013 
z=1.245
print(math.sin(x**math.cos(z))+(math.tan(z))**math.sin(x))