import pandas as pd
import unicodedata

weather_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

start_date = "2015-01-01"
end_date = "2023-12-31"

#City normalization
def normalize_city(city):
    if pd.isna(city):
        return ""

    city = str(city)

    city = unicodedata.normalize("NFKD",city)

    city = "".join(char
                   for char in city
                   if not unicodedata.combining(char))
    city = city.lower()
    city = city.replace("-", " ")
    city = city.replace("_", " ")
    city = " ".join(city.split())

    return city.strip()

#City mapping
city_mapping = {
    "guwahati": "Guwahati",
    "kolkata": "Kolkata",

    #Weather name variations
    "haora": "Howrah",
    "howrah": "Howrah",

    "patna": "Patna",

    "delhi": "Delhi",
    "lucknow": "Lucknow",
    "kanpur": "Kanpur",
    "agra": "Agra",

    "bangalore": "Bengaluru",
    "bengaluru": "Bengaluru",

    "chennai": "Chennai",
    "hyderabad": "Hyderabad",

    "vishakhapatnam": "Visakhapatnam",
    "visakhapatnam": "Visakhapatnam",

    "ahmedabad": "Ahmedabad",
    "mumbai": "Mumbai",

    "nasik": "Nashik",
    "nashik": "Nashik",

    "pune": "Pune"
}

selected_cities = set(city_mapping.values())

#Weather cleaning
weather = pd.read_csv(weather_path, low_memory=False)

#Convert datetime
weather["datetime"] = pd.to_datetime(weather["datetime"], errors="coerce")

#Remove rows with invalid dates
weather = weather.dropna(subset=["datetime"])

#Normalize city names
weather["normalized_city"] = (weather["city_name"].apply(normalize_city))

#Map to standard city names
weather["city"] = (weather["normalized_city"].map(city_mapping))

#Keep selected cities only
weather = weather[weather["city"].isin(selected_cities)]

#Keep required period
weather = weather[(weather["datetime"] >= start_date) & (weather["datetime"] <= end_date)]

#Remove temporary column
weather = weather.drop(columns=["city_name", "normalized_city"])

#Rename date column
weather = weather.rename(columns={"datetime": "date"})

#Remove duplicate city/date records
weather = weather.drop_duplicates(subset=["city", "date"])

#Sort
weather = weather.sort_values(["city", "date"])

#Save
weather_output = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_Weather_Info.csv"

weather.to_csv(weather_output, index=False, encoding="utf-8-sig")

print("Weather cleaned shape:", weather.shape)

aqi = pd.read_csv(aqi_path, low_memory=False)


#Convert date
aqi["date"] = pd.to_datetime(aqi["date"], errors="coerce")

#Remove invalid dates
aqi = aqi.dropna(subset=["date"])

#Normalize city
aqi["normalized_city"] = (aqi["City"].apply(normalize_city))

#Map city names
aqi["city"] = (aqi["normalized_city"].map(city_mapping))

#Keep selected cities
aqi = aqi[aqi["city"].isin(selected_cities)]

#Keep required period
aqi = aqi[(aqi["date"] >= start_date) &(aqi["date"] <= end_date)]

#Convert AQI value to numeric
aqi["Index Value"] = pd.to_numeric(aqi["Index Value"], errors="coerce")

#Remove rows without AQI value
aqi = aqi.dropna(subset=["Index Value"])

# HANDLE CITY + DATE DUPLICATES
duplicate_count = (aqi.duplicated(subset=["city", "date"], keep=False).sum())

print("Duplicate AQI rows before aggregation:",duplicate_count)


# Since final dataset requires one AQI value
# per city per day, aggregate duplicate records.

aqi = (aqi.groupby(["city", "date"], as_index=False)
    .agg({"Index Value": "mean",
          "Air Quality": lambda x: x.mode().iloc[0]
          if not x.mode().empty else x.iloc[0],
          "Prominent Pollutant": lambda x: x.mode().iloc[0]
          if not x.mode().empty else x.iloc[0]
        }))

#Round AQI after averaging
aqi["Index Value"] = (aqi["Index Value"].round(0).astype(int))

#Sort
aqi = aqi.sort_values(["city", "date"])

#Save
aqi_output = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_AQI_Info.csv"

aqi.to_csv(aqi_output,index=False, encoding="utf-8-sig")

print("AQI cleaned shape:", aqi.shape)

print("Saved:", aqi_output)

# FINAL CLEANING SUMMARY
print("Weather rows:", len(weather))

print("AQI rows:", len(aqi))

print("Weather cities:", weather["city"].nunique())

print("AQI cities:", aqi["city"].nunique())

print("Weather date range:", weather["date"].min(), "to", weather["date"].max())

print("AQI date range:", aqi["date"].min(), "to", aqi["date"].max())

