import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model and data
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

# Title and description
st.title("Car Price Predictor")
st.write("This app predicts the price of a car you want to sell. Try filling the details below:")

# Selection options
companies = sorted(car['company'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = car['fuel_type'].unique()

# User inputs
company = st.selectbox("Select the company", ["Select Company"] + companies)
if company != "Select Company":
    filtered_models = car[car['company'] == company]['name'].unique()
    car_model = st.selectbox("Select the model", filtered_models)
else:
    car_model = st.selectbox("Select the model", [])

year = st.selectbox("Select Year of Purchase", years)
fuel_type = st.selectbox("Select the Fuel Type", fuel_types)
kilo_driven = st.text_input("Enter the Number of Kilometers that the car has travelled", placeholder="Enter the kilometers driven")

# Predict button
if st.button("Predict Price"):
    if company == "Select Company":
        st.error("Please select a valid company.")
    elif not car_model:
        st.error("Please select a model.")
    else:
        # Perform prediction
        input_data = pd.DataFrame({
            'name': [car_model],
            'company': [company],
            'year': [year],
            'kms_driven': [kilo_driven],
            'fuel_type': [fuel_type]
        })

        prediction = model.predict(input_data)
        st.write(f"Prediction: ₹ {np.round(prediction[0], 2)}")
