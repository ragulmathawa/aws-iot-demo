# Import the AWS IoT Device SDK
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define the callbacks for when a message is received
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)

# Specify the path to your private key, certificate, and Amazon Root CA 1
privateKeyPath = "./certs/device.private.key"
certificatePath = "./certs/device.cert.pem"
caPath = "./certs/root-CA.crt"

# Specify your AWS IoT endpoint
endpoint = "a17xbon89p9o7a-ats.iot.ap-south-1.amazonaws.com"

# Specify your client ID (typically the name of the IoT Thing)
clientId = "Ragul_device"

# Initialize the AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(endpoint, 8883)
myAWSIoTMQTTClient.configureCredentials(caPath, privateKeyPath, certificatePath)

# Connect to the AWS IoT platform
myAWSIoTMQTTClient.connect()

# Subscribe to a topic and specify the callback function
myAWSIoTMQTTClient.subscribe(clientId + "/test", 1, customCallback)

print("Subscribed to topic: " + clientId+"/test")
# Keep the connection open
while True:
    pass
