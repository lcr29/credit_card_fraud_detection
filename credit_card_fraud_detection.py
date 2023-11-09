import streamlit as st
import numpy as np
import joblib

# Load the model and scaler
xgboost_model = joblib.load('xgboost_model.pkl')
scaler = joblib.load('scaler.pkl')

# Set page config to wide mode
st.set_page_config(layout="wide")

st.image('header_image.png', width=150)  
st.title('Credit Card Fraud Detection')

st.markdown("""
    Enter the details of the transaction to predict if it is fraudulent.
    Adjust the values of each feature using the sliders below.
""")

# Sidebar for feature input
st.sidebar.header('Input Features')
input_features = []
feature_names = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5', 'Feature 6', 'Feature 7', 'Feature 8',
                 'Feature 9', 'Feature 10', 'Feature 11', 'Feature 12', 'Feature 13', 'Feature 14', 'Feature 15',
                 'Feature 16', 'Feature 17', 'Feature 18', 'Feature 19','Feature 20', 'Feature 21', 'Feature 22',
                 'Feature 23', 'Feature 24', 'Feature 25', 'Feature 26', 'Feature 27', 'Feature 28', 'Amount']

# You can decide the range of your sliders based on the actual range of your features
for feature_name in feature_names:
    value = st.sidebar.slider(feature_name, min_value=-10.0, max_value=10.0, value=0.0, step=0.01)
    input_features.append(value)

# Button to make the prediction
if st.sidebar.button('Detect Fraud'):
    input_array = np.array(input_features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = xgboost_model.predict(input_scaled)
    if prediction[0] == 1:
        st.error('This transaction is likely to be fraudulent.')
        st.image('risk.png', caption='High risk of fraud', width=300)
    else:
        st.success('This transaction is likely to be legitimate.')
        st.image('accept.png', caption='Transaction is legitimate', width=300)

# About section
expander = st.expander("About this app")
expander.write("""
    This app uses a machine learning model to predict fraudulent credit card transactions.
    It comprises over 550,000 records, and the data has been anonymized to protect the cardholders' identities. 
    The dataset contains transactions made by European cardholders in 2023.

    **Features:**
    - **Feature 1 - Feature 28**: Anonymized credit card transaction features.
    - **Amount**: Transaction amount.

    **Model:**
    - The prediction model is based on XGBoost, trained to detect patterns indicative of fraud.
""")

