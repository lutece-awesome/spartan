import json
from abc import ABC, abstractmethod

from src.conf.config import Setting
from .type import RunningData


class DataParser(ABC):
    setting: Setting

    def __init__(self, setting: Setting):
        self.setting = setting

    @abstractmethod
    def parse(self, input_data: str) -> RunningData:
        pass


class JsonDataParser(DataParser):

    def parse(self, input_data: str) -> RunningData:
        running_data_json = json.loads(input_data)
        setting = self.setting
        running_data = RunningData.parse(data=running_data_json.get('data', setting.DEFAULT_DATA),
                                         data_type=running_data_json.get('data_type', setting.DEFAULT_DATA_TYPE),
                                         time_limit=running_data_json.get('time_limit', setting.DEFAULT_TIME_LIMIT),
                                         memory_limit=running_data_json.get('memory_limit', setting.DEFAULT_MEMORY_LIMIT),
                                         cpu_number_limit=running_data_json.get('cpu_number_limit',
                                                                                setting.DEFAULT_CPU_NUMBER_LIMIT),
                                         output_limit=running_data_json.get('output_limit',
                                                                            setting.DEFAULT_OUTPUT_LIMIT),
                                         compile_time_limit=running_data_json.get('compile_time_limit',
                                                                                  setting.DEFAULT_COMPILE_TIME_LIMIT),
                                         compile_memory_limit=running_data_json.get('compile_memory_limit',
                                                                                    setting.DEFAULT_COMPILE_MEMORY_LIMIT),
                                         checker_time_limit=running_data_json.get('checker_time_limit',
                                                                                  setting.DEFAULT_CHECKER_TIME_LIMIT),
                                         checker_memory_limit=running_data_json.get('checker_memory_limit',
                                                                                    setting.DEFAULT_CHECKER_MEMORY_LIMIT),
                                         checker_type=running_data_json.get('checker_type',
                                                                            setting.DEFAULT_CHECKER_TYPE),
                                         checker_data=running_data_json.get('checker_data',
                                                                            setting.DEFAULT_CHECKER_DATA))
        return running_data


class ProtoDataParser(DataParser):

    def parse(self, input_data: str) -> RunningData:
        # TODO(qscqesze): impl it
        pass
