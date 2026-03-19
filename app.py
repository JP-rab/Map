import plotly.express as px
import pandas as pd
import json
import os
import glob

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

def load_geojson_data():
    """Load and combine all regional GeoJSON files"""
    try:
        
        geojson_files = glob.glob('ph_regions/*.json')
        
        combined_features = []
        
        for file_path in geojson_files:
            with open(file_path, 'r') as f:
                geojson_data = json.load(f)
                
            
            if 'features' in geojson_data:
                for feature in geojson_data['features']:
                   
                    if 'properties' in feature and 'name' in feature['properties']:
                        region_name = feature['properties']['name']
                        
                        # mapping
                        name_mapping = {
                            "National Capital Region": "National Capital Region (NCR)",
                            "Cordillera Administrative Region": "Cordillera Administrative Region (CAR)",
                            "Ilocos": "Region I (Ilocos Region)",
                            "Cagayan Valley": "Region II (Cagayan Valley)",
                            "Central Luzon": "Region III (Central Luzon)",
                            "CALABARZON": "Region IV-A (CALABARZON)",
                            "Calabarzon": "Region IV-A (CALABARZON)",
                            "MIMAROPA": "MIMAROPA Region",
                            "Mimaropa": "MIMAROPA Region",
                            "Bicol": "Region V (Bicol Region)",
                            "Western Visayas": "Region VI (Western Visayas)",
                            "Negros Island Region": "Negros Island Region (NIR)",
                            "Central Visayas": "Region VII (Central Visayas)",
                            "Eastern Visayas": "Region VIII (Eastern Visayas)",
                            "Zamboanga Peninsula": "Region IX (Zamboanga Peninsula)",
                            "Northern Mindanao": "Region X (Northern Mindanao)",
                            "Davao": "Region XI (Davao Region)",
                            "SOCCSKSARGEN": "Region XII (SOCCSKSARGEN)",
                            "Soccsksargen": "Region XII (SOCCSKSARGEN)",
                            "Caraga": "Region XIII (Caraga)",
                            "Autonomous Region in Muslim Mindanao": "Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)"
                        }
                        
                        
                        mapped_name = name_mapping.get(region_name, region_name)
                        feature['properties']['region_name'] = mapped_name
                        combined_features.append(feature)
        
        
        combined_geojson = {
            "type": "FeatureCollection",
            "features": combined_features
        }
        
        return combined_geojson
        
    except Exception as e:
        print(f"Error loading GeoJSON files: {e}")
        return None

def create_choropleth_map():
    """Create and display the Philippine population choropleth map"""
    
    
    philippine_data = load_philippine_data()
    if not philippine_data:
        print("Failed to load population data. Please ensure data.json exists and contains valid JSON.")
        return None
    
    
    geojson_data = load_geojson_data()
    if not geojson_data:
        print("Failed to load GeoJSON data. Please ensure ph_regions directory contains valid GeoJSON files.")
        return None
        
   
    population_df = pd.DataFrame(philippine_data)
    
    
    fig = px.choropleth(
        population_df,
        geojson=geojson_data,
        locations='region',  
        featureidkey="properties.region_name",  
        color='population',
        color_continuous_scale=["yellow", "darkgreen"],
        scope="asia",
        title="Population by Philippine Region",
        labels={"population": "Population", "region": "Region"},
        hover_data={
            "provinces": True,
            "cities": True,
            "municipalities": True,
            "barangays": True
        }
    )
    
    # map layout
    fig.update_layout(
        geo=dict(
            projection_scale=9,
            center=dict(lat=12.8797, lon=121.7740), # centerpoint
            showland=True,
            landcolor="rgb(243, 243, 243)",
            showocean=True,
            oceancolor="rgb(204, 229, 255)",
            showlakes=True,
            lakecolor="rgb(204, 229, 255)",
            showcountries=True,
            countrycolor="rgb(204, 204, 204)"
        ),
        coloraxis_colorbar=dict(
            title="Population",
            thicknessmode="pixels",
            thickness=20,
            lenmode="pixels",
            len=300
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )
    
    
    fig.update_traces(
        hovertemplate=(
            "<b>%{location}</b><br>" +
            "Population: %{z:,}<br>" +
            "Provinces: %{customdata[0]}<br>" +
            "Cities: %{customdata[1]}<br>" +
            "Municipalities: %{customdata[2]}<br>" +
            "Barangays: %{customdata[3]}"
        )
    )
    
    fig.show()
    return fig

if __name__ == "__main__":
    create_choropleth_map()