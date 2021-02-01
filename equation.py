class VelocityA:
    def __init__(self, d=0, t=0):
        self.dist = d
        self.time = t

    def FindVelocity(self):
        ans = float(self.dist) / int(self.time)
        return ans

    def FindDistanceAsM(self):
        return float(self.dist) * 1000

    def FindDistanceAsKm(self):
        return float(self.dist) / 1000

    def FindTimeAsSecond(self):
        return float(self.time) * 3600

    def FindTimeAsHr(self):
        return float(self.time) / 3600