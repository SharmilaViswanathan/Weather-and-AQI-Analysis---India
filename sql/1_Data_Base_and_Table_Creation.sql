CREATE DATABASE weather_aqi_analysis;
USE weather_aqi_analysis;

SELECT DATABASE();

CREATE TABLE finalized_weather_aqi (
date DATE,
weather_code INT,
temperature_2m_max DECIMAL(6,2),
temperature_2m_min DECIMAL(6,2),
temperature_2m_mean DECIMAL(6,2),
apparent_temperature_max DECIMAL(6,2),
apparent_temperature_min DECIMAL(6,2),
apparent_temperature_mean DECIMAL(6,2),
sunrise DATETIME,
sunset DATETIME,
daylight_duration DECIMAL(10,2),
sunshine_duration DECIMAL(10,2),
precipitation_sum DECIMAL(10,2),
rain_sum DECIMAL(10,2),
snowfall_sum DECIMAL(10,2),
precipitation_hours DECIMAL(10,2),
wind_speed_10m_max DECIMAL(10,2),
wind_gusts_10m_max DECIMAL(10,2),
wind_direction_10m_dominant DECIMAL(10,2),
shortwave_radiation_sum DECIMAL(10,2),
et0_fao_evapotranspiration DECIMAL(10,2),
city VARCHAR(50),
`Index Value` INT,
`Air Quality` VARCHAR(30),
`Prominent Pollutant` VARCHAR(30)
);

SHOW TABLES;