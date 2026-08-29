import pandas as pd

weather_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

weather = pd.read_csv(weather_path)
aqi = pd.read_csv(aqi_path, low_memory=False)

weather["datetime"] = pd.to_datetime(weather["datetime"], errors="coerce")

aqi["date"] = pd.to_datetime(aqi["date"], errors="coerce")

#City mapping
city_pairs = {
    "Guwāhāti": "Guwahati",
    "Kolkāta": "Kolkata",
    "Hāora": "Howrah",
    "Patna": "Patna",

    "Delhi": "Delhi",
    "Lucknow": "Lucknow",
    "Kanpur": "Kanpur",
    "Āgra": "Agra",

    "Bangalore": "Bengaluru",
    "Chennai": "Chennai",
    "Hyderābād": "Hyderabad",
    "Vishākhapatnam": "Visakhapatnam",

    "Ahmedabad": "Ahmedabad",
    "Mumbai": "Mumbai",
    "Nāsik": "Nashik",
    "Pune": "Pune"
}

#City coverage analysis
results = []

for weather_city, aqi_city in city_pairs.items():
    weather_city_data = weather[weather["city_name"] == weather_city]

    aqi_city_data = aqi[aqi["City"] == aqi_city]

    if len(aqi_city_data) == 0:
        continue

    aqi_start = aqi_city_data["date"].min()
    aqi_end = aqi_city_data["date"].max()

    expected_dates = pd.date_range(start=aqi_start, end=aqi_end, freq="D")

    actual_dates = (aqi_city_data["date"].dropna().dt.normalize().unique())

    actual_dates = pd.DatetimeIndex(actual_dates)

    expected_days = len(expected_dates)

    aqi_days = len(actual_dates)

    missing_days = expected_days - aqi_days

    coverage = (aqi_days / expected_days * 100 if expected_days > 0 
                else 0)

    results.append({
        "weather_city": weather_city,
        "aqi_city": aqi_city,
        "weather_rows": len(weather_city_data),
        "aqi_rows": len(aqi_city_data),
        "aqi_start": aqi_start,
        "aqi_end": aqi_end,
        "expected_days": expected_days,
        "aqi_days": aqi_days,
        "missing_days": missing_days,
        "coverage_percentage": round(coverage, 2)
    })

coverage_df = pd.DataFrame(results)

print(coverage_df.to_string(index=False))

region_mapping = {
    "Guwahati": "East",
    "Kolkata": "East",
    "Howrah": "East",
    "Patna": "East",

    "Delhi": "North",
    "Lucknow": "North",
    "Kanpur": "North",
    "Agra": "North",

    "Bengaluru": "South",
    "Chennai": "South",
    "Hyderabad": "South",
    "Visakhapatnam": "South",

    "Ahmedabad": "West",
    "Mumbai": "West",
    "Nashik": "West",
    "Pune": "West"
}

coverage_df["region"] = coverage_df["aqi_city"].map(region_mapping)

regional_average = (coverage_df.groupby("region")["coverage_percentage"].mean().round(2))

print(regional_average)

print(round(coverage_df["coverage_percentage"].mean(),2),"%")
