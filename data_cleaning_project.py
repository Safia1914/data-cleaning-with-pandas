# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 02:23:03 2025

@author: pc
"""

import pandas as pd

# Sample raw data
data = {
    'Student': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [20, None, 22, 19, 21],
    'Score': [88, 76, None, 92, 85]
}

# Convert to DataFrame
df = pd.DataFrame(data)
print("📌 Raw Data:\n", df)

# Drop rows with missing values
cleaned_df = df.dropna()
print("\n✅ Cleaned Data:\n", cleaned_df)

# Add grade column
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

cleaned_df['Grade'] = cleaned_df['Score'].apply(assign_grade)

# Summary statistics
print("\n📊 Summary Statistics:\n", cleaned_df.describe())

# Final cleaned data
print("\n🏁 Final Processed Table:\n", cleaned_df)
