from data_collection_package import data_collector
from generate_image import draw_network_map
from multiprocessing import Process
from datetime import datetime
import calendar


def timestamp(year, mouth, day, hour, mins):
    dt = datetime(year, mouth, day, hour, mins)
    return int(calendar.timegm(dt.timetuple()))


def start_collection(date):
    date = int(date)
    start = timestamp(date, 8, 1, 0, 0)
    end = timestamp(date, 8, 1, 2, 0)

    collector_ipv4 = data_collector.DataCollector(start, end, "IPv4")
    collector_ipv6 = data_collector.DataCollector(start, end, "IPv6")

    network_map_ipv4 = collector_ipv4.get_data_graph()
    network_map_ipv6 = collector_ipv6.get_data_graph()

    map_drawer = draw_network_map.MapDrawer(network_map_ipv4)
    map_drawer_ipv6 = draw_network_map.MapDrawer(network_map_ipv6)

    map_drawer.draw_map('AS_MAP_' + str(date) + '_IPV4')
    map_drawer_ipv6.draw_map('AS_MAP_' + str(date) + '_IPV6')


def main():
    # 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018
    time_list = [2008]
    processes = list()

    for date in time_list:
        p = Process(target=start_collection, args=(date, ))
        processes.append(p)

    for p in processes:
        p.start()


if __name__ == '__main__':
    main()
