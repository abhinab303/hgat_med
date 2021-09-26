data_dir = "/content/drive/MyDrive/hgat_med/hgat_med/data"
data_path = "/content/drive/MyDrive/hgat_med/hgat_med/data/2021MergedEnglish.csv"

import pandas as pd
import numpy as np

df = pd.read_csv(data_path)
print(f'columns: {df.columns} ... Shape: {df.shape}')

from bertopic import BERTopic
topic_model = BERTopic()

docs = df.loc[:,['Record - subjective']]
print(f'fitting topic model')
topics, probs = topic_model.fit_transform(docs['Record - subjective'])
print(f'saving topic model')
model_path = "/content/drive/MyDrive/hgat_med/hgat_med/model/bertopic"
topic_model.save(model_path)
