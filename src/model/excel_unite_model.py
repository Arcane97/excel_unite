import logging
import os
import re

from pandas import concat

from src.model.excel_handler import ExcelHandler


class ExcelUniteModel:
    def __init__(self, excel_file_name_pattern, output_excel_file_name='_check_yobit_airdrop.xlsx', log_name='excel_unite'):
        self._excel_file_name_pattern = excel_file_name_pattern
        self._output_excel_file_name = output_excel_file_name

        self._logger = logging.getLogger(f'{log_name}.excel_unite_model')

        self._excel_handler = ExcelHandler(None, output_excel_file_name)

    def set_excel_file_name_pattern(self, excel_file_name_pattern):
        self._excel_file_name_pattern = excel_file_name_pattern

    def set_output_excel_file_name(self, output_excel_file_name):
        self._output_excel_file_name = output_excel_file_name

    def _get_excel_table_from_file(self,  input_excel_file_name):
        return self._excel_handler.get_excel_table_from_file(input_excel_file_name)

    def _get_excel_file_names(self):
        files_list = os.listdir(path=".")
        self._logger.info(f'Файлы в текущей папке: {files_list}')
        return list(filter(lambda file_name: re.match(self._excel_file_name_pattern, file_name), files_list))

    def _unite_tables(self, excel_tables):
        try:
            table = concat(excel_tables, axis=0, ignore_index=True)
        except Exception:
            self._logger.exception('Ошибка при объединении таблиц')
            return None
        return table

    def unite_excel_files(self):
        excel_file_names = self._get_excel_file_names()
        if len(excel_file_names) == 0:
            cur_dir = os.path.abspath(".")
            self._logger.error(f'Не нашли ни одного подходящего файла в текущей директории {cur_dir}')
            return
        excel_tables = [self._get_excel_table_from_file(excel_file_name) for excel_file_name in excel_file_names]
        # todo добавить столбец со временем
        united_table = self._unite_tables(excel_tables)

        self._excel_handler.save_to_excel(united_table)


if __name__ == "__main__":
    obj = ExcelUniteModel(re.compile(r'yobit_airdrop.*\.xlsx$'))
    # files_list_ = obj._get_excel_file_names()
    # # print(files_list_)
    # for file_name_ in files_list_:
    #     print(file_name_)
    #     table = obj._get_excel_table_from_file(file_name_)
    #     print(table, '\n')
    obj.unite_excel_files()
