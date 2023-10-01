import streamlit as st
import joblib

# Load the regression model
model = joblib.load('regression_model.pkl')  # Replace with your model file path

# Feature names
features = ['ph', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Title and instructions
st.title("Water hardness, a measure of mineral content")
st.write("Enter the values for the following features:")

# User input for features
user_input = {}
for feature in features:
    user_input[feature] = st.number_input(feature, min_value=0.0)

# When the user clicks the "Predict" button
if st.button("Predict"):
    # Prepare the data for prediction
    new_data = [[user_input[feature] for feature in features]]
    
    # Make a prediction
    prediction = model.predict(new_data)
    
    # Display the prediction
    st.write(f"The predicted value is: {prediction[0]}")
