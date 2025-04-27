import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def load_data():
    """Load and preprocess the credit data"""
    try:
        # Direct path to your credit_data.csv
        data_path = os.path.join('deta', 'credit_data.csv')
        data = pd.read_csv(data_path)
        
        # Verify required columns exist
        required_columns = ['income', 'credit_score', 'employment', 'debt', 'age', 'approved']
        if not all(col in data.columns for col in required_columns):
            missing = [col for col in required_columns if col not in data.columns]
            raise ValueError(f"Missing required columns: {missing}")
        
        # Convert employment to binary
        data['employed'] = data['employment'].map({'employed': 1, 'unemployed': 0})
        return data[['income', 'credit_score', 'debt', 'age', 'employed', 'approved']]
    
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        raise

def train_model():
    print("Starting model training...")
    
    # Load and prepare data
    try:
        data = load_data()
        print(f"Successfully loaded {len(data)} records")
        
        X = data.drop('approved', axis=1)
        y = data['approved']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=0.2, 
            random_state=42,
            stratify=y  # Maintain class balance
        )
        
        # Train model
        print("Training Random Forest model...")
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight='balanced'  # Handle class imbalance
        )
        model.fit(X_train, y_train)
        
        # Evaluate
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print("\nModel Evaluation:")
        print(f"Accuracy: {accuracy:.2%}")
        print("\nClassification Report:")
        print(classification_report(y_test, predictions))
        
        # Save model
        os.makedirs('model', exist_ok=True)
        model_path = os.path.join('model', 'model.pkl')
        joblib.dump(model, model_path)
        print(f"\nModel successfully saved to {model_path}")
        
    except Exception as e:
        print(f"Error during model training: {str(e)}")
        raise

if __name__ == '__main__':
    train_model()