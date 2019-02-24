#!/usr/bin/env python
# coding=utf-8
from enum import Enum, unique

@unique
class DataType(Enum):
    CPLUSPLUS = 0
    JAVA = 1
    PYTHON2 = 2
    PYTHON3 = 3
    GO = 4
    # print DataType.GO

class Limit():
    def __init__(self, time_limit = 1000, memory_limit = 1024, cpu_num = 1):
        self.TimeLimit = time_limit
        self.MemoryLimit = memory_limit
        self.CpuNum = cpu_num

class InputType():
    def __init__(self):
        return

class Input:
    def __init__(self, req):
        self.data = req.get('Data') # string
        self.data_type = req.get('DataType')
        self.limit = Limit()
        self.input_type = req.get('InputType')


class SpartanContext:
    def __init__(self, req):
        self.input = Input(req)

    def show(self):
        print(self.input.data)