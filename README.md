# Philippine Population Map

An interactive choropleth map application that displays population data for all Philippine regions.

## How to Run


### Command Line 
From your terminal/command prompt:
```bash
python app.py
```

Both methods will display the same interactive choropleth map.

## Features

- Interactive choropleth map showing all 18 Philippine regions
- Population visualization using color shading 
- simple hover information showing breakdown by:
  - Population count
  - Provinces
  - Cities
  - Municipalities
  - Barangays
- Focused view on the Philippines
- Data visualization using inaccurate Philippine population data
- Geographic boundaries from GeoJSON files for regional representation

## Data Source

This application uses comprehensive data from philippine standard geographic code (psgc) `data.json` containing:
- **112+ million** total population across all regions
- **81 provinces** across all regions
- **120 cities** nationwide
- **1,578 municipalities** 
- **42,046 barangays** total

- **region coordinates** from a simple map "https://simplemaps.com/gis/country/ph#admin1" 


## Dependencies

- plotly
- pandas
- json 
- glob 


