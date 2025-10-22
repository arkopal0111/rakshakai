from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(data):
    """
    Preprocess the input data for machine learning models.
    
    Parameters:
    - data: pd.DataFrame, the input data to preprocess
    
    Returns:
    - pd.DataFrame, the preprocessed data
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Normalize numerical features
    scaler = StandardScaler()
    numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    
    return data

def encode_categorical_features(data):
    """
    Encode categorical features using one-hot encoding.
    
    Parameters:
    - data: pd.DataFrame, the input data with categorical features
    
    Returns:
    - pd.DataFrame, the data with encoded categorical features
    """
    categorical_features = data.select_dtypes(include=['object']).columns
    data = pd.get_dummies(data, columns=categorical_features, drop_first=True)
    
    return data

def preprocess_for_model(data):
    """
    Complete preprocessing pipeline for preparing data for the model.
    
    Parameters:
    - data: pd.DataFrame, the input data to preprocess
    
    Returns:
    - pd.DataFrame, the fully preprocessed data
    """
    data = preprocess_data(data)
    data = encode_categorical_features(data)
    
    return data