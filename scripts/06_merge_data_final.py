import pandas as pd

weather_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_AQI_Info.csv"

output_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\finalized_data.csv"

weather = pd.read_csv(weather_path, parse_dates=["date"])

aqi = pd.read_csv(aqi_path, parse_dates=["date"])

print("Weather shape:", weather.shape)

print("AQI shape:", aqi.shape)

print("Weather duplicate city/date:", weather.duplicated(["city", "date"]).sum())

print("AQI duplicate city/date:", aqi.duplicated(["city", "date"]).sum())

#Merge weather and aqi datasets
final = pd.merge(weather, aqi, on=["city", "date"], how="inner")

print("Merged shape:", final.shape)

#Sort
final = final.sort_values(["city", "date"])

final["Prominent Pollutant"] = (final["Prominent Pollutant"].fillna("Unknown"))

#Final checks on merged data
print("Rows:", len(final))

print("Columns:", len(final.columns))

print("Cities:", final["city"].nunique())

print("Date range:", final["date"].min(), "to", final["date"].max())

#Checking null values again
print(final.isnull().sum())

print(final["city"].value_counts().sort_index())

#Save final dataset
final.to_csv(output_path, index=False)

print(output_path)
