import streamlit as st
import pandas as pd
import json
from src.extract import extract
from src.summarize import summarize

# 🎯 Streamlit UI Title
st.set_page_config(page_title="LLM Invoice Extractor", layout="wide")
st.title("📄 LLM Invoice Extractor & Summarizer")

# 📤 Upload File Section
uploaded_file = st.file_uploader("Upload Invoice File (CSV)", type=["csv"])

# ✅ Process the file if uploaded
if uploaded_file is not None:
    # Read CSV into DataFrame
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("🔍 Uploaded CSV Preview")
    st.dataframe(df.head(5))

    # Process and show each row dynamically
    st.subheader("✅ Processed Rows in JSON Format")

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # Create invoice text dynamically from row data
        invoice_text = f"""
        Invoice Date: {row['invoice_date']}
        Name: {row['first_name']} {row['last_name']}
        Email: {row['email']}
        Address: {row['address']}
        City: {row['city']}
        Product ID: {row['product_id']}
        Quantity: {row['qty']}
        Amount: {row['amount']}
        Stock Code: {row['stock_code']}
        Job: {row['job']}
        """

        # Extract and summarize the invoice
        extracted_data = extract(invoice_text)
        summary = summarize(invoice_text)

        # Prepare processed row with extracted data and summary
        processed_row = {
            "invoice_date": row["invoice_date"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "email": row["email"],
            "address": row["address"],
            "city": row["city"],
            "product_id": row["product_id"],
            "qty": row["qty"],
            "amount": row["amount"],
            "stock_code": row["stock_code"],
            "job": row["job"],
            "extracted_data": extracted_data,
            "summary": summary
        }

        # 🎯 Display JSON side by side (Two columns)
        col1, col2 = st.columns(2)

        with col1:
            st.json({"🧠 Extracted Data": extracted_data})

        with col2:
            st.json({"📝 Summary": summary})

    st.success("✅ All rows processed successfully!")

else:
    st.warning("⚠️ Please upload a valid CSV file to proceed.")
