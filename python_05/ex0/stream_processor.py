from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def format_output(self, result: str) -> str:
        pass
    def format_output(self, result: str) -> str:
        return f"Output: {result}"

if __name__ == "__main__":
