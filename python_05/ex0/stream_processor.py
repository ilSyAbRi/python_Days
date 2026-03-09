from abc import ABC, abstractmethod
from typing import Any


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
        total = sum(data)
        count = len(data)

        if count == 0:
            avg = 0
        else:
            avg = total / count

        result = (
                f"Processed {count} numeric values,"
                f" sum={total}, avg={avg}"
        )

        return self.format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) is str

    def process(self, data: Any) -> str:

        num_chars = len(data)
        num_words = len(data.split())

        result = (
            f"Processed text: {num_chars} characters, {num_words} words"
        )

        return self.format_output(result)


class LogProcessor(DataProcessor):
    ALLOWED_LEVELS = ["ERROR", "WARNING", "INFO"]

    def validate(self, data: Any) -> bool:
        return type(data) is str

    def process(self, data: Any) -> str:

        try:
            level, msg = data.split(":", 1)
            level = level.strip()
            msg = msg.strip()
        except ValueError:
            return self.format_output("Error: Malformed log entry")

        if level not in self.ALLOWED_LEVELS:
            return self.format_output("Error: Invalid log level")

        if level == "ERROR":
            result = f"[ALERT] {level} level detected: {msg}"
        elif level == "WARNING":
            result = f"[WARNING] {level} level detected: {msg}"
        else:
            result = f"[INFO] {level} level detected: {msg}"

        return self.format_output(result)


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]

    print("Processing data:", data)
    if processor.validate(data):
        print("Validation: Numeric data verified")
        print(processor.process(data))
    else:
        print("Error: Invalid numeric data")

    print("\nInitializing Text Processor...")
    processor = TextProcessor()
    data = "Hello Nexus World"

    print("Processing data:", f'"{data}"')
    if processor.validate(data):
        print("Validation: Text data verified")
        print(processor.process(data))
    else:
        print("Error: Invalid text data")

    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    log_entry = "ERROR: Connection timeout"

    print("Processing data:", f'"{log_entry}"')
    if log_processor.validate(log_entry):
        print("Validation: Log entry verified")
        print(log_processor.process(log_entry))
    else:
        print("Error: Invalid log data")

    numeric_data = [1, 2, 3]
    text_data = "Hello Nexus"
    log_data = "INFO: System ready"

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_list = [
        numeric_data,
        text_data,
        log_data
    ]

    print("\nProcessing multiple data types through same interface...")

    for i in range(len(processors)):
        result = processors[i].process(data_list[i])
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
