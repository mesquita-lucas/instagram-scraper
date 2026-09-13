from abc import ABC, abstractmethod
from typing import Any

class Filter(ABC):

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

class DateFilter(Filter):
    def __init__(self):
        super().__init__()

    def process(self, data):
        pass