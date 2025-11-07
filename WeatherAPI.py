import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):

        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):

        response = requests.get (f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=e54d776778b242f766cfb8c9bab95cef")

        response_json = response.json()

        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def temp_print(self):

        print(f"It is currently {self.temp} degrees celsius in Sofia")
        print(f"Lowest temperature will reach {self.temp_min} degrees celsius")
        print(f"Highest temperature will reach {self.temp_max} degrees celsius")

my_city = City("Sofia", 42.69, 23.31)
my_city.temp_print()