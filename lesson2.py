class Monitor:
    displayResolution = 0
    screenSize = 0
    rate = 0
    def __init__(self,px,dm,Hz):
        print("Create nem Monitor")
        self.displayResolution = px
        self.screenSize = dm
        self.rate = Hz
    def printInto(selt,name):
        print(f"{name:^10}")
        print("Display Resolution:", selt.displayResolution)
        print("Screen Size:", selt.screenSize)
        print("Image refresh rate:", selt.rate)


lg = Monitor(1500,500,1000)
philips = Monitor(500,345,6789)
print("LG")
print("PHILIPS")