import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

surmap=gpd.read_file('SUR_adm1.shp')
surmap.plot()

plt.show()
print(surmap.head(20))

df=pd.read_csv('SUR_adm1.csv',header=0)
print(df.head())
merged=surmap.set_index('NAME_1').join(df('NAME_1'))
print(merged.head(20))

