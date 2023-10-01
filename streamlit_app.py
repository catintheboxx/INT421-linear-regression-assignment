import streamlit as st
import joblib

# Load the regression model
model = joblib.load('regression_model.pkl')  # Replace with your model file path

# Define the features
features = ['ph', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Create a sidebar with slider bars for each feature
st.sidebar.header('Feature Values')

# Initialize a dictionary to store feature values
feature_values = {}

# Iterate through features
for feature in features:
    # Add a slider for each feature
    feature_values[feature] = st.sidebar.slider(f'{feature}', min_value=0.0, max_value=50000.0, value=50.0, step=0.000000000000000001)

# Assuming you have a function to make predictions
def predict(feature_values):
    new_data = [[feature_values[feature] for feature in features]]
    prediction = model.predict(new_data)
    return prediction[0]

# Make prediction
prediction = predict(feature_values)

# Display the prediction
st.title('Water hardness, a measure of mineral content')
st.write(f"The predicted value is: {prediction}")
