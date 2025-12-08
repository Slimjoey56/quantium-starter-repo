from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by=['date'])

# 1. Create the base line chart
fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales')

# 2. Add the vertical line for the price increase
# This draws a red dashed line at Jan 15, 2021
fig.add_vline(x="2021-01-15", line_width=3, line_dash="dash", line_color="red")  ### <--- ADD THIS LINE

app.layout = html.Div(children=[
    html.H1(children='Soul Foods: Pink Morsel Sales Visualizer'),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig,
    )
])

if __name__ == '__main__':
    app.run(debug=True)