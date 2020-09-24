import math
import numpy as np

def convert(inp, From=None, To=None):
    f = From.title(); t = To.title()
    From_dict = {"Kilometer":inp*1000, "Meter":inp, "Centimeter":inp/100, "Nanometer":inp*1e-9,
                 "Micrometer":inp*1e-7,
                 "Kilogram":inp*1000, "Gram":inp,
                 "Kilocalorie":inp*1000, "Calorie":inp,
                 "Second":inp, "Minute":inp*60, "Hour":inp*3600, "Day":inp*86400, "Week":inp*604800,
                 "Month":inp*2592000, "Year":inp*236520000, "Milisecond":inp/1000,
                 "Microsecond":inp*1e-7, "Nanosecond":inp*1e-9}
    To_dict = {"Kilometer":1000, "Meter":1, "Centimeter":1e-2, "Nanometer":1e-9,
                 "Micrometer":1e-7,
               "Kilogram":1000, "Gram":1,
               "Kilocalorie":1000, "Calorie":1,
               "Second":1, "Minute":60, "Hour":3600, "Day":86400, "Week":604800,
               "Month":2592000,  "Year":236520000, "Milisecond":1/1000,
               "Microsecond":1e-7, "Nanosecond":1e-9}
    var1 = 0; var2 = 0
    for aux in From_dict.keys():
        if f == aux:
            var1 = From_dict[aux]
        if t == aux:
            var2 = To_dict[aux]
    return var1/var2

def gravity(radius=None, Planet=None, Mass=None):
    if radius == None:
        radius = 6371000
    if Planet != None:
        Planet = Planet.title()
    if Planet == None and Mass == None:
        Planet = "Earth"
    planets = {"Earth":5.972e24, "Mars":6.39e23, "Jupiter":1.899e27, "Venus":4.867e24,
              "Mercury":3.285e23, "Saturn":5.683e26, "Uranus":8.681e25, "Neptune":1.024e26}
    for planet in planets.keys():
        if planet == Planet:
            Mass = planets[planet]
    G = 6.67e-11
    g = G * (Mass/(radius**2))
    return g

def Cinematics(Degree=True, cos=True, x=None, v=None, t=None, a=None, x0=0, t0=0, v0=0, kind=None,
               find=None, T=None, f=None, w=None, angle0=0, R=None, A=None):
    arg = None; cond = True
    if find == None:
        return "specify Find"
    if kind == None:
        return "specify Kind"
    if kind != None:
        kind = kind.upper()

        if kind == "MRU":
            if find == "x":
                dt = t-t0
                arg = x0 + (v*dt)
            elif find == "t":
                dx = x-x0
                arg = (dx - v)/t0
            elif find == "v":
                dx = x-x0; dt = t-t0
                arg = dx/dt
        elif kind == "MRUV":
            if find == "x":
                dt = t-t0
                arg = x0 + (v0*dt) + (a/2 * (dt**2))
            elif find == "t":
                from math import sqrt
                dx = x-x0; A = a/2; B = v; C = -dx
                x1 = (-B + sqrt(B ** 2 - (4 * A * C))) / (2 * A)
                x2 = (-B - sqrt(B ** 2 - (4 * A * C))) / (2 * A)
                arg = (x1, x2)
            elif find == "v":
                dt = t-t0
                arg = v0 + (a*dt)
            elif find == "a":
                dv = v-v0; dt = t-t0
                arg = dv/dt
        elif kind == "MCU":
            pi = math.pi
            if find == "angle":
                dt = t-t0
                arg = angle0 + (w*dt)
            elif find == "T":
                if f != None:
                    arg = 1/f
                else:
                    arg = (2*pi)/w
            elif find == "f":
                if T != None:
                    arg = 1/T
                else:
                    arg = w/(2*pi)
            elif find == "w":
                if f != None:
                    arg = 2*pi*f
                else:
                    arg = (2*pi)/T
            elif find == "v":
                if w != None:
                    arg = R*w
                elif f != None:
                    arg = 2*pi*R*f
                else:
                    arg = (2*pi*R)/T
            elif find == "a":
                if v != None:
                    arg = (v**2)/R
                elif w != None:
                    arg = R * w**2
                elif f != None:
                    arg = (2*pi*R*f)**2 / R
                else:
                    arg = ((2*pi*R)/T)**2 / R
        elif kind == "MAS":
            if Degree == True:
                angle0 *= math.pi / 180
            if cos != True:
                cond = False
            a = w*t + angle0
            if cond == True:
                if find == "x":
                    arg = A * np.cos(a)
                elif find == "v":
                    arg = -A * w * np.sin(a)
                elif find == "a":
                    arg = -A*(w**2) * np.cos(a)
                elif find == "t":
                    if x != None:
                        arg = (np.arccos(x/A) - angle0) / w
                    elif v != None:
                        arg = (np.arcsin(v/(-A*w)) - angle0) / w
                    else:
                        arg = (np.arccos(a/(-A*(w**2)))-angle0) / w
            else:
                if find == "x":
                    arg = A * np.sin(a)
                elif find == "v":
                    arg = -A * w * np.cos(a)
                elif find == "a":
                    arg = -A*(w**2) * np.sin(a)
                elif find == "t":
                    if x != None:
                        arg = (np.arcsin(x/A) - angle0) / w
                    elif v != None:
                        arg = (np.arccos(v/(-A*w)) - angle0) / w
                    else:
                        arg = (np.arcsin(a/(-A*(w**2)))-angle0) / w

    return arg