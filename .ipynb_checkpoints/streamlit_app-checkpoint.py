import streamlit as st
import joblib

# Load the regression model
model = joblib.load('regression_model.pkl')  # Replace with your model file path

# Define the features
features = ['ph', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Create sliders for each feature
sliders = {feature: st.slider(f'Select {feature}', min_value=0.0, max_value=100000.0, step=0.1, value=0.0)
           for feature in features}

# Convert slider values to a list for prediction
new_data = [[sliders[feature] for feature in features]]

# Make a prediction
prediction = model.predict(new_data)

# Display the prediction
st.write(f"The predicted value is: {prediction[0]}")
