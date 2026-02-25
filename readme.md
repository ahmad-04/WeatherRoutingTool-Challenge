# Weather Routing Tool – Code Challenge

## 1. Overview

This project demonstrates the use of the **52°North Weather Routing Tool (WRT)** to generate an optimal maritime route based on real weather and oceanographic data.  
The final route is visualized and analyzed in **QGIS**, where the total route distance is calculated.

## 2. Environment

- **Operating System:** Windows
- **Python Version:** 3.12.10
- **Weather Routing Tool:** 52°North WRT (main branch)
- **Routing Algorithm:** Isochrone-based routing
- **Ship Model:** Direct Power Method
- **GIS Software:** QGIS (EPSG:4326 – WGS 84)

## 3. Weather Data Preparation

Weather and ocean data were downloaded automatically using WRT’s built-in data download mechanism.

**Data sources:**

- NOAA GFS – atmospheric data
- Copernicus Marine Service – waves and currents

**Geographic region:** Mediterranean Sea (limited bounding box)  
**Time range:** 24–28 February 2026

Generated files:

- `data/weather_data_region1.nc`
- `data/depth_data_region1.nc`

## 4. Configuration

The routing configuration is defined in:
config/config.json

**Key parameters:**

- Source: `(38.192, 13.392)`
- Destination: `(41.349, 2.188)`
- Boat type: `direct_power_method`
- Constraints:
  - No land crossing
  - Minimum water depth = 30 m
  - Stay within weather map
- Routing steps: 60 (terminated early when destination reached)

## 5. Routing Result

The Weather Routing Tool successfully computed a route and terminated automatically at routing step **13** when the destination was reached.

**Final route file:**
data/min_time_route.json

The file is a valid **GeoJSON FeatureCollection** containing ordered waypoint points with associated properties such as:

- timestamp
- vessel speed
- engine power
- fuel consumption

## 6. QGIS Visualization

The GeoJSON route points were loaded directly into QGIS using CRS **EPSG:4326**.

**Basemap:**

- OpenStreetMap (XYZ Tiles)

To enable distance measurement, the waypoint points were converted into a route line using the **Points to Path** tool (ordered by the `time` attribute).

Generated QGIS files:

qgis/min_time_route_line.geojson
qgis/min_time_route.qgz

Screenshot:

- `screenshots/route_map.png`

## 7. Distance Calculation

The total route distance was calculated using the **QGIS Python Console** with geodesic distance on the WGS84 ellipsoid.

**Script used:**

qgis/distance_calc.py

The script measures the length of the route LineString and prints the distance in kilometers.

Screenshot of result:

- `screenshots/distance_result.png`

## 8. Final Output

- Final route (GeoJSON points): `data/min_time_route.json`
- Route line (GeoJSON): `qgis/min_time_route_line.geojson`
- Total route distance: 1059.386 km

All steps are fully reproducible using the provided configuration, data files, and scripts.

## 9. Notes

- The routing terminated early due to all route segments reaching the destination.
- Automatic weather and depth data download was used as recommended.
- QGIS was chosen for visualization and distance.
