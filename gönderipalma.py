import can
from can import message

bus = can.interface.Bus(bustype = "socketcan", channel = "vcan0", bitrate = 250000)

msg = can.Message(arbitration_id =0x560, data = [1,2,3,4,5,6,7,8],is_extended_id = False)

try:
    bus.send_periodic(msg,1)  # periyodik olarak saniyede 1 kez gönder dedik
    print("{} can hattına mesaj gönderildi".format(bus.channel_info))

    while True:
        message = bus.recv()
        print(message)

except can.CanError:
    print("Mesaj iletilemedi")

