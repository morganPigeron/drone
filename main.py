from flask import Flask, request, render_template
import smbus

app = Flask(__name__)

bus = smbus.SMBus(0)

@app.route("/")
def root():
    return render_template("index.html")

#api 
@app.route("/api", methods = ['GET', 'POST'])
def command():
    if request.method == 'GET':
        #"sudo i2ctransfer 0 w3@0x2c 0x01 0x00 50"

        direction = request.args['command']
        speed = request.args['speed']
        track = request.args['track']

        bus.write_i2c_block_data(int(track), 0x01,[int(direction),int(speed)])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)