# ML-Approach-for-Employee-Performance-Prediction
🏭 Garment Factory Productivity Predictor
A machine learning-powered web application that predicts worker productivity in garment factories based on operational parameters. This system helps factory managers optimize workforce allocation, improve efficiency, and make data-driven decisions.

🎯 Features
🤖 Machine Learning
Accurate Predictions: XGBoost model with 50.5% explained variance

Performance Classification: Automatically categorizes as Worst/Average/Best

Real-time Analysis: Instant predictions with <2 second response time

💻 Web Application
Modern UI: Glass-morphism design with responsive layout

Interactive Dashboard: Beautiful charts and visualizations

Input Validation: Comprehensive form validation with real-time feedback

Professional Reports: Printable results with actionable insights

📈 Analytics
Productivity Distribution: Visual representation of performance categories

Factor Impact Analysis: Identify key drivers of productivity

Historical Trends: Performance tracking over time

Smart Recommendations: Data-driven optimization suggestions

🏗️ Project Structure
text
garment-productivity-predictor/
│
├── 📁 Training Files/
│   └── best_xgboost_model.pkl          # Trained ML model
│
├── 📁 Flask/
│   ├── app.py                          # Flask application
│   ├── check_model_features.py               # Model training script
│   ├── save_preprocessor.py                 # Data preprocessing
│   └── preprocessor.pkl                # Utility functions
|   ├── best_xgboost_model.pkl  
|   ├── garments_worker_productivity.csv
│   📁 templates/
│     ├── home.html                      # Landing page
│     ├── predict.html                   # Prediction form
│     └── submit.html                    # Results page
│   📁 static/
│     ├── home.css
│     ├── predict.css
│     └── submit.css
│
├── 📁 Dataset/
│   └── garments_worker_productivity.csv  # Original dataset
│
├── requirements.txt                   # Python dependencies
├── README.md                         # Project documentation
🚀 Quick Start
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation
Clone the repository

git clone https://github.com/yourusername/garment-productivity-predictor.git
cd garment-productivity-predictor
Create virtual environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Set up the model and preprocessor

python Flask/app.py
Access the application
Open your browser and navigate to http://localhost:5000

📊 Model Performance
Our XGBoost model delivers reliable predictions:

Metric	Score	Interpretation
R² Score	0.505	Explains 50.5% of productivity variance
Mean Absolute Error	0.074	±7.4% average prediction error
Mean Squared Error	0.013	Low error magnitude
Productivity Classification:
🔴 Worst: <= 0.3 (Needs improvement)

🟡 Average: 0.3 - 0.8 (Meeting expectations)

🟢 Best: > 0.8 (Exceeding targets)

🎮 Usage Guide
1. Home Page
Learn about the project features

View system capabilities

Click "Start Prediction" to begin

2. Input Data
Fill in the production parameters:

Parameter	Range	Description
Department	Sweing/Finishing	Work department
Team Number	1-12	Team identifier
Target Productivity	0.3-0.9	Expected performance
SMV	2.5-55	Standard Minute Value
Overtime	0-15,000 min	Extra work time
Incentive	0-100	Motivation amount
Workers	2-60	Team size
3. View Results
Productivity Score: 0-1 scale prediction

Performance Classification: Color-coded category

Analytics Dashboard: Interactive charts

Optimization Recommendations: Actionable insights

🔧 API Documentation
Prediction Endpoint
http
POST /api/predict
Content-Type: application/json

{
  "department": "sweing",
  "team": 5,
  "day": "Monday",
  "targeted_productivity": 0.75,
  "smv": 26.16,
  "over_time": 7080,
  "incentive": 98,
  "no_of_workers": 59
}
Response
json
{
  "success": true,
  "prediction": 0.741,
  "class": "Average",
  "class_color": "#ffaa00"
}
🛠️ Development
Training Your Own Model
Prepare the data

python src/model_training.py --data data/garments_worker_productivity.csv
Model comparison

Linear Regression: Baseline

Random Forest: Robust ensemble

XGBoost: Best performance (selected)

Hyperparameter tuning

python
# Example tuning parameters
param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.1, 0.01],
    'n_estimators': [100, 200]
}
Adding New Features
Extend preprocessing in src/preprocessor.py

Update form validation in templates/predict.html

Modify API handling in src/app.py

Retrain model with new features

🌐 Deployment
Local Production
bash
# Use production WSGI server
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 src.app:app
Cloud Deployment Options
Heroku

heroku create your-app-name
git push heroku main
AWS Elastic Beanstalk

eb init -p python-3.8 your-app-name
eb create production
Docker

dockerfile
FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "src/app.py"]
📈 Dataset
Source
File: garments_worker_productivity.csv

Records: 1,197 production entries

Period: January - March 2015

Features: 14 operational parameters

Key Features
Temporal: Date, quarter, day of week

Organizational: Department, team, workforce size

Performance: Targeted vs actual productivity

Operational: SMV, overtime, incentives, disruptions

🤝 Contributing
We welcome contributions! Please see our Contributing Guidelines for details.

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

Development Setup
bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Code formatting
black src/ tests/
🐛 Troubleshooting
Common Issues
ModuleNotFoundError

# Reinstall dependencies
pip install -r requirements.txt
Model loading failed

# Regenerate preprocessor
python src/preprocessor.py
Port already in use

# Use different port
python src/app.py --port 5001
Getting Help
📖 Check the documentation

🙏 Acknowledgments
Dataset provided by Kaggle Garment Productivity Dataset

Icons by Font Awesome

Charts by Chart.js

UI inspiration from modern web design patterns

⭐️ Don't forget to star this repository if you find it helpful!
"Data-driven decisions lead to optimized operations and improved productivity."
