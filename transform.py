def transform(df):
    print("Transforming data...")

    # dim_customers
    dim_customers = df[['Customer_Age']].copy()
    dim_customers['customer_id'] = range(1, len(dim_customers) + 1)
    dim_customers = dim_customers.rename(columns={'Customer_Age': 'customer_age'})
    dim_customers = dim_customers[['customer_id', 'customer_age']]

    # dim_delivery_partners
    dim_partners = df[['Delivery_Partner_Rating']].drop_duplicates().copy()
    dim_partners['partner_id'] = range(1, len(dim_partners) + 1)
    dim_partners = dim_partners.rename(columns={'Delivery_Partner_Rating': 'delivery_partner_rating'})
    dim_partners = dim_partners[['partner_id', 'delivery_partner_rating']]

    # dim_promotions
    dim_promotions = df[['Discount_Applied']].drop_duplicates().copy()
    dim_promotions['promo_id'] = range(1, len(dim_promotions) + 1)
    dim_promotions = dim_promotions.rename(columns={'Discount_Applied': 'discount_applied'})
    dim_promotions = dim_promotions[['promo_id', 'discount_applied']]

    # fact_orders
    fact_orders = df.rename(columns={
        'Order_ID':                'order_id',
        'Order_Value':             'order_value',
        'Delivery_Time_Min':       'delivery_time_min',
        'Distance_Km':             'distance_km',
        'Items_Count':             'items_count',
        'Customer_Rating':         'customer_rating',
        'Discount_Applied':        'discount_applied',
        'Delivery_Partner_Rating': 'delivery_partner_rating',
        'Customer_Age':            'customer_age',
    })
    fact_orders = fact_orders[[
        'order_id', 'order_value', 'delivery_time_min',
        'distance_km', 'items_count', 'customer_rating',
        'discount_applied', 'delivery_partner_rating', 'customer_age',
    ]]

    print("Transformation complete!")
    return dim_customers, dim_partners, dim_promotions, fact_orders

if __name__ == "__main__":
    from extract import extract
    df = extract()
    dim_customers, dim_partners, dim_promotions, fact_orders = transform(df)
    print(fact_orders.head())