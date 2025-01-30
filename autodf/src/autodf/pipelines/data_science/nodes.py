"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.10
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

import numpy as np

import logging
logger = logging.getLogger(__name__)

def split_dataset(df, test_size):
    df = df.dropna(how='any')
    y = df['city-mpg']
    df = df.drop('city-mpg',axis=1)
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test 

def train_model(X_train, y_train):
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train.values.ravel())

    logger.info('Model is Trained')
    return lin_reg


def evaluate_model(model, X_test, y_test):
    y_predicted = model.predict(X_test)
    lin_mse = mean_squared_error(y_test, y_predicted)
    lin_rmse = np.sqrt(lin_mse)

    logger.info(f'RMSE: {lin_rmse}')
    return None

def train_model_with_gridsearch(X_train, y_train):
    param_grid = [
        {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
        {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
    ]

    forest_reg = RandomForestRegressor(random_state=42)

    grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                               scoring='neg_mean_squared_error',
                               return_train_score=True)
    
    grid_search.fit(X_train, y_train.values.ravel())

    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_

    logger.info(f"Mejores parámetros: {best_params}")

    return best_model, best_params 

def train_random_forest(X_train, y_train):
    forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
    forest_reg.fit(X_train, y_train.values.ravel())

    logger.info("Random Forest model entrenado.")

    return forest_reg

def evaluate_random_forest(model, X_test, y_test):
    y_predicted = model.predict(X_test)
    forest_mse = mean_squared_error(y_test, y_predicted)
    forest_rmse = np.sqrt(forest_mse)

    logger.info(f"Random Forest: {forest_rmse}")
    
    return forest_rmse