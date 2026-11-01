from abc import ABC, abstractmethod
from .generate_report import GenerateReport

class CVReportGeneration(ABC):
    def generate_cv_report(self, file_path: str) -> GenerateReport:
        print("Generating CV Report ...")
        raw = self._read_file(file_path)
        extracted = self.extract_data(raw)
        analyzed = self._analyze_data(extracted)
        return self._generate_report(analyzed)


    def _read_file(self, file_path: str) -> bytes:
        print(f"reading file from: {file_path}")
        with open(file_path, "rb") as f:
            return f.read()

    @abstractmethod
    def extract_data(self, raw: bytes) -> dict: ...

    def _analyze_data(self, data: dict) -> dict:
        print("analyzing data....")
        return data

    def _generate_report(self, data: dict) -> GenerateReport:
        print("generate report...")
        return GenerateReport(True)