import cv2
from opcua import Client, ua

objects = None
server_url = "opc.tcp://DESKTOP-6P06VFE:4840"
client = Client(server_url)

originalBottleImage = None
imageName = "Resources/bottle_with_label.png"
originalBottleImageWithColour = cv2.imread(imageName)

lastSession = 0



def connectOpcua():

    global objects
    client.connect()
    print("Connected to server")
    objects = client.get_objects_node()

# Checks proximity sensor to check for bottle
def checkSensor():

    var = client.get_node("ns=4;s=LadderLogicBottleChecker.BottleDetected")
    return var.get_value()

# Trigger ejection sequence in PLC when no label is found
def activateEject():
    var = client.get_node("ns=4;s=LadderLogicBottleChecker.EjectBottle")
    print("Ejecting Bottle")
    var.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))

# Reads image (could be implemented to take snapshot from camera or cycle through photos in a folder)
def grabFrame():
    global originalBottleImage
    originalBottleImage = cv2.imread(imageName)

# Detects if bottle has image or not
def classifyCameraImage():
    originalBottleImage = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
    image = cv2.adaptiveThreshold(originalBottleImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
    contours, hier= cv2.findContours(image= image, mode= cv2.RETR_TREE, method= cv2.CHAIN_APPROX_NONE)

    if not (check_label(contours)):
        print("No labels detected, eject")
        return True

# Increases contrast on image to check for volume of closed square contours, if found and area is sufficient bottle is valid
def check_label(contours_list):

    for contour in contours_list:

        epsilon = 0.1 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        area = cv2.contourArea(contour)

        if len(approx) == 4 and 1000 < area < 20000:    # ensures neither small squares nor entire bottle are counted as labels
            cv2.drawContours(originalBottleImageWithColour, contour, -1, (0, 255, 0), 10)
            print("Label found")
            return True
    return False

# Triggers exit script in PLC
def exitScript():
    return client.get_node("ns=4;s=LadderLogicBottleChecker.ExitScript").get_value()

def getSessionNumber():
    return client.get_node("ns=4;s=LadderLogicBottleChecker.sessionNumber").get_value()


if __name__ == '__main__':
    connectOpcua()

    while 1:
        if (exitScript()):
            print("ExitScript")
            client.disconnect()
            print("Disconnected")
            break

        else:
            if checkSensor() and lastSession != getSessionNumber():
                # Prevents PLC from being oversampled by python code
                if getSessionNumber() == 5:
                    lastSession = 0
                else:
                    lastSession = getSessionNumber()
                grabFrame()

                if classifyCameraImage():
                    activateEject()
