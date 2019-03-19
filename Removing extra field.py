# Removing the extra fields in the Eagle Owl point data
import os
from qgis.core import *
import qgis.utils

# Path to shapefile
Sample_pointe = r'E:\\Thangamani appa\\first sem\\python\\final project\\movebank\\movebank\\goose\\points.shp'

# load the shapefile
layer = iface.addVectorLayer(Sample_pointe, "shape:", "ogr")
if not layer:
    print("sample points failed to load!")

# Check for editing rights (capabilities)
caps = layer.dataProvider().capabilities()
print(caps)
caps_string = layer.dataProvider().capabilitiesString()
print(caps_string)

# Adding a field (attribute)
if caps & QgsVectorDataProvider.DeleteAttributes:
    # Deleting the items, each with
    # The name and the data type of the field
    layer.dataProvider().deleteAttributes([3,4,5,6,7,8,9,11,12,16,17,18,19,26,27])

# Update to propagate the changes
layer.updateFields()