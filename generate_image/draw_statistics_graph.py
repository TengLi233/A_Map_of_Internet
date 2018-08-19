import plotly
import plotly.graph_objs as go


def draw_bar_graph(data_list, time_list, filename):
    trace0 = go.Bar(
        x=time_list,
        y=data_list,
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=1
    )

    data = [trace0]
    layout = go.Layout(
        title=filename,
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename=filename + ".html")
