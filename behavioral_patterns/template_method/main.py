from .pdf_report_generation import PDFReportGeneration
from .word_report_generation import WordReportGeneration

pdf = PDFReportGeneration()
pdf.generate_cv_report(file_path="template_method/file.pdf")

word = WordReportGeneration()
word.generate_cv_report(file_path="template_method/file.docx")