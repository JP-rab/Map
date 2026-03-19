# Philippine Population Map

An interactive choropleth map application that displays population data for all Philippine regions.

## How to Run

You can run this application in two ways:

### Method 1: Command Line (Recommended)
From your terminal/command prompt:
```bash
python app.py
```

### Method 2: Python Interpreter
From within a Python interpreter session:
```python
import app
app.create_population_map()
```

Both methods will display the same interactive choropleth map.

## Features

- Interactive map showing all 18 Philippine regions
- Population visualization using bubble sizes and colors
- Detailed hover information showing breakdown by:
  - Population count
  - Provinces
  - Cities
  - Municipalities
  - Barangays
- Focused view on the Philippines with enhanced styling
- Data-driven visualization using real Philippine population data

## Data Source

This application uses comprehensive data from `data.json` containing:
- **112+ million** total population across all regions
- **81 provinces** across all regions
- **120 cities** nationwide
- **1,578 municipalities** 
- **42,046 barangays** total

## Population by Region

The visualization shows population distribution across all Philippine regions:

- **Most Populous**: Region IV-A (CALABARZON) - 16,048,978 people
- **Second Largest**: NCR (National Capital Region) - 13,484,462 people
- **Third Largest**: Region XI (Davao Region) - 11,374,823 people
- **Smallest**: CAR (Cordillera Administrative Region) - 1,797,660 people

## Dependencies

- plotly
- pandas
- json (built-in)

Install dependencies with:
```bash
pip install plotly pandas
```

## Technical Implementation

- **Data Loading**: Dynamic JSON file reading with error handling
- **Visualization**: Plotly scatter_geo for precise regional mapping
- **Coordinates**: Accurate geographic center points for each region
- **Interactivity**: Hover details and color-coded data representation
- **Styling**: Custom map styling focused on Philippine geography

## Customization

To modify the visualization:
1. Edit `data.json` to update administrative unit counts
2. Modify coordinate values in `region_coordinates` for different centering
3. Change color schemes in the `color_continuous_scale` parameter
4. Adjust map focus by modifying the `projection_scale` and `center` values

This application provides a comprehensive view of Philippine administrative structure and can be easily extended for additional regional analysis.
