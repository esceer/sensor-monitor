# sensor-monitor
Home automation project for collecting and transmitting sensor data. 

### Install
```
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

### Usage
##### Via shell script
`bin/monitor_<sensor_type>_sensor.sh <sensor_name>`

##### Directly via python3
`venv/bin/python3 monitor.py <sensor_type> <sensor_name>`

### Supported sensor type(s)
* **tsl2591**

### Timing
Crontab is used to schedule a full reboot of the application *(every 5 minutes)*
which initiates the sensors to synchronize with the backend.
Between these synchronization points, the application sends the current sensor state
to the backend every 30 seconds.
<br/>
The timing properties can be modified in the **bin/sm.ini** file.

##### Configure
```
crontab -u <username> -e
*/5 * * * * <install_dir>/sensor-monitor/bin/monitor_ts2591_sensor.sh <sensor_name> > <log_dir>/sm.log 2>&1
```


## ESP32
In order to use this script on ESP32 microcontrollers, the following configuration steps might be necessary:

##### Install esptool
```
sudo apt install python3-pip
sudo pip3 install esptool
```

##### Then connect the microcontroller and check if it's mounted:
`dmesg | grep ttyUSB`

##### Configure the current user's group:
`sudo usermod -a -G dialout <userid>`

##### Setup micropython on the microcontroller
```
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 <micropython_image_file_name>
```

##### Install rshell and connect to the board
```
sudo pip3 install rshell
sudo rshell --buffer-size=30 -p /dev/ttyUSB0
```
For further information on rshell, refer to the following github page:<br/>
https://github.com/dhylands/rshell

##### Network setup on the ESP32
Call the below code from the `boot.py` file on the microcontroller or simply run the function using `repl`:
```
def connect_to_wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
```

#### Run custom code upon boot time
In order to run a custom python code upon microcontroller boot time,
first copy the source files onto the microcontroller with `rshell cp <source_file_path> /pyboard` 
and import them in the `boot.py` file.
