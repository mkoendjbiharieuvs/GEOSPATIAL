import pandas as pd
import geopandas
import matplotlib.pyplot as plt

#Dataframe with cities in SA with lats and longs
df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas','Paramaribo'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela', 'Suriname'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48, 5.83],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86, -55.20]})

#Transform lat and long into list of objects and set it as a geometry while creating the GeoDataFrame
gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

print(gdf.head())

#Plot the coordinates over a country-level map
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# We restrict to South America.
ax = world[world.continent == 'South America'].plot(color='white', edgecolor='grey')

# We can now plot our GeoDataFrame
#gdf.plot(ax=ax, color='red')
gdf.plot(ax=ax)

plt.show()
