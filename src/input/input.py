#!/usr/bin/env python
# coding=utf-8
from src.conf.config import Setting
from src.input.type import RunningData
from .parser import JsonDataParser, DataParser, ProtoDataParser


class Input:
    _data_parser: DataParser

    def __init__(self, setting: Setting):
        data_parser_type = setting.DATA_PARSER
        print(f'- Initializing input data parser with <{data_parser_type}>')
        if data_parser_type == 'json':
            self._data_parser = JsonDataParser(setting=setting)
        elif data_parser_type == 'proto':
            self._data_parser = ProtoDataParser(setting=setting)
        else:
            raise TypeError(f'Unknown data parser type with <{data_parser_type}>')

    def parse_data(self, input_str: str) -> RunningData:
        return self._data_parser.parse(input_str)
