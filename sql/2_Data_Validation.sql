DESCRIBE finalized_weather_aqi;

SELECT COUNT(*) AS total_rows
FROM finalized_weather_aqi;

SELECT city, date, COUNT(*) AS record_count
FROM finalized_weather_aqi
GROUP BY city, date
HAVING COUNT(*) > 1;

SELECT DISTINCT city
FROM finalized_weather_aqi
ORDER BY city;

SELECT MIN(date) AS start_date,
MAX(date) AS end_date
FROM finalized_weather_aqi;

SELECT COUNT(*) AS total_rows,
SUM(date IS NULL) AS missing_dates,
SUM(city IS NULL) AS missing_cities,
SUM(`Index Value` IS NULL) AS missing_aqi,
SUM(`Air Quality` IS NULL) AS missing_air_quality,
SUM(`Prominent Pollutant` IS NULL) AS missing_pollutant
FROM finalized_weather_aqi;

