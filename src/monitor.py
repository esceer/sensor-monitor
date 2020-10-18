import sys
import time

from config.config import Config, DriverLoader
from clients.warehouse_client import WarehouseClient

if __name__ == '__main__':
    try:
        print('Initializing...')
        if len(sys.argv) != 3:
            print('Invalid arguments')
            print('Usage:')
            print('monitor.py <sensor_type> <sensor_name>')
            sys.exit(1)

        sensor_type = sys.argv[1]
        sensor_name = sys.argv[2]

        config = Config(sensor_type)
        driver_loader = DriverLoader(config)
        sensor_driver = driver_loader.get_sensor_driver()
        sensor = sensor_driver(sensor_name)

        warehouse_client = WarehouseClient(config)
        sensor_id = warehouse_client.setup_sensor(sensor.name)

        print('Monitoring sensor \'%s...\'' % sensor.name)
        for i in range(config.get_sensor_measurement_cycle_count()):
            sensor_value = sensor.get_value()
            try:
                warehouse_client.send_sensor_update(sensor_id, sensor_value)
            except Exception as e:
                print(e)
            time.sleep(config.get_sensor_refresh_interval())
    finally:
        print('Shutting down...')