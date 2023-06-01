import pandas as pd

df = pd.read_csv('./lyrics_test.csv')
print(df.shape)
print([x for x in df['lyrics'][0:1]])
