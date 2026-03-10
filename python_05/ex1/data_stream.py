from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Tuple


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [x for x in data_batch if criteria in str(x)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: Dict[str, float]) -> str:
        try:
            if not isinstance(data_batch, dict):
                raise TypeError("Sensor data must be a dictionary")

            readings: int = len(data_batch)
            temp: float = data_batch["temp"]

            return f"Sensor analysis: {readings} readings processed, avg temp: {temp:.1f}°C"

        except (TypeError, KeyError) as e:
            return f"Sensor processing error: {e}"

    def get_stats(self) -> Dict[str, str]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Tuple[str, int]]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Transaction batch must be a list")

            buy_total: int = 0
            sell_total: int = 0

            for op, value in data_batch:
                if op == "buy":
                    buy_total += value
                elif op == "sell":
                    sell_total += value

            net_flow: int = buy_total - sell_total
            return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: {net_flow:+} units"
            )

        except TypeError as e:
            return f"Transaction processing error: {e}"

    def get_stats(self) -> Dict[str, str]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Event batch must be a list")

            events: int = len(data_batch)
            errors: int = data_batch.count("error")

            return f"Event analysis: {events} events, {errors} error detected"

        except TypeError as e:
            return f"Event processing error: {e}"

    def get_stats(self) -> Dict[str, str]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


def main():

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")

    data_batch: Dict[str, float] = {
        "temp": 22.5,
        "humidity": 65,
        "pressure": 1013
    }

    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing sensor batch:", data_batch)

    print(sensor.process_batch(data_batch))


    print("\nInitializing Transaction Stream...")
    transaction_data: List[Tuple[str, int]] = [("buy", 100), ("sell", 150), ("buy", 75)]

    transaction_stream = TransactionStream("TRANS_001")

    stats = transaction_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing transaction batch:", transaction_data)
    print(transaction_stream.process_batch(transaction_data))


    print("\nInitializing Event Stream...")

    event_data: List[str] = ["login", "error", "logout"]

    event_stream = EventStream("EVENT_001")

    stats = event_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing event batch:", event_data)

    print(event_stream.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    
    print("\nBatch 1 Results:")
    streams: List[DataStream] = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002")
    ]

    batches: List[Any] = [
        {"temp": 20.0, "humidity": 70},
        [("buy", 50), ("sell", 120), ("sell", 40), ("buy", 10)],
        ["login", "login", "error"]
    ]

    for stream, batch in zip(streams, batches):
        try:
            result = stream.process_batch(batch)
            print(result)
        except Exception as e:
            print("Batch processing failed:", e)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    main()
