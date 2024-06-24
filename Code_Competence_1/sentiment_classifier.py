import pandas as pd
import os

class SentimentClassifier:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        csv_path = os.path.join(self.data_path, 'file.csv')
        self.df = pd.read_csv(csv_path)

    def classify_sentiment(self):
        if self.df is None:
            raise Exception("Dataset tidak ada. Jalankan load_data() terlebih dahulu.")
        
        self.df['sentiment_category'] = self.df['labels'].apply(lambda x: 'good' if x == 'positive' else ('bad' if x == 'negative' else 'neutral'))

    def save_to_csv(self):
        if self.df is None:
            raise Exception("Dataset tidak ada. Jalankan load_data() terlebih dahulu.")
        
        data_folder = os.path.join(self.data_path, '..', 'data')
        os.makedirs(data_folder, exist_ok=True)

        for sentiment_category in ['good', 'bad', 'neutral']:
            df_category = self.df[self.df['sentiment_category'] == sentiment_category]
            csv_name = f'sentiment_{sentiment_category}.csv'
            csv_path = os.path.join(data_folder, csv_name)
            
            df_category.to_csv(csv_path, index=False)
    
    def summarize_counts(self):
        if self.df is None:
            raise Exception("Dataset tidak ada. Jalankan load_data() terlebih dahulu.")
        
        counts = self.df['sentiment_category'].value_counts().reset_index()
        counts.columns = ['sentiment_category', 'count']

        data_folder = os.path.join(self.data_path, '..', 'data')
        os.makedirs(data_folder, exist_ok=True)
        
        counts.to_csv(os.path.join(data_folder, 'sentiment_counts.csv'), index=False)

if __name__ == "__main__":
    classifier = SentimentClassifier(data_path='data_source')
    classifier.load_data()
    classifier.classify_sentiment()
    classifier.save_to_csv()
    classifier.summarize_counts()