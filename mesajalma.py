import can 

bus = can.interface.Bus(bustype = "socketcan", channel= "vcan0", bitrate = 250000)

while True:
    msg = bus.recv()
    print(msg)