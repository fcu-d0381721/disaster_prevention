import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd
import numpy as np
from scipy import signal

df = pd.read_csv('./output/201801.csv')
A_area = df.loc[df['TownID'].str.contains('A')].reset_index(drop=True)
# A:台北 H:桃園 F:新北 C:基隆 G:宜蘭
A_area = A_area[['Time', 'TownID', 'Longitude', 'Latitude', 'Total']]
print(A_area)


print(A_area.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].std())
lats = sorted(A_area['Latitude'].unique().tolist())
lngs = sorted(A_area['Longitude'].unique().tolist())
z = []
for i in lats:
    z_inside = []
    for j in lngs:
        con1 = A_area['Latitude'] == i
        con2 = A_area['Longitude'] == j
        if A_area[con1 & con2].empty:
            # print('empty')
            z_inside.append(0)
        else:
            # print(A_area[con1 & con2]['Total'].mean())
            z_inside.append(A_area[con1 & con2]['Total'].mean())
            # z_inside.append(A_area[con1 & con2]['Total'].std())
    z.append(z_inside)

nn = np.array(z)
print(nn)
w_k = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1], ],
               dtype='float')
f = signal.convolve2d(nn, w_k, 'valid')
print(f.shape[0])
n = f.tolist()
print(f.tolist())

data = [
    go.Heatmap(
        z=n,
        x=[i for i in range(43)],
        y=[i for i in range(33)],
        colorscale='Viridis',
    )
]



# layout = go.Layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=go.layout.Mapbox(
#         accesstoken='pk.eyJ1Ijoid2VpaGFuMDUyNSIsImEiOiJjanVtNDN6bHkwN3NiNDRwZ2VmbXF3a291In0.ToEAI9lcYJqON1FXCUBNmw',
#         bearing=0,
#         center=go.layout.mapbox.Center(
#             lat=23.732253,
#             lon=121.942442
#         ),
#         pitch=0,
#         zoom=10
#     ),
# )

# fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(data, filename='Mapbox.html')