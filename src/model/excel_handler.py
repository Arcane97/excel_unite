import logging

from pandas import read_excel, ExcelWriter


class ExcelHandler:
    def __init__(self, input_excel_file_name, output_excel_file_name='_check_yobit_airdrop.xlsx',
                 log_name='excel_unite'):
        self._input_excel_file_name = input_excel_file_name
        self._output_excel_file_name = output_excel_file_name

        self._logger = logging.getLogger(f'{log_name}.excel_handler')

        self._excel_table = None

    def set_input_excel_file_name(self, input_excel_file_name):
        self._input_excel_file_name = input_excel_file_name

    def set_output_excel_file_name(self, output_excel_file_name):
        self._output_excel_file_name = output_excel_file_name

    def read_table(self):
        try:
            self._excel_table = read_excel(self._input_excel_file_name, dtype=str)
        except FileNotFoundError:
            self._logger.error(f'Не найден файл: {self._input_excel_file_name}')
            self._excel_table = None
        except ValueError:
            self._logger.error(f'Введено неправильное название файла: {self._input_excel_file_name}')
            self._excel_table = None

    def get_excel_table(self):
        return self._excel_table

    def get_excel_table_from_file(self, input_excel_file_name):
        self.set_input_excel_file_name(input_excel_file_name)
        self.read_table()
        return self._excel_table

    def save_to_excel(self, excel_table_to_save):
        self._logger.info(f'Сохраняем в Excel файл: {self._output_excel_file_name}')
        try:
            writer = ExcelWriter(self._output_excel_file_name, engine='xlsxwriter')
            excel_table_to_save.to_excel(writer, index=False)
            writer.save()
        except Exception:
            self._logger.exception('Ошибка записи в файл Excel')


if __name__ == "__main__":
    file_name = 'yobit_airdrop-57.xlsx'
    obj = ExcelHandler(file_name, 'result_yobit_airdrop')
    obj.read_table()
    excel_data_df = obj.get_excel_table()
    print(excel_data_df)
