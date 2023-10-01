import streamlit as st
import joblib

# Load the regression model
model = joblib.load('regression_model.pkl')  # Replace with your model file path

# Define the features
features = ['ph', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Set up Streamlit app
st.title('Water Quality Predictor')

# Create sliders for each feature
feature_values = []
for feature in features:
    value = st.slider(f'Select value for {feature}', min_value=0.0, max_value=100000.0, step=0.01, key=feature)
    feature_values.append(value)

# Create a button to trigger prediction
if st.button('Predict'):
    new_data = [feature_values]
    prediction = model.predict(new_data)
    st.write(f"The predicted value is: {prediction[0]}")