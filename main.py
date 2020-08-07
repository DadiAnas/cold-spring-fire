import os
import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
import geopandas as gpd
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# Download data and set working directory
data = et.data.get_data('cold-springs-fire')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

naip_data_path = os.path.join("data", "cold-springs-fire", "naip", "m_3910505_nw_13_1_20150919", "crop", "m_3910505_nw_13_1_20150919_crop.tif")

with rio.open(naip_data_path) as src:
    naip_data = src.read()

# View shape of the data
naip_data.shape

naip_ndvi = es.normalized_diff(naip_data[3], naip_data[0])

ep.plot_bands(naip_ndvi, 
              cmap='PiYG',
              scale=False,
              vmin=-1, vmax=1,
              title="NAIP Derived NDVI\n 19 September 2015 - Cold Springs Fire, Colorado")
plt.show()

