import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pickle as pk
from model.pipeline.preparation import prepare_data
from loguru import logger
from config.config import settings


def build_model():
    logger.info('building model pipline')

    df = prepare_data()

    y = df['Type']
    X = df.drop('Type',axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=42, 
                                                        stratify=y)
    
    rf_model = build_rf(X_train,y_train)

    evaluate_model(rf_model, X_test, y_test)

    save_model(rf_model)

def build_rf(X_train, y_train):
    rf = RandomForestClassifier()

    rf_grid1 = {
        'n_estimators': np.arange(100,300,50),
        'max_features': ['log2','sqrt'],
        'max_depth': np.arange(10,50,5)
    }   

    grid_rf = GridSearchCV(rf, rf_grid1, cv=5, n_jobs=-1, return_train_score=True)
    grid_rf.fit(X_train,y_train)
    print(grid_rf.best_params_)

    return(grid_rf.best_estimator_)

def evaluate_model(model, X_test, y_test):

    logger.info(f"evaluating model performance. SCORE={model.score(X_test, y_test)}")
    return model.score(X_test, y_test)

def save_model(model):

    logger.info(f"saving a model to a directory: {settings.model_path}/{settings.model_name}")
    pk.dump(model, open(f'{settings.model_path}/{settings.model_name}', 'wb'))