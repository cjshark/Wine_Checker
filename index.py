import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model_filename = 'wine_quality_model.joblib'
model = joblib.load(model_filename)

# Page configuration
st.set_page_config(page_title="🍷 Red Wine Quality Predictor", layout="wide")

# Title and description
st.title('🍷 Red Wine Quality Predictor')
st.markdown(
    """
    This app predicts whether a red wine is of **good quality** or **not good quality** based on its chemical properties.  
    Adjust the sliders in the sidebar to enter wine attributes and click **Predict Quality**.
    """
)

# Sidebar inputs
st.sidebar.title("🧪 Wine Attributes")

# Group inputs into sections
st.sidebar.subheader("Acidity & Sugar")
fixed_acidity = st.sidebar.slider('Fixed Acidity', 0.0, 20.0, 7.4)
volatile_acidity = st.sidebar.slider('Volatile Acidity', 0.0, 2.0, 0.7)
citric_acid = st.sidebar.slider('Citric Acid', 0.0, 1.0, 0.0)
residual_sugar = st.sidebar.slider('Residual Sugar', 0.0, 20.0, 1.9)

st.sidebar.subheader("Salt & Sulfur")
chlorides = st.sidebar.slider('Chlorides', 0.0, 1.0, 0.076)
free_sulfur_dioxide = st.sidebar.slider('Free Sulfur Dioxide', 0.0, 100.0, 11.0)
total_sulfur_dioxide = st.sidebar.slider('Total Sulfur Dioxide', 0.0, 300.0, 34.0)

st.sidebar.subheader("Other Properties")
density = st.sidebar.slider('Density', 0.9900, 1.0100, 0.9978, step=0.0001, format="%.4f")
pH = st.sidebar.slider('pH', 2.5, 4.5, 3.51)
sulphates = st.sidebar.slider('Sulphates', 0.0, 2.0, 0.56)
alcohol = st.sidebar.slider('Alcohol', 8.0, 15.0, 9.4)

# Predict button
if st.button('🚀 Predict Quality'):
    input_data = pd.DataFrame([[
        fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
        free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol
    ]], columns=[
        'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
    ])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    confidence = prediction_proba[0][prediction[0]] * 100

    # Display result
    st.markdown("## 🔍 Prediction Result")
    if prediction[0] == 1:
        st.success("✅ The wine is predicted to be of **Good Quality**.")
    else:
        st.error("❌ The wine is predicted to be of **Not Good Quality**.")
    
    st.metric("🎯 Confidence Score", f"{confidence:.2f}%")
