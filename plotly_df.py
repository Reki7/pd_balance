from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
from plotly import graph_objs as go
init_notebook_mode(connected = True)

def plotly_df(df, title = ''):
    data = []

    for column in df.columns:
        trace = go.Scatter(
            x = df.index,
            y = df[column],
            mode = 'lines',
            name = column
        )
        data.append(trace)

    layout = dict(title = title)
    fig = dict(data = data, layout = layout)
    iplot(fig, show_link=False)


def decomposition_data(decomposition, df, field):
    data = [
        go.Scatter(
            x=df.index, y=decomposition.trend[field],
            name='Trend', mode='lines'
        ),
        go.Scatter(
            x=df.index, y=decomposition.seasonal[field],
            name='Seasonal', mode='lines'
        ),
        go.Scatter(
            x=df.index, y=decomposition.resid[field],
            name='Residual', mode='lines'
        ),
        go.Scatter(
            x=df.index, y=df[field],
            name='Observed', mode='lines'
        )
    ]
    return data
