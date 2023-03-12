class Device():
    def __init__(self):
        self.amps = 0
        self.psuWatts = 0
        self.deviceKW = 0
        self.btu = 0
        self.db = 0.0
        self.lbs = 0.0
        self.uSize = 0
        self.deviceType = ""
        self.deviceName = ""
        self.deviceData = {}

    def initializeDeviceData(self):
        self.deviceData.update({"Name": self.deviceName})
        self.deviceData.update({"Type": self.deviceType})
        self.deviceData.update({"uSize": self.uSize})
        self.deviceData.update({"lbs": self.lbs})
        self.deviceData.update({"db": self.db})
        self.deviceData.update({"psuWatts": self.psuWatts})

        return

    def updateDeviceData(self):
        self.deviceName = self.deviceData.get("Name")
        self.deviceType = self.deviceData.get("Type")
        self.uSize = self.deviceData.get("uSize")
        self.lbs = self.deviceData.get("lbs")
        self.db = self.deviceData.get("db")
        self.psuWatts = self.deviceData.get("psuWatts")

        return

    def readDeviceData(self, json):
        self.deviceData.update({"Name": json.get("Name")})
        self.deviceData.update({"Type": json.get("Type")})
        self.deviceData.update({"uSize": int(json.get("uSize"))})
        self.deviceData.update({"lbs": float(json.get("lbs"))})
        self.deviceData.update({"db": float(json.get("db"))})
        self.deviceData.update({"psuWatts": int(json.get("psuWatts"))})

        return

    def ampsPerServer(self, VAC):
        self.amps = self.psuWatts / VAC
        self.deviceData.update({"Amps": self.amps})

        return

    def calcServerKW(self):
        self.deviceKW = self.psuWatts / 1000
        self.deviceData.update({"DeviceKW": self.deviceKW})

        return

    def calcServerBTU(self):
        self.btu = float(self.psuWatts) * 3.4
        self.deviceData.update({"btu": self.btu})

        return

    def computeData(self, VAC):
        # Pushes data from deviceData to the object variables
        self.updateDeviceData()

        # Calculates amps for this device
        self.ampsPerServer(VAC)

        # Calculates kW for this device
        self.calcServerKW()

        # Calculates BTU Produced from this device
        self.calcServerBTU()

        return


    def collectDeviceData(self, VAC):
        deviceVar = [self.deviceType, self.deviceName, self.uSize, self.lbs, self.db, self.psuWatts]
        inputVar = ["type", "name", "U size", "weight in lbs", "db level", "PSU wattage"]
        dataVar = ["Type", "Name", "uSize", "lbs", "db", "psuWatts"]

        # Prompts user for input in terminal for information on each device
        for i, r in enumerate(inputVar):
            if i == 0:
                devtype = input("What type of device is this? (Server, Switch, Firewall, etc.): ")
                self.deviceData.update({dataVar[i]: devtype})
            else:
                response = input(f"What is the {r} of this {devtype}?: ")
                if type(deviceVar[i]) == str:
                    self.deviceData.update({dataVar[i]: response})
                elif type(deviceVar[i]) == float:
                    self.deviceData.update({dataVar[i]: float(response)})
                else:
                    self.deviceData.update({dataVar[i]: int(response)})
        
        self.computeData(VAC)

        return print(f"{self.deviceName} information updated")