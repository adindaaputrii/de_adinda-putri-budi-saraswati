import pandas as pd
import os
from google.cloud import storage
from datetime import datetime

class DataWarehouseLoader:
    def __init__(self, bucket_name):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\ALTERRA\cc2-key.json'
        self.bucket_name = bucket_name
        self.storage_client = storage.Client()
        self.bucket = self. storage_client.bucket(self.bucket_name)

    def load_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df):
        transactions_tickets = pd.merge(df['transactions'], df['tickets'], on='ticket_id', how='inner')
        combined_data = pd.merge(transactions_tickets, df['events'], on='event_id', how='inner')
        
        tickets_sold_per_event = combined_data.groupby(['event_id', 'name']).agg({'quantity': 'sum'}).reset_index()
        
        revenue_per_event = combined_data.groupby(['event_id', 'name']).agg({'total_amount': 'sum'}).reset_index()

        cust_feedback_analysis = pd.merge(df['customer_feedback'], df['transactions'], on='transaction_id', how='inner')
        
        if 'event_id' in combined_data.columns:
            cust_feedback_analysis = pd.merge(cust_feedback_analysis, combined_data[['transaction_id', 'event_id', 'name']], on='transaction_id', how='inner')
            rating_per_event = cust_feedback_analysis.groupby(['event_id', 'name']).agg({'rating': 'mean'}).reset_index()
        else:
            print("Error: 'event_id' column not found in cust_feedback_analysis after merge.")
            cust_feedback_analysis = None

        return{
            'tickets_sold_per_event': tickets_sold_per_event,
            'revenue_per_event': revenue_per_event,
            'cust_feedback_analysis': cust_feedback_analysis
        }

    def save_to_warehouse(self, df, table_name):
        if df is not None:
            current_date = datetime.now().strftime('%Y-%m-%d')
            folder_path = current_date.replace('-', '/')
            folder_path = current_date
            filename = f"{table_name}.parquet"
            full_path = f"{folder_path}/{filename}"
        
            blob = self.bucket.blob(full_path)
            df.to_parquet(f"gs://{self.bucket_name}/{full_path}", index=False)
            print(f"Data saved to gs://{self.bucket_name}/{full_path} successfully.")


if __name__ == "__main__":
    loader = DataWarehouseLoader(bucket_name='cc-2')

    data_files = {
        'events': r'D:\data-engineer\Code_Competence_2\processed_data\events.parquet',
        'customers': r'D:\data-engineer\Code_Competence_2\processed_data\customers.parquet',
        'tickets': r'D:\data-engineer\Code_Competence_2\processed_data\tickets.parquet',
        'transactions': r'D:\data-engineer\Code_Competence_2\processed_data\transactions.parquet',
        'customer_feedback': r'D:\data-engineer\Code_Competence_2\processed_data\customer_feedback.parquet'
    }

    df = {}

    for key, path in data_files.items():
        df[key] = loader.load_data(path)

    transformed_data = loader.transform_data(df)

    loader.save_to_warehouse(transformed_data['tickets_sold_per_event'], 'tickets_sold_per_event')
    loader.save_to_warehouse(transformed_data['revenue_per_event'], 'revenue_per_event')
    loader.save_to_warehouse(transformed_data['cust_feedback_analysis'], 'cust_feedback_analysis')