import pandas as pd

aqi_path = r"C:\Users\ELCOT\Weather Analysis\data\raw\AQI_Info.csv"

aqi = pd.read_csv(aqi_path, low_memory=False)

aqi["date"] = pd.to_datetime(aqi["date"], errors="coerce")

#Duplicate analysis
print("Total AQI rows:", len(aqi))

#Finding City+Date Duplicates
duplicate_rows = aqi[aqi.duplicated(subset=["City", "date"], keep=False)]

print("Rows involved in City + Date duplicates:", len(duplicate_rows))

duplicate_groups = (aqi.groupby(["City", "date"]).size().reset_index(name="row_count"))

duplicate_groups = duplicate_groups[duplicate_groups["row_count"] > 1]

print("Duplicated City + Date combinations:", len(duplicate_groups))

#Displaying Duplicates
if len(duplicate_groups) > 0:
    print(duplicate_groups.sort_values(["City", "date"]).to_string(index=False))
else:
    print("No duplicates found.")

if len(duplicate_rows) > 0:
    print(
        duplicate_rows
        .sort_values(["City", "date"])
        .to_string(index=False)
    )
else:
    print("No duplicate records found.")