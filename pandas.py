import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 90, 78],
    'Age': [20, 21, 19]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df['Updated Marks'] = df['Marks'] + 5
print("\nDataFrame after adding new column:")
print(df)
