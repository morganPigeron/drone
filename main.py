import paho.mqtt.client as mqtt
import smbus
import json

bus = smbus.SMBus(0)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("drone")
    print("subscribed to drone")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    
    print("topic drone : ")

    payload = json.loads(msg.payload)
    print(payload)
    direction = payload['direction']
    speed = payload['speed']
    track = payload['track']

    print(direction)
    print(speed)
    print(track)
    try:
        bus.write_i2c_block_data(int(track), 0x01,[int(direction),int(speed)])
    except :
        print("ERREUR ENVOI I2C")
    print("---END---")



if __name__ == "__main__":

    client = mqtt.Client("orangePi")
    client.on_connect = on_connect
    client.on_message = on_message
    print("connecting to MQTT server ....")
    client.connect("192.168.1.38", 1883, 60)
    print("connected")
    client.loop_forever()
