import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


df1 = pd.read_csv("A_area.csv", encoding='utf-8')
df1 = df1[['Total', 'Longitude', 'Latitude', 'TownID']]
df1 = df1.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].sum()
df1 = df1.values.tolist()
df2 = pd.read_csv("H_area.csv", encoding='utf-8')
df2 = df2[['Total', 'Longitude', 'Latitude', 'TownID']]
df2 = df2.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].sum()
df2 = df2.values.tolist()
df3 = pd.read_csv("G_area.csv", encoding='utf-8')
df3 = df3[['Total', 'Longitude', 'Latitude', 'TownID']]
df3 = df3.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].sum()
df3 = df3.values.tolist()
df4 = pd.read_csv("F_area.csv", encoding='utf-8')
df4 = df4[['Total', 'Longitude', 'Latitude', 'TownID']]
df4 = df4.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].sum()
df4 = df4.values.tolist()
df5 = pd.read_csv("C_area.csv", encoding='utf-8')
df5 = df5[['Total', 'Longitude', 'Latitude', 'TownID']]
df5 = df5.groupby(['TownID', 'Latitude', 'Longitude'])['Total'].sum()
df5 = df5.values.tolist()



trace1 = go.Box(
    y=df1,
    name="台北市",
    boxpoints='outliers',
    marker=dict(
        color='rgba(93, 164, 214, 0.5)',
    ),
    line=dict(
        width=1,
        color='rgba(93, 164, 214, 0.5)',
    ),
)
trace2 = go.Box(
    y=df2,
    name="桃園市",
    boxpoints='outliers',
    marker=dict(
        color='rgba(255, 144, 14, 0.5)',
    ),
    line=dict(
        width=1,
        color='rgba(255, 144, 14, 0.5)',
    ),
)
trace3 = go.Box(
    y=df3,
    name="宜蘭市",
    boxpoints='outliers',
    marker=dict(
        color='rgba(44, 160, 101, 0.5)',
    ),
    line=dict(
        width=1,
        color='rgba(44, 160, 101, 0.5)',
    ),
)
trace4 = go.Box(
    y=df4,
    name="新北市",
    boxpoints='outliers',
    marker=dict(
        color='rgba(255, 65, 54, 0.5)',
    ),
    line=dict(
        width=1,
        color='rgba(255, 65, 54, 0.5)',
    ),
)
trace5 = go.Box(
    y=df5,
    name="基隆市",
    boxpoints='outliers',
    marker=dict(
        color='rgba(207, 114, 255, 0.5)'),
    line=dict(
        width=1,
        color='rgba(207, 114, 255, 0.5)'),
)

plotly.offline.plot([trace1,trace2,trace3,trace4,trace5], filename='Mapbox.html')