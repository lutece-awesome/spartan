import unittest

from src.conf.config import Setting
from src.input.module import Input
from src.input.type import RunningData, DataType, CheckerType


class TestJsonParser(unittest.TestCase):
    mock_settings: Setting

    def setUp(self):
        self.mock_settings = Setting
        self.mock_settings.DATA_PARSER = 'json'

    def test_right_json_parse(self):
        json_str = '''
        {
            "data": "Hello Word",
            "data_type" : "c",
            "time_limit": 1234,
            "memory_limit": 64,
            "cpu_number_limit": 1,
            "output_limit": 55,
            "compile_time_limit": 1111,
            "compile_memory_limit": 66,
            "checker_time_limit": 3200,
            "checker_memory_limit": 67,
            "checker_type": "custom",
            "checker_data": "123"
        }            
        '''
        result = Input(setting=self.mock_settings).parse_data(json_str)
        self.assertEqual(result, RunningData(
            data="Hello Word",
            data_type=DataType.C,
            time_limit=1234,
            memory_limit=64,
            cpu_number_limit=1,
            output_limit=55,
            compile_time_limit=1111,
            compile_memory_limit=66,
            checker_time_limit=3200,
            checker_memory_limit=67,
            checker_type=CheckerType.CUSTOM,
            checker_data="123"
        ))

    def test_json_parse_with_wrong_data_type(self):
        json_str = '''
        {
            "data": "Hello Word",
            "data_type" : "c--",
            "time_limit": 1234,
            "memory_limit": 64,
            "cpu_number_limit": 1,
            "output_limit": 55,
            "compile_time_limit": 1111,
            "compile_memory_limit": 66,
            "checker_time_limit": 3200,
            "checker_memory_limit": 67,
            "checker_type": "custom",
            "checker_data": "123"
        }            
        '''
        try:
            Input(setting=self.mock_settings).parse_data(json_str)
            assert False
        except TypeError:
            pass
