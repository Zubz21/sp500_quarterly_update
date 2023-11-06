import streamlit as st
import pandas as pd
import pickle
import numpy as np
from scipy.stats import zscore
from scipy import stats


# Load your model
with open('model_1_xgbc.pkl', 'rb') as pickle_in:
    pipe = pickle.load(pickle_in)

# Load your data
database = pd.read_csv("total_market.csv")
stocks = pd.read_csv("trained_market.csv")
stocks.fillna(0, inplace=True)
for col in stocks.columns:
    # Only try to convert columns that are still object types
    if stocks[col].dtype == 'object':
        stocks[col] = stocks[col].replace('[\$,BM]', '', regex=True).astype(float)
st.write(stocks.dtypes)


# Calculate Z-scores for the specified columns
# Calculate the Z-scores of the columns


# Sorting values by 'Market Cap' may not be necessary for the prediction
# If it's not needed, you can remove the sort_values part.
# stocks = stocks.sort_values('Market Cap')
# database = database.sort_values('Market Cap')

# Ensure 'Ticker' and 'in_index' are in the correct format (if they are not already)
stocks['Ticker'] = database['Ticker'].str.upper()
stocks['in_index'] = database['in_index']

# Title of the web app
st.title('S&P 500 Predictive Analysis App')

# Description
st.write('This app predicts whether a ticker is currently in the S&P 500, if it will be in 3 months')

# User input for ticker symbol
user_input_ticker = st.text_input("Enter a stock ticker:").upper()

# When the user clicks the 'Predict' button
if st.button('Predict'):
    if user_input_ticker:
        # Check if the ticker is in the database and get the row
        if user_input_ticker in stocks['Ticker'].values:
            stock_info = stocks[stocks['Ticker'] == user_input_ticker]
            # Here, ensure that the input to the model is in the correct format
            # For example, you might need to drop or transform certain columns
            prediction_input = stock_info.drop(columns=['Ticker', 'in_index'])
            prediction = pipe.predict(prediction_input)
            
            # Check if the stock is in the S&P 500
            if stock_info['in_index'].iloc[0] == 1:
                st.success(f"{user_input_ticker} is in the S&P 500. Prediction: {prediction[0]}")
            else:
                st.warning(f"{user_input_ticker} is in the Russell 1000 but not in the S&P 500. Prediction: {prediction[0]}")
        else:
            st.error(f"{user_input_ticker} was not found in the database.")
    else:
        st.error("Please enter a ticker.")

st.write('This next part will take in the features for a stock and predict whether or not that stock will enter the S&P 500 in the next quarter')

#st.sidebar.header('User Input Features')

def user_input_features():
    inputs = {}
    inputs['Market Cap'] = st.sidebar.number_input('Market Cap', format="%f")
    inputs['Outstanding Shares'] = st.sidebar.number_input('Outstanding Shares', format="%f")
    inputs['Q1_NetIncome'] = st.sidebar.number_input('Q1 Net Income', format="%f")
    inputs['Q2_NetIncome'] = st.sidebar.number_input('Q2 Net Income', format="%f")
    inputs['Q3_NetIncome'] = st.sidebar.number_input('Q3 Net Income', format="%f")
    inputs['Q4_NetIncome'] = st.sidebar.number_input('Q4 Net Income', format="%f")
    inputs['Q5_NetIncome'] = st.sidebar.number_input('Q5 Net Income', format="%f")
    inputs['Q6_NetIncome'] = st.sidebar.number_input('Q6 Net Income', format="%f")
    inputs['Q7_NetIncome'] = st.sidebar.number_input('Q7 Net Income', format="%f")
    inputs['Q8_NetIncome'] = st.sidebar.number_input('Q8 Net Income', format="%f")
    inputs['Month1_Volume'] = st.sidebar.number_input('Month1 Volume', format="%f")
    inputs['Month2_Volume'] = st.sidebar.number_input('Month2 Volume', format="%f")
    inputs['Month3_Volume'] = st.sidebar.number_input('Month3 Volume', format="%f")
    inputs['Month4_Volume'] = st.sidebar.number_input('Month4 Volume', format="%f")
    inputs['Month5_Volume'] = st.sidebar.number_input('Month5 Volume', format="%f")
    inputs['Month6_Volume'] = st.sidebar.number_input('Month6 Volume', format="%f")
    inputs['Month7_Volume'] = st.sidebar.number_input('Month7 Volume', format="%f")
    inputs['Month8_Volume'] = st.sidebar.number_input('Month8 Volume', format="%f")
    inputs['Month9_Volume'] = st.sidebar.number_input('Month9 Volume', format="%f")
    inputs['Month10_Volume'] = st.sidebar.number_input('Month10 Volume', format="%f")
    inputs['Month11_Volume'] = st.sidebar.number_input('Month11 Volume', format="%f")
    inputs['Month12_Volume'] = st.sidebar.number_input('Month12 Volume', format="%f")
    inputs['Month13_Volume'] = st.sidebar.number_input('Month13 Volume', format="%f")
    inputs['Month14_Volume'] = st.sidebar.number_input('Month14 Volume', format="%f")
    inputs['Month15_Volume'] = st.sidebar.number_input('Month15 Volume', format="%f")
    inputs['Month16_Volume'] = st.sidebar.number_input('Month16 Volume', format="%f")
    inputs['Month17_Volume'] = st.sidebar.number_input('Month17 Volume', format="%f")
    inputs['Month18_Volume'] = st.sidebar.number_input('Month18 Volume', format="%f")
    inputs['Month19_Volume'] = st.sidebar.number_input('Month19 Volume', format="%f")
    inputs['Month20_Volume'] = st.sidebar.number_input('Month20 Volume', format="%f")
    inputs['Month21_Volume'] = st.sidebar.number_input('Month21 Volume', format="%f")
    inputs['Month22_Volume'] = st.sidebar.number_input('Month22 Volume', format="%f")
    inputs['Month23_Volume'] = st.sidebar.number_input('Month23 Volume', format="%f")
    inputs['Month24_Volume'] = st.sidebar.number_input('Month24 Volume', format="%f")
    inputs['Underaged'] = st.sidebar.number_input('Underaged', format="%f")
    inputs['Oustanding Shares'] = st.sidebar.number_input('Oustanding Shares', format="%f")
    inputs['MarketCap_Q8NetIncome'] = st.sidebar.number_input('MarketCap Q8 Net Income', format="%f")
    inputs['MarketCap_Q7NetIncome'] = st.sidebar.number_input('MarketCap Q7 Net Income', format="%f")
    inputs['MarketCap_duplicate'] = st.sidebar.number_input('MarketCap Duplicate', format="%f")
    inputs['Q1_NetIncome_duplicate'] = inputs['Q1_NetIncome'] * 2
    inputs['Q2_NetIncome_duplicate'] = inputs['Q2_NetIncome'] * 2
    inputs['Q3_NetIncome_duplicate'] = inputs['Q3_NetIncome'] * 2
    inputs['Q4_NetIncome_duplicate'] = inputs['Q4_NetIncome'] * 2
  
    # If any features are categorical or need different treatment, use appropriate widgets
    # For example:
    # inputs['Categorical Feature'] = st.sidebar.selectbox('Categorical Feature', options=['Option 1', 'Option 2'])
    
    return pd.DataFrame([inputs])


