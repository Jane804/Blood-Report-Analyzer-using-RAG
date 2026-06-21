from app.services.summary_service import generate_summary

sample_report = """
Hemoglobin: 13.5

LDL Cholesterol: 190

HDL Cholesterol: 55
"""

summary = generate_summary(
    sample_report
)

print(summary)