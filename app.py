import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
from voila.app import Voila

# Read Data
df = pd.read_csv("merged_heatData.csv")
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.GCPNT_LON, df.GCPNT_LAT))

# Create Kepler.gl Map (with your specific configuration)
map_1 = KeplerGl(height=400, config=config)  # Reuse your 'config' from the original script
map_1.add_data(data=gdf, name='merged_data')

# Voila App
app = Voila(map_1)  # Create the Voila app, passing your Kepler.gl map as content

# Run App (Optional if using 'voila app.py' command later)
if __name__ == '__main__':
    app.run()
