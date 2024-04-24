import sys
import minimalmodbus

cells = dict(
    Vin = 1,
    HZin = 7,
    Iin = 16,
    HZout = 19,
    Vout = 25,
    Iout = 28,
    Pout = 40,
    LOADout = 46,
    Vbatt = 50,
    STATE = 55,
    CHARGEbatt = 56
)

port = '/dev/USB_to_UPS'

instrument = minimalmodbus.Instrument(port, 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 5
instrument.mode = minimalmodbus.MODE_ASCII

def getValue(name):
    value = instrument.read_register(cells[name], 1)
    if name == 'HZin' or name == 'HZout':
        value /= 10
    if name == 'STATE' and value > 0:
        value = 1
    return round(value, 1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        for name in cells:
            value = getValue(name)
            print(name, "=", value)
    else:
         print(getValue(sys.argv[1]))
