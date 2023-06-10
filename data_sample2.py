import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data Sample
data_sample = pd.Series([10, 12, 15, 18, 20])

# Menghitung Total
total = data_sample.sum()
print("Total:", total)

# Menghitung rata-rata
mean_value = data_sample.mean()
print("Rata-rata:", mean_value)

# Menghitung Median
median_value = data_sample.median()
print("Median:", median_value)

# Menghitung Modus
modus_value = data_sample.mode().values[0]
print("Modus:", modus_value)

# Menghitung Nilai Variansi
var_value = data_sample.var()
print("Variansi:", var_value)

# Menghitung Standar Deviasi
sd_value = data_sample.std()
print("Standar Deviasi:", sd_value)

# Menghitung Distribusi Normal > 8.0
mean_dist = 8.704
sd_dist = 2.981218
x_dist = 8
dist_value = 1 - norm.cdf(x_dist, mean_dist, sd_dist)
print("Distribusi Normal > 8.0:", dist_value)

# Membuat Grafik Distribusi Normal
rata_rata = 8.704
standar_deviasi = 2.981218
a = np.arange(-4, 16, 0.01)
b = norm.pdf(a, loc=rata_rata, scale=standar_deviasi)
data = pd.DataFrame({'a': a, 'b': b})

plt.plot(data['a'], data['b'])
plt.xlabel("Rentang sumbu")
plt.ylabel("Densitas Distribusi Normal")
plt.title("Grafik Distribusi Normal")
plt.axvline(x=6, color="blue")
plt.scatter(6, norm.pdf(6, loc=rata_rata, scale=standar_deviasi), color="yellow", marker='o')
plt.fill_between(data['a'], 0, np.where(data['a'] > 6, data['b'], 0), color="darkblue", alpha=0.3)
plt.show()
