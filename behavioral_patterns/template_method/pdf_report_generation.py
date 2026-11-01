from .cv_report_generation import CVReportGeneration


class PDFReportGeneration(CVReportGeneration):
    def extract_data(self, raw: bytes) -> dict:
        print("Extracting PDF File ...")
        return {}