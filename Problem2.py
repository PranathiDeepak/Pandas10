import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales_1 = daily_sales.groupby(['date_id','make_name'])[['lead_id','partner_id']].nunique().reset_index()
    return daily_sales_1.rename(columns = {'lead_id':'unique_leads','partner_id':'unique_partners'})