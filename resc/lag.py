import pandas as pd

def lag(X, n, include_unlagged = False):
    
    """
    Lags X, a DataFrame, n times. By default does not include the original.
    """
    
    if n == 0:
        return X
    
    X_lag = X.shift(1)
    
    for i in range (2, n +1):
        X_lag = pd.concat([X_lag, X.shift(i)], axis = 1)
    
    if include_unlagged:
        X_lag = pd.concat([X, X_lag], axis = 1)
        
    return X_lag

def lag_dataset(X, y, n, include_unlagged = False):
    
    """
    Lags X, a DataFrame, n times. Removes the first n observations of X and y to avoid missing values.
    By default, does not include the unlagged data.
    """
    
    X_lag = lag(X, n, include_unlagged)
    
    X_lag = X_lag.iloc[n:,:]
    
    y_lag = y.iloc[n:,:]
    
    return X_lag, y_lag