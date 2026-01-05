import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filtered_df = customers[~customers["id"].isin(orders["customerId"])]

    return filtered_df[["name"]].rename(columns={"name": "Customers"})
