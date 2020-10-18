class WarehouseClient:
    from config.config import Config

    def __init__(self, connection_params: Config):
        import requests
        self._requests = requests
        self._connection_params = connection_params

    def setup_sensor(self, sensor_name: str) -> str:
        fetch_response = self._requests.get(self._get_fetch_by_name_url(sensor_name))
        try:
            return ResponseParser.gather_sensor_id_from_response(fetch_response)
        except ValueError:
            create_response = self._requests.post(self._get_setup_sensor_url(sensor_name))
            return ResponseParser.gather_sensor_id_from_response(create_response)

    def send_sensor_update(self, sensor_id: str, sensor_state: str):
        self._requests.put(self._get_update_state_url(sensor_id, sensor_state))

    def _get_fetch_by_name_url(self, sensor_name: str) -> str:
        return self._get_base_path() + '/name/%s' % sensor_name

    def _get_setup_sensor_url(self, sensor_name: str) -> str:
        return self._get_base_path() + '/%s/state/init' % sensor_name

    def _get_update_state_url(self, sensor_id: str, sensor_state: str) -> str:
        return self._get_base_path() + '/%s/state/%s' % (
            sensor_id,
            sensor_state
        )

    def _get_base_path(self) -> str:
        return 'http://%s:%s/sensors' % (
            self._connection_params.get_warehouse_host(),
            self._connection_params.get_warehouse_port()
        )


class ResponseParser:
    from requests import Response

    @staticmethod
    def gather_sensor_id_from_response(response: Response) -> str:
        json = response.json()
        if 'id' in json:
            return json.get('id')
        else:
            raise ValueError('Sensor name cannot be gathered from response: %s' % json)
