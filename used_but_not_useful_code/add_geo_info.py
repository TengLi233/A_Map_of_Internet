from collections import defaultdict
import IP2Location
import get_data

IP2LocObj = IP2Location.IP2Location()
IP2LocObj.open("../IP2LocationDBs/IP2LOCATION-LITE-DB5.BIN")


curr_as = get_data.main()
AS = defaultdict(set)
as_with_geo = defaultdict(None)
with open('../IPv4_IPv6_ASN/IP2LOCATION-LITE-ASN.CSV') as f:
    for lines in f:
        aslist = lines.split(",")

        prefix = aslist[2][1:-1]
        asn = aslist[3][1:-1]
        if len(curr_as[asn]) > 0:
            AS[asn].add(prefix)

for key in AS:
    sum_longtitude = 0.0
    for elem in AS[key]:
        ip_adress = elem.split('/')
        rec = IP2LocObj.get_all(ip_adress[0])
        sum_longtitude += rec.longitude
    as_with_geo[key] = sum_longtitude/len(AS[key])

with open("../Autonomous_System_File/AS_Geo_Table.csv", 'w') as f:
    f.write("asn" + "\t" + "longtitude\n")
    for key in as_with_geo:
        f.write(key + "\t" +str(as_with_geo[key]) + "\n")

print as_with_geo
print len(as_with_geo)




