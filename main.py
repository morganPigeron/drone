import paho.mqtt.client as mqtt
import smbus

bus = smbus.SMBus(0)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.topic == "drone":

        direction = msg.payload.direction
        speed = msg.payload.speed
        track = msg.payload.track

        bus.write_i2c_block_data(int(track), 0x01,[int(direction),int(speed)])



if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("192.168.1.38", 1883, 60)