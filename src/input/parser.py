from abc import ABC, abstractmethod

from .type import RunningData


class DataParser(ABC):

    @staticmethod
    @abstractmethod
    def parse(cls, input_data: str) -> RunningData:
        pass


class JsonDataParser(DataParser):

    @staticmethod
    def parse(cls, input_data: str) -> RunningData:
        # TODO(keshen): impl it
        pass


class ProtoDataParser(DataParser):

    @staticmethod
    def parse(cls, input_data: str) -> RunningData:
        # TODO(qscqesze): impl it
        pass
