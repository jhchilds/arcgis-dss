# Usage

This is a demo of the ArcGIS API for JavaScript displaying dummy GPR data for specific locations.

Make sure you have installed [Python 3.7+](https://www.python.org/) on your machine.
(Be sure to add Python to your PATH upon installation) 
Make sure you have [Git Bash](https://git-scm.com/) if you are working in Windows

### Windows
1. Clone or download repository from GitHub.
2. Open Git Bash
3. Navigate to root directory of this repository: ```arcgis-dss/```
4. Install requirements with ```pip install -r requirements.txt```
5. Run ```python app.py```
6. Open web browser and navigate to localhost:8888/arcgis-dss

You should see this:

![Image of ARCGIS-DSS](example.png)

### GeoJSON Database

This application utilizes a geojson database structure in order to organize georeferenced
data. GeoJson is a json-like format for encoding a variety of geographic data structures.

### Porting GeoJSON to ArcGIS Pro

In the [ArcGIS Pro documentation](https://pro.arcgis.com/en/pro-app/tool-reference/conversion/json-to-features.htm),
it clearly explains how to port this type of data into the ArcGIS Pro desktop 
software if that is preferred. The data is converted into a feature class that can be
readily manipulated in ArcGIS applications. 
