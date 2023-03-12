import json

import rackClass
import deviceClass

def populateDevices(VAC):
    device = deviceClass.Device()
    device.initializeDeviceData()
    device.collectDeviceData(VAC)
    deviceData = device.deviceData

    return deviceData

def readDevices(dev, VAC):
    deviceData = list()
    devicePower = list()
    for d in dev:
        device = deviceClass.Device()
        device.readDeviceData(d)
        device.computeData(VAC)
        deviceData.append(device.deviceData)
        devicePower.append(device.deviceKW)
    
    return deviceData, devicePower

def writeOut(rackOutput):
    with open("rackAssessment.json", "w") as o:
        o.write(json.dumps(rackOutput, indent=4))

    return print("File successfully written")

def main():
    rackList = list()
    rackOutput = dict()
    VAC = 120
    count = 1
    mode = 1

    # Mode indicates if the process is manual or reads from template JSON
    # 0 = manual and 1 = read from file
    if mode == 0:
        rackAmount = input("How many racks in datacenter?: ")
        for i in range(rackAmount):
            rackList.append(rackClass.Rack())

        for rack in rackList:
            rack.initializeData()
            deviceAmount = input(f"How many devices in {rack.name}: ")
            for i in range(int(deviceAmount)):
                deviceData = populateDevices(VAC)
                rack.deviceList.append(deviceData)
            rackOutInfo = rack.rackData()
            rackOutput.update({f"Rack_{count}": rackOutInfo})
            count += 1
    else:
        rackJSON = list()
        allDevices = list()
        rackBTU = list()
        rackAmount = 0

        with open("rackTemplate.json", "r") as rackTemplate:
            template = json.load(rackTemplate)

        for i in template:
            rackList.append(rackClass.Rack())
            rackDetail = template.get(i)
            rackJSON.append(rackDetail)
            deviceJSON = rackDetail.get("deviceList")
            allDevices.append(deviceJSON)

        for rack in rackList:
            for d in rackJSON:
                rack.readData(d)
            for dev in allDevices:
                deviceData, devicePower = readDevices(dev, VAC)
                rack.deviceList.append(deviceData)
                rack.maxKWPerRack(devicePower)
                rack.totalRackBTU()
            rackOutInfo = rack.rackData()
            rackOutput.update({f"Rack_{count}": rackOutInfo})
            count += 1

    writeOut(rackOutput)

if __name__ == "__main__":
    main()