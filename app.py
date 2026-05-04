
import streamlit as st
import pandas as pd
import joblib
model = joblib.load("house_price_model.pkl")
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")
st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict price")
st.sidebar.header("Input Features")

longitude = st.sidebar.number_input("Longitude", value=-122.23)
latitude = st.sidebar.number_input("Latitude", value=37.88)
housing_median_age = st.sidebar.slider("Housing Median Age", 1, 52, 20)
total_rooms = st.sidebar.number_input("Total Rooms", value=1500)
total_bedrooms = st.sidebar.number_input("Total Bedrooms", value=300)
population = st.sidebar.number_input("Population", value=1000)
households = st.sidebar.number_input("Households", value=400)
median_income = st.sidebar.slider("Median Income", 0.0, 15.0, 4.5)

ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR BAY", "NEAR OCEAN", "<1H OCEAN", "ISLAND"]
)

input_data = pd.DataFrame([{
    "longitude": longitude,
    "latitude": latitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    "ocean_proximity": ocean_proximity
}])
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted House Price: ${prediction:,.2f}")