input_df = user_input_features()

# Display the input dataframe
st.subheader('User Input features')
st.write(input_df)

# Prediction
# Prediction
if st.button('Predict', key='predict_button'):
    prediction = pipe.predict(input_df)
    st.success(f'The predicted value is: {prediction[0]}')



#######################################################################
columns_to_convert = [
    'Market Cap', 'Outstanding Shares', 'Q1_NetIncome', 'Q2_NetIncome', 'Q3_NetIncome',
    'Q4_NetIncome', 'Q5_NetIncome', 'Q6_NetIncome', 'Q7_NetIncome', 'Q8_NetIncome',
    'Month1_Volume', 'Month2_Volume', 'Month3_Volume', 'Month4_Volume', 'Month5_Volume',
    'Month6_Volume', 'Month7_Volume', 'Month8_Volume', 'Month9_Volume', 'Month10_Volume',
    'Month11_Volume', 'Month12_Volume', 'Month13_Volume', 'Month14_Volume', 'Month15_Volume',
    'Month16_Volume', 'Month17_Volume', 'Month18_Volume', 'Month19_Volume', 'Month20_Volume',
    'Month21_Volume', 'Month22_Volume', 'Month23_Volume', 'Month24_Volume', 'Underaged',
    'Oustanding Shares', 'MarketCap_Q8NetIncome', 'MarketCap_Q7NetIncome', 'MarketCap_duplicate',
    'Q1_NetIncome_duplicate', 'Q2_NetIncome_duplicate', 'Q3_NetIncome_duplicate', 'Q4_NetIncome_duplicate'
]


st.subheader("Will it be in the SP")

ticker = st.text_input("Enter stock ticker", "AAPL")
q1_net_income_input = st.number_input("Enter project FY23Q4 Earnings", 1000000000)
month1_volume_input = st.number_input("Enter projected October Volume",100000000)
month2_volume_input = st.number_input("Enter projected November Volume",100000000)
month3_volume_input = st.number_input("Enter projected December Volume",100000000)

# Check if the button is pressed
if st.button("Run Model"):
    # 2. Retrieve data for entered ticker
    if ticker in stocks['Ticker'].values:
        stock_data = stocks[stocks['Ticker'] == ticker]
        
        for i in range(8, 1, -1):
            stock_data[f'Q{i}_NetIncome'] = stock_data[f'Q{i-1}_NetIncome']
            
        # Update 'Q1_NetIncome' with the user input
        stock_data['Q1_NetIncome'] = q1_net_income_input
        
        # Shift 'Volume' columns by 3
        for i in range(24, 3, -1):
            stock_data[ f'Month{i}_Volume'] = stock_data[f'Month{i-3}_Volume']

        stock_data['Month1_Volume'] = month1_volume_input
        stock_data['Month2_Volume'] = month2_volume_input
        stock_data['Month3_Volume'] = month3_volume_input

        # Preprocessing if needed, assuming a function 'preprocess' is defined
        # processed_data = preprocess(stock_data)
        stock_data = stock_data.drop(columns=['Ticker', 'in_index'])

        # 3. Make sure the data is in the correct format for the model
        # For example, you might need to reshape the data or select specific columns
        # model_input = processed_data.values.reshape(1, -1)  # Reshaping if necessary
        
        # 4. Run the model on the processed data
        prediction = pipe.predict(stock_data)
        
        # 5. Display the results
        st.write(f"Prediction for {ticker}: {prediction[0]}")
    else:
        st.error("Ticker not found in the database")