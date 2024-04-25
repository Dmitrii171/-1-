import os
import pandas as pd

class PriceMachine():

    def __init__(self):
        self.all_data = {'товар': [],
                         'вес': [],
                         'цена': [],
                         'цена за кг': [],
                         'файл': []
                         }

    def load_prices(self, file_path='C:\\Users\\user\\Desktop\\Test task'):
        files = os.listdir(file_path)
        for file in files:
            if 'price' in file:
                with open(file_path + '\\' + file, 'r', encoding='UTF-8') as opened_file:
                    data = pd.read_csv(opened_file)
                    columns = list(data.columns)
                    for column in columns:
                        if column in ('товар', 'название', 'наименование', 'продукт'):
                            self.all_data['товар'] += list(data[column])
                        if column in ('цена', 'розница'):
                            self.all_data['цена'] += list(data[column])
                            prices = list(data[column])
                        if column in ('вес', 'масса', 'фасовка'):
                            self.all_data['вес'] += list(data[column])
                            weight = list(data[column])
                    price_for_kg = []
                    files_list = []
                    for i in range(len(prices)):
                        price_for_kg.append(prices[i] / weight[i])
                        files_list.append(file)
                    self.all_data['цена за кг'] += price_for_kg
                    self.all_data['файл'] += files_list

        self.df_all_data = pd.DataFrame(self.all_data)
        self.sorted_all_data = self.df_all_data.sort_values('цена за кг')

    def export_to_html(self, file, data):
        data.to_html(file)

    def find_text(self, text):
        finded_goods = []
        for column, row in self.sorted_all_data.iterrows():
            if text in row['товар']:
                finded_goods.append(row)
        df = pd.DataFrame(finded_goods)
        return df


pm = PriceMachine()
pm.load_prices()
fname = 'output.html'
html_file = open(fname, 'w', encoding='UTF-8')
text = input("Введите название товара для поиска: ")
while (text != 'exit'):
    if text != '':
        data = pm.find_text(text)
        if data.empty:
            print('Данные не найдены!')
        else:
            print(data)
            pm.export_to_html(html_file, data)
    else:
        print('Введено неправильное значение')
    text = input("Введите название товара для поиска: ")
print('Поиск окончен')
html_file.close()
