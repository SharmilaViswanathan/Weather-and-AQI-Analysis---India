SELECT ROUND(temperature_2m_mean, 0) AS temperature,
COUNT(*) AS days, ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY ROUND(temperature_2m_mean, 0)
ORDER BY temperature;

SELECT CASE WHEN precipitation_sum = 0 THEN 'No Rain'
			WHEN precipitation_sum > 0 AND precipitation_sum <= 5 THEN 'Light Rain'
			WHEN precipitation_sum > 5 AND precipitation_sum <= 20 THEN 'Moderate Rain'
			ELSE 'Heavy Rain'
END AS rainfall_category,
COUNT(*) AS days,
ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY CASE WHEN precipitation_sum = 0 THEN 'No Rain'
			WHEN precipitation_sum > 0 AND precipitation_sum <= 5 THEN 'Light Rain'
			WHEN precipitation_sum > 5 AND precipitation_sum <= 20 THEN 'Moderate Rain'
			ELSE 'Heavy Rain'
            END
ORDER BY avg_aqi DESC;

SELECT CASE WHEN wind_speed_10m_max < 10 THEN 'Low Wind'
        WHEN wind_speed_10m_max < 20 THEN 'Moderate Wind'
        WHEN wind_speed_10m_max < 30 THEN 'High Wind'
        ELSE 'Very High Wind'
		END AS wind_category,
COUNT(*) AS days,
ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY CASE WHEN wind_speed_10m_max < 10 THEN 'Low Wind'
			WHEN wind_speed_10m_max < 20 THEN 'Moderate Wind'
			WHEN wind_speed_10m_max < 30 THEN 'High Wind'
			ELSE 'Very High Wind'
            END
ORDER BY avg_aqi DESC;

SELECT `Prominent Pollutant`, COUNT(*) AS days,
ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM finalized_weather_aqi), 2) AS percentage
FROM finalized_weather_aqi
GROUP BY `Prominent Pollutant`
ORDER BY days DESC;

SELECT city, `Prominent Pollutant`, COUNT(*) AS days
FROM finalized_weather_aqi
GROUP BY city, `Prominent Pollutant`
ORDER BY city, days DESC;
    
SELECT `Prominent Pollutant`, COUNT(*) AS days, ROUND(AVG(`Index Value`), 2) AS avg_aqi,
MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
GROUP BY `Prominent Pollutant`
ORDER BY avg_aqi DESC;

SELECT ROUND(shortwave_radiation_sum, 0) AS temperature,
COUNT(*) AS days, ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY ROUND (shortwave_radiation_sum, 0)
ORDER BY temperature;