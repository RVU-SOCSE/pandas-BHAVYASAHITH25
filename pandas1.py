import pandas as pd

# Step 1: Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [80, 75, 90, 85]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 4: Add a new column (e.g., Marks increased by 10%)
df['Updated Marks'] = df['Marks'] * 1.10

# Step 5: Display updated DataFrame
print("\nDataFrame after adding new column:")
print(df)
