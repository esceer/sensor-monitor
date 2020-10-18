import configparser


class Config:
    def __init__(self, sensor_type: str):
        self._config_file_path = '../resources/sm.ini'
        self._config = self._parse_config_file()
        self._sensor_type = sensor_type

    def get_warehouse_host(self) -> str:
        return self._config['Warehouse']['host']

    def get_warehouse_port(self) -> str:
        return self._config['Warehouse']['port']

    def get_sensor_module(self) -> str:
        return self._config[self._sensor_type]['module']

    def get_sensor_driver(self) -> str:
        return self._config[self._sensor_type]['driver']

    def get_sensor_refresh_interval(self) -> int:
        return int(self._config[self._sensor_type]['refresh-interval-seconds'])

    def _parse_config_file(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self._config_file_path)
        return config


class DriverLoader:
    def __init__(self, config: Config):
        self._config = config

    def get_sensor_driver(self):
        from importlib import import_module
        sensor_module = import_module(self._config.get_sensor_module())
        return getattr(sensor_module, self._config.get_sensor_driver())
