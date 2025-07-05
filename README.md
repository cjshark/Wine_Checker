# 🍷 Red Wine Quality Predictor

A machine learning web application built with Streamlit that predicts red wine quality based on chemical properties.

## Features

- Interactive web interface with intuitive sliders
- Real-time wine quality prediction
- Confidence score display
- Professional UI with emojis and clear visual feedback

## Wine Attributes Used

The model uses the following 11 chemical properties to predict wine quality:

**Acidity & Sugar:**
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar

**Salt & Sulfur:**
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide

**Other Properties:**
- Density
- pH
- Sulphates
- Alcohol

## How to Use

1. Adjust the sliders in the sidebar to input wine attributes
2. Click "🚀 Predict Quality" button
3. View the prediction result and confidence score

## Live Demo

🚀 **[Try the app live on Streamlit Cloud!](your-streamlit-url-here)**

## Local Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run index.py
```

## Model Information

The app uses a pre-trained machine learning model (`wine_quality_model.joblib`) that classifies wines as either "Good Quality" or "Not Good Quality" based on the input features.

## Tech Stack

- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Model Persistence:** Joblib

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
