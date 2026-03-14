from abc import ABC, abstractmethod
from typing import Any, Protocol, Union, List
from collections import defaultdict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def process(self, data: Any) -> Any:
    print("Transform: Input validation and parsing")

    try:
        if not isinstance(data, dict):
            raise TypeError("Expected dict for JSON input")

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

        except Exception as e:
            print(f"Error detected in InputStage: {e}")
            print("Recovery: passing data as-is to next stage")

        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        pass


class OutputStage:
    def process(self, data: Any) -> Any:
        pass


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
        print("Input:", data)
        result = self.run_stages(data):
        return result


class CSVAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        print("Input:", data)
        result = self.run_stages(data):
        return result


class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        print("Input:", data)
        result = self.run_stages(data):
        return result


class NexusManager:

    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline):
        pass

    def run_all(self, data_list: List[Any]):
        pass

    def chain(self, pipelines: List[ProcessingPipeline], data: Any):
        pass


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print("\n=== Multi-Format Data Processing ===")
