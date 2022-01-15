class Placed:

    def __init__(self, country, place, changed, points):
        self.country = country
        self.place = place
        self.changed = changed
        self.points = points

    def __str__(self):
        return "ország: " + self.country + " helyezés: " + self.place + " változás: " + self.changed + " pontszám: " + self.points
