import plotly.express as px
import pandas as pd
import json

def load_philippine_data():
    """Load Philippine administrative data from data.json"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: data.json file not found!")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json!")
        return None

def get_population_data(region_data):
    """Get population data for a region"""
    return region_data.get('population', 0)


region_coordinates = { #coordinate
    "National Capital Region (NCR)": {"lat": 14.5995, "lon": 120.9842},
    "Cordillera Administrative Region (CAR)": {"lat": 16.4122, "lon": 120.5932},
    "Region I (Ilocos Region)": {"lat": 16.7989, "lon": 120.5889},
    "Region II (Cagayan Valley)": {"lat": 17.6494, "lon": 121.7145},
    "Region III (Central Luzon)": {"lat": 15.2144, "lon": 120.5932},
    "Region IV-A (CALABARZON)": {"lat": 14.2361, "lon": 121.0589},
    "MIMAROPA Region": {"lat": 12.3400, "lon": 121.0000},
    "Region V (Bicol Region)": {"lat": 13.1333, "lon": 123.7333},
    "Region VI (Western Visayas)": {"lat": 10.5929, "lon": 122.6277},
    "Negros Island Region (NIR)": {"lat": 9.4167, "lon": 123.2500},
    "Region VII (Central Visayas)": {"lat": 9.8170, "lon": 123.8860},
    "Region VIII (Eastern Visayas)": {"lat": 11.2400, "lon": 124.9500},
    "Region IX (Zamboanga Peninsula)": {"lat": 7.8333, "lon": 123.3833},
    "Region X (Northern Mindanao)": {"lat": 8.4936, "lon": 124.6408},
    "Region XI (Davao Region)": {"lat": 7.1667, "lon": 125.6000},
    "Region XII (SOCCSKSARGEN)": {"lat": 6.7833, "lon": 124.3833},
    "Region XIII (Caraga)": {"lat": 8.9833, "lon": 125.5333},
    "Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)": {"lat": 6.5000, "lon": 124.1500}
}

def create_population_map():
    """Create and display the Philippine population choropleth map"""
    
    philippine_data = load_philippine_data()
    
    if philippine_data:
        
        processed_data = []
        for region in philippine_data:
            region_name = region['region']
            if region_name in region_coordinates:
                coords = region_coordinates[region_name]
                population = get_population_data(region)
                
                processed_data.append({
                    'region': region_name,
                    'population': population,
                    'provinces': region['provinces'],
                    'cities': region['cities'],
                    'municipalities': region['municipalities'],
                    'barangays': region['barangays'],
                    'lat': coords['lat'],
                    'lon': coords['lon']
                })
        
        
        df = pd.DataFrame(processed_data)
        
        
        fig = px.scatter_geo(
            df,
            lat="lat",
            lon="lon",
            size="population",
            color="population",
            color_continuous_scale="Viridis",
            scope="asia",
            title="Population by Philippine Region",
            labels={"population": "Population", "region": "Region"},
            hover_name="region",
            hover_data={
                "lat": False, 
                "lon": False,
                "provinces": True,
                "cities": True,
                "municipalities": True,
                "barangays": True
            }
        )
        
        
        fig.update_layout( #layout
            geo=dict(
                projection_scale=9,  
                center=dict(lat=12.8797, lon=121.7740),  
                showland=True,
                landcolor="rgb(243, 243, 243)",
                showocean=True,
                oceancolor="rgb(204, 229, 255)",
                showlakes=True,
                lakecolor="rgb(204, 229, 255)"
            ),
            coloraxis_colorbar=dict(
                title="Population"
            )
        )
        
        fig.show()
        return fig
    else:
        print("Failed to load data. Please ensure data.json exists and contains valid JSON.")
        return None


if __name__ == "__main__":
    create_population_map()