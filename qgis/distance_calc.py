# QGIS Python Console script
# Calculates total geodesic distance of the active route layer

layer = iface.activeLayer()

# get the first (and only) feature
feature = next(layer.getFeatures())
geom = feature.geometry()

# geodesic distance calculator
d = QgsDistanceArea()
d.setEllipsoid("WGS84")
d.setSourceCrs(layer.crs(), QgsProject.instance().transformContext())

distance_m = d.measureLength(geom)
distance_km = distance_m / 1000

print(f"Total route distance: {distance_km:.3f} km")