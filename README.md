# sensor-monitor
Home automation project for collecting and transmitting sensor data. 

### Install
1. python3 -m venv venv
2. venv/bin/pip install -r requirements.txt

### Usage
##### Via shell script
bin/monitor_<*sensor_type*>_sensor.sh <*sensor_name*>

##### Directly via python3
venv/bin/python3 monitor.py <*sensor_type*> <*sensor_name*>

### Supported sensor type(s)
* **tsl2591**

### Timing
Crontab is used to schedule a full reboot of the application *(every 5 minutes)*
which initiates the sensors to synchronize with the backend.
Between these synchronization points, the application sends the current sensor state
to the backend every 30 seconds.<br/>
The timing properties can be modified in the **bin/sm.ini** file.
