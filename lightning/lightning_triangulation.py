import math
import random

class BaseStation:
    def __init__(self):
        self.coordinates = RandomPosition()
        self.timeHit = strikeTime + Distance(lightningPosition, self.coordinates) / shockwaveSpeed

def Distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def RandomPosition():
    return random.randint(0, 500), random.randint(0, 500)

def circle_intersections(x1, y1, r1, x2, y2, r2):
    d = Distance((x1, y1), (x2, y2))
    if (d > r1 + r2 or d < abs(r1 - r2) or d == 0):
        return []
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    x0 = x1 + a * (x2 - x1) / d
    y0 = y1 + a * (y2 - y1) / d
    rx = -(y2 - y1) * (h / d)
    ry = (x2 - x1) * (h / d)
    return [(x0 + rx, y0 + ry), (x0 - rx, y0 - ry)]

def cluster_intersections(points, radius):
    clusters = []
    for point in points:
        found_cluster = False
        for cluster in clusters:
            if (any(Distance(point, other) <= radius for other in cluster)):
                cluster.append(point)
                found_cluster = True
                break
        if (not found_cluster):
            clusters.append([point])
    return clusters

def estimate_lightning_position(base_stations):
    intersections = []
    
    for i in range(len(base_stations)):
        for j in range(i + 1, len(base_stations)):
            s1, s2 = base_stations[i], base_stations[j]
            if (s1.broadcastRadius > 0 and s2.broadcastRadius > 0):
                intersections += circle_intersections(
                    s1.coordinates[0], s1.coordinates[1], s1.broadcastRadius,
                    s2.coordinates[0], s2.coordinates[1], s2.broadcastRadius
                )

    if (not intersections):
        return None
    
    clusters = cluster_intersections(intersections, .25)
    cluster = max(clusters, key=len)

    avg_x = sum(p[0] for p in cluster) / len(cluster)
    avg_y = sum(p[1] for p in cluster) / len(cluster)
    return len(cluster), avg_x, avg_y

size = 500
shockwaveSpeed = 1

strikeTime = random.randint(0, 100000)
lightningPosition = RandomPosition()

baseStationCount = 3
baseStations = []
firstBaseStationHit = None
lastBaseStationHit = None
for _ in range(baseStationCount):
    baseStation = BaseStation()
    if (not firstBaseStationHit or baseStation.timeHit < firstBaseStationHit.timeHit):
        firstBaseStationHit = baseStation
    if (not lastBaseStationHit or baseStation.timeHit > lastBaseStationHit.timeHit):
        lastBaseStationHit = baseStation

