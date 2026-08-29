SELECT city,
COUNT(*) AS observation_days,
ROUND(AVG(`Index Value`), 2) AS avg_aqi,
MIN(`Index Value`) AS min_aqi,
MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
GROUP BY city
ORDER BY avg_aqi DESC;

SELECT city, ROUND(AVG(`Index Value`), 2) AS avg_aqi,
RANK() OVER (ORDER BY AVG(`Index Value`) DESC) AS aqi_rank
FROM finalized_weather_aqi
GROUP BY city
ORDER BY avg_aqi DESC;

SELECT city, ROUND(AVG(`Index Value`), 2) AS avg_aqi,
FROM finalized_weather_aqi
GROUP BY city
ORDER BY avg_aqi ASC;

SELECT city, ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY city
HAVING AVG(`Index Value`) >
       (SELECT AVG(`Index Value`)
           FROM finalized_weather_aqi)
ORDER BY avg_aqi DESC;

SELECT city, date, `Index Value`, `Air Quality`, `Prominent Pollutant`
FROM finalized_weather_aqi
ORDER BY `Index Value` DESC
LIMIT 10;

SELECT city, `Air Quality`, COUNT(*) AS days
FROM finalized_weather_aqi
GROUP BY city, `Air Quality`
ORDER BY city, days DESC;

SELECT city, COUNT(*) AS total_days,
SUM(CASE WHEN `Index Value` >= 200 THEN 1 ELSE 0 END) AS high_aqi_days,
ROUND(100.0 * SUM(CASE WHEN `Index Value` >= 200 THEN 1 ELSE 0 END) / COUNT(*), 2) AS high_aqi_percentage
FROM finalized_weather_aqi
GROUP BY city
ORDER BY high_aqi_percentage DESC;

SELECT city, YEAR(date) AS year,
ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY city, YEAR(date)
ORDER BY city, year;

WITH yearly_aqi AS
(SELECT city, YEAR(date) AS year, AVG(`Index Value`) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY city, YEAR(date)
), 
ranked_years AS 
(SELECT city, year, ROUND(avg_aqi, 2) AS avg_aqi,
RANK() OVER (PARTITION BY city ORDER BY avg_aqi DESC) AS year_rank
FROM yearly_aqi
)
SELECT city, year, avg_aqi
FROM ranked_years
WHERE year_rank = 1
ORDER BY avg_aqi DESC;

SELECT city, COUNT(*) AS total_days,
SUM(CASE WHEN LOWER(`Air Quality`) 
IN ('poor', 'very poor', 'severe') THEN 1 ELSE 0 END) AS poor_or_worse_days,
ROUND(100.0 * SUM(CASE WHEN LOWER(`Air Quality`) IN
('poor', 'very poor', 'severe')THEN 1 ELSE 0 END) / COUNT(*),2) AS poor_or_worse_percentage
FROM finalized_weather_aqi
GROUP BY city
ORDER BY poor_or_worse_percentage DESC;
