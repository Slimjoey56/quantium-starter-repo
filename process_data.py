import pandas as pd

# --- PART 1: LOAD ALL DATA ---
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

all_dfs = []
# Loop through the files and stack them up
for file in files:
    temp_df = pd.read_csv(file)
    all_dfs.append(temp_df)

# Combine into one big dataframe
df = pd.concat(all_dfs)

# --- PART 2: CLEAN & CALCULATE ---
# Filter for "pink morsel" only
filtered_df = df[df['product'] == 'pink morsel'].copy()

# Clean price (remove "$" and turn into number)
filtered_df['price'] = filtered_df['price'].str.replace('$', '').astype(float)
# --- THE MISSING PART WAS LIKELY HERE ---
# Calculate Sales (Price * Quantity)
filtered_df['sales'] = filtered_df['price'] * filtered_df['quantity']
# Select only the columns we need
final_df = filtered_df[['sales', 'date', 'region']]

# --- PART 3: SAVE THE FILE ---
# This creates the output file expected by the instructions
final_df.to_csv("formatted_data.csv", index=False)

print("Success! File 'formatted_data.csv' has been created.")
