# PMS5003 Particulate Sensor Adafruit IO integration
## Requirements
This setup requires account on [Adafruit IO](https://io.adafruit.com). Free subscription is absolutely suitable for this purpose. 

## Hardware
* [Raspberry Pi Zero](https://botland.com.pl/pl/moduly-i-zestawy-raspberry-pi-zero/5215-raspberry-pi-zero-v13-512mb-ram.html?search_query=raspberry+pi&results=1189)
* [Plantower PMS5003 sensor](https://botland.com.pl/pl/czujniki-czystosci-powietrza/6797-czujnik-pylu-czystosci-powietrza-pm25-pms5003-5v-uart.html?search_query=pms5003&results=3)
* [Logic Level Converter](https://botland.com.pl/pl/konwertery-napiec/8590-konwerter-poziomow-logicznych-dwukierunkowy-8-kanalowy.html)
### Software
* Install Raspian on RPi
* Install needed packages

```bash 
sudo apt install python3-pip git vim
```
* Enable serial port on Raspbian

```bash
sudo raspi-config nonint do_serial 1
sudo raspi-config nonint set_config_var enable_uart 1 /boot/config.txt
```

* Enable full UART instead of default miniUART by adding the line ```dtoverlay=pi3-miniuart-bt``` to **/boot/config.txt** file.
## Installing
* Clone this repo
* Copy env.example to .env
```
cp .env.example .env
```
* Adapt variables
* Install requirements
```pip3 install -r requirements.txt```

## Credits
[Pimoroni](https://github.com/pimoroni/pms5003-python) - great pms5003 library
