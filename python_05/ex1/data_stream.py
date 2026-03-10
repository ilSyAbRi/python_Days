from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

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
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch):
        readings = len(data_batch)
        temp = data_batch["temp"]
        return f"Sensor analysis: {readings} readings processed, avg temp: {temp:.1f}°C"

    def get_stats(self):
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch):
        buy_total = 0
        sell_total = 0

        for op, value in data_batch:
            if op == "buy":
                buy_total += value
            elif op == "sell":
                sell_total += value

        net_flow = sell_total - buy_total
        return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: {net_flow:+} units"
            )

    def get_stats(self):
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch):
        events = len(data_batch)
        errors = data_batch.count("error")

        return f"Event analysis: {events} events, {errors} error detected"

    def get_stats(self):
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


def main():
    
    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")

    data_batch = {
        "temp": 22.5,
        "humidity": 65,
        "pressure": 1013
    }

    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing sensor batch:", data_batch)

    print(sensor.process_batch(data_batch))

    
    print("\nInitializing Transaction Stream...")
    transaction_data = [("buy", 100), ("sell", 150), ("buy", 75)]

    transaction_stream = TransactionStream("TRANS_001")

    stats = transaction_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing transaction batch:", transaction_data)
    print(transaction_stream.process_batch(transaction_data))

    print("\nInitializing Event Stream...")

    event_data = ["login", "error", "logout"]

    event_stream = EventStream("EVENT_001")

    stats = event_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")

    print("Processing event batch:", event_data)

    print(event_stream.process_batch(event_data))


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    main()
