from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            for value in data:
                value + 0
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"

        total = sum(data)
        count = len(data)

        if count == 0:
            avg = 0
        else:
            avg = total / count

            result = (
                    f"Validation: Numeric data verified"
                    f"\nProcessed {count} numeric values,"
                    f" sum={total}, avg={avg}"
            )

        return self.format_output(result)

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")

    processor = NumericProcessor()
    data = [1, 2, "a", 4, 5]

    print("Processing data:",data)
    print(processor.process(data))
