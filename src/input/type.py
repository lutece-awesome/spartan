from enum import Enum, unique


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
    data: str
    data_type: DataType
    time_limit: int
    memory_limit: int
    cpu_number_limit: int
    output_limit: int
    compile_time_limit: int
    compile_memory_limit: int
    checker_time_limit: int
    checker_memory_limit: int
    checker_type: CheckerType
    checker_data: str

    def __init__(self, data: str, data_type: DataType, time_limit: int, memory_limit: int, cpu_number_limit: int,
                 output_limit: int, compile_time_limit: int, compile_memory_limit: int, checker_time_limit: int,
                 checker_memory_limit: int, checker_type: CheckerType,
                 checker_data: str) -> None:
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
