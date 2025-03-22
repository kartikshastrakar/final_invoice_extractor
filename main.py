import os
from src.extract import extract
from src.summarize import summarize
from src.evaluate import evaluate_extraction, evaluate_summary

# Load sample text invoice
invoice_text = """
Invoice #12345 from XYZ Corp, dated 2024-01-01, with total amount $500.00 and $50.00 tax.
"""

# Ground truth for evaluation
ground_truth = {
    "invoice_id": "12345",
    "company": "XYZ Corp",
    "date": "2024-01-01",
    "total": "500.00",
    "tax": "50.00"
}

# Extracted data and summarized information
extracted_data = extract(invoice_text)
summary = summarize(invoice_text)

print(f"Extracted Data: {extracted_data}")
print(f"Summary: {summary}")

# Convert extracted data and ground truth to list for evaluation
extracted_data_list = list(extracted_data.values())
ground_truth_list = list(ground_truth.values())

# Sanity check: Verify lengths before evaluation
if len(extracted_data_list) != len(ground_truth_list):
    print(f"⚠️ Warning: Mismatched data lengths! Ground truth: {len(ground_truth_list)}, Extracted: {len(extracted_data_list)}")

# Evaluate extraction and summary
extraction_eval = evaluate_extraction([ground_truth_list], [extracted_data_list])
summary_eval = evaluate_summary(" ".join(ground_truth_list), summary)

# Print evaluation results
print(f"Extraction Precision: {extraction_eval:.2f}")
print(f"Summary F1 Score: {summary_eval:.2f}")
