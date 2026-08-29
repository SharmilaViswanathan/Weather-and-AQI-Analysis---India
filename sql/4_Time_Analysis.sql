SELECT YEAR(date) AS year,
COUNT(*) AS observation_days,
ROUND(AVG(`Index Value`), 2) AS avg_aqi,
MIN(`Index Value`) AS min_aqi,
MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
GROUP BY YEAR(date)
ORDER BY year;

SELECT MONTH(date) AS month_number,
MONTHNAME(date) AS month_name,
COUNT(*) AS days,
ROUND(AVG(`Index Value`), 2) AS avg_aqi,
MIN(`Index Value`) AS min_aqi,
MAX(`Index Value`) AS max_aqi
FROM finalized_weather_aqi
GROUP BY MONTH(date), MONTHNAME(date)
ORDER BY month_number;

SELECT MONTH(date) AS month_number,
MONTHNAME(date) AS month_name,
`Air Quality`, COUNT(*) AS days
FROM finalized_weather_aqi
GROUP BY MONTH(date), MONTHNAME(date), `Air Quality`
ORDER BY month_number, days DESC;

SELECT city, MONTH(date) AS month_number,
MONTHNAME(date) AS month_name,
ROUND(AVG(`Index Value`), 2) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY city, MONTH(date), MONTHNAME(date)
ORDER BY city, month_number;

WITH monthly_aqi AS
(SELECT city, MONTH(date) AS month_number,
MONTHNAME(date) AS month_name,
AVG(`Index Value`) AS avg_aqi
FROM finalized_weather_aqi
GROUP BY city, MONTH(date), MONTHNAME(date)
),
ranked AS
(SELECT city, month_number, month_name,
ROUND(avg_aqi, 2) AS avg_aqi,
ROW_NUMBER() OVER (PARTITION BY city ORDER BY avg_aqi DESC) AS rn
FROM monthly_aqi
)
SELECT city, month_name, avg_aqi
FROM ranked
WHERE rn = 1
ORDER BY avg_aqi DESC;