#!/usr/bin/env python
# coding=utf-8

# 该文件是存储传递上下文类的信息
from enum import Enum, unique

class DataType(Enum):
    CPLUSPLUS = 0
    JAVA = 1
    PYTHON = 2
    GO = 3
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
    def __init__(self):
        self.data = '' # string
        self.data_type = 0
        self.limit = Limit()



class SpartanContext:
    def __init__(self):
        input = Input()