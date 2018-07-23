import  plotly.graph_objs as go
import data_collection_package.data_collector as dc
import datetime
import calendar



def timestamp(year, mounth, day, hour, min):
    dt = datetime(year, mounth, day, hour, min)
    return int(calendar.timegm(dt.timetuple()))


def draw_map(as_graph):
    node_trace = go.scatter()
    edge_trace = go.scatter()


def main():
    start = timestamp(2001, 8, 30, 15, 0)
    end = timestamp(2001, 8, 30, 15, 10)
    collector = dc.Data_Collector('rrc06', start, end)
    as_graph = collector.get_data_graph()
    draw_map(as_graph)


if __name__ == '__main__':
    main()