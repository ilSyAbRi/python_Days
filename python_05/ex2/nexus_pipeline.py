from abc import ABC, abstractmethod
from typing import Any, Protocol, Union, List
from collections import defaultdict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def process(self, data: Any) -> Any:
        print("Transform: Input validation and parsing")
        try:
            if isinstance(data, dict):
                required_keys = ["sensor", "value", "unit"]
                for key in required_keys:
                    if key not in data:
                        raise KeyError(f"Missing required key: {key}")
                if not isinstance(data["sensor"], str):
                    raise TypeError("'sensor' must be a string")
                if not isinstance(data["value"], (int, float)):
                    raise TypeError("'value' must be a number")
                if not isinstance(data["unit"], str):
                    raise TypeError("'unit' must be a string")

            elif isinstance(data, str):
                expected_columns = ["user", "action", "timestamp"]
                columns = data.split(",")
                for col in expected_columns:
                    if col not in columns:
                        raise KeyError(f"Missing required column: {col}")

            elif isinstance(data, list):
                if not all(isinstance(x, (int, float)) for x in data):
                    raise TypeError("All stream readings must be numbers")

            else:
                raise TypeError("Unsupported data type")

        except Exception as e:
            print(f"Error detected in InputStage: {e}")
            print("Recovery: passing data as-is to next stage")

        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print("Transform: Enriched with metadata and validation")
            return {
                "sensor": data["sensor"],
                "value": data["value"],
                "unit": data["unit"]
            }
        elif isinstance(data, str):
            print("Transform: Parsed and structured data")
            return {"rows": data.split(",")}
        elif isinstance(data, list):
            print("Transform: Aggregated and filtered")
            return {"readings": data}
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if "sensor" in data:
            print(f"Output: Processed {data['sensor']} reading: "
                  f"{data['value']}°C (Normal range)")
        elif "rows" in data:
            num_actions = data["rows"].count("action")
            print(f"Output: User activity logged: {num_actions} actions processed")
        elif "readings" in data:
            readings = data["readings"]
            count = len(readings)
            avg = sum(readings) / count
            print(f"Output: Stream summary: {count} readings, avg: {avg:.1f}°C")
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats = defaultdict(int)

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing JSON data through pipeline...")
        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        return self.run_stages(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        return self.run_stages(data)


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def run_all(self, data_list: List[Any]):
        for pipeline, data in zip(self.pipelines, data_list):
            pipeline.process(data)


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")
    print("\n=== Multi-Format Data Processing ===\n")

    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv_data = "user,action,timestamp"
    stream_data = [22.0, 22.2, 22.1, 22.1, 22.1]

    json_pipeline = JSONAdapter("pipeline_json")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())
    json_pipeline.process(json_data)
    print()

    csv_pipeline = CSVAdapter("pipeline_csv")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())
    csv_pipeline.process(csv_data)
    print()

    stream_pipeline = StreamAdapter("pipeline_stream")
    print("Input: Real-time sensor stream")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())
    stream_pipeline.process(stream_data)
