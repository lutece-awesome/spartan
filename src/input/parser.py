import json
from abc import ABC, abstractmethod

from src.conf.config import DEFAULT_DATA, DEFAULT_DATA_TYPE, DEFAULT_TIME_LIMIT, DEFAULT_CPU_NUMBER_LIMIT, \
    DEFAULT_OUTPUT_LIMIT, DEFAULT_COMPILE_TIME_LIMIT, DEFAULT_COMPILE_MEMORY_LIMIT, DEFAULT_CHECKER_TIME_LIMIT, \
    DEFAULT_CHECKER_MEMORY_LIMIT, DEFAULT_CHECKER_TYPE, DEFAULT_CHECKER_DATA
from .type import RunningData


class DataParser(ABC):

    @staticmethod
    @abstractmethod
    def parse(cls, input_data: str) -> RunningData:
        pass


class JsonDataParser(DataParser):

    @classmethod
    def parse(cls, input_data: str) -> RunningData:
        running_data_json = json.loads(input_data)
        running_data = RunningData(running_data_json.get('data', DEFAULT_DATA),
                                   running_data_json.get('data_type', DEFAULT_DATA_TYPE),
                                   running_data_json.get('time_limit', DEFAULT_TIME_LIMIT),
                                   running_data_json.get('cpu_number_limit', DEFAULT_CPU_NUMBER_LIMIT),
                                   running_data_json.get('output_limit', DEFAULT_OUTPUT_LIMIT),
                                   running_data_json.get('compile_time_limit', DEFAULT_COMPILE_TIME_LIMIT),
                                   running_data_json.get('compile_memory_limit', DEFAULT_COMPILE_MEMORY_LIMIT),
                                   running_data_json.get('checker_time_limit', DEFAULT_CHECKER_TIME_LIMIT),
                                   running_data_json.get('checker_memory_limit', DEFAULT_CHECKER_MEMORY_LIMIT),
                                   running_data_json.get('checker_type', DEFAULT_CHECKER_TYPE),
                                   running_data_json.get('checker_data', DEFAULT_CHECKER_DATA))
        return running_data


class ProtoDataParser(DataParser):

    @staticmethod
    def parse(cls, input_data: str) -> RunningData:
        # TODO(qscqesze): impl it
        pass
