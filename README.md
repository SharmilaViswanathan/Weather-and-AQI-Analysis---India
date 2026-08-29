# Weather & AQI Analysis - India

This project follows an end to end Data Analytics workflow using Python, MySQL, Power BI
This project analyzes the relationship between weather condition and air quality across 16 Major Indian cities from 2015 to 2023

## Power BI Dashboard

### Executive Overview
![Executive Overview](screenshots/Page%201%20Overview.jpg)

### City Level AQI Analysis
![City Level AQI Analysis](screenshots/Page%202%20City%20Level%20Analysis.jpg)

### AQI Trends and Seasonality Patterns
![AQI Trends and Seasonality Patterns](screenshots/Page%203%20AQI%20Trends.jpg)

### Weather and AQI Analysis
![Weather and AQI Analysis](screenshots/Page%204%20Weather%20&%20AQI%20Analysis.jpg)

### Extreme AQI Events
![Extreme AQI Events](screenshots/Page%205%20Extreme%20AQI%20Events.jpg)

## Business Problem

Air quality varies significantly across Indian cities and over time. Weather conditions such as temperature, Wind speed, Rainfall, Sunlight can influence atmospheric pollution

This project analyzes Daily weather information with Air Quality Index (AQI) to answer questions such as:
- Cities with highest AQI levels
- cities experiencing the most severe air quality conditions
- Yearly and seasonal AQI trends
- Relationships between weather and AQI conditions
- Worst indidvidual days
- Extreme pollution events
- Difference in air quality between Indian cities

## Objectives of the project

- Clean and standardize raw weather and AQI datasets using Python
- Combine weather and AAQI datasets using City+Date as a common key
- Perform exploratory and analytics queries using MySQL
- Build an interactive Power BI dashboard to communicate major findings using charts, KPI cards, navigation and filters

## Dataset

- The final dataset covers
- Cities - 16
- Time period - 2015 to 2023
- Final records - 43,691
- Weather records - 52,592
- AQI records - 43,691
- Final columns - 25

Cities
- Agra
- Ahmedabad
- Bengaluru
- Chennai
- Delhi
- Guwahati
- Howrah
- Hyderabad
- Kanpur
- Kolkata
- Lucknow
- Mumbai
- Nashik
- Patna
- Pune
- Visakhapatnam

## Tools and Technologies

### Python
Data cleaning and preparation

### Pandas
Data manipulation

### MySQL
Data storage and analytical queries

### Power BI
Interactive dashboard

### Dax
Measure and  calculated analysis

### Git/Github
Project version control and documentation

## Data pipeline

Raw csv  files
        |
Python data cleaning
        |
Cleaned weather and AQI datasets
        |
Weather and AQI merge
        |
Finalized Dataset
        |
MySQL
        |
Query Analysis
        |
Power BI
        |
Interactive dashboard

## Data cleaning and preparation using Python

Python was used to prepare and clean raw data before analysis

The process includes:
- Reading raw CSV files
- Converting date columns
- Handling invald dates
- Normalizing city names
- Standardizing city name differences
- Filtering the 16 city names
- Filtering the required date range
- Removing duplicate city and date records
- Converting AQI values to  numeric format
- Handling missing AQI informations
- Merging weather and AQI datasets

## MySQL analysis

The cleaned and finalized dataset was imported to MySQL for analytical querying

The SQL analysis includes:
- Overall record validation
- Null value check
- Date range validation
- City level record counts
- AQI statistics
- AQI category distribution
- Cities with high AQI
- Yearly AQI trends
- Montly AQI patterns
- Worst individual AQI days
- Cities with most severe AQI days
- Extreme AQI events
- Weather condition vs AQI analysis

## Power BI dashboard

The final Power BI report provides an interactive view of weather and air quality patterns

Users can explore the data by:
- City
- Year
- Month
- AQI category
- Weather conditions

The dashboard uses:
- KPI cards
- Bar charts
- Line charts
- Donut chart
- Tables
- matrix
- Slicers
- Navigation buttons
- Filters

### Dashboard Pages

Page 1 - Overview

Provides a high level summary of the dataset

key information includes:
- Highest recorded AQI 
- Lowest recored AQI
- Average AQI
- Average AQI across cities
- Air quality category by date
- Total Records and cities
- Severe AQI days

