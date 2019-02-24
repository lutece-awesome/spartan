#!/usr/bin/env python
# coding=utf-8
from enum import Enum, unique
import ConfigParser
cf = ConfigParser.ConfigParser()

cf.read('../conf/spartan.config')
@unique
class DataType(Enum):
    CPLUSPLUS = 0
    JAVA = 1
    PYTHON2 = 2
    PYTHON3 = 3
    GO = 4

class Limit():
    def __init__(self, time_limit = cf.get('default', 'DEFAULT_TIMELIMIT'),
                    memory_limit = cf.get('default', 'DEFAULT_MEMORYLIMIT'),
                    cpu_num = cf.get('default', 'DEFAULT_CPUNUM')):
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