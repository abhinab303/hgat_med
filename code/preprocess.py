data_dir = "/content/drive/MyDrive/hgat_med/hgat_med/data"
data_path = "/content/drive/MyDrive/hgat_med/hgat_med/data/2021MergedEnglish.csv"

import pandas as pd
import numpy as np

df = pd.read_csv(data_path)
print(df.head())