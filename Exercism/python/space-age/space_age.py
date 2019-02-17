class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.Earth   = 31557600

    def on_earth(self):
        return float("{0:.2f}".format(self.seconds / self.Earth))
    def on_mercury(self):
        return float("{0:.2f}".format(self.seconds / (0.2408467  * self.Earth)))
    def on_venus(self):
        return float("{:.2f}".format(self.seconds / (0.61519726 * self.Earth)))
    def on_mars(self):
        return float("{:.2f}".format(self.seconds / (1.8808158  * self.Earth)))
    def on_jupiter(self):
        return float("{:.2f}".format(self.seconds / (11.862615  * self.Earth)))
    def on_uranus(self):
        return float("{:.2f}".format(self.seconds / (84.016846  * self.Earth)))
    def on_neptune(self):
        return float("{:.2f}".format(self.seconds / (164.79132  * self.Earth)))
    def on_saturn(self):
        return float("{:.2f}".format(self.seconds / (29.447498  * self.Earth)))

#print("{:.2f}".format(SpaceAge(1000000000).on_earth()))

