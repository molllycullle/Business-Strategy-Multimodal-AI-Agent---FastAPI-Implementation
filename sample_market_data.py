import pandas as pd
import numpy as np

# Generate market data
dates = pd.date_range(start="2024-01-01", end="2024-12-31")
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Furniture", "Groceries"]

# Expanded data with random sales and units sold
market_data = pd.DataFrame({
    "Date": np.tile(dates, len(regions) * len(categories)),
    "Region": np.repeat(regions, len(dates) * len(categories)),
    "Product_Category": np.tile(np.repeat(categories, len(dates)), len(regions)),
    "Sales": (1500 * np.random.rand(len(dates) * len(regions) * len(categories))).round(2),
    "Units_Sold": np.random.randint(1, 50, len(dates) * len(regions) * len(categories))
})

# Save to CSV
market_data.to_csv("sample_market_data.csv", index=False)
print("Market data saved to sample_market_data.csv")
