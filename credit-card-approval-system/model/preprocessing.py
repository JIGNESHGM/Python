import pandas as pd

def preprocess_input(data):
    """Preprocess user input for prediction"""
    processed = {
        'income': float(data['income']),
        'credit_score': int(data['credit_score']),
        'debt': float(data['debt']),
        'age': int(data['age']),
        'employed': 1 if data['employment'] == 'employed' else 0
    }
    return pd.DataFrame([processed])