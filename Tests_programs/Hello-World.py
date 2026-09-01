import pandas as pd

print("Pandas version:", pd.__version__)

# Simple test DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [90, 85, 95]
})

print(df)
print("\nAverage score:", df["Score"].mean())