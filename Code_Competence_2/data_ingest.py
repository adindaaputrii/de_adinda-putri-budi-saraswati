import pandas as pd
import os
import numpy as np
import pyarrow.parquet as pq

class DataLakeBuilder:
    def __init__(self):
        pass

    def read_csv_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            print(f"Data {file_path} loaded successfully.")
            return df
        except FileNotFoundError:
            print(f"File {file_path} not found!")
            return None

    def handle_missing_values(self, df):
        #numerik digantikan median, kategorikal digantikan mode
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna(df[col].median(), inplace=True)
            return df

    def handle_outliers(self, df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df.loc[(df[column] < lower_bound) | (df[column] > upper_bound), column] = np.nan
        df = self.handle_missing_values(df)
        return df

    def save_to_parquet(self, df, file_name):
        try:
            processed_data_dir = 'processed_data'
            if not os.path.exists(processed_data_dir):
                os.makedirs(processed_data_dir)

            file_path = os.path.join(processed_data_dir, file_name + '.parquet')
            df.to_parquet(file_path, index=False)
            print(f"Data saved on {file_path} successfully.")
        except Exception as err:
            print(f"Failed to save data to parquet: {str(err)}")


    def validate_data(self, file_path):
        try:
            table = pq.read_table(file_path)
            df = table.to_pandas()
            print(f"Summary of data on {file_path}: ")
            print(df.head())
            print(df.describe())
        except FileNotFoundError:
            print(f"File {file_path} not found!")
        except Exception as err:
            print(f"Failed to validate data: {str(err)}")

if __name__ == "__main__":
    builder = DataLakeBuilder()

    events_df = builder.read_csv_data('data_source/events.csv')
    if events_df is not None:
        events_df = builder.handle_missing_values(events_df)  
        builder.save_to_parquet(events_df, 'events')
        builder.validate_data('processed_data/events.parquet')

    customers_df = builder.read_csv_data('data_source/customers.csv')
    if customers_df is not None:
        customers_df = builder.handle_missing_values(customers_df)
        builder.save_to_parquet(customers_df, 'customers')
        builder.validate_data('processed_data/customers.parquet')

    customer_feedback_df = builder.read_csv_data('data_source/customer_feedback.csv')
    if customer_feedback_df is not None:
        customers_df = builder.handle_missing_values(customer_feedback_df)
        builder.save_to_parquet(customer_feedback_df, 'customer_feedback')
        builder.validate_data('processed_data/customer_feedback.parquet')

    tickets_df = builder.read_csv_data('data_source/tickets.csv')
    if tickets_df is not None:
        tickets_df = builder.handle_missing_values(tickets_df)
        builder.save_to_parquet(tickets_df, 'tickets')
        builder.validate_data('processed_data/tickets.parquet')

    transactions_df = builder.read_csv_data('data_source/transactions.csv')
    if transactions_df is not None:
        transactions_df = builder.handle_missing_values(transactions_df)
        transactions_df = builder.handle_outliers(transactions_df, 'total_amount')  
        builder.save_to_parquet(transactions_df, 'transactions')
        builder.validate_data('processed_data/transactions.parquet')