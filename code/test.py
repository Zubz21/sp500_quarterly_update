def update_and_prepare_data(ticker, q1_net_income, m1_volume, m2_volume, m3_volume, stocks_df):
    """
    Update the stocks DataFrame with user-provided inputs and prepare the row for prediction.

    Parameters:
    - ticker: str, the stock ticker symbol.
    - q1_net_income: float, the net income for Q1.
    - m1_volume, m2_volume, m3_volume: float, the volumes for month 1, 2, and 3.
    - stocks_df: pd.DataFrame, the DataFrame containing stock information.

    Returns:
    - pd.Series, the row prepared for prediction.
    """
    # Check if the ticker is in the dataframe


    #stocks_df.fillna(0, inplace=True)
    #stocks = convert_columns_to_float(stocks_df, columns_to_convert)

    if ticker in stocks_df['Ticker'].values:
        # Get the index of the row with the given ticker
        row_index = stocks_df.index[stocks_df['Ticker'] == ticker].tolist()[0]
        
        # Shift 'NetIncome' columns by 1
        for i in range(7, 1, -1):
            stocks_df.at[row_index, f'Q{i}_NetIncome'] = stocks_df.at[row_index, f'Q{i-1}_NetIncome']
            
        # Update 'Q1_NetIncome' with the user input
        stocks_df.at[row_index, 'Q1_NetIncome'] = q1_net_income
        
        # Shift 'Volume' columns by 3
        for i in range(24, 3, -1):
            stocks_df.at[row_index, f'Month{i}_Volume'] = stocks_df.at[row_index, f'Month{i-3}_Volume']
        
        # Update 'Month1_Volume', 'Month2_Volume', and 'Month3_Volume' with the user input
        stocks_df.at[row_index, 'Month1_Volume'] = m1_volume
        stocks_df.at[row_index, 'Month2_Volume'] = m2_volume
        stocks_df.at[row_index, 'Month3_Volume'] = m3_volume
        


        # Prepare the row for prediction
        prediction_row = stocks_df.loc[row_index].drop(['Ticker', 'in_index'])
        st.write(prediction_row)
        return prediction_row
    else:
        raise ValueError(f"Ticker {ticker} not found in the database.")



# User input for the ticker symbol
ticker_input = st.text_input("Enter the stock ticker for update:").upper()

# User input for Q1 Net Income
q1_net_income_input = st.number_input("Enter the Q1 Net Income:", format="%f")

# User input for volumes of the first three months
month1_volume_input = st.number_input("Enter the Month1 Volume:", format="%f")
month2_volume_input = st.number_input("Enter the Month2 Volume:", format="%f")
month3_volume_input = st.number_input("Enter the Month3 Volume:", format="%f")

# When the user clicks the 'Update and Predict' button
if st.button('Update and Predict',key="test button"):
    #stocks = convert_columns_to_float(stocks, columns_to_convert)
    st.write(stocks.isna().sum())
    if ticker_input:
        try:
            # Update the DataFrame and prepare the data for prediction
            updated_row = update_and_prepare_data(ticker_input, q1_net_income_input,
                                                  month1_volume_input, month2_volume_input,
                                                  month3_volume_input, stocks)
            # Convert the Series to DataFrame as expected by the model
            updated_row_df = updated_row.to_frame().T
            # Make the prediction
            prediction = pipe.predict(updated_row_df)
            # Display the prediction
            st.success(f"The prediction for {ticker_input} is: {prediction[0]}")
        except ValueError as e:
            st.error(e)
    else: