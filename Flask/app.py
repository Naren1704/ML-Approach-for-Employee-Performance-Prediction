from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import os

app = Flask(__name__)

# Load the trained model AND preprocessing objects
MODEL_PATH = 'best_xgboost_model.pkl'
PREPROCESSOR_PATH = 'preprocessor.pkl'

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

with open(PREPROCESSOR_PATH, 'rb') as file:
    preprocessor = pickle.load(file)

def preprocess_input(input_data):
    """Preprocess the input data to match training format"""
    
    # Create DataFrame
    df = pd.DataFrame([input_data])
    
    # Ensure correct data types
    numeric_fields = ['targeted_productivity', 'smv', 'over_time', 'incentive', 
                    'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers', 
                    'month', 'day_of_month', 'team']
    
    for field in numeric_fields:
        if field in df.columns:
            df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0)
    
    try:
        # Get all possible feature names from preprocessor
        all_possible_features = []
        
        # Numerical features (always present)
        numerical_features = [
            'targeted_productivity', 'smv', 'over_time', 'incentive', 
            'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers', 
            'month', 'day_of_month'
        ]
        all_possible_features.extend(numerical_features)
        
        # Categorical features with all possible values
        categorical_mappings = preprocessor['unique_values']
        for col, values in categorical_mappings.items():
            for val in values:
                feature_name = f"{col}_{val}"
                all_possible_features.append(feature_name)
        
        # Start with all zeros
        feature_dict = {feature: 0 for feature in all_possible_features}
        
        # Fill numerical features
        for num_feat in numerical_features:
            if num_feat in df.columns:
                feature_dict[num_feat] = float(df[num_feat].iloc[0])
        
        # Fill categorical features (one-hot encoding)
        categorical_cols = ['department', 'day', 'quarter']
        for col in categorical_cols:
            if col in df.columns:
                input_value = str(df[col].iloc[0])
                feature_name = f"{col}_{input_value}"
                if feature_name in feature_dict:
                    feature_dict[feature_name] = 1
        
        # Convert to DataFrame
        final_df = pd.DataFrame([feature_dict])
        
        # Ensure we only have the features the model expects
        if hasattr(model, 'feature_names_in_'):
            expected_features = model.feature_names_in_
            # Align columns with model expectations
            final_df = final_df.reindex(columns=expected_features, fill_value=0)
        
        print(f"Final shape: {final_df.shape}")  # Debug
        return final_df
        
    except Exception as e:
        raise ValueError(f"Preprocessing error: {str(e)}")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        print(f"Received data: {data}")  # Debug
        
        # Preprocess the input data
        processed_data = preprocess_input(data)
        print(f"Processed data shape: {processed_data.shape}")  # Debug
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        
        # Convert numpy float32 to Python native float for JSON serialization
        prediction = float(prediction)
        
        # Ensure prediction is within valid range
        prediction = max(0.1, min(0.99, prediction))
        
        # Classify the prediction
        if prediction <= 0.3:
            productivity_class = "Worst"
            class_color = "#ff4444"
        elif prediction <= 0.8:
            productivity_class = "Average" 
            class_color = "#ffaa00"
        else:
            productivity_class = "Best"
            class_color = "#44ff44"
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 3),
            'class': productivity_class,
            'class_color': class_color,
            'input_data': data
        })
        
    except Exception as e:
        print(f"Prediction error: {str(e)}")  # For debugging
        return jsonify({
            'success': False,
            'error': f"Prediction failed: {str(e)}"
        })

if __name__ == '__main__':
    app.run(debug=True)