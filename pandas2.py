import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('Mcd.csv')

# Step 2: Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 3: Identify missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Fill missing values with mean (for numeric columns only)
df_filled = df.fillna(df.mean(numeric_only=True))

# Step 5: Display updated DataFrame
print("\nDataFrame after filling missing values with mean:")
print(df_filled)
