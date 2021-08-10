import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
weight=df["Weight(Pounds)"].tolist()

fig=ff.create_distplot([weight], ["weight"],show_hist=True)
fig.show()


