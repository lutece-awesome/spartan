from enum import Enum, unique

from ..conf.conf import *


@unique
class DataType(Enum):
    C = 0
    CPP = 1
    JAVA = 2
    PYTHON2 = 3
    PYTHON3 = 4
    GO = 5
    RUBY = 6
    RUST = 7
    JAVASCRIPT = 8
    FILE = 9


# For the default testlib checker, please ref to https://github.com/MikeMirzayanov/testlib/tree/master/checkers
@unique
class CheckerType(Enum):
    WCMP = 0
    CUSTOM = 1


class RunningData:
    # data: str
    # data_type: DataType
    # time_limit: int
    # memory_limit: int
    # cpu_number_limit: int
    # output_limit: int
    # compile_time_limit: int
    # compile_memory_limit: int
    # checker_time_limit: int
    # checker_memory_limit: int
    # checker_type: CheckerType
    # checker_data: str

    def __init__(self,
                 data: str = DEFAULT_DATA,
                 data_type: DataType = DEFAULT_DATA_TYPE,
                 time_limit: int = DEFAULT_TIME_LIMIT,
                 memory_limit: int = DEFAULT_MEMORY_LIMIT,
                 cpu_number_limit: int = DEFAULT_CPU_NUMBER_LIMIT,
                 output_limit: int = DEFAULT_OUTPUT_LIMIT,
                 compile_time_limit: int = DEFAULT_COMPILE_TIME_LIMIT,
                 compile_memory_limit: int = DEFAULT_COMPILE_MEMORY_LIMIT,
                 checker_time_limit: int = DEFAULT_CHECKER_TIME_LIMIT,
                 checker_memory_limit: int = DEFAULT_CHECKER_MEMORY_LIMIT,
                 checker_type: CheckerType = DEFAULT_CHECKER_TYPE,
                 checker_data: str = DEFAULT_CHECKER_DATA) -> None:
        self.data = data
        self.data_type = data_type
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.cpu_number_limit = cpu_number_limit
        self.output_limit = output_limit
        self.compile_time_limit = compile_time_limit
        self.compile_memory_limit = compile_memory_limit
        self.checker_time_limit = checker_time_limit
        self.checker_memory_limit = checker_memory_limit
        self.checker_type = checker_type
        self.checker_data = checker_data
