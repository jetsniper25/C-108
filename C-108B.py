import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
height=df["Height(Inches)"].tolist()
print(height)

print(df)

fig=ff.create_distplot([height], ["height"],show_hist=False)
fig.show()

