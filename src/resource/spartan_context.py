#!/usr/bin/env python
# coding=utf-8
from enum import Enum, unique
from typing import List

from ..conf.conf import *


@unique
class DataType(Enum):
    CPLUSPLUS = 0
    JAVA = 1
    PYTHON2 = 2
    PYTHON3 = 3
    GO = 4


class Limit:
    def __init__(self, time_limit=DEFAULT_TIMELIMIT,
                 memory_limit=DEFAULT_MEMORYLIMIT,
                 cpu_num=DEFAULT_CPUNUM):
        # type: (List(str), dict) -> None
        self.TimeLimit = time_limit
        self.MemoryLimit = memory_limit
        self.CpuNum = cpu_num


class InputType():
    def __init__(self):
        # type: (List(str), dict) -> None
        return


class Input:
    def __init__(self, req):
        # type: (List(str), dict) -> None
        self.data = req.get('Data')  # string
        self.data_type = req.get('DataType')
        self.limit = Limit()
        self.input_type = req.get('InputType')


class SpartanContext:
    def __init__(self, req):
        # type: (List(str), dict) -> None
        self.input = Input(req)

    def show(self):
        # type: (List(str), dict) -> None
        print(self.input.data)
