import can 

bus = can.interface.Bus(bustype = "socketcan",channel = "vcan0", bitrate = 250000)  # busımızı tanımladık

msg = can.Message(arbitration_id=0x01, data= [1, 2, 3, 4, 5, 6, 7, 8],is_extended_id=False)



try:
    bus.send(msg)
    print(" {} mesaj hattına mesaj yollandı".format(bus.channel_info))

except can.CanError:
    print("mesaj gönderilemedi")
