# SNR-UPS-ONRT мониторинг по SNMP

Проверено на SNR-UPS-ONRT-6000-INTXL

## Зависимости
https://github.com/pyhys/minimalmodbus

## Постоянное имя для usb
/etc/udev/rules.d/99-usb-serial.rules
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="1d6b", ATTRS{idProduct}=="0001", SYMLINK+="USB_to_UPS"
```

### Работа модуля отдельно от agentx
```
$python3 ./snr_modbus.py
Vin = 221.5
HZin = 50.0
Iin = 5.4
HZout = 50.0
Vout = 220.1
Iout = 4.6
Pout = 0.8
LOADout = 17.4
Vbatt = 215
STATE = 0
CHARGEbatt = 100
$python3 ./snr_modbus.py Vin
222.3
```
