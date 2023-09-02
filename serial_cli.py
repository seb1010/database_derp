import serial
import time
import sys
from tinydb import TinyDB

import remote_cli
import thermistor_ntcs0805e3103jht

def main(argv):
    ser = serial.Serial(argv[0])
    ser.baudrate=9600
    ser.timeout = None
    
    filename = "local_boi.json"
    db = TinyDB(filename)
    therm = thermistor_ntcs0805e3103jht.ThermMath()
    rm = remote_cli.RemoteCli() 
    

    start_time = int(time.time())
    send_data_time = start_time
    update_delta = 60 # updating every minute for debug

    while(True):
        val = 0
        byte = b'0'
        while(byte != b'\n'):
            val = (val << 4) + int(byte, 16) # hex input
            byte = ser.read()
        temp_c = therm.convert(val)
        print(f"thermistor reading: {temp_c} C")

        if time.time() > send_data_time:
            send_data_time += update_delta;
            db.insert({"time": int(time.time()),
                "temp_c": (temp_c * 10 // 1 / 10)})
            try:
                rm.update_remote(db.all())  
            #print(db.all())
                print("updating json")
            except:
                print("idk it's broken or something") 



if __name__ == "__main__":
    main(sys.argv[1:])
