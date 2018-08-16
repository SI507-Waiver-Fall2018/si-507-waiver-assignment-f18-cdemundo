# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
import csv

#login to plot.ly required to save offline image files
py.sign_in('cdemundo', 'UEVvPcPrIgVPn6YTRLBF')

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
csv_file_path = "./noun_data.csv"

with open(csv_file_path) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

data = [go.Bar(
            x=[d["Noun"] for d in data],
            y=[d["Number"] for d in data]
    )]

layout = go.Layout(
    title='Analysis of Tweets',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Number of Times Used',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='Tweet Analysis.png')