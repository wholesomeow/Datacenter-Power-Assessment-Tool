class Rack():
    def __init__(self):
        self.name = ""
        self.uAmount = 0
        self.lbs = 0.0
        self.totalLBS = 0.0
        self.deviceList = []
        self.totalPower = 0
        self.totalDB = 0.0
        self.totalBTU = 0.0

    def initializeData(self):
        classVar = [self.name, self.uAmount, self.lbs]
        inputVar = ["name", "U Amount", "weight"]
        responseList = list()
        
        for i, e in enumerate(inputVar):
            response = input(f"What is the {e} of this rack?: ")
            if type(classVar[i]) == str:
                responseList.append(response)
            elif type(classVar[i]) == float:
                responseList.append(float(response))
            else:
                responseList.append(int(response))

        self.name = responseList[0]
        self.uAmount = responseList[1]
        self.lbs = responseList[2]

    def readData(self, data):
        self.name = data.get("name")
        self.uAmount = data.get("uAmount")
        self.lbs = data.get("lbs")

    def maxKWPerRack(self, devicesKW):
        self.totalPower = sum(devicesKW)

    def totalRackBTU(self):
        self.totalBTU = float(self.totalPower) * 3.4

    def rackData(self):
        rackData = dict()
        rackData.update({"Name": self.name})
        rackData.update({"uAmount": f"{self.uAmount}U"})
        rackData.update({"Weight": f"{self.lbs} lbs"})
        rackData.update({"Devices": self.deviceList})
        rackData.update({"TotalPower": f"{self.totalPower} kw"})
        rackData.update({"TotalBTU": f"{self.totalBTU} BTU per hour"})
        rackData.update({"TotalDB": f"{self.totalDB} db"})

        return rackData