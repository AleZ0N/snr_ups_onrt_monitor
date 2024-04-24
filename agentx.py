#!/usr/bin/python3

import pyagentx3
import sys

sys.path.append('../lib/')
import snr_modbus

values = {}

class NetSnmpPlaypen(pyagentx3.Updater):
    def update(self):
        for name in snr_modbus.cells:
            values[name] = snr_modbus.getValue(name)
        self.set_OCTETSTRING('110.1', values['CHARGEbatt'])
        self.set_OCTETSTRING('110.2', values['Vbatt'])
        self.set_OCTETSTRING('110.3', values['Vin'])
        self.set_OCTETSTRING('110.4', values['Vout'])
        self.set_OCTETSTRING('110.5', values['LOADout'])
        self.set_OCTETSTRING('110.7', values['HZin'])
        if values['STATE'] == 0:
            self.set_OCTETSTRING('110.8', 'OL')
        else:
            self.set_OCTETSTRING('110.8', 'OB')

class MyAgent(pyagentx3.Agent):
    def setup(self):
        self.register('1.3.6.1.4.1.8072.9999.9999', NetSnmpPlaypen)

pyagentx3.setup_logging()
try:
    a = MyAgent()
    a.start()
except Exception as e:
    print("Unhandled exception:", e)
    a.stop()
except KeyboardInterrupt:
    a.stop()
