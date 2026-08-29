import pandas as pd


# ============================================================
# FILE PATHS
# ============================================================

# Original raw data
weather_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info.csv"
aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

# Cleaned data
cleaned_weather_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_Weather_Info.csv"
cleaned_aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_AQI_Info.csv"

# Final merged dataset
final_dataset_path = r"C:\Users\ELCOT\Weather Analysis\data\processed\finalized_data.csv"


# ============================================================
# CREATE SAMPLE DATA
# ============================================================

print("=" * 70)
print("CREATING SAMPLE DATASETS")
print("=" * 70)


# ------------------------------------------------------------
# RAW WEATHER SAMPLE
# ------------------------------------------------------------

weather = pd.read_csv(
    weather_path,
    low_memory=False
)

weather_sample = weather.sample(
    n=min(500, len(weather)),
    random_state=42
)

weather_sample.to_csv(
    r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info_sample.csv",
    index=False
)

print("Raw Weather sample created:")
print(weather_sample.shape)


# ------------------------------------------------------------
# RAW AQI SAMPLE
# ------------------------------------------------------------

aqi = pd.read_csv(
    aqi_path,
    low_memory=False
)

aqi_sample = aqi.sample(
    n=min(500, len(aqi)),
    random_state=42
)

aqi_sample.to_csv(
    r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info_sample.csv",
    index=False
)

print("Raw AQI sample created:")
print(aqi_sample.shape)


# ------------------------------------------------------------
# CLEANED WEATHER SAMPLE
# ------------------------------------------------------------

cleaned_weather = pd.read_csv(
    cleaned_weather_path,
    low_memory=False
)

cleaned_weather_sample = cleaned_weather.sample(
    n=min(500, len(cleaned_weather)),
    random_state=42
)

cleaned_weather_sample.to_csv(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_Weather_Info_sample.csv",
    index=False
)

print("Cleaned Weather sample created:")
print(cleaned_weather_sample.shape)


# ------------------------------------------------------------
# CLEANED AQI SAMPLE
# ------------------------------------------------------------

cleaned_aqi = pd.read_csv(
    cleaned_aqi_path,
    low_memory=False
)

cleaned_aqi_sample = cleaned_aqi.sample(
    n=min(500, len(cleaned_aqi)),
    random_state=42
)

cleaned_aqi_sample.to_csv(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_AQI_Info_sample.csv",
    index=False
)

print("Cleaned AQI sample created:")
print(cleaned_aqi_sample.shape)


# ------------------------------------------------------------
# FINAL DATASET SAMPLE
# ------------------------------------------------------------

final_data = pd.read_csv(
    final_dataset_path,
    low_memory=False
)

final_data_sample = final_data.sample(
    n=min(500, len(final_data)),
    random_state=42
)

final_data_sample.to_csv(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\finalized_data_sample.csv",
    index=False
)

print("Final dataset sample created:")
print(final_data_sample.shape)


# ============================================================
# COMPLETED
# ============================================================

print("\n" + "=" * 70)
print("SAMPLE DATA CREATION COMPLETED")
print("=" * 70)

print("\nFiles created:")

print(
    r"C:\Users\ELCOT\Weather Analysis\data\raw\Weather_Info_sample.csv"
)

print(
    r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info_sample.csv"
)

print(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_Weather_Info_sample.csv"
)

print(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\Cleaned_AQI_Info_sample.csv"
)

print(
    r"C:\Users\ELCOT\Weather Analysis\data\processed\finalized_data_sample.csv"
)