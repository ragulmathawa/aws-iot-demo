import json
import time
import os
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Update these with your AWS IoT details
HOST_NAME = "a17xbon89p9o7a-ats.iot.ap-south-1.amazonaws.com"
ROOT_CA = "./certs/root-CA.crt"
PRIVATE_KEY = "./certs/device.private.key"
CERTIFICATE = "./certs/device.cert.pem"
SHADOW_HANDLER = "shadow-handler"

# Initialize the AWS IoT MQTT Shadow Client
myShadowClient = AWSIoTMQTTShadowClient("Ragul_device")
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)

# Connect to AWS IoT
myShadowClient.connect()

# Create a device shadow instance using persistent subscriptions
myDeviceShadow = myShadowClient.createShadowHandlerWithName("Ragul_device", True)

moduleDir = os.path.dirname(__file__)

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(moduleDir + '/state.json'):
            with open(moduleDir + '/state.json') as f:
                state = json.load(f)
                print("Updating the shadow with state: " + json.dumps(state))
                myDeviceShadow.shadowUpdate(json.dumps({"state": {"reported": state},"clientToken":"123"}), None, 5)

def delta_callback(payload, responseStatus, token):
    print("Received a delta message:", json.dumps(payload))
    # Load the delta message
    payloadDict = json.loads(payload)
    deltaMessage = payloadDict["state"]

    # Load the current state
    with open(moduleDir + '/state.json') as f:
        currentState = json.load(f)

    # Merge the delta message into the current state
    currentState.update(deltaMessage)

    # Write the updated state back to state.json
    with open(moduleDir + '/state.json', 'w') as f:
        json.dump(currentState, f)

def shadow_callback(payload, responseStatus, token):
    # Load the shadow state
    payloadDict = json.loads(payload)
    shadowState = payloadDict["state"]["desired"]

    # Write the shadow state to state.json
    with open(moduleDir + '/state.json', 'w') as f:
        json.dump(shadowState, f)

# Initialize the file observer
observer = Observer()
event_handler = FileChangeHandler()
observer.schedule(event_handler, path=moduleDir, recursive=False)

# Start the observer
observer.start()

# Initialize the shadow with the current state
# with open(moduleDir + '/state.json') as f:
#     state = json.load(f)
#     print("Updating the shadow with state: " + json.dumps(state))
#     myDeviceShadow.shadowUpdate(json.dumps({"state": {"reported": state}}), None, 5)
# or Download the latest shadow state
myDeviceShadow.shadowGet(shadow_callback, 5)
# Register the delta callback
myDeviceShadow.shadowRegisterDeltaCallback(delta_callback)
print("Listening for shadow changes in state.json as well as in shadow delta")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
