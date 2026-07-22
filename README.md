# 🚦 Traffic Prediction System using Machine Learning

A Machine Learning–based Traffic Prediction System that predicts the expected vehicle count at traffic junctions using historical traffic data. The application is powered by a **Random Forest Regression** model and deployed as an interactive **Streamlit** web application for real-time predictions.

## Live Demo

👉 https://trafficpredictions-bbbg4ws5bdqxutbyspqzh9.streamlit.app/

---

##  Project Overview

Traffic congestion is one of the major challenges in modern cities. This project leverages machine learning to predict future traffic volume based on historical traffic patterns and time-related features.

The trained model is deployed through a Streamlit interface where users can enter traffic parameters and instantly receive predicted vehicle counts.

---

##  Features

- Predicts vehicle count using historical traffic data
- Built using **Random Forest Regression**
- Interactive web interface using **Streamlit**
- Real-time traffic prediction
- Uses serialized ML model for faster inference
- Consistent preprocessing using saved feature scaler

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression
- Streamlit
- Pickle

---

##  Project Structure

```
Traffic_Predictions/
│
├── app.py              # Streamlit web application
├── model.pkl           # Trained Random Forest model
├── scaler.pkl          # Saved feature scaler
├── traffic.csv         # Dataset
├── traffic_bg.avif     # Background image
├── requirements.txt    # Required dependencies
└── README.md
```

---

##  Machine Learning Workflow

### 1. Data Collection & Preprocessing

- Loaded the traffic dataset
- Cleaned missing values
- Extracted time-based features
- Prepared input features
- Applied feature scaling

---

### 2. Model Training

The prediction model was trained using **Random Forest Regression**, which offers:

- High prediction accuracy
- Ability to capture non-linear relationships
- Robustness against overfitting
- Minimal hyperparameter tuning

---

### 3. Model Serialization

After training:

- Saved the trained model as `model.pkl`
- Saved the feature scaler as `scaler.pkl`

Using Pickle avoids retraining the model every time the application starts, resulting in faster deployment.

---

### 4. Deployment

The application is deployed using **Streamlit**.

Workflow:

1. User enters traffic-related inputs.
2. Input features are scaled using the saved scaler.
3. The trained Random Forest model predicts vehicle count.
4. Prediction is displayed instantly.

---

##  Model Used

**Random Forest Regression**

### Why Random Forest?

- Ensemble learning algorithm
- Handles non-linear traffic patterns
- Works well with tabular datasets
- Reduces overfitting through multiple decision trees
- Provides reliable prediction performance

---

##  Running the Project Locally

### Clone the repository

```bash
git clone https://github.com/yourusername/Traffic_Predictions.git
```

### Navigate to the project

```bash
cd Traffic_Predictions
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

##  Input Parameters

The application accepts traffic-related features such as:

- Time-based information
- Traffic conditions
- Other historical traffic parameters

The input is automatically preprocessed before prediction.

---

##  Output

The model predicts:

**Estimated Vehicle Count**

which can assist in:

- Traffic monitoring
- Smart city applications
- Congestion analysis
- Urban traffic planning

---

##  Application Preview

You can view the deployed application here:

https://trafficpredictions-bbbg4ws5bdqxutbyspqzh9.streamlit.app/

*(You may also add screenshots of the application here.)*

---

##  Future Improvements

- Live traffic API integration
- Deep Learning models (LSTM/GRU)
- Weather-aware traffic prediction
- Interactive traffic visualization
- Multi-location prediction
- Traffic congestion classification

---

## Author

**Shivam Sen**

GitHub: https://github.com/shivamsen23

---

## If you found this project useful, consider giving it a star!
