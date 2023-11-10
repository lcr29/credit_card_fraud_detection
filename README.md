# Credit Card Fraud Detection App
# Overview
This repository contains a Streamlit-based web application designed to predict fraudulent credit card transactions. The application leverages an XGBoost machine learning model to analyze transaction data and identify potential fraud.

# Features
User-Friendly Interface: The app offers an easy-to-use interface where users can input transaction details and get instant predictions.
Dynamic Input via Sliders: Users can adjust transaction feature values through sliders, providing a flexible way to test different scenarios.
Immediate Fraud Detection: The app quickly evaluates the input data and predicts whether a transaction is fraudulent.
Visual Feedback: Based on the prediction, the app displays an appropriate image and message, enhancing the user experience.

# Data and Model
Data: The model is trained on over 550,000 anonymized transaction records from European cardholders in 2023.
Privacy-Focused: All data has been anonymized to maintain the confidentiality of cardholders' identities.
Model Details: The core of this application is an XGBoost model, fine-tuned to detect patterns and signs of fraudulent transactions.

# Using the App
Launch the app and navigate through the sidebar to input features of a credit card transaction.
Adjust the values of each feature using the provided sliders.
Click the 'Detect Fraud' button to receive a prediction.
The app will display whether the transaction is likely to be legitimate or fraudulent.

# About
This app serves as a practical tool for detecting potentially fraudulent credit card transactions. Its foundation is a robust dataset combined with a powerful machine learning algorithm, offering a glimpse into the possibilities of AI in enhancing financial security.
