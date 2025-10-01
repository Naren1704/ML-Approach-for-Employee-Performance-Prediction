import pickle
import pandas as pd

# Load your model
with open('best_xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("=== MODEL INFORMATION ===")
print(f"Model type: {type(model)}")

# Try to get feature names if available
try:
    if hasattr(model, 'feature_names_in_'):
        print(f"Expected features: {len(model.feature_names_in_)}")
        print("Feature names:")
        for i, feature in enumerate(model.feature_names_in_):
            print(f"  {i+1:2d}. {feature}")
    else:
        print("No feature names stored in model")
except Exception as e:
    print(f"Could not get feature names: {e}")

# Check model parameters
if hasattr(model, 'get_params'):
    print(f"\nModel parameters: {model.get_params()}")