import numpy as np

np.random.seed(42)

#100 random numbers
arr = np.random.randint(0, 100, size=100)
print("100 random numbers:\n", arr)

#find numbers divisible by 3
mask = arr % 3 == 0

#replace them with -1
arr[mask] = -1
print("\nnumbers divisible by 3, and replace them with -1:\n", arr)

#5x5 matrix
matrix = np.random.randint(0, 100, size=(5, 5))
print("5x5 matrix:\n", matrix)

#alternate row
alternate_rows = matrix[::2]

print("\nEvery alternate row:\n", alternate_rows)

#10x10 random integer matrix
matrix_10x10 = np.random.randint(0, 100, size=(10, 10))
print("10x10 matrix:\n", matrix_10x10)

#sort by first column
sorted_matrix = matrix_10x10[np.argsort(matrix_10x10[:, 0])]  # Sort by first column

print("\nMatrix sorted by first column:\n", sorted_matrix)

import numpy as np

np.random.seed(42)

#synthetic daily rainfall data
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)

#100 dry days
rainfall[np.random.choice(365, 100, replace=False)] = 0



#Boolean Arrays & Masks (Section 2.06)

print("\n1.Boolean Arrays & Masks\n")

# 1.1 Basic Rainy Day Count: Count days with rainfall > 0 mm
rainy_days = rainfall > 0
num_rainy_days = np.sum(rainy_days)
print(f"Number of rainy days: {num_rainy_days}")

# 1.2 Heavy Rain Days: Percentage of days with rainfall > 5 mm
heavy_rain_days = rainfall > 5
percent_heavy_rain = (np.sum(heavy_rain_days) / len(rainfall)) * 100
print(f"Percentage of heavy rain days (>5 mm): {percent_heavy_rain:.2f}%")

# 1.3 Dry Spells: Longest consecutive sequence of dry days (rainfall == 0)
is_dry = rainfall == 0
# Find lengths of consecutive dry days
from itertools import groupby
dry_spells = [sum(1 for _ in g) for k, g in groupby(is_dry) if k]
longest_dry_spell = max(dry_spells) if dry_spells else 0
print(f"Longest dry spell (days): {longest_dry_spell}")



#Fancy Indexing (Section 2.07)

print("\n2.Fancy Indexing")

# 2.1 Top Rainfall Days
top_10_indices = np.argsort(rainfall)[-10:][::-1]
top_10_rainfall = rainfall[top_10_indices]
print("Top 10 wettest days (mm):", top_10_rainfall)

# 2.2 Monthly Averages: Average monthly rainfall
month_days = np.array_split(rainfall, 12)
monthly_averages = np.array([month.mean() for month in month_days])
print("Monthly average rainfall (mm):", monthly_averages)



#Sorting (Section 2.08)

print("\n3.Sorting")

# 3.1 Sort rainfall data and find median
sorted_rainfall = np.sort(rainfall)
median_rainfall = np.median(rainfall)
print(f"Median rainfall (mm): {median_rainfall:.2f}")

# 3.2 Percentile Analysis: 90th percentile
percentile_90 = np.percentile(rainfall, 90)
print(f"90th percentile rainfall (mm): {percentile_90:.2f}")



#Structured Data (Section 2.09)

print("\n4.Structured Data")

# 4.1 Creating a Structured Array
structured_rainfall = np.zeros(365, dtype=[('day', 'i4'), ('rainfall', 'f4'), ('is_rainy', 'bool')])
structured_rainfall['day'] = np.arange(1, 366)
structured_rainfall['rainfall'] = rainfall
structured_rainfall['is_rainy'] = rainfall > 0

# 4.2 Filtering Data: Extract rainy days and compute average rainfall
rainy_structured = structured_rainfall[structured_rainfall['is_rainy']]
average_rainy_rainfall = rainy_structured['rainfall'].mean()
print(f"Average rainfall on rainy days (mm): {average_rainy_rainfall:.2f}")

# 4.3 Sorting Structured Data: Top 5 rainiest days
sorted_structured = np.sort(structured_rainfall, order='rainfall')[::-1]
top_5_rainiest = sorted_structured[:5]
print("Top 5 rainiest days:")
print(top_5_rainiest)
