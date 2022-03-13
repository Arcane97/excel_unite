import logging
import re

from src.model.excel_unite_model import ExcelUniteModel


def create_log():
    LOG_FILE_NAME = "_excel_unite_log.log"
    log_name = 'excel_unite'
    main_logger = logging.getLogger(log_name)
    main_logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(LOG_FILE_NAME, encoding="utf-8")
    formatter_fh = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter_fh)
    main_logger.addHandler(file_handler)


create_log()
model = ExcelUniteModel(re.compile(r'yobit_airdrop.*\.xlsx$'))
model.unite_excel_files()
