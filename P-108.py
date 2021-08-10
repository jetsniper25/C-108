import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv("P-data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()

