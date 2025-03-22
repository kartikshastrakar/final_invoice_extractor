import pandas as pd

def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def clean_invoice_data(df):
    if 'invoice_date' in df.columns:
        df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    else:
        print("Warning: 'invoice_date' column not found in DataFrame.")

    if 'amount' in df.columns:
        df['amount'] = df['amount'].replace('[\$,]', '', regex=True).astype(float)
    else:
        print("Warning: 'amount' column not found in DataFrame.")
    return df