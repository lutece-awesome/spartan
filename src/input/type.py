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

    @classmethod
    def value_of(cls, value: str):
        if value == 'c':
            return cls.C
        elif value == 'cpp':
            return cls.CPP
        elif value == 'java':
            return cls.JAVA
        elif value == 'python2':
            return cls.PYTHON2
        elif value == 'python3':
            return cls.PYTHON3
        elif value == 'go':
            return cls.GO
        elif value == 'ruby':
            return cls.RUBY
        elif value == 'rust':
            return cls.RUST
        elif value == 'javascript':
            return cls.JAVASCRIPT
        elif value == 'file':
            return cls.FILE
        else:
            raise TypeError(f'Unknown checker type with <{value}>')


# For the default testlib checker, please ref to https://github.com/MikeMirzayanov/testlib/tree/master/checkers
@unique
class CheckerType(Enum):
    WCMP = 0
    CUSTOM = 1

    @classmethod
    def value_of(cls, value: str):
        if value == 'wcmp':
            return cls.WCMP
        elif value == 'custom':
            return cls.CUSTOM
        else:
            raise TypeError(f'Unknown checker type with <{value}>')


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

    @classmethod
    def parse(cls, data: str, data_type: str, time_limit: int, memory_limit: int, cpu_number_limit: int,
              output_limit: int, compile_time_limit: int, compile_memory_limit: int, checker_time_limit: int,
              checker_memory_limit: int, checker_type: str, checker_data: str):
        return cls(
            data=data,
            data_type=DataType.value_of(data_type),
            time_limit=time_limit,
            memory_limit=memory_limit,
            cpu_number_limit=cpu_number_limit,
            output_limit=output_limit,
            compile_time_limit=compile_time_limit,
            compile_memory_limit=compile_memory_limit,
            checker_time_limit=checker_time_limit,
            checker_memory_limit=checker_memory_limit,
            checker_type=CheckerType.value_of(checker_type),
            checker_data=checker_data
        )

    def __init__(self, data: str, data_type: DataType, time_limit: int, memory_limit: int, cpu_number_limit: int,
                 output_limit: int, compile_time_limit: int, compile_memory_limit: int, checker_time_limit: int,
                 checker_memory_limit: int, checker_type: CheckerType, checker_data: str) -> None:
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

    def __eq__(self, other):
        return self.data == other.data \
               and self.data_type == other.data_type \
               and self.time_limit == other.time_limit \
               and self.memory_limit == other.memory_limit \
               and self.cpu_number_limit == other.cpu_number_limit \
               and self.output_limit == other.output_limit \
               and self.compile_time_limit == other.compile_time_limit \
               and self.compile_memory_limit == other.compile_memory_limit \
               and self.checker_time_limit == other.checker_time_limit \
               and self.checker_memory_limit == other.checker_memory_limit \
               and self.checker_type == other.checker_type \
               and self.checker_data == other.checker_data
