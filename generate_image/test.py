import plotly
import plotly.graph_objs as go

color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
print color

data = [
    go.Scatter(
        y=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        marker=dict(
            symbol = 'square',
            sizemin=5,
            size=color,
            cmax=0,
            color=map(lambda x : x * -1, color),
            colorbar=dict(
                title='Colorbar'
            ),
            colorscale='RdBu',
            line=dict(width=2)
        ),
        mode='markers'),
    go.Scatter(
        y=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        marker=dict(
            symbol = 'square',
            sizemin=5,
            size=color,
            cmax=0,
            color=map(lambda x : x * -1, color),
            colorscale='RdBu',
        ),
        mode='lines')
]

fig = go.Figure(data=data)
plotly.offline.plot(fig, filename='basic-heatmap.html', auto_open=True)
