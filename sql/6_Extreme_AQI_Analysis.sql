SELECT `Air Quality`, COUNT(*) AS days
FROM finalized_weather_aqi
GROUP BY `Air Quality`
ORDER BY days DESC;

SELECT date, MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
ORDER BY max_aqi DESC;

SELECT city, COUNT(*) AS severe_days
FROM finalized_weather_aqi
WHERE `Air Quality` = 'severe'
GROUP BY city
ORDER BY severe_days DESC;

SELECT city, date, `Index Value` AS aqi, `Air Quality`, `Prominent Pollutant`, 
temperature_2m_mean, precipitation_sum, wind_speed_10m_max
FROM finalized_weather_aqi
ORDER BY `Index Value` DESC
LIMIT 20;

SELECT city, COUNT(*) AS days_above_200
FROM finalized_weather_aqi
WHERE `Index Value` > 200
GROUP BY city
ORDER BY days_above_200 DESC;

SELECT
    YEAR(date) AS year,
    city,
    COUNT(*) AS extreme_aqi_days,
    MAX(`Index Value`) AS highest_aqi
FROM finalized_weather_aqi
WHERE `Index Value` >= 300
GROUP BY
    YEAR(date),
    city
ORDER BY
    extreme_aqi_days DESC,
    highest_aqi DESC;

    
SELECT city, YEAR(date) AS year, COUNT(*) AS days,
MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
GROUP BY city, YEAR(date)
ORDER BY max_aqi DESC;

