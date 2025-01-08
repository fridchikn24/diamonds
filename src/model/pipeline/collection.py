import pandas as pd
from loguru import logger
from config.config import settings


def load_data_from_csv(path=settings.data_file_name):
    logger.info("extracting the table from the csv")
    return pd.read_csv(path)