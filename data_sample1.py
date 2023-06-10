x = [1,2,3,4,5,6,7,8,9,10]
print (x)

import pandas as pd

df = pd.DataFrame(x, columns=['Nilai'])
print(df)

#total jumlah
total = df["Nilai"].sum()
print("total jumlah dari seluruh data adalah", total)

data_sample = pd.read_csv("data_sample.csv")
print (data_sample)

total_data = data_sample['x'].sum()
print ("total data adalah", total_data)