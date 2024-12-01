import math
import random
from tkinter import *

# Helper functions
def Circle(x, y, radius, _fill="", _outline="", _tags="temp"):
    return c.create_oval(x-radius, y-radius, x+radius, y+radius, fill=_fill, outline=_outline, tags=_tags)
    
def DistanceSquared(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def Distance(a, b):
    return math.sqrt(DistanceSquared(a, b))

def RandomPosition():
    return random.randint(0, 500), random.randint(0, 500)

def CircleIntersections(x1, y1, r1, x2, y2, r2):
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

# Constants
shockwaveSpeed = 1
time_step = 0.1
size = 500

# Setup window + canvas
window = Tk()
window.title("Lightning Triangulation")
c = Canvas(window, width=size, height=size, background="black")
c.pack()
window.update()

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

    def isCollided(self):
        return self.collided

# Base stations
baseStationCount = 100
baseStations = []

for i in range(baseStationCount):
    baseStations.append(BaseStation(i, RandomPosition()))

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
        lightningRadius += shockwaveSpeed

    # Render time & estimate text
    c.create_text(35, 0, text=str(round(time, 1)), fill="white", anchor="nw", tags="temp")
    c.create_text(90, 30, text=str(round(estimateStrikeTime, 1)), fill="white", anchor="nw", tags="temp")

    # Render lightning
    if (hasStriken and not reverseBroadcast):
        Circle(lightningPosition[0], lightningPosition[1], lightningRadius, "", "white")

    # Check for Collisions
    for baseStation in baseStations:
        if (not baseStation.isCollided()):
            distanceSquared = DistanceSquared(baseStation.coordinates, lightningPosition)
            if (lightningRadius**2 >= distanceSquared):
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

        for _ in range(int(shockwaveSpeed / time_step)):
            c.delete("broadcast")
            for baseStation in baseStations:
                if (baseStation.shouldBroadcast):
                    baseStation.broadcastRadius += time_step
                    Circle(baseStation.coordinates[0], baseStation.coordinates[1], baseStation.broadcastRadius, "", "white", "broadcast")

            # Get intersections
            station1 = baseStations[0]
            station2 = baseStations[1]
            intersections = CircleIntersections(station1.coordinates[0], station1.coordinates[1], station1.broadcastRadius, station2.coordinates[0], station2.coordinates[1], station2.broadcastRadius)
            if (not intersections):
                continue
            bestIntersection = None
            for intersection in intersections:
                intersected = 0
                averageDistance = 0
                for baseStation in baseStations:
                    distance = Distance(intersection, baseStation.coordinates) - baseStation.broadcastRadius
                    if (distance <= 1):
                        averageDistance += distance
                        intersected += 1
                averageDistance /= intersected
                if (not bestIntersection or (intersected > bestIntersection[0]) or (intersected >= bestIntersection[0] and averageDistance < bestIntersection[1])):
                    bestIntersection = (intersected, averageDistance, intersection)

            # Estimate Lightning Position
            estimate = bestIntersection
            if (estimate):
                if (not bestEstimate or (estimate[0] > bestEstimate[0]) or (estimate[0] >= bestEstimate[0] and estimate[1] < bestEstimate[1])):
                    bestEstimate = estimate
                    estimateStrikeTime = firstBaseStationHit.timeHit - Distance(firstBaseStationHit.coordinates, bestEstimate[2])
            if (bestEstimate):
                Circle(bestEstimate[2][0], bestEstimate[2][1], 5, "cyan", "", "broadcast")

            # End if estimate matches
            if (bestEstimate and Distance(lightningPosition, bestEstimate[2]) <= .1):
                ticking = False
                break
    
    # Update window
    window.update()

while not ticking:
    c.delete("")
    window.update()