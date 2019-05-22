import pandas as pd

df1 = pd.read_csv('all_data.csv', encoding='utf-8')
df1 = df1[['TownID', 'Longitude', 'Latitude', 'Total']]

A_area = df1.loc[df1['TownID'].str.contains('A')].reset_index(drop=True)
A_area.to_csv('A_area.csv')
F_area = df1.loc[df1['TownID'].str.contains('F')].reset_index(drop=True)
F_area.to_csv('F_area.csv')
G_area = df1.loc[df1['TownID'].str.contains('G')].reset_index(drop=True)
G_area.to_csv('G_area.csv')
H_area = df1.loc[df1['TownID'].str.contains('H')].reset_index(drop=True)
H_area.to_csv('H_area.csv')
C_area = df1.loc[df1['TownID'].str.contains('C')].reset_index(drop=True)
C_area.to_csv('C_area.csv')