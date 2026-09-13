from abc import ABC, abstractmethod
from typing import Any

class Exporter(ABC):

    @abstractmethod
    def add(self) -> Any:
        pass

    @abstractmethod
    def save(self) -> Any:
        pass