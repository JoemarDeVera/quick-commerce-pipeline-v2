def validate(df):
    print("Validating data...")
    errors = []

    # Check 1: No null values in critical columns
    critical_columns = ['Order_ID', 'Order_Value', 'Delivery_Time_Min', 'Distance_Km']
    for col in critical_columns:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            errors.append(f"Column '{col}' has {nulls} null values")

    # Check 2: Order value must be positive
    negative_orders = (df['Order_Value'] <= 0).sum()
    if negative_orders > 0:
        errors.append(f"{negative_orders} orders have negative or zero order value")

    # Check 3: Delivery time must be between 1 and 120 mins
    invalid_time = ((df['Delivery_Time_Min'] < 1) | (df['Delivery_Time_Min'] > 120)).sum()
    if invalid_time > 0:
        errors.append(f"{invalid_time} orders have invalid delivery time")

    # Check 4: Customer rating must be between 1 and 5
    invalid_rating = ((df['Customer_Rating'] < 1) | (df['Customer_Rating'] > 5)).sum()
    if invalid_rating > 0:
        errors.append(f"{invalid_rating} orders have invalid customer rating")

    # Check 5: No duplicate Order IDs
    duplicates = df['Order_ID'].duplicated().sum()
    if duplicates > 0:
        errors.append(f"{duplicates} duplicate Order IDs found")

    # Report results
    if errors:
        print("Validation FAILED:")
        for error in errors:
            print(f"  - {error}")
        raise ValueError("Data validation failed — pipeline stopped!")
    else:
        print(f"Validation PASSED — {len(df):,} rows are clean!")

if __name__ == "__main__":
    from extract import extract
    df = extract()
    validate(df)