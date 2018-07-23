class AS(object):
    def __init__(self, asn):
        self.asn = asn

    def set_degrees(self, degree):
        self.degrees = degree

    def set_longtitude(self, longtitude):
        self.longtitude = longtitude

    def get_asn(self):
        return self.asn

    def get_degrees(self):
        return self.degrees

    def get_longtitude(self):
        return self.longtitude

    def __str__(self):
        return str(self.asn)



