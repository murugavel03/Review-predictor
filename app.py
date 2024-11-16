import streamlit as st
import requests

# Flask API URL
API_URL = "http://localhost:5000/predict"  # Make sure the Flask API is running at this URL

# Streamlit UI Setup
st.title("Fake Review Detection")

# Create an input box for the review text
review = st.text_area("Enter the Review:")

# Create a button to submit the review
if st.button("Check Review"):
    if review:
        # Send the review to Flask API for prediction
        response = requests.post(API_URL, json={"review": review})
        
        if response.status_code == 200:
            # Get the prediction from the response
            result = response.json().get("prediction", "Error")
            st.write(f"Prediction: {result}")
        else:
            st.write("Error: Unable to get prediction from API")
    else:
        st.write("Please enter a review before submitting.")
