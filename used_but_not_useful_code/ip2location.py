import IP2Location

IP2LocObj = IP2Location.IP2Location()
IP2LocObj.open("../IP2LocationDBs/IP2LOCATION-LITE-DB5.IPV6.BIN")
rec = IP2LocObj.get_all("2001:250::")

print rec.country_short
print rec.country_long
print rec.region
print rec.city
print rec.latitude
print rec.longitude
