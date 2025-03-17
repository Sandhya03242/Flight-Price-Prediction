```markdown
# Flight Price Prediction

## Overview

The Flight Price Prediction project is a machine learning-based web application built using Streamlit. It predicts flight ticket prices based on various input features such as airline, source, destination, travel date, departure time, arrival time, and total stops. The model is trained on a dataset of flight prices and helps users estimate airfare before booking.

## Dataset

The dataset used for training the model contains details such as:

- Airline  
- Date of Journey  
- Source  
- Destination  
- Route  
- Departure and Arrival Time  
- Duration  
- Total Stops  
- Price  

## Features

✅ Predicts flight ticket prices based on user input.  
✅ Uses a trained Random Forest Regression model.  
✅ Dynamic user interface using Streamlit.  
✅ Encodes categorical features for better predictions.  
✅ Displays results in an interactive format.  

## Installation & Usage

### Prerequisites

Ensure you have Python 3.7+ installed along with the required libraries.

### Clone the Repository

```sh
git clone https://github.com/your-username/flight-price-prediction.git
cd flight-price-prediction
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Run the Application

```sh
streamlit run app.py
```

## Model Training

The machine learning model is trained using Random Forest Regression. Steps involved:

1. **Data Preprocessing** (handling missing values, encoding categorical features, feature selection).  
2. **Splitting Data** into training and testing sets.  
3. **Training** the Random Forest Regression model.  
4. **Evaluating** model performance.  
5. **Saving** the trained model using pickle.  

## Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- **Machine Learning** (Random Forest Regression)  
- **Streamlit** (Web UI)  
- **Pickle** (Model serialization)  

## Project Structure

```
📂 flight-price-prediction
 ├── 📄 main.py           # Streamlit app
 ├── 📄 flight_rf.pkl    # Trained model
 ├── 📂 dataset          # Dataset files
 ├── 📂 images           # Background images
 ├── 📄 README.md        # Project Documentation
```

## Screenshots


## Future Improvements

🚀 Add more airline companies for better predictions.  
🚀 Improve model accuracy with advanced ML techniques.  
🚀 Integrate real-time flight price API.  
```

