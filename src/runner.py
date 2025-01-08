import pandas as pd
from model.model_service import ModelService
from model.pipeline.preparation import encode_categories, fill_na
from loguru import logger

@logger.catch 
def main():
    logger.info("running the application...")
    ml_svc = ModelService()
    ml_svc.load_model()

    test = pd.read_csv('diamonds.csv')
    test = fill_na(test)
    test = encode_categories(test)
    test = test.drop('Type',axis=1)
    pred = ml_svc.predict(test.iloc[41])
    logger.info(f"prediction = {pred}")

if __name__ == '__main__':
    main()