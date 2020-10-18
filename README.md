# sensor-data-producer
Home automation project for collecting and transmitting sensor data. 

### Install
python3 -m venv venv
venv/bin/pip install -r requirements.txt

### Usage
##### Via shell script
bin/monitor_<sensor_type>_sensor.sh

##### Directly via python3
venv/bin/python3 monitor.py <*sensor_type*> <*sensor_name*>

### Supported sensor type(s)
* tsl2591

