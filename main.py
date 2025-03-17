import streamlit as st
import pickle
import pandas as pd
import base64
from datetime import datetime

# Load Model
with open("flight_rf.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(input_data):
    return model.predict(input_data)[0]

# Function to Convert Image to Base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_base64 = get_base64_of_image("photo-1437846972679-9e6e537be46e.avif")
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{image_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
[data-testid="stHeader"], [data-testid="stSidebar"] {{
    background: rgba(0, 0, 0, 0.7);
    color: white;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: white;'>Flight Price Prediction</h1>", unsafe_allow_html=True)

# Input Fields
airlines = ['Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet', 
                   'Vistara', 'Air Asia', 'GoAir', 'Multiple carriers Premium economy', 
                   'Jet Airways Business', 'Vistara Premium economy', 'Trujet']

sources = ['Chennai', 'Delhi', 'Kolkata', 'Mumbai', 'Bangalore']
destinations = ['Cochin', 'Banglore', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata']

# Layout: 3 Columns in 2 Rows, Last One in the Middle
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, _, _ = st.columns([1, 1, 1])

with col1:
    date_of_journey = st.date_input("Date of Journey", datetime.today())
with col2:
    source = st.selectbox("Source", sources)
with col3:
    destination = st.selectbox("Destination", destinations)

with col4:
    airline = st.selectbox("Airline", airlines)
with col5:
    total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])
with col6:
    departure_time = st.time_input("Departure Time")

with col7:
    arrival_time = st.time_input("Arrival Time")

# Convert date and time inputs
Journey_day = date_of_journey.day
Journey_month = date_of_journey.month
Dep_hour = departure_time.hour
Dep_min = departure_time.minute
Arrival_hour = arrival_time.hour
Arrival_min = arrival_time.minute

# Duration Calculation
duration_hours = abs(Arrival_hour - Dep_hour)
duration_mins = abs(Arrival_min - Dep_min)

# Encoding categorical variables
airline_dict = {name: 0 for name in airlines}
source_dict = {name: 0 for name in sources}
destination_dict = {name: 0 for name in destinations}

airline_dict[airline] = 1
source_dict[source] = 1
destination_dict[destination] = 1

# Creating input DataFrame
input_data = pd.DataFrame([[total_stops, Journey_day, Journey_month, Dep_hour, Dep_min, 
                            Arrival_hour, Arrival_min, duration_hours, duration_mins, 
                            *airline_dict.values(), *source_dict.values(), *destination_dict.values()]], 
                          columns=['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_min',
                                   'Arrival_hour', 'Arrival_min', 'Duration_hours', 'Duration_mins', 
                                   *airlines, *sources, *destinations])

# Prediction Button
if st.button("Predict Price"):
    price = predict_price(input_data)
    st.markdown(f"""<h2 style='text-align: center; font-size: 28px; font-weight: bold; color: white;'>
                  Estimated Flight Price: ₹{price:.2f}
                  </h2>""", unsafe_allow_html=True)