Page 2 - City AQI analysis

Focuses on differences in air quality between cities 

Analysis includes:
- Poor or worse days by city
- City summary table
- Count of days by city and Air Quality

Page 3 - Time & seasonal analysis

Examines how air quality changes over time

Analysis include:
- Yearly Average AQI
- Monthly Average AQI
- Average AQI by month and city

Page 4 - Weather and air quality analysis

Explores the relationships between weather conditions and air quality

Analysis includes:
- Temperature vs AQI
- Wind vs AQI
- Wind category vs AQI
- Rain vs AQI

Page 5 - Extreme AQI events

Focuses on most significant pollution changes

Analysis includes:
- AQI by pollutant
- Pollutant frequency
- Worst 10 AQI days

## Key Insights

- Delhi recorded the highest average AQI among the 16 cities, with an average AQI of 217, highest number of poor or worse air quality days with 1,648 days
- Bengaluru recorded comparatively better air quality. Bengaluru had an average AQI of 95 and only 15 Poor or worse days
- AQI levels were highest during the winter months, especially in January and decreased in the monsoon period. The lowest average AQI values were observed around July and August.
- The yearly analysis showed a decline in average AQI over the study period. Average AQI decreased from approximately 154 in 2016 to approximately 117 in 2023.
- Weather conditions can coincide with significant changes in AQI, particularly through wind and seasonal changes.
- Wind conditions showed an inverse relationship with average AQI
- PM2.5 was associated with the highest average AQI
- Extreme AQI events were concentrated in a smaller group of cities such as Delhi, Patna, Kanpur, Agra
## Project Structure

Weather_and_AQI_analysis_of_Indian_cities/
│
├── data/
├── logs/
├── powerbi/
├── screenshots/
├── scripts/
├── sql/
├── .gitignore
├── README.md
└── requirements.txt

## How to run

- Replace the paths in the Python scripts with your computer's path and place the raw datasets in data/raw/ and run the Python scripts to generate the processed datasets

### 1. Clone the repository

### 2. Install dependencies
pip install -r requirements.txt

### 3. Prepare the raw data
- Place the original datasets inside data/raw/

### 4. Run the Python scripts
- The python scripts cleans and standardizes the weather and AQI datasets
The output is
- Cleaned_AQI_Info.csv
- Cleaned_Weather_Info.csv
- Finalized_data.csv

### 5. Import the finalized dataset to MySQL
- Create MySQL database and import Finalized_data.csv
- Into finalized_weather_aqi

### 6. Run SQL analysis
- Execute the SQL analysis script to get the analytical results

### 7. Open Power BI
- Connect Power BI to the finalized analytical data and load the required field/measures
- Use the slicers and navigation buttons to explore the different analytical pages

## Data Availability

- The original datasets contain approximately 43,691 city-day AQI records and 52,592 weather records across 16 Indian cities from 2015 to 2023
- Due to repository size considerations, the full datasets are not included in this repository
- Small sample datasets are provided in the `data/` directory to demonstrate the structure and columns used in the analysis
- The complete data processing pipeline is included in the Python scripts, SQL analysis and Power BI dashboard

## Important Notes

- The weather dataset contains more records than the finalized dataset because the weather dataset contains records where AQI doesn't have the same records
- Final merged dataset contains 43,691 records because the analysis uses dates where weather and AQI information are available
- So, the final dataset covers 01-05-2015 to 31-12-2023

## Future Improvements

- Adding geographical maps
- Adding more Indian cities
- incoporating real time AQI data
- Adding pollutant specific analysis
- Building AQI forecasting models
- Applying Machine Learning techniques to predict AQI
- Adding population and traffic related variables
- Deploying the Power BI report online

## Author

Sharmila V

B.Tech. Artificial Intelligence & Data Science Graduate

Interested in Data Analytics, Business Analytics, SQL, Python and Business Intelligence

Skills Demonstrated in this project:
- Python
- Pandas
- MySQL
- Power BI
- Dax
- Data Visualization

LinkedIn: https://www.linkedin.com/in/sharmilaviswanathan/
GitHub: https://github.com/SharmilaViswanathan
