import pandas as pd
from model.pipeline.collection import load_data_from_csv
from loguru import logger

def prepare_data():
    logger.info('beginning preprocessing')

    data = load_data_from_csv()

    data = fill_na(data)

    data = encode_categories(data)

    return data

def fill_na(data):
    data['Fluorescence'] = data['Fluorescence'].fillna('None')

    data = data.drop('Cut', axis=1)

    data = data.dropna(axis=0)

    return data

def encode_categories(data):
    categorical = ['Fluorescence','Shape','Color','Clarity','Polish','Symmetry','Girdle','Culet']

    data = pd.get_dummies(data, columns=categorical)

    return data