import math
import random
from tkinter import *

speed = 1
time_step = 0.1
size = 500

# Setup window + canvas
window = Tk()
window.title("Lightning Triangulation")
c = Canvas(window, width=size, height=size, background="black")
c.pack()
window.update()

# Helper functions
def Circle(x, y, radius, _fill="", _outline="", _tags="temp"):
    return c.create_oval(x-radius, y-radius, x+radius, y+radius, fill=_fill, outline=_outline, tags=_tags)
    
def Distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def RandomPosition():
    return random.randint(0, c.winfo_width()), random.randint(0, c.winfo_height())

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
    
# Render lightning
lightningPosition = RandomPosition()
Circle(lightningPosition[0], lightningPosition[1], 5, "", "yellow", "lightning")

# Render loop
time = random.randint(0, 10000)
ticking = True
strikeTime = time + random.randint(400, 600)
hasStriken = False
bestEstimate = None
estimateStrikeTime = 0
lightningRadius = 0
debug = False

reverseBroadcast = False
firstBaseStationHit = None
lastBaseStationHit = None

# Base station class
class BaseStation:
    
    def __init__(self, index, coordinates):
        self.index = index
        self.coordinates = coordinates
        self.collided = False
        self.shouldBroadcast = False
        self.increaseRadius = False
        self.timeBroadcasting = 0
        self.timeHit = 0
        self.broadcastRadius = 0
        Circle(self.coordinates[0], self.coordinates[1], 5, "gray", "", "basestation" + str(self.index))

    def collide(self):
        if (not self.collided):
            self.collided = True
            self.timeHit = time
            c.delete("basestation" + str(self.index))
            Circle(self.coordinates[0], self.coordinates[1], 5, "red", "", "basestation" + str(self.index))

    def tick(self):
        if (self.increaseRadius):
            self.broadcastRadius += time_step
            self.timeBroadcasting += time_step
        
        if (self.shouldBroadcast):
            Circle(self.coordinates[0], self.coordinates[1], self.broadcastRadius, "", "white")

    def isCollided(self):
        return self.collided

# Base stations
baseStationCount = 5
baseStations = []

for i in range(baseStationCount):
    baseStations.append(BaseStation(i, RandomPosition()))

trackingStation = random.choice(baseStations)

# Setup Permanent Visuals
c.create_text(0, 0, text="Time: ", fill="white", anchor="nw")
c.create_text(0, 15, text="Time of strike: " + str(round(strikeTime, 1)), fill="white", anchor="nw")
c.create_text(0, 30, text="(E)Time of strike: ", fill="white", anchor="nw")

while ticking:
    # Clear canvas
    c.delete("temp")

    # Update simulation state
    time += time_step

    if (time > strikeTime):
        if (not hasStriken):
            Circle(lightningPosition[0], lightningPosition[1], 5, "yellow", "", "lightning_fill")
            hasStriken = True
        lightningRadius += speed * time_step

    # Render time & estimate text
    c.create_text(35, 0, text=str(round(time, 1)), fill="white", anchor="nw", tags="temp")
    c.create_text(90, 30, text=str(round(estimateStrikeTime, 1)), fill="white", anchor="nw", tags="temp")

    # Render lightning
    if (hasStriken and not reverseBroadcast):
        Circle(lightningPosition[0], lightningPosition[1], lightningRadius, "", "white")

    # Tick basestations
    for baseStation in baseStations:
        baseStation.tick()

    # Check for Collisions
    for baseStation in baseStations:
        if (not baseStation.isCollided()):
            distance = Distance(baseStation.coordinates, lightningPosition)
            if (lightningRadius >= distance):
                baseStation.collide()
                lastBaseStationHit = baseStation
                if (firstBaseStationHit == None):
                    firstBaseStationHit = baseStation

    # Check if we should start reversing the broadcast
    if (not reverseBroadcast):
        allBaseStationsHit = True
        for baseStation in baseStations:
            if (not baseStation.isCollided()):
                allBaseStationsHit = False
                break
        reverseBroadcast = allBaseStationsHit

    # Reverse broadcast
    if (reverseBroadcast):
        for baseStation in baseStations:
            if (not baseStation.shouldBroadcast):
                timeToBroadcast = lastBaseStationHit.timeHit + (lastBaseStationHit.timeHit - baseStation.timeHit)
                if (time >= timeToBroadcast):
                    baseStation.shouldBroadcast = True
                    baseStation.increaseRadius = True
    
    # Estimate Lightning Position
    estimate = estimate_lightning_position(baseStations)
    if (estimate != None):
        if (bestEstimate == None or estimate[0] >= bestEstimate[0]):
            bestEstimate = estimate
            estimateStrikeTime = firstBaseStationHit.timeHit - Distance(firstBaseStationHit.coordinates, (bestEstimate[1], bestEstimate[2]))
        Circle(bestEstimate[1], bestEstimate[2], 5, "cyan", "")
    
    # Update window
    window.update()
