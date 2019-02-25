#!/usr/bin/env python
# coding=utf-8
from .parser import JsonDataParser


class Input:
    def __init__(self):
        self.json_data_parser = JsonDataParser()
        return

    def input(self, req):
        # type: (List[str], str) -> RunningData
        # todo
        running_data = self.json_data_parser.parse(req)
        return running_data
