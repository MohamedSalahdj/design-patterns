from .cv_report_generation import CVReportGeneration


class WordReportGeneration(CVReportGeneration):
    def extract_data(self, raw: bytes) -> dict:
            print("Extracting Word File ...")
            return {}