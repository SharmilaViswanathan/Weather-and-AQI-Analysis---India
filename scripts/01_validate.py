import pandas as pd

weather_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

weather = pd.read_csv(weather_path)
aqi = pd.read_csv(aqi_path, low_memory=False)

print(weather.shape)
print(aqi.shape)

print(weather.info())
print(aqi.info())

print(weather.head())
print(aqi.head())

print(weather.describe())
print(aqi.describe())

print(weather.dtypes)
print(aqi.dtypes)

weather["datetime"] = pd.to_datetime(weather["datetime"], errors="coerce")
aqi["date"] = pd.to_datetime(aqi["date"], errors="coerce")

print(weather["datetime"].isna().sum())
print(aqi["date"].isna().sum())

print(weather.isnull().sum())
print(aqi.isnull().sum())

print(weather["datetime"].min(), weather["datetime"].max())
print(aqi["date"].min(), aqi["date"].max())

print(weather["city_name"].nunique())
print(aqi["City"].nunique())
