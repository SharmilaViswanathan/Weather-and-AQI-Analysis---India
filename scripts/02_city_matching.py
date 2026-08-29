import pandas as pd
import unicodedata

weather_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

weather = pd.read_csv(weather_path)
aqi = pd.read_csv(aqi_path, low_memory=False)

#Normalization
def normalize_city(city):
    if pd.isna(city):
        return ""

    city = str(city)

    #Remove accents
    city = unicodedata.normalize("NFKD", city)

    city = "".join(char 
        for char in city
        if not unicodedata.combining(char)
    )

    #Lowercase
    city = city.lower()

    #Replace separators
    city = city.replace("-", " ")
    city = city.replace("_", " ")

    #Remove extra spaces
    city = " ".join(city.split())

    return city.strip()

#Create normalized city columns
weather["normalized_city"] = (
    weather["city_name"]
    .apply(normalize_city)
)

aqi["normalized_city"] = (
    aqi["City"]
    .apply(normalize_city)
)

city_mapping = {"bangalore": "bengaluru",
                "pimpri chinchwad": "pimpri chinchwad",}

weather["normalized_city"] = weather["normalized_city"].replace(city_mapping)

#Finalized cities
selected_cities = {
    #East
    "guwahati": "Guwahati",
    "kolkata": "Kolkata",
    "howrah": "Howrah",
    "patna": "Patna",

    #North
    "delhi": "Delhi",
    "lucknow": "Lucknow",
    "kanpur": "Kanpur",
    "agra": "Agra",

    #South
    "bengaluru": "Bengaluru",
    "chennai": "Chennai",
    "hyderabad": "Hyderabad",
    "visakhapatnam": "Visakhapatnam",

    #West
    "ahmedabad": "Ahmedabad",
    "mumbai": "Mumbai",
    "nashik": "Nashik",
    "pune": "Pune"
}

for normalized, display_name in selected_cities.items():
    print(display_name)

for normalized, display_name in selected_cities.items():
    count = (weather["normalized_city"] == normalized).sum()
    print(f"{display_name:20} → {count:,} weather rows")

for normalized, display_name in selected_cities.items():
    count = (aqi["normalized_city"] == normalized).sum()
    print(f"{display_name:20} → {count:,} AQI rows")
