import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        products = ('product',lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    return activities.sort_values(by = ['sell_date'])