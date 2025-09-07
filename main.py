import numpy as np
import pandas as pd

train_data_fp = r'C:\Users\thebi\house-prices-ml-project\data\train.csv'
df_train = pd.read_csv(train_data_fp)
print(df_train.describe())
print(df_train.head())


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